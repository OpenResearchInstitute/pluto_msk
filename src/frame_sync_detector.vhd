------------------------------------------------------------------------------------------------------
-- Frame Sync Detector with Frame Tracking and Flywheel - IMPROVED VERSION
------------------------------------------------------------------------------------------------------
-- IMPROVEMENTS OVER ORIGINAL:
-- 1. Frame Tracking: Knows exactly where to expect next sync word
-- 2. Flywheel: Tolerates missed syncs during brief interference (stays locked)
-- 3. Adaptive Threshold: Stricter when hunting, more relaxed when locked
-- 4. Better lock management: Distinguishes between acquiring lock vs maintaining lock
------------------------------------------------------------------------------------------------------
-- Based on original by Open Research Institute
-- Enhanced with robust sync tracking for low-SNR operation
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;


ENTITY frame_sync_detector IS
    GENERIC (
        SYNC_WORD           : std_logic_vector(23 DOWNTO 0) := x"02B8DB";  -- MSB-first sync word (CORRECTED)
        PAYLOAD_BYTES       : NATURAL := 268;
        
        -- Threshold when hunting for initial sync (conservative)
        HUNTING_THRESHOLD   : NATURAL := 3;
        
        -- Threshold when locked (more tolerant to maintain lock)
        LOCKED_THRESHOLD    : NATURAL := 5;
        
        -- How many consecutive missed syncs before declaring lock lost
        FLYWHEEL_TOLERANCE  : NATURAL := 2;
        
        -- How many consecutive good frames needed to declare lock acquired
        LOCK_FRAMES         : NATURAL := 3;
        
        BUFFER_DEPTH        : NATURAL := 11
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
        frames_received       : OUT std_logic_vector(31 DOWNTO 0);
        frame_sync_errors     : OUT std_logic_vector(31 DOWNTO 0);
        buffer_overflow       : OUT std_logic;
        
        -- Debug outputs (optional, helpful for monitoring)
        debug_state           : OUT std_logic_vector(2 DOWNTO 0);
        debug_missed_syncs    : OUT std_logic_vector(3 DOWNTO 0);
        debug_consecutive_good: OUT std_logic_vector(3 DOWNTO 0)

    );
END ENTITY frame_sync_detector;


