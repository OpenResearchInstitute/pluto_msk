------------------------------------------------------------------------------------------------------
-- Frame Sync Detector with Circular Buffer - MSB-FIRST VERSION
------------------------------------------------------------------------------------------------------
-- MODIFIED: Now uses MSB-first bit ordering (standard serial convention)
-- Receives bit 7 first, assembles bytes in standard order
-- Sync word updated to 0x02B8DB (matches TX, no bit reversal!)
------------------------------------------------------------------------------------------------------
-- Now uses frame_ready handshake signal between reception_proc and output_proc
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;


ENTITY frame_sync_detector IS
    GENERIC (
        SYNC_WORD : std_logic_vector(23 DOWNTO 0) := x"02B8DB";  -- MSB-first sync word
        PAYLOAD_BYTES   : NATURAL := 268;
        SYNC_THRESHOLD  : NATURAL := 3;
        BUFFER_DEPTH    : NATURAL := 11;
        LOCK_FRAMES     : NATURAL := 3
    );
    PORT (
        clk             : IN  std_logic;
        reset           : IN  std_logic;
        
        -- BIT Input Interface
        rx_bit          : IN  std_logic;
        rx_bit_valid    : IN  std_logic;
        
        -- AXIS Master Interface (to FIFO)
        m_axis_tdata    : OUT std_logic_vector(7 DOWNTO 0);
        m_axis_tvalid   : OUT std_logic;
        m_axis_tready   : IN  std_logic;
        m_axis_tlast    : OUT std_logic;
        
        -- Status Outputs
        frame_sync_locked     : OUT std_logic;
        frames_received : OUT std_logic_vector(31 DOWNTO 0);
        frame_sync_errors     : OUT std_logic_vector(31 DOWNTO 0);
        buffer_overflow : OUT std_logic
    );
END ENTITY frame_sync_detector;


