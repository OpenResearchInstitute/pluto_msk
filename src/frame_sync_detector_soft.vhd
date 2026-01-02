------------------------------------------------------------------------------------------------------
-- Frame Sync Detector with Soft Decision Support (frame_sync_detector_soft.vhd)
------------------------------------------------------------------------------------------------------
-- 
-- This is a variant of frame_sync_detector.vhd that additionally buffers quantized
-- soft decision values for the downstream soft Viterbi decoder.
--
------------------------------------------------------------------------------------------------------
-- SOFT DECISION CORRELATION (from original frame_sync_detector):
-- Instead of counting bit mismatches (hard decision), we compute:
--   correlation = ?(soft_sample[i] × sync_bipolar[i])
-- Where sync_bipolar[i] = +1 if SYNC_WORD bit is '1', -1 if '0'
--
-- This preserves confidence information from the demodulator, giving us:
--   - Better detection at low SNR
--   - Full benefit of optimized PSLR sync word
--   - Sharp correlation peak with suppressed sidelobes
------------------------------------------------------------------------------------------------------
-- SOFT VITERBI INTEGRATION (NEW in this variant):
-- 
-- In addition to the byte stream output (m_axis_*), this module outputs a
-- stream of 3-bit quantized soft values (m_axis_soft_bit_*) for use by the
-- soft Viterbi decoder in ov_frame_decoder_soft.
--
-- Data flow:
--   1. As each bit arrives during LOCKED state, we:
--      a. Assemble bytes as usual (for m_axis output)
--      b. Quantize the 16-bit soft value to 3 bits and store in soft_frame_buffer
--   
--   2. When frame is complete (268 bytes = 2144 bits):
--      a. Output 268 bytes via m_axis_* interface
--      b. Then output 2144 3-bit soft values via m_axis_soft_bit_* interface
--
--   3. The downstream ov_frame_decoder_soft receives both streams:
--      - Bytes for hard decision path (backwards compatibility)
--      - Soft values for soft Viterbi decoder (~2-3 dB coding gain)
--
------------------------------------------------------------------------------------------------------
-- FEATURES:
-- 1. Frame Tracking: Knows exactly where to expect next sync word
-- 2. Flywheel: Tolerates missed syncs during brief interference (stays locked)
-- 3. Adaptive Threshold: Stricter when hunting, more relaxed when locked
-- 4. Better lock management: Distinguishes between acquiring lock vs maintaining lock
-- 5. Correlation-based detection using soft decisions
-- 6. NEW: Soft value buffering and streaming for soft Viterbi decoder
------------------------------------------------------------------------------------------------------
-- by Open Research Institute
-- Enhanced with soft-decision correlation and soft Viterbi support
------------------------------------------------------------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;