ARCHITECTURE rtl OF frame_sync_detector IS

    -- Bit-level sync detection (MSB shifts in from left)
    SIGNAL sync_shift_bits : std_logic_vector(23 DOWNTO 0) := (OTHERS => '0');
    SIGNAL sync_bit_count  : unsigned(4 DOWNTO 0) := (OTHERS => '0');  -- Counts 0-23
    
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
    
    -- Enhanced state machine
    TYPE state_t IS (HUNTING, LOCKED, VERIFYING_SYNC);
    SIGNAL state : state_t := HUNTING;
    
    -- Frame tracking
    SIGNAL frame_start_ptr      : unsigned(BUFFER_DEPTH-1 DOWNTO 0);
    SIGNAL frame_byte_count     : natural range 0 to PAYLOAD_BYTES;
    SIGNAL frames_count         : unsigned(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL errors_count         : unsigned(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL consecutive_good     : natural range 0 to LOCK_FRAMES := 0;
    SIGNAL missed_sync_count    : natural range 0 to FLYWHEEL_TOLERANCE := 0;
    SIGNAL lock_status          : std_logic := '0';
    SIGNAL acquiring_lock       : std_logic := '0';  -- True during initial lock acquisition
    
    -- Handshake signals
    SIGNAL frame_ready      : std_logic := '0';
    SIGNAL frame_ack        : std_logic := '0';
    SIGNAL frame_rd_ptr     : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    
    SIGNAL output_active    : std_logic := '0';
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
    
    -- Debug outputs
    WITH state SELECT debug_state <=
        "001" WHEN HUNTING,
        "010" WHEN LOCKED,
        "011" WHEN VERIFYING_SYNC,
        "000" WHEN OTHERS;
    
    debug_missed_syncs <= std_logic_vector(to_unsigned(missed_sync_count, 4));
    debug_consecutive_good <= std_logic_vector(to_unsigned(consecutive_good, 4));

    ------------------------------------------------------------------------------
    -- Main Process: Frame Tracking with Flywheel
    ------------------------------------------------------------------------------
    reception_proc: PROCESS(clk)
        VARIABLE hamming_dist : natural range 0 to 24;
        VARIABLE assembled_byte : std_logic_vector(7 DOWNTO 0);
        VARIABLE threshold_to_use : natural range 0 to 24;
    BEGIN
        IF rising_edge(clk) THEN
            IF reset = '1' THEN
                sync_shift_bits <= (OTHERS => '0');
                sync_bit_count <= (OTHERS => '0');
                byte_shift_reg <= (OTHERS => '0');
                bit_count <= (OTHERS => '0');
                wr_ptr <= (OTHERS => '0');
                state <= HUNTING;
                frame_start_ptr <= (OTHERS => '0');
                frame_byte_count <= 0;
                consecutive_good <= 0;
                missed_sync_count <= 0;
                lock_status <= '0';
                acquiring_lock <= '0';
                frame_ready <= '0';
                frame_rd_ptr <= (OTHERS => '0');
                buffer_overflow <= '0';
                
            ELSE
                buffer_overflow <= '0';
                
                -- Clear frame_ready when acknowledged
                IF frame_ack = '1' THEN
                    frame_ready <= '0';
                END IF;
                
                -- Always shift in new bits to both registers
                IF rx_bit_valid = '1' THEN
                    -- MSB-FIRST: Shift LEFT so first bit ends up at position 23
                    sync_shift_bits <= sync_shift_bits(22 DOWNTO 0) & rx_bit;
                    byte_shift_reg <= byte_shift_reg(6 DOWNTO 0) & rx_bit;
                END IF;
                
                -- State machine
                CASE state IS
                    ------------------------------------------------------
                    -- HUNTING: Looking for initial sync
                    ------------------------------------------------------
                    WHEN HUNTING =>
                        acquiring_lock <= '1';  -- We're trying to acquire lock
                        
                        IF rx_bit_valid = '1' THEN
                            -- Use conservative threshold when hunting
                            threshold_to_use := HUNTING_THRESHOLD;
                            
                            hamming_dist := calc_hamming_distance(
                                sync_shift_bits,
                                SYNC_WORD
                            );
                            
                            IF hamming_dist <= threshold_to_use THEN
                                -- Found potential sync!
                                frame_byte_count <= 0;
                                bit_count <= (OTHERS => '0');
                                sync_bit_count <= (OTHERS => '0');
                                state <= LOCKED;
                                
                                -- Track consecutive good detections
                                IF consecutive_good < LOCK_FRAMES THEN
                                    consecutive_good <= consecutive_good + 1;
                                ELSE
                                    -- Achieved stable lock
                                    lock_status <= '1';
                                    acquiring_lock <= '0';
                                    missed_sync_count <= 0;
                                END IF;
                            END IF;
                        END IF;
                    
                    ------------------------------------------------------
                    -- LOCKED: Collecting frame payload
                    ------------------------------------------------------
                    WHEN LOCKED =>
                        IF rx_bit_valid = '1' THEN
                            bit_count <= bit_count + 1;
                            sync_bit_count <= sync_bit_count + 1;
                            
                            IF bit_count = 7 THEN
                                -- Byte complete (MSB-first assembly)
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
                                    -- Frame payload complete
                                    -- Signal frame is ready for output
                                    IF frame_ready = '0' THEN
                                        frame_ready <= '1';
                                        frame_rd_ptr <= frame_start_ptr;
                                        frames_count <= frames_count + 1;
                                    ELSE
                                        -- Output process hasn't taken previous frame yet
                                        errors_count <= errors_count + 1;
                                    END IF;
                                    
                                    frame_start_ptr <= wr_ptr;
                                    frame_byte_count <= 0;
                                    
                                    -- Now expect next sync word
                                    state <= VERIFYING_SYNC;
                                    sync_bit_count <= (OTHERS => '0');
                                    sync_shift_bits <= (OTHERS => '0');  -- AI!!!
                                END IF;
                            END IF;
                        END IF;
                    
                    ------------------------------------------------------
                    -- VERIFYING_SYNC: Check for next sync at expected position
                    ------------------------------------------------------
                    WHEN VERIFYING_SYNC =>
                        IF rx_bit_valid = '1' THEN
                            sync_bit_count <= sync_bit_count + 1;
                            
                            -- After collecting 24 bits, verify it's a sync word
                            IF sync_bit_count = 23 THEN
                                -- Choose threshold based on lock status
                                IF lock_status = '1' THEN
                                    -- Already locked: use relaxed threshold (flywheel)
                                    threshold_to_use := LOCKED_THRESHOLD;
                                ELSE
                                    -- Still acquiring lock: use strict threshold
                                    threshold_to_use := HUNTING_THRESHOLD;
                                END IF;
                                
                                hamming_dist := calc_hamming_distance(
                                    sync_shift_bits,
                                    SYNC_WORD
                                );
                                
                                IF hamming_dist <= threshold_to_use THEN
                                    -- Good! Next sync found where expected
                                    missed_sync_count <= 0;
                                    
                                    IF acquiring_lock = '1' THEN
                                        -- Still building confidence
                                        IF consecutive_good < LOCK_FRAMES - 1 THEN
                                            consecutive_good <= consecutive_good + 1;
                                        ELSE
                                            -- Achieved stable lock
                                            lock_status <= '1';
                                            acquiring_lock <= '0';
                                            consecutive_good <= LOCK_FRAMES;
                                        END IF;
                                    ELSE
                                        -- Already locked, maintain it
                                        consecutive_good <= LOCK_FRAMES;
                                    END IF;
                                    
                                    -- Continue with next frame
                                    state <= LOCKED;
                                    bit_count <= (OTHERS => '0');
                                    
                                ELSE
                                    -- Missed expected sync!
                                    IF lock_status = '1' THEN
                                        -- We're locked: use flywheel tolerance
                                        IF missed_sync_count < FLYWHEEL_TOLERANCE THEN
                                            -- Tolerate this miss, keep going
                                            missed_sync_count <= missed_sync_count + 1;
                                            state <= LOCKED;
                                            bit_count <= (OTHERS => '0');
                                            
                                            -- Note the error but stay locked
                                            errors_count <= errors_count + 1;
                                        ELSE
                                            -- Too many misses, lost lock
                                            lock_status <= '0';
                                            consecutive_good <= 0;
                                            missed_sync_count <= 0;
                                            state <= HUNTING;
                                            errors_count <= errors_count + 1;
                                        END IF;
                                    ELSE
                                        -- Still acquiring lock: any miss sends us back to hunting
                                        consecutive_good <= 0;
                                        state <= HUNTING;
                                        errors_count <= errors_count + 1;
                                    END IF;
                                END IF;
                            ELSE
                                -- Still collecting sync bits, stay in this state
                                NULL;
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
