------------------------------------------------------------------------------------------------------
-- Frame Sync Detector with Circular Buffer - VERSION 3 (FIXED)
------------------------------------------------------------------------------------------------------
-- FIX: Simplified handshake - once output starts, it MUST complete all 268 bytes
-- No early exits, no edge detection complexity
-- BUGFIX: Added internal signal for m_axis_tvalid to allow readback
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;


ENTITY frame_sync_detector IS
    GENERIC (
        SYNC_WORD : std_logic_vector(23 DOWNTO 0) := x"447FAA";
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

    -- Bit-level sync detection
    SIGNAL sync_shift_bits : std_logic_vector(23 DOWNTO 0) := (OTHERS => '0');
    
    -- Byte assembly
    SIGNAL byte_shift_reg  : std_logic_vector(7 DOWNTO 0);
    SIGNAL bit_count       : unsigned(2 DOWNTO 0);
    
    -- Circular buffer
    CONSTANT BUFFER_SIZE : NATURAL := 2**BUFFER_DEPTH;
    TYPE byte_buffer_t IS ARRAY(0 TO BUFFER_SIZE-1) OF std_logic_vector(7 DOWNTO 0);
    SIGNAL circ_buffer : byte_buffer_t;
    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF circ_buffer : SIGNAL IS "block";
    
    SIGNAL wr_ptr : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    SIGNAL rd_ptr : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    
    -- Reception state
    TYPE rx_state_t IS (HUNTING, LOCKED);
    SIGNAL rx_state : rx_state_t := HUNTING;
    
    SIGNAL frame_start_ptr  : unsigned(BUFFER_DEPTH-1 DOWNTO 0);
    SIGNAL frame_byte_count : natural range 0 to PAYLOAD_BYTES;
    SIGNAL frames_count     : unsigned(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL errors_count     : unsigned(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL consecutive_good : natural range 0 to LOCK_FRAMES := 0;
    SIGNAL lock_status      : std_logic := '0';
    
    -- Frame ready handshake (NO multi-driver!)
    SIGNAL frame_req : std_logic := '0';  -- reception sets/clears
    SIGNAL frame_ack : std_logic := '0';  -- output sets when consuming
    SIGNAL frame_available_ptr : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    
    -- Internal version of m_axis_tvalid that we CAN read
    SIGNAL m_axis_tvalid_int : std_logic := '0';
    
    -- Output state - SIMPLIFIED
    TYPE output_state_t IS (IDLE, OUTPUTTING);
    SIGNAL output_state     : output_state_t := IDLE;
    SIGNAL output_count     : natural range 0 to PAYLOAD_BYTES := 0;
    SIGNAL output_rd_ptr    : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    
    -- Hamming distance
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
    
    -- Connect internal signal to output port
    m_axis_tvalid <= m_axis_tvalid_int;

    ------------------------------------------------------------------------------
    -- Reception Process
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
                rx_state <= HUNTING;
                frame_start_ptr <= (OTHERS => '0');
                frame_byte_count <= 0;
                consecutive_good <= 0;
                lock_status <= '0';
                frame_req <= '0';
                frame_available_ptr <= (OTHERS => '0');
                buffer_overflow <= '0';
                
            ELSE
                buffer_overflow <= '0';
                
                -- Clear frame_req when output acknowledges
                IF frame_ack = '1' THEN
                    frame_req <= '0';
                END IF;
                
                IF rx_bit_valid = '1' THEN
                    sync_shift_bits <= sync_shift_bits(22 DOWNTO 0) & rx_bit;
                    byte_shift_reg <= byte_shift_reg(6 DOWNTO 0) & rx_bit;
                END IF;
                
                CASE rx_state IS
                    WHEN HUNTING =>
                        hamming_dist := calc_hamming_distance(sync_shift_bits, SYNC_WORD);
                        IF hamming_dist <= SYNC_THRESHOLD THEN
                            frame_byte_count <= 0;
                            bit_count <= (OTHERS => '0');
                            rx_state <= LOCKED;
                            
                            IF consecutive_good < LOCK_FRAMES THEN
                                consecutive_good <= consecutive_good + 1;
                            ELSE
                                lock_status <= '1';
                            END IF;
                        END IF;
                        
                    WHEN LOCKED =>
                        IF rx_bit_valid = '1' THEN
                            bit_count <= bit_count + 1;
                            
                            IF bit_count = 7 THEN
                                assembled_byte := byte_shift_reg(6 DOWNTO 0) & rx_bit;
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
                                    -- Frame complete - signal frame available
                                    IF frame_req = '0' THEN
                                        -- Only signal if previous frame was consumed
                                        frame_req <= '1';
                                        frame_available_ptr <= frame_start_ptr;
                                        frames_count <= frames_count + 1;
                                    ELSE
                                        -- Output hasn't consumed previous frame - overflow!
                                        errors_count <= errors_count + 1;
                                        buffer_overflow <= '1';
                                    END IF;
                                    frame_start_ptr <= wr_ptr;
                                    rx_state <= HUNTING;
                                    frame_byte_count <= 0;
                                END IF;
                            END IF;
                        END IF;
                END CASE;
                
            END IF;
        END IF;
    END PROCESS reception_proc;

    ------------------------------------------------------------------------------
    -- Output Process - SIMPLIFIED
    ------------------------------------------------------------------------------
    output_proc: PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF reset = '1' THEN
                m_axis_tdata <= (OTHERS => '0');
                m_axis_tvalid_int <= '0';
                m_axis_tlast <= '0';
                output_count <= 0;
                output_state <= IDLE;
                output_rd_ptr <= (OTHERS => '0');
                rd_ptr <= (OTHERS => '0');
                frame_ack <= '0';
                
            ELSE
                -- Default: clear ack
                frame_ack <= '0';
                
                CASE output_state IS
                    
                    WHEN IDLE =>
                        m_axis_tvalid_int <= '0';
                        m_axis_tlast <= '0';
                        
                        -- Start output if frame is available
                        IF frame_req = '1' THEN
                            output_state <= OUTPUTTING;
                            output_rd_ptr <= frame_available_ptr;
                            output_count <= 0;
                            -- Acknowledge - we're consuming this frame
                            frame_ack <= '1';
                        END IF;
                    
                    WHEN OUTPUTTING =>
                        -- Output bytes with AXI handshaking
                        IF m_axis_tready = '1' OR m_axis_tvalid_int = '0' THEN
                            m_axis_tdata <= circ_buffer(to_integer(output_rd_ptr));
                            m_axis_tvalid_int <= '1';
                            
                            -- Check if last byte
                            IF output_count = PAYLOAD_BYTES - 1 THEN
                                m_axis_tlast <= '1';
                                output_count <= 0;
                                rd_ptr <= output_rd_ptr + 1;  -- Update global rd_ptr
                                output_state <= IDLE;
                            ELSE
                                m_axis_tlast <= '0';
                                output_count <= output_count + 1;
                                output_rd_ptr <= output_rd_ptr + 1;
                            END IF;
                        END IF;
                        
                END CASE;
                
            END IF;
        END IF;
    END PROCESS output_proc;

END ARCHITECTURE rtl;