ENTITY frame_sync_detector_soft IS
    GENERIC (
        -- Sync word: 0x02B8DB (24 bits, MSB-first)
        SYNC_WORD           : std_logic_vector(23 DOWNTO 0) := x"02B8DB";
        PAYLOAD_BYTES       : NATURAL := 268;
        
        ------------------------------------------------------------------------
        -- Correlation Threshold Tuning Guide
        ------------------------------------------------------------------------
        -- The soft input (s_axis_soft_tdata) comes from msk_demodulator.rx_data_soft
        -- which is data_f1_sum - data_f2_sum (16-bit signed).
        --
        -- Typical soft values depend on:
        --   - ADC input level and scaling
        --   - Costas loop gain settings
        --   - Integration period
        --
        -- CALIBRATION PROCEDURE:
        -- 1. Connect debug_correlation to a register or ILA
        -- 2. Transmit known sync words and observe peak correlation
        -- 3. Set HUNTING_THRESHOLD ? 70-80% of observed peak
        -- 4. Set LOCKED_THRESHOLD ? 40-50% of observed peak (flywheel mode)
        --
        -- EXAMPLE: If soft values are ±4000 nominal at good SNR:
        --   Peak correlation ? 24 × 4000 = 96,000
        --   HUNTING_THRESHOLD ? 72,000 (75%)
        --   LOCKED_THRESHOLD ? 48,000 (50%)
        --
        -- Conservative starting values (adjust after measurement):
        -- Start moderate - observe debug_corr_peak and adjust
        HUNTING_THRESHOLD   : INTEGER := 10000;  -- Moderate for initial testing
        LOCKED_THRESHOLD    : INTEGER := 5000;   -- More tolerant when locked
        ------------------------------------------------------------------------
        
        -- How many consecutive missed syncs before declaring lock lost
        FLYWHEEL_TOLERANCE  : NATURAL := 2;
        
        -- How many consecutive good frames needed to declare lock acquired
        LOCK_FRAMES         : NATURAL := 3;
        
        BUFFER_DEPTH        : NATURAL := 11;
        
        -- Soft value width (3-bit quantization for Viterbi)
        SOFT_WIDTH          : NATURAL := 3
    );
    PORT (
        clk             : IN  std_logic;
        reset           : IN  std_logic;
        
        -- BIT Input Interface (hard decision, still used for byte assembly)
        rx_bit          : IN  std_logic;
        rx_bit_valid    : IN  std_logic;

        ------------------------------------------------------------------------
        -- Soft Decision Interface
        ------------------------------------------------------------------------
        -- s_axis_soft_tdata must be SYNCHRONOUS with rx_bit_valid!
        -- Both signals come from msk_demodulator:
        --   rx_bit       ? rx_data      (hard decision)
        --   rx_bit_valid ? rx_dvalid    (symbol strobe)
        --   s_axis_soft  ? rx_data_soft (16-bit soft metric)
        --
        -- Polarity: Positive = likely '1', Negative = likely '0'
        -- Magnitude = confidence (larger |value| = stronger decision)
        ------------------------------------------------------------------------
        s_axis_soft_tdata  : IN  signed(15 DOWNTO 0);  -- Soft decision input
        m_axis_soft_tdata  : OUT signed(15 DOWNTO 0);  -- Soft decision passthrough
        
        -- AXIS Master Interface - Bytes (to decoder)
        m_axis_tdata    : OUT std_logic_vector(7 DOWNTO 0);
        m_axis_tvalid   : OUT std_logic;
        m_axis_tready   : IN  std_logic;
        m_axis_tlast    : OUT std_logic;
        
        -- AXIS Master Interface - Soft bits (to decoder)
        -- Outputs 2144 3-bit soft values AFTER the 268 bytes
        m_axis_soft_bit_tdata  : OUT std_logic_vector(SOFT_WIDTH-1 DOWNTO 0);
        m_axis_soft_bit_tvalid : OUT std_logic;
        m_axis_soft_bit_tready : IN  std_logic;
        m_axis_soft_bit_tlast  : OUT std_logic;
        
        -- Status Outputs
        frame_sync_locked     : OUT std_logic;
        frames_received       : OUT std_logic_vector(31 DOWNTO 0);
        frame_sync_errors     : OUT std_logic_vector(31 DOWNTO 0);
        frame_buffer_overflow : OUT std_logic;
        
        -- Debug outputs
        debug_state           : OUT std_logic_vector(2 DOWNTO 0);
        debug_missed_syncs    : OUT std_logic_vector(3 DOWNTO 0);
        debug_consecutive_good: OUT std_logic_vector(3 DOWNTO 0);
        
        -- Correlation debug outputs (useful for threshold tuning)
        debug_correlation     : OUT signed(31 DOWNTO 0);  -- Current correlation
        debug_corr_peak       : OUT signed(31 DOWNTO 0);  -- Peak correlation seen (for calibration)
        
        -- Additional debug for troubleshooting
        debug_soft_current    : OUT signed(15 DOWNTO 0);  -- Current soft input value
        debug_bit_count       : OUT std_logic_vector(31 DOWNTO 0)  -- Total bits received
    );
END ENTITY frame_sync_detector_soft;