ARCHITECTURE rtl OF frame_sync_detector IS

    -- Bit-level sync detection (MSB shifts in from left)
    SIGNAL sync_shift_bits : std_logic_vector(23 DOWNTO 0) := (OTHERS => '0');
    
    -- Byte assembly for output (MSB shifts in from left)
    SIGNAL byte_shift_reg  : std_logic_vector(7 DOWNTO 0);
    SIGNAL bit_count       : unsigned(2 DOWNTO 0);
    
    -- Circular buffer for BYTES (after sync found)
    CONSTANT BUFFER_SIZE : NATURAL := 2**BUFFER_DEPTH;
    TYPE byte_buffer_t IS ARRAY(0 TO BUFFER_SIZE-1) OF std_logic_vector(7 DOWNTO 0);
    SIGNAL circ_buffer : byte_buffer_t;
    -- Force Block RAM usage for circular buffer
    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF circ_buffer : SIGNAL IS "block";

    
    SIGNAL wr_ptr : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    SIGNAL rd_ptr : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    
    -- State machine
    TYPE state_t IS (HUNTING, LOCKED, OUTPUTTING);
    SIGNAL state : state_t := HUNTING;
    
    -- Frame tracking
    SIGNAL frame_start_ptr  : unsigned(BUFFER_DEPTH-1 DOWNTO 0);
    SIGNAL frame_byte_count : natural range 0 to PAYLOAD_BYTES;
    SIGNAL frames_count     : unsigned(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL errors_count     : unsigned(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL consecutive_good : natural range 0 to LOCK_FRAMES := 0;
    SIGNAL lock_status      : std_logic := '0';
    
    -- Handshake signals replace output_active being driven by two processes
    SIGNAL frame_ready      : std_logic := '0';  -- Reception sets, output clears
    SIGNAL frame_ack        : std_logic := '0';  -- Output acknowledges frame taken
    SIGNAL frame_rd_ptr     : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    
    SIGNAL output_active    : std_logic := '0';  -- NOW ONLY IN output_proc
    SIGNAL output_count     : natural range 0 to PAYLOAD_BYTES := 0;
    SIGNAL tvalid_int       : std_logic := '0';
    SIGNAL tlast_int        : std_logic := '0';
    
    -- Hamming distance calculator
    FUNCTION calc_hamming_distance(
        pattern1 : std_logic_vector;
        pattern2 : std_logic_vector
    ) RETURN natural IS
        VARIABLE distance : natural := 0;
    BEGIN
        FOR i IN pattern1'RANGE LOOP
            IF pattern1(i) /= pattern2(i) THEN
                distance := distance + 1;
            END IF;
        END LOOP;
        RETURN distance;
    END FUNCTION;

BEGIN

    frame_sync_locked <= lock_status;
    frames_received <= std_logic_vector(frames_count);
    frame_sync_errors <= std_logic_vector(errors_count);
    m_axis_tvalid <= tvalid_int;
    m_axis_tlast <= tlast_int;

    ------------------------------------------------------------------------------
    -- Main Process: Bit-by-Bit Sync Detection + Byte Assembly
    -- MODIFIED: MSB-first bit ordering
    ------------------------------------------------------------------------------
    reception_proc: PROCESS(clk)
        VARIABLE hamming_dist : natural range 0 to 24;
        VARIABLE assembled_byte : std_logic_vector(7 DOWNTO 0);
    BEGIN
        IF rising_edge(clk) THEN
            IF reset = '1' THEN
                sync_shift_bits <= (OTHERS => '0');
                byte_shift_reg <= (OTHERS => '0');
                bit_count <= (OTHERS => '0');
                wr_ptr <= (OTHERS => '0');
                state <= HUNTING;
                frame_start_ptr <= (OTHERS => '0');
                frame_byte_count <= 0;
                consecutive_good <= 0;
                lock_status <= '0';
                frame_ready <= '0';
                frame_rd_ptr <= (OTHERS => '0');
                buffer_overflow <= '0';
                
            ELSE
                buffer_overflow <= '0';
                
                -- Clear frame_ready when acknowledged
                IF frame_ack = '1' THEN
                    frame_ready <= '0';
                END IF;
                


IF rx_bit_valid = '1' THEN
    -- MSB-FIRST: Shift LEFT so first bit ends up at position 23
    sync_shift_bits <= sync_shift_bits(22 DOWNTO 0) & rx_bit;
    byte_shift_reg <= byte_shift_reg(6 DOWNTO 0) & rx_bit;
END IF;



-- Check state on EVERY clock (not just when rx_bit_valid)
CASE state IS
    WHEN HUNTING =>
        IF rx_bit_valid = '1' THEN
            hamming_dist := calc_hamming_distance(
                sync_shift_bits,
                SYNC_WORD
            );
            IF hamming_dist <= SYNC_THRESHOLD THEN
                -- Found sync!
                frame_byte_count <= 0;
                bit_count <= (OTHERS => '0');
                state <= LOCKED;
                IF consecutive_good < LOCK_FRAMES THEN
                    consecutive_good <= consecutive_good + 1;
                ELSE
                    lock_status <= '1';
                END IF;
            END IF;
        END IF;




-- The LOCKED state stays outside since it has its own rx_bit_valid check
    WHEN LOCKED =>
        IF rx_bit_valid = '1' THEN
            -- Collecting frame bytes
            bit_count <= bit_count + 1;
            
            IF bit_count = 7 THEN
                -- Byte complete (MSB-first assembly)
                -- Last bit received (rx_bit) is the LSB
                assembled_byte := byte_shift_reg;
                
                -- Write to circular buffer
                circ_buffer(to_integer(wr_ptr)) <= assembled_byte;
                wr_ptr <= wr_ptr + 1;
                
                IF wr_ptr + 1 = rd_ptr THEN
                    buffer_overflow <= '1';
                    errors_count <= errors_count + 1;
                END IF;
                
                bit_count <= (OTHERS => '0');
                
                IF frame_byte_count < PAYLOAD_BYTES - 1 THEN
                    frame_byte_count <= frame_byte_count + 1;
                ELSE
                    -- Frame complete
                    IF frame_ready = '0' THEN
                        -- Signal frame is ready for output
                        frame_ready <= '1';
                        frame_rd_ptr <= frame_start_ptr;
                        frames_count <= frames_count + 1;
                    ELSE
                        -- Output process hasn't taken previous frame yet
                        errors_count <= errors_count + 1;
                    END IF;
                    
                    -- Return to hunting for next frame
                    frame_start_ptr <= wr_ptr;
                    state <= HUNTING;
                    frame_byte_count <= 0;
                END IF;
            END IF;
        END IF;
        
    WHEN OTHERS =>
        state <= HUNTING;
END CASE;




            END IF;  -- End of ELSE for reset
        END IF;  -- End of rising_edge(clk)







                
    END PROCESS reception_proc;

    ------------------------------------------------------------------------------
    -- Output Process: Stream bytes to AXIS interface
    -- (No changes needed - byte-level interface)
    ------------------------------------------------------------------------------
    output_proc: PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF reset = '1' THEN
                m_axis_tdata <= (OTHERS => '0');
                tvalid_int <= '0';
                tlast_int <= '0';
                output_count <= 0;
                output_active <= '0';
                frame_ack <= '0';
                rd_ptr <= (OTHERS => '0');
                
            ELSE
                -- Default: no ack
                frame_ack <= '0';
                
                -- Check if new frame is ready
                IF frame_ready = '1' AND output_active = '0' THEN
                    output_active <= '1';
                    rd_ptr <= frame_rd_ptr;
                    output_count <= 0;
                    frame_ack <= '1';  -- Acknowledge we took the frame
                END IF;
                
                -- Output state machine
                IF output_active = '1' THEN
                    IF m_axis_tready = '1' OR tvalid_int = '0' THEN
                        m_axis_tdata <= circ_buffer(to_integer(rd_ptr));
                        tvalid_int <= '1';
                        rd_ptr <= rd_ptr + 1;
                        
                        IF output_count = PAYLOAD_BYTES - 1 THEN
                            tlast_int <= '1';
                            output_active <= '0';
                            output_count <= 0;
                        ELSE
                            tlast_int <= '0';
                            output_count <= output_count + 1;
                        END IF;
                    END IF;
                ELSE
                    IF m_axis_tready = '1' THEN
                        tvalid_int <= '0';
                        tlast_int <= '0';
                    END IF;
                END IF;
            END IF;
        END IF;
    END PROCESS output_proc;

END ARCHITECTURE rtl;
