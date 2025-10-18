------------------------------------------------------------------------------------------------------
-- Frame Sync Detector with Circular Buffer
------------------------------------------------------------------------------------------------------
-- Continuously searches for sync word in byte stream
-- Outputs payload bytes with TLAST marking frame boundaries
-- Uses circular buffer to decouple reception from output
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY frame_sync_detector IS
    GENERIC (
        SYNC_WORD       : std_logic_vector(23 DOWNTO 0) := x"E25F35";
        PAYLOAD_BYTES   : NATURAL := 268;
        SYNC_THRESHOLD  : NATURAL := 3;      -- Max bit errors in sync detection
        BUFFER_DEPTH    : NATURAL := 11;     -- 2^11 = 2048 bytes circular buffer
        LOCK_FRAMES     : NATURAL := 3       -- Consecutive good frames to declare lock
    );
    PORT (
        -- Clock and Reset
        clk             : IN  std_logic;
        reset           : IN  std_logic;
        
        -- Byte Input Interface
        rx_byte         : IN  std_logic_vector(7 DOWNTO 0);
        rx_byte_valid   : IN  std_logic;
        
        -- AXIS Master Interface (to FIFO)
        m_axis_tdata    : OUT std_logic_vector(7 DOWNTO 0);
        m_axis_tvalid   : OUT std_logic;
        m_axis_tready   : IN  std_logic;
        m_axis_tlast    : OUT std_logic;
        
        -- Status Outputs
        sync_locked     : OUT std_logic;
        frames_received : OUT std_logic_vector(31 DOWNTO 0);
        sync_errors     : OUT std_logic_vector(31 DOWNTO 0);
        buffer_overflow : OUT std_logic
    );
END ENTITY frame_sync_detector;

ARCHITECTURE rtl OF frame_sync_detector IS

    -- Circular buffer for incoming bytes
    CONSTANT BUFFER_SIZE : NATURAL := 2**BUFFER_DEPTH;
    TYPE byte_buffer_t IS ARRAY(0 TO BUFFER_SIZE-1) OF std_logic_vector(7 DOWNTO 0);
    SIGNAL circ_buffer : byte_buffer_t;
    
    -- Buffer pointers
    SIGNAL wr_ptr : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    SIGNAL rd_ptr : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    
    -- Sync detection shift register
    SIGNAL sync_shift : std_logic_vector(23 DOWNTO 0) := (OTHERS => '0');
    
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
    
    -- Output control - INTERNAL SIGNALS (FIX for synthesis error)
    SIGNAL output_active    : std_logic := '0';
    SIGNAL output_count     : natural range 0 to PAYLOAD_BYTES := 0;
    SIGNAL tvalid_int       : std_logic := '0';  -- Internal signal for m_axis_tvalid
    SIGNAL tlast_int        : std_logic := '0';  -- Internal signal for m_axis_tlast
    
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

    -- Output status signals
    sync_locked <= lock_status;
    frames_received <= std_logic_vector(frames_count);
    sync_errors <= std_logic_vector(errors_count);
    
    -- Connect internal signals to outputs
    m_axis_tvalid <= tvalid_int;
    m_axis_tlast <= tlast_int;

    ------------------------------------------------------------------------------
    -- Main Process: Reception and Sync Detection
    ------------------------------------------------------------------------------
    reception_proc: PROCESS(clk)
        VARIABLE hamming_dist : natural range 0 to 24;
    BEGIN
        IF rising_edge(clk) THEN
            IF reset = '1' THEN
                wr_ptr <= (OTHERS => '0');
                sync_shift <= (OTHERS => '0');
                state <= HUNTING;
                frame_start_ptr <= (OTHERS => '0');
                frame_byte_count <= 0;
                consecutive_good <= 0;
                lock_status <= '0';
                output_active <= '0';
                buffer_overflow <= '0';
                
            ELSE
                -- Default: clear overflow flag
                buffer_overflow <= '0';
                
                -- ALWAYS write incoming bytes to circular buffer
                IF rx_byte_valid = '1' THEN
                    circ_buffer(to_integer(wr_ptr)) <= rx_byte;
                    wr_ptr <= wr_ptr + 1;  -- Wraps automatically
                    
                    -- Check for buffer overflow (write catching up to read)
                    IF wr_ptr + 1 = rd_ptr THEN
                        buffer_overflow <= '1';
                        errors_count <= errors_count + 1;
                    END IF;
                    
                    -- Shift in byte for sync detection
                    sync_shift <= sync_shift(15 DOWNTO 0) & rx_byte;
                    
                    -- Check for sync pattern
                    hamming_dist := calc_hamming_distance(sync_shift(15 DOWNTO 0) & rx_byte, SYNC_WORD);
                    
                    CASE state IS
                        WHEN HUNTING =>
                            -- Looking for sync word
                            IF hamming_dist <= SYNC_THRESHOLD THEN
                                -- Found sync! Next byte is start of payload
                                frame_start_ptr <= wr_ptr + 1;
                                frame_byte_count <= 0;
                                state <= LOCKED;
                                
                                -- Start building lock confidence
                                IF consecutive_good < LOCK_FRAMES THEN
                                    consecutive_good <= consecutive_good + 1;
                                ELSE
                                    lock_status <= '1';
                                END IF;
                            END IF;
                            
                        WHEN LOCKED =>
                            -- Collecting frame bytes
                            IF frame_byte_count < PAYLOAD_BYTES - 1 THEN
                                frame_byte_count <= frame_byte_count + 1;
                            ELSE
                                -- Frame complete, trigger output
                                IF output_active = '0' THEN
                                    output_active <= '1';
                                    rd_ptr <= frame_start_ptr;  -- Position read pointer
                                    output_count <= 0;
                                    frames_count <= frames_count + 1;
                                ELSE
                                    -- Previous frame still outputting - error condition
                                    errors_count <= errors_count + 1;
                                END IF;
                                
                                -- Return to hunting for next frame
                                state <= HUNTING;
                                frame_byte_count <= 0;
                            END IF;
                            
                        WHEN OTHERS =>
                            state <= HUNTING;
                    END CASE;
                    
                END IF;
                
            END IF;
        END IF;
    END PROCESS reception_proc;

    ------------------------------------------------------------------------------
    -- Output Process: Stream bytes to AXIS interface
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
                rd_ptr <= (OTHERS => '0');
                
            ELSE
                -- Output bytes when frame is ready and downstream is ready
                IF output_active = '1' THEN
                    IF m_axis_tready = '1' OR tvalid_int = '0' THEN  -- FIXED: Use internal signal
                        -- Output next byte
                        m_axis_tdata <= circ_buffer(to_integer(rd_ptr));
                        tvalid_int <= '1';
                        rd_ptr <= rd_ptr + 1;
                        
                        -- Check if this is the last byte
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
                    -- No active frame - idle
                    IF m_axis_tready = '1' THEN
                        tvalid_int <= '0';
                        tlast_int <= '0';
                    END IF;
                END IF;
                
            END IF;
        END IF;
    END PROCESS output_proc;

END ARCHITECTURE rtl;