ARCHITECTURE rtl OF frame_sync_detector_soft IS

    ----------------------------------------------------------------------------
    -- Soft Decision Shift Register for Correlation
    ----------------------------------------------------------------------------
    -- We maintain 24 soft samples (one per sync word bit)
    -- Each sample is 16-bit signed from the demodulator
    TYPE soft_shift_array_t IS ARRAY(0 TO 23) OF signed(15 DOWNTO 0);
    SIGNAL soft_shift_reg : soft_shift_array_t;

    -- Bit-level shift for hard decisions (still needed for byte assembly)
    SIGNAL sync_shift_bits : std_logic_vector(23 DOWNTO 0);
    SIGNAL sync_bit_count  : unsigned(4 DOWNTO 0);  -- Counts 0-23
    
    -- Byte assembly for output (MSB shifts in from left)
    SIGNAL byte_shift_reg  : std_logic_vector(7 DOWNTO 0);
    SIGNAL bit_count       : unsigned(2 DOWNTO 0);
    
    -- Circular buffer for BYTES (after sync found)
    CONSTANT BUFFER_SIZE : NATURAL := 2**BUFFER_DEPTH;
    TYPE byte_buffer_t IS ARRAY(0 TO BUFFER_SIZE-1) OF std_logic_vector(7 DOWNTO 0);
    SIGNAL circ_buffer : byte_buffer_t;
    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF circ_buffer : SIGNAL IS "block";
    
    -- Soft frame buffer (one frame worth of quantized 3-bit soft values)
    CONSTANT PAYLOAD_BITS : NATURAL := PAYLOAD_BYTES * 8;  -- 2144
    TYPE soft_frame_buffer_t IS ARRAY(0 TO PAYLOAD_BITS-1) OF 
        std_logic_vector(SOFT_WIDTH-1 DOWNTO 0);
    SIGNAL soft_frame_buffer : soft_frame_buffer_t;
    SIGNAL frame_soft_idx : natural RANGE 0 TO PAYLOAD_BITS;
    ATTRIBUTE ram_style OF soft_frame_buffer : SIGNAL IS "block";
    
    SIGNAL wr_ptr : unsigned(BUFFER_DEPTH-1 DOWNTO 0);
    SIGNAL rd_ptr : unsigned(BUFFER_DEPTH-1 DOWNTO 0);
    
    -- Enhanced state machine
    TYPE state_t IS (HUNTING, LOCKED, VERIFYING_SYNC);
    SIGNAL state : state_t := HUNTING;
    
    -- Frame tracking
    SIGNAL frame_start_ptr      : unsigned(BUFFER_DEPTH-1 DOWNTO 0);
    SIGNAL frame_byte_count     : natural range 0 to PAYLOAD_BYTES;
    SIGNAL frames_count         : unsigned(31 DOWNTO 0);
    SIGNAL errors_count         : unsigned(31 DOWNTO 0);
    SIGNAL consecutive_good     : natural range 0 to LOCK_FRAMES;
    SIGNAL missed_sync_count    : natural range 0 to FLYWHEEL_TOLERANCE;
    
    SIGNAL lock_status          : std_logic := '0';
    SIGNAL acquiring_lock       : std_logic := '0';
    
    SIGNAL frame_ready      : std_logic := '0';
    SIGNAL frame_ack        : std_logic := '0';
    SIGNAL frame_rd_ptr     : unsigned(BUFFER_DEPTH-1 DOWNTO 0);
    
    SIGNAL output_active    : std_logic := '0';
    SIGNAL output_count     : natural range 0 to PAYLOAD_BYTES;
    SIGNAL tvalid_int       : std_logic := '0';
    SIGNAL tlast_int        : std_logic := '0';
    
    -- Soft output signals
    SIGNAL soft_output_active   : std_logic := '0';
    SIGNAL soft_output_count    : natural RANGE 0 TO PAYLOAD_BITS;
    SIGNAL soft_tvalid_int      : std_logic := '0';
    SIGNAL soft_tlast_int       : std_logic := '0';
    
    -- Current correlation value (updated each bit)
    SIGNAL correlation_value : signed(31 DOWNTO 0);
    
    -- Peak correlation tracker (for threshold calibration)
    -- Readable via debug output, cleared on reset
    SIGNAL correlation_peak  : signed(31 DOWNTO 0);
    
    -- Debug: count total bits received (to verify data is flowing)
    SIGNAL debug_bits_received : unsigned(31 DOWNTO 0);
    
    ----------------------------------------------------------------------------
    -- Correlation Calculator
    -- Returns: ?(soft_sample[i] × bipolar_coeff[i]) for i = 0..23
    -- 
    -- IMPORTANT: VHDL signal assignments don't take effect until process ends,
    -- so we pass the NEW sample explicitly. The function calculates correlation
    -- "as if" the shift had already happened:
    --   Position 0 = new_sample (just arrived, corresponds to SYNC_WORD bit 0)
    --   Position 1 = soft_samples(0) (corresponds to SYNC_WORD bit 1)
    --   Position 2 = soft_samples(1) (corresponds to SYNC_WORD bit 2)
    --   ... etc
    --   Position 23 = soft_samples(22) (corresponds to SYNC_WORD bit 23)
    --
    -- MSB-FIRST TRANSMISSION:
    --   SYNC_WORD(23) is transmitted FIRST, shifts to position 23
    --   SYNC_WORD(0) is transmitted LAST, arrives at position 0
    --   So shift register position i corresponds to SYNC_WORD(i)
    --
    -- POLARITY (from msk_demodulator):
    --   NEGATIVE soft value ? '1' bit
    --   POSITIVE soft value ? '0' bit
    --
    -- For correlation:
    --   When SYNC bit = '1': we WANT negative soft ? SUBTRACT (negative becomes positive)
    --   When SYNC bit = '0': we WANT positive soft ? ADD (positive stays positive)
    ----------------------------------------------------------------------------
    
    ----------------------------------------------------------------------------
    -- Quantize 16-bit signed soft value to 3-bit unsigned for Viterbi decoder
    ----------------------------------------------------------------------------
    --
    -- PURPOSE:
    --   Convert the 16-bit signed soft decision from msk_demodulator into a
    --   3-bit quantized value suitable for the soft Viterbi decoder.
    --
    -- SOFT VALUE SOURCE (msk_demodulator.vhd):
    --   rx_data_soft <= data_sum WHEN data_bit_enc_t = '0' ELSE -data_sum
    --   where data_sum = data_f1_sum - data_f2_sum (difference of matched filters)
    --
    --   The signal path includes:
    --     1. Costas loop integrate-and-dump (shifted right by SINUSOID_W)
    --     2. Additional shift right by 5 in data_out
    --     3. Two-sample addition (data_f1_signed + data_f1_T)
    --     4. F1 - F2 difference
    --     5. Differential decoding (sign flip based on previous bit)
    --
    -- OBSERVED VALUES:
    --   In simulation loopback (perfect channel): approximately ±360
    --   In hardware with noise: expect a distribution around these values
    --
    -- 3-BIT QUANTIZATION CONVENTION:
    --   000 = Strong '0'    (highest confidence in '0')
    --   001 = Medium '0'
    --   010 = Weak '0'
    --   011 = Erasure/uncertain (near decision boundary)
    --   100 = Weak '1'
    --   101 = Medium '1'
    --   110 = (unused, mapped to medium '1')
    --   111 = Strong '1'    (highest confidence in '1')
    --
    -- THRESHOLD CALIBRATION:
    --   Thresholds are set based on observed rx_data_soft magnitudes.
    --   Current values calibrated for simulation with ±360 nominal:
    --     |soft| > 300  ? Strong decision
    --     |soft| > 150  ? Medium decision
    --     |soft| > 50   ? Weak decision
    --     |soft| < 50   ? Uncertain/erasure
    --
    --   For hardware deployment, monitor rx_data_soft distribution and
    --   adjust thresholds if needed. Could also make configurable via CSR.
    --
    -- POLARITY:
    --   msk_demodulator convention: NEGATIVE soft ? '1', POSITIVE soft ? '0'
    --   Therefore: negative soft ? high quantized value (111 = strong '1')
    --              positive soft ? low quantized value (000 = strong '0')
    --
    ----------------------------------------------------------------------------
    FUNCTION quantize_soft(soft : signed(15 DOWNTO 0)) RETURN std_logic_vector IS
    BEGIN
        -- POLARITY: negative soft = '1' bit, positive soft = '0' bit
        IF soft < -300 THEN
            RETURN "111";  -- Strong '1' (large negative soft)
        ELSIF soft < -150 THEN
            RETURN "101";  -- Medium '1'
        ELSIF soft < -50 THEN
            RETURN "100";  -- Weak '1'
        ELSIF soft < 50 THEN
            RETURN "011";  -- Erasure/uncertain
        ELSIF soft < 150 THEN
            RETURN "010";  -- Weak '0'
        ELSIF soft < 300 THEN
            RETURN "001";  -- Medium '0'
        ELSE
            RETURN "000";  -- Strong '0' (large positive soft)
        END IF;
    END FUNCTION;
    
    FUNCTION calc_correlation(
        soft_samples : soft_shift_array_t;
        new_sample   : signed(15 DOWNTO 0)
    ) RETURN signed IS
        VARIABLE sum : signed(31 DOWNTO 0) := (OTHERS => '0');
        VARIABLE sample : signed(15 DOWNTO 0);
    BEGIN
        FOR i IN 0 TO 23 LOOP
            -- Get the appropriate sample (accounting for pending shift)
            IF i = 0 THEN
                sample := new_sample;
            ELSE
                sample := soft_samples(i - 1);
            END IF;
            
            -- Add or subtract based on expected sync word bit
            -- Position i in shift register corresponds to SYNC_WORD(i)
            -- (MSB transmitted first, shifts to high positions)
            --
            -- After differential decoding in demodulator:
            --   Positive soft ? decoded hard bit '0'
            --   Negative soft ? decoded hard bit '1'
            --
            -- For correlation:
            --   When SYNC bit = '1': expect negative soft ? SUBTRACT (neg becomes pos contribution)
            --   When SYNC bit = '0': expect positive soft ? ADD (pos stays pos contribution)
            IF SYNC_WORD(i) = '1' THEN
                sum := sum - resize(sample, 32);  -- Expect negative soft
            ELSE
                sum := sum + resize(sample, 32);  -- Expect positive soft
            END IF;
        END LOOP;
        RETURN sum;
    END FUNCTION;

BEGIN

    frame_sync_locked <= lock_status;
    frames_received <= std_logic_vector(frames_count);
    frame_sync_errors <= std_logic_vector(errors_count);
    m_axis_tvalid <= tvalid_int;
    m_axis_tlast <= tlast_int;
    
    -- Passthrough soft decisions (for downstream use)
    m_axis_soft_tdata <= s_axis_soft_tdata;
    
    -- Debug outputs
    WITH state SELECT debug_state <=
        "001" WHEN HUNTING,
        "010" WHEN LOCKED,
        "011" WHEN VERIFYING_SYNC,
        "000" WHEN OTHERS;
    
    debug_missed_syncs <= std_logic_vector(to_unsigned(missed_sync_count, 4));
    debug_consecutive_good <= std_logic_vector(to_unsigned(consecutive_good, 4));
    debug_correlation <= correlation_value;
    debug_corr_peak <= correlation_peak;
    debug_soft_current <= s_axis_soft_tdata;  -- See what soft values look like
    debug_bit_count <= std_logic_vector(debug_bits_received);  -- Verify bits flowing

    ------------------------------------------------------------------------------
    -- Main Process: Frame Tracking with Flywheel (Correlator Version)
    ------------------------------------------------------------------------------
    reception_proc: PROCESS(clk)
        VARIABLE corr_result : signed(31 DOWNTO 0);
        VARIABLE assembled_byte : std_logic_vector(7 DOWNTO 0);
        VARIABLE threshold_to_use : integer;
    BEGIN
        IF rising_edge(clk) THEN
            IF reset = '1' THEN
                -- Initialize soft shift register
                FOR i IN 0 TO 23 LOOP
                    soft_shift_reg(i) <= (OTHERS => '0');
                END LOOP;
                
                sync_shift_bits <= (OTHERS => '0');
                sync_bit_count <= (OTHERS => '0');
                byte_shift_reg <= (OTHERS => '0');
                bit_count <= (OTHERS => '0');
                wr_ptr <= (OTHERS => '0');
                state <= HUNTING;
                frame_start_ptr <= (OTHERS => '0');
                frame_byte_count <= 0;
                frame_soft_idx <= 0;
                frames_count <= (OTHERS => '0');
                errors_count <= (OTHERS => '0');
                consecutive_good <= 0;
                missed_sync_count <= 0;
                lock_status <= '0';
                acquiring_lock <= '0';
                frame_ready <= '0';
                frame_rd_ptr <= (OTHERS => '0');
                frame_buffer_overflow <= '0';
                correlation_value <= (OTHERS => '0');
                correlation_peak <= (OTHERS => '0');  -- Clear peak on reset
                debug_bits_received <= (OTHERS => '0');  -- Clear bit counter
                
            ELSE
                frame_buffer_overflow <= '0';
                
                -- Clear frame_ready when acknowledged
                IF frame_ack = '1' THEN
                    frame_ready <= '0';
                END IF;
                
                -- Always shift in new samples when valid
                IF rx_bit_valid = '1' THEN
                    -- Count bits for debug (verify data is flowing!)
                    debug_bits_received <= debug_bits_received + 1;
                    
                    -- Shift soft samples (newest at position 0, oldest at 23)
                    FOR i IN 23 DOWNTO 1 LOOP
                        soft_shift_reg(i) <= soft_shift_reg(i-1);
                    END LOOP;
                    soft_shift_reg(0) <= s_axis_soft_tdata;
                    
                    -- Also shift hard decision bits (for byte assembly)
                    sync_shift_bits <= sync_shift_bits(22 DOWNTO 0) & rx_bit;
                    byte_shift_reg <= byte_shift_reg(6 DOWNTO 0) & rx_bit;
                END IF;
                
                -- State machine
                CASE state IS
                    ------------------------------------------------------
                    -- HUNTING: Looking for initial sync using correlation
                    ------------------------------------------------------
                    WHEN HUNTING =>
                        acquiring_lock <= '1';
                        
                        IF rx_bit_valid = '1' THEN
                            -- Calculate correlation including the new sample
                            -- (signal assignments pending, so we pass new sample explicitly)
                            corr_result := calc_correlation(soft_shift_reg, s_axis_soft_tdata);
                            correlation_value <= corr_result;
                            
                            -- Track peak correlation for threshold calibration
                            IF corr_result > correlation_peak THEN
                                correlation_peak <= corr_result;
                            END IF;
                            
                            -- Use conservative threshold when hunting
                            threshold_to_use := HUNTING_THRESHOLD;
                            
                            -- Check if correlation exceeds threshold
                            IF corr_result >= to_signed(threshold_to_use, 32) THEN
                                -- Found potential sync!
                                frame_byte_count <= 0;
                                bit_count <= (OTHERS => '0');
                                sync_bit_count <= (OTHERS => '0');
                                frame_start_ptr <= wr_ptr;
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
                    -- LOCKED: Collecting frame payload (bytes AND soft values)
                    ------------------------------------------------------
                    WHEN LOCKED =>
                        IF rx_bit_valid = '1' THEN
                            -- Store quantized soft value in ARRIVAL order.
                            -- frame_soft_idx counts 0, 1, 2, ... as bits arrive.
                            -- The decoder will handle deinterleaving and MSB-first correction.
                            IF frame_soft_idx < PAYLOAD_BITS THEN
                                soft_frame_buffer(frame_soft_idx) <= 
                                    quantize_soft(s_axis_soft_tdata);
                                frame_soft_idx <= frame_soft_idx + 1;
                            END IF;
                            
                            bit_count <= bit_count + 1;
                            
                            IF bit_count = 7 THEN
                                -- Byte complete (MSB-first assembly)
                                -- NOTE: byte_shift_reg hasn't been updated yet (signal assignment pending)
                                -- so we must manually include the current rx_bit
                                assembled_byte := byte_shift_reg(6 DOWNTO 0) & rx_bit;
                                
                                -- Write to circular buffer
                                circ_buffer(to_integer(wr_ptr)) <= assembled_byte;
                                wr_ptr <= wr_ptr + 1;
                                
                                IF wr_ptr + 1 = rd_ptr THEN
                                    frame_buffer_overflow <= '1';
                                    errors_count <= errors_count + 1;
                                END IF;
                                
                                bit_count <= (OTHERS => '0');
                                
                                IF frame_byte_count < PAYLOAD_BYTES - 1 THEN
                                    frame_byte_count <= frame_byte_count + 1;
                                ELSE
                                    -- Frame payload complete
                                    IF frame_ready = '0' THEN
                                        frame_ready <= '1';
                                        frame_rd_ptr <= frame_start_ptr;
                                        frames_count <= frames_count + 1;
                                    ELSE
                                        -- Output process hasn't taken previous frame yet
                                        errors_count <= errors_count + 1;
                                    END IF;
                                    
                                    frame_byte_count <= 0;
                                    frame_soft_idx <= 0;  -- Reset soft index for next frame
                                    state <= VERIFYING_SYNC;
                                    sync_bit_count <= (OTHERS => '0');
                                END IF;
                            END IF;
                        END IF;
                    
                    ------------------------------------------------------
                    -- VERIFYING_SYNC: Check for next sync using correlation
                    ------------------------------------------------------
                    WHEN VERIFYING_SYNC =>
                        IF rx_bit_valid = '1' THEN
                            sync_bit_count <= sync_bit_count + 1;
                            
                            -- After collecting 24 bits, verify via correlation
                            IF sync_bit_count = 23 THEN
                                -- Calculate correlation (include new sample in calculation)
                                corr_result := calc_correlation(soft_shift_reg, s_axis_soft_tdata);
                                correlation_value <= corr_result;
                                
                                -- Track peak correlation for threshold calibration
                                IF corr_result > correlation_peak THEN
                                    correlation_peak <= corr_result;
                                END IF;
                                
                                -- Choose threshold based on lock status
                                IF lock_status = '1' THEN
                                    threshold_to_use := LOCKED_THRESHOLD;
                                ELSE
                                    threshold_to_use := HUNTING_THRESHOLD;
                                END IF;
                                
                                IF corr_result >= to_signed(threshold_to_use, 32) THEN
                                    -- Good! Sync found where expected
                                    missed_sync_count <= 0;
                                    
                                    IF acquiring_lock = '1' THEN
                                        IF consecutive_good < LOCK_FRAMES - 1 THEN
                                            consecutive_good <= consecutive_good + 1;
                                        ELSE
                                            lock_status <= '1';
                                            acquiring_lock <= '0';
                                            consecutive_good <= LOCK_FRAMES;
                                        END IF;
                                    ELSE
                                        consecutive_good <= LOCK_FRAMES;
                                    END IF;
                                    
                                    state <= LOCKED;
                                    bit_count <= (OTHERS => '0');
                                    frame_start_ptr <= wr_ptr;
                                    
                                ELSE
                                    -- Missed expected sync!
                                    IF lock_status = '1' THEN
                                        IF missed_sync_count < FLYWHEEL_TOLERANCE THEN
                                            missed_sync_count <= missed_sync_count + 1;
                                            state <= LOCKED;
                                            bit_count <= (OTHERS => '0');
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
                                        -- Still acquiring lock: any miss sends us back
                                        consecutive_good <= 0;
                                        state <= HUNTING;
                                        errors_count <= errors_count + 1;
                                    END IF;
                                END IF;
                            END IF;
                        END IF;
                    
                    WHEN OTHERS =>
                        state <= HUNTING;
                END CASE;
                
            END IF;
        END IF;
    END PROCESS reception_proc;

    ------------------------------------------------------------------------------
    -- Output Process: Stream bytes then soft values to AXIS interfaces
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
                soft_output_active <= '0';
                soft_output_count <= 0;
                soft_tvalid_int <= '0';
                soft_tlast_int <= '0';
                frame_ack <= '0';
                rd_ptr <= (OTHERS => '0');
                
            ELSE
                frame_ack <= '0';
                
                -- Start byte output when frame is ready
                IF frame_ready = '1' AND output_active = '0' AND soft_output_active = '0' THEN
                    output_active <= '1';
                    rd_ptr <= frame_rd_ptr;
                    output_count <= 0;
                    frame_ack <= '1';
                END IF;
                
                -- Output bytes
                IF output_active = '1' THEN
                    IF m_axis_tready = '1' OR tvalid_int = '0' THEN
                        m_axis_tdata <= circ_buffer(to_integer(rd_ptr));
                        tvalid_int <= '1';
                        rd_ptr <= rd_ptr + 1;
                        
                        IF output_count = PAYLOAD_BYTES - 1 THEN
                            tlast_int <= '1';
                            output_active <= '0';
                            output_count <= 0;
                            -- Start soft output after bytes complete
                            soft_output_active <= '1';
                            soft_output_count <= 0;
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
                
                -- Output soft values (after bytes are done)
                IF soft_output_active = '1' THEN
                    IF m_axis_soft_bit_tready = '1' OR soft_tvalid_int = '0' THEN
                        m_axis_soft_bit_tdata <= soft_frame_buffer(soft_output_count);
                        soft_tvalid_int <= '1';
                        
                        IF soft_output_count = PAYLOAD_BITS - 1 THEN
                            soft_tlast_int <= '1';
                            soft_output_active <= '0';
                            soft_output_count <= 0;
                        ELSE
                            soft_tlast_int <= '0';
                            soft_output_count <= soft_output_count + 1;
                        END IF;
                    END IF;
                ELSE
                    IF m_axis_soft_bit_tready = '1' THEN
                        soft_tvalid_int <= '0';
                        soft_tlast_int <= '0';
                    END IF;
                END IF;
            END IF;
        END IF;
    END PROCESS output_proc;
    
    -- Connect internal signals to outputs
    m_axis_soft_bit_tvalid <= soft_tvalid_int;
    m_axis_soft_bit_tlast <= soft_tlast_int;

END ARCHITECTURE rtl;
