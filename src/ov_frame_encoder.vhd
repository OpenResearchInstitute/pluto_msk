------------------------------------------------------------------------------------------------------
-- Opulent Voice Protocol Frame Encoder - DUAL MODE (Bit-level or Byte-level Interleaver)
------------------------------------------------------------------------------------------------------
-- Supports both interleaver modes via generic parameter:
--   USE_BIT_INTERLEAVER = TRUE  : 67x32 bit-level (correct protocol, requires large FPGA)
--   USE_BIT_INTERLEAVER = FALSE : 67x4 byte-level (fits PlutoSDR, breaks protocol compatibility)
------------------------------------------------------------------------------------------------------
-- CRITICAL DESIGN PRINCIPLE: TLAST-DRIVEN FRAME COLLECTION
------------------------------------------------------------------------------------------------------
-- This encoder uses AXI-Stream TLAST signal to detect frame boundaries, NOT fixed byte counting!
--
-- WHY THIS MATTERS:
--   When data flows continuously (e.g., FIFO buffering multiple frames), counting to a fixed
--   number of bytes and ignoring tlast causes the encoder to "steal" bytes from the next frame.
--   This creates cascading byte loss:
--     Frame 3: Missing byte 0 (stolen during Frame 2 collection)
--     Frame 4: Missing bytes 0-1 (stolen during Frame 3 collection)
--     Frame 5: Missing bytes 0-2 (stolen during Frame 4 collection)
--     ... continues until no more data available
--
-- CORRECT APPROACH (implemented here):
--   1. IDLE state: Wait for first byte
--   2. COLLECT state: Accept bytes until s_axis_tlast = '1' (frame boundary marker)
--   3. Validate we got exactly PAYLOAD_BYTES (134)
--   4. Process the complete frame through randomization, FEC, interleaving
--   5. Pre-set s_axis_tready = '1' before returning to IDLE for next frame
--
-- This approach:
--   Respects AXI-Stream protocol (tlast marks frame boundaries)
--   Works with continuous data streams (FIFO buffering)
--   Prevents byte stealing across frame boundaries
--   Validates frame size for error detection
--   Works for BOTH bit-level and byte-level interleaving modes
--
-- NEVER count to a fixed byte number and ignore tlast - this violates AXI-Stream protocol!
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY ov_frame_encoder IS
    GENERIC (
        PAYLOAD_BYTES       : NATURAL := 134;
        ENCODED_BYTES       : NATURAL := 268;
        COLLECT_SIZE        : NATURAL := 4;      -- DEPRECATED: No longer used (kept for compatibility)
        ENCODED_BITS        : NATURAL := 2144;   -- Kept for compatibility
        BYTE_WIDTH          : NATURAL := 8;      -- Kept for compatibility
        USE_BIT_INTERLEAVER : BOOLEAN := TRUE;   -- TRUE=bit-level(67x32), FALSE=byte-level(67x4)
        -- Debug bypass controls (must match decoder settings!)
        BYPASS_RANDOMIZE    : BOOLEAN := FALSE;  -- TRUE=skip pre-FEC LFSR randomization
        BYPASS_FEC          : BOOLEAN := FALSE;  -- TRUE=duplicate bytes instead of convolutional encode
        BYPASS_INTERLEAVE   : BOOLEAN := FALSE   -- TRUE=skip 67x32 bit interleaving
    );
    PORT (
        clk          : IN  std_logic;
        aresetn      : IN  std_logic;
        
        -- AXI-Stream Input (from application)
        s_axis_tdata  : IN  std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        s_axis_tvalid : IN  std_logic;
        s_axis_tready : OUT std_logic;
        s_axis_tlast  : IN  std_logic;
        
        -- AXI-Stream Output (to modulator)
        m_axis_tdata  : OUT std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        m_axis_tvalid : OUT std_logic;
        m_axis_tready : IN  std_logic;
        m_axis_tlast  : OUT std_logic;
        
        -- Status outputs
        frames_encoded : OUT std_logic_vector(31 DOWNTO 0);
        encoder_active : OUT std_logic;
        debug_state : OUT std_logic_vector(2 DOWNTO 0);

        -- Randomizer debug outputs
        debug_lfsr        : OUT std_logic_vector(7 DOWNTO 0);
        debug_input_byte  : OUT std_logic_vector(7 DOWNTO 0);
        debug_rand_byte   : OUT std_logic_vector(7 DOWNTO 0);
        debug_rand_active : OUT std_logic;  -- HIGH during RANDOMIZE state

        -- FEC encoder debug outputs (for ILA verification)
        debug_conv_start  : OUT std_logic;
        debug_conv_busy   : OUT std_logic;
        debug_conv_done   : OUT std_logic

    );
END ENTITY ov_frame_encoder;

ARCHITECTURE rtl OF ov_frame_encoder IS

    ------------------------------------------------------------------------------
    -- CCSDS LFSR Functions (for RANDOMIZE - standard pre-FEC randomization)
    ------------------------------------------------------------------------------
    -- Polynomial: x^8 + x^7 + x^5 + x^3 + 1 (CCSDS standard randomizer)
    -- Seed: 0xFF
    -- Period: 255 bits
    -- This is a well-documented standard from CCSDS (Consultative Committee for
    -- Space Data Systems) used in many space communication systems.
    ------------------------------------------------------------------------------
    
    -- Generate 8 output bits from LFSR (for byte-level XOR)
    FUNCTION lfsr_output_byte(seed : std_logic_vector(7 DOWNTO 0)) 
        RETURN std_logic_vector IS
        VARIABLE lfsr : std_logic_vector(7 DOWNTO 0) := seed;
        VARIABLE result : std_logic_vector(7 DOWNTO 0);
        VARIABLE feedback : std_logic;
    BEGIN
        FOR i IN 7 DOWNTO 0 LOOP
            result(i) := lfsr(7);  -- Output bit (MSB)
            feedback := lfsr(7) XOR lfsr(6) XOR lfsr(4) XOR lfsr(2);
            lfsr := lfsr(6 DOWNTO 0) & feedback;
        END LOOP;
        RETURN result;
    END FUNCTION;
    
    -- Compute LFSR state after 8 advances
    FUNCTION lfsr_advance_8(seed : std_logic_vector(7 DOWNTO 0))
        RETURN std_logic_vector IS
        VARIABLE lfsr : std_logic_vector(7 DOWNTO 0) := seed;
        VARIABLE feedback : std_logic;
    BEGIN
        FOR i IN 0 TO 7 LOOP
            feedback := lfsr(7) XOR lfsr(6) XOR lfsr(4) XOR lfsr(2);
            lfsr := lfsr(6 DOWNTO 0) & feedback;
        END LOOP;
        RETURN lfsr;
    END FUNCTION;

    ------------------------------------------------------------------------------
    -- STATE MACHINE DESIGN PHILOSOPHY
    ------------------------------------------------------------------------------
    -- CRITICAL: This encoder uses TLAST-DRIVEN frame detection, NOT fixed byte counting!
    --
    -- WHY: AXI-Stream protocol uses tlast to mark frame boundaries. Ignoring tlast
    --      causes the encoder to "steal" bytes from the next frame when data is
    --      continuously available (e.g., from a buffering FIFO). This causes
    --      cascading byte loss errors across multiple frames.
    --
    -- COLLECT state strategy:
    --   1. Accept bytes one at a time
    --   2. Store each byte in input_buffer[collect_idx]
    --   3. Watch for s_axis_tlast = '1' (frame boundary)
    --   4. When tlast seen, validate we got PAYLOAD_BYTES (134), then process
    --
    -- This works for BOTH byte-level and bit-level interleaving modes because:
    --   - Collection only fills input_buffer
    --   - Interleaving happens later (INTERLEAVE state) on FEC-encoded bits
    --   - Interleaver type doesn't affect how we collect input bytes
    --
    -- NEVER count to a fixed number and ignore tlast - this violates AXI protocol!
    ------------------------------------------------------------------------------
    TYPE state_t IS (
        IDLE,       -- Wait for first byte of frame
        COLLECT,    -- Gather bytes until tlast (AXI-Stream frame boundary marker)
        RANDOMIZE,  -- XOR with randomizer sequence
        PREP_FEC,   -- Prepare for convolutional encoding
        FEC_ENCODE, -- Apply K=7 convolutional code
        INTERLEAVE, -- Shuffle bits (bit-level) or bytes (byte-level) per generic
        OUTPUT      -- Stream encoded frame to modulator
    );
    SIGNAL state : state_t := IDLE;

    TYPE byte_buffer_t IS ARRAY(0 TO PAYLOAD_BYTES-1) OF std_logic_vector(7 DOWNTO 0);
    TYPE bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic;
    
    SIGNAL input_buffer       : byte_buffer_t;
    SIGNAL randomized_buffer  : byte_buffer_t;
    SIGNAL fec_buffer         : bit_buffer_t := (OTHERS => '0');
    SIGNAL interleaved_buffer : bit_buffer_t := (OTHERS => '0');
    
    -- CCSDS LFSR register for randomization
    SIGNAL lfsr_randomize : std_logic_vector(7 DOWNTO 0) := x"FF";

    -- Index counters
    SIGNAL collect_idx : NATURAL RANGE 0 TO PAYLOAD_BYTES;  -- Now collects all bytes until tlast
    SIGNAL byte_idx    : NATURAL RANGE 0 TO ENCODED_BYTES;
    SIGNAL bit_idx     : NATURAL RANGE 0 TO ENCODED_BITS;
    SIGNAL out_idx     : NATURAL RANGE 0 TO ENCODED_BYTES;
    
    -- AXI-Stream control
    SIGNAL s_axis_tready_reg : std_logic := '0';
    SIGNAL m_axis_tdata_reg  : std_logic_vector(BYTE_WIDTH-1 DOWNTO 0) := (OTHERS => '0');
    SIGNAL m_axis_tvalid_reg : std_logic := '0';
    SIGNAL m_axis_tlast_reg  : std_logic := '0';
    
    -- Status counters
    SIGNAL frames_encoded_reg : unsigned(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL encoder_active_reg : std_logic := '0';

    -- Convolutional encoder signals
    SIGNAL encoder_start      : std_logic := '0';
    SIGNAL encoder_busy       : std_logic;
    SIGNAL encoder_done       : std_logic;
    SIGNAL encoder_input_buf  : std_logic_vector(1071 DOWNTO 0);
    SIGNAL encoder_output_buf : std_logic_vector(2143 DOWNTO 0);

    -- preserve the output registers from synthesis optimization
    ATTRIBUTE dont_touch : STRING;
    ATTRIBUTE dont_touch OF m_axis_tvalid_reg : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF m_axis_tdata_reg : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF m_axis_tlast_reg : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF s_axis_tready_reg : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF input_buffer : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF randomized_buffer : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF fec_buffer : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF interleaved_buffer : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF encoder_input_buf : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF encoder_output_buf : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF state : SIGNAL IS "true";
    -- adding these stalled the FIFO from draining past two frames
    --ATTRIBUTE dont_touch OF out_idx : SIGNAL IS "true";
    --ATTRIBUTE dont_touch OF byte_idx : SIGNAL IS "true";
    --ATTRIBUTE dont_touch OF collect_idx : SIGNAL IS "true";

    -- Protect conv_encoder_k7 interface signals (prevent optimization)
    ATTRIBUTE dont_touch OF encoder_start : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF encoder_busy : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF encoder_done : SIGNAL IS "true";
    -- Protect the conv_encoder_k7 instance itself
    ATTRIBUTE dont_touch OF U_ENCODER : LABEL IS "true";

    -- Also force BRAM on the large buffers 
    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF interleaved_buffer : SIGNAL IS "block";
    ATTRIBUTE ram_style OF input_buffer : SIGNAL IS "block";
    ATTRIBUTE ram_style OF randomized_buffer : SIGNAL IS "block";
    ATTRIBUTE ram_style OF fec_buffer : SIGNAL IS "block";


    
    ----------------------------------------------------------------------------
    -- BIT-LEVEL INTERLEAVER (67x4) - For LibreSDR, etc.
    -- Consecutive input bits end up 67 positions apart in output.
    ----------------------------------------------------------------------------
    FUNCTION interleave_address_bit(bit_addr : NATURAL) RETURN NATURAL IS
        -- 67 rows × 32 columns = 2144 bits
        -- Write by rows, read by columns
        CONSTANT NUM_ROWS : NATURAL := 67;
        CONSTANT NUM_COLS : NATURAL := 32;
        VARIABLE row, col : NATURAL;
    BEGIN
        -- Input bit_addr is linear (row-major order: row 0 bits, then row 1, etc.)
        row := bit_addr / NUM_COLS;
        col := bit_addr MOD NUM_COLS;
        
        -- Output in column-major order (column 0 bits, then column 1, etc.)
        RETURN col * NUM_ROWS + row;
    END FUNCTION;

    ----------------------------------------------------------------------------
    -- BYTE-LEVEL INTERLEAVER (67x4) - For PlutoSDR, fits in xc7z010
    ----------------------------------------------------------------------------
    FUNCTION interleave_address_byte(addr : NATURAL) RETURN NATURAL IS
        CONSTANT ROWS : NATURAL := 67;
        CONSTANT COLS : NATURAL := 4;
        VARIABLE row : NATURAL;
        VARIABLE col : NATURAL;
    BEGIN
        row := addr / COLS;
        col := addr MOD COLS;
        RETURN col * ROWS + row;
    END FUNCTION;




BEGIN 

    -- to find the state of the state machine for debug
    debug_state <= "000" WHEN state = IDLE ELSE
               "001" WHEN state = COLLECT ELSE
               "010" WHEN state = RANDOMIZE ELSE
               "011" WHEN state = PREP_FEC ELSE
               "100" WHEN state = FEC_ENCODE ELSE
               "101" WHEN state = INTERLEAVE ELSE
               "110" WHEN state = OUTPUT ELSE
               "111";


    -- Randomizer debug outputs
        debug_lfsr        <= lfsr_randomize;
        debug_input_byte  <= input_buffer(byte_idx) WHEN byte_idx < PAYLOAD_BYTES ELSE x"00";
        debug_rand_byte   <= randomized_buffer(byte_idx) WHEN byte_idx < PAYLOAD_BYTES ELSE x"00";
        debug_rand_active <= '1' WHEN state = RANDOMIZE ELSE '0';

    -- FEC encoder debug
        debug_conv_start <= encoder_start;
        debug_conv_busy  <= encoder_busy;
        debug_conv_done  <= encoder_done;


    -- Convolutional Encoder Instantiation
    U_ENCODER : ENTITY work.conv_encoder_k7
        GENERIC MAP (
            PAYLOAD_BYTES => PAYLOAD_BYTES,
            ENCODED_BYTES => ENCODED_BYTES
        )
        PORT MAP (
            clk           => clk,
            aresetn       => aresetn,
            start         => encoder_start,
            busy          => encoder_busy,
            done          => encoder_done,
            input_buffer  => encoder_input_buf,
            output_buffer => encoder_output_buf
        );

    -- AXI-Stream output assignments
    s_axis_tready  <= s_axis_tready_reg;
    m_axis_tdata   <= m_axis_tdata_reg;
    m_axis_tvalid  <= m_axis_tvalid_reg;
    m_axis_tlast   <= m_axis_tlast_reg;
    
    -- Status outputs
    frames_encoded <= std_logic_vector(frames_encoded_reg);
    encoder_active <= encoder_active_reg;

    -- Main State Machine
    PROCESS(clk, aresetn)
        VARIABLE out_bit_idx : NATURAL RANGE 0 TO ENCODED_BITS-1;
    BEGIN
        IF aresetn = '0' THEN
            state <= IDLE;
            collect_idx <= 0;
            byte_idx <= 0;
            bit_idx <= 0;
            out_idx <= 0;
            s_axis_tready_reg <= '0';
            m_axis_tdata_reg <= (OTHERS => '0');
            m_axis_tvalid_reg <= '0';
            m_axis_tlast_reg <= '0';
            encoder_start <= '0';
            frames_encoded_reg <= (OTHERS => '0');
            encoder_active_reg <= '0';
            lfsr_randomize <= x"FF";  -- Reset LFSR to seed
            
        ELSIF rising_edge(clk) THEN
            encoder_start <= '0';
            
            CASE state IS
                
                ----------------------------------------------------------------------
                -- IDLE: Wait for first byte of frame
                ----------------------------------------------------------------------
                -- Ready to accept data. When valid data arrives, capture first byte
                -- and check for tlast (single-byte frame, unlikely but possible).
                ----------------------------------------------------------------------
                WHEN IDLE =>
                    s_axis_tready_reg <= '1';  -- Always ready in IDLE
                    m_axis_tvalid_reg <= '0';
                    m_axis_tlast_reg <= '0';
                    encoder_active_reg <= '0';
                    
                    IF s_axis_tvalid = '1' AND s_axis_tready_reg = '1' THEN
                        -- Capture first byte
                        input_buffer(0) <= s_axis_tdata;
                        collect_idx <= 1;
                        encoder_active_reg <= '1';
                        
                        -- Check for single-byte frame (shouldn't happen for 134-byte frames)
                        IF s_axis_tlast = '1' THEN
                            s_axis_tready_reg <= '0';
                            REPORT "Single-byte frame detected (unexpected)" SEVERITY WARNING;
                            byte_idx <= 0;
                            lfsr_randomize <= x"FF";  -- Reset LFSR BEFORE entering RANDOMIZE
                            state <= RANDOMIZE;
                        ELSE
                            state <= COLLECT;
                        END IF;
                    END IF;


                ----------------------------------------------------------------------
                -- COLLECT: Gather bytes until tlast (AXI-Stream frame boundary)
                ----------------------------------------------------------------------
                -- This is the CRITICAL state that prevents byte loss!
                --
                -- Strategy:
                --   - Keep s_axis_tready = 1 (accept data)
                --   - Capture each byte to input_buffer[collect_idx]
                --   - Increment collect_idx
                --   - WATCH FOR TLAST (frame boundary marker)
                --   - When tlast seen, validate frame size and proceed to encoding
                --
                -- Why not count to 134 and ignore tlast?
                --   Because when FIFO has next frame buffered, we'd keep accepting
                --   bytes past the frame boundary, "stealing" from the next frame.
                --   This causes cascading byte loss (Frame 3 missing byte 0, 
                --   Frame 4 missing bytes 0-1, etc.)
                --
                -- TLAST is the ONLY reliable frame boundary in AXI-Stream protocol!
                ----------------------------------------------------------------------
                WHEN COLLECT =>
                    s_axis_tready_reg <= '1';  -- Keep accepting data
                    
                    IF s_axis_tvalid = '1' AND s_axis_tready_reg = '1' THEN
                        -- Capture byte
                        input_buffer(collect_idx) <= s_axis_tdata;
                        
                        -- Check for frame boundary (tlast = end of frame)
                        IF s_axis_tlast = '1' THEN
                            -- Frame complete! Stop accepting data
                            s_axis_tready_reg <= '0';
                            
                            -- Validate frame size (collect_idx is 0-indexed, so +1 for count)
                            IF collect_idx + 1 /= PAYLOAD_BYTES THEN
                                REPORT "Frame size mismatch: expected " & 
                                       INTEGER'IMAGE(PAYLOAD_BYTES) & " bytes, got " & 
                                       INTEGER'IMAGE(collect_idx + 1) & " bytes" 
                                       SEVERITY WARNING;
                            END IF;
                            
                            -- Proceed to randomization (even if size is wrong, try to process)
                            byte_idx <= 0;
                            lfsr_randomize <= x"FF";  -- Reset LFSR BEFORE entering RANDOMIZE
                            state <= RANDOMIZE;
                        ELSE
                            -- Not end of frame yet, continue collecting
                            collect_idx <= collect_idx + 1;
                            
                            -- Safety check: prevent buffer overflow
                            IF collect_idx >= PAYLOAD_BYTES - 1 THEN
                                REPORT "Collected " & INTEGER'IMAGE(PAYLOAD_BYTES) & 
                                       " bytes but tlast not seen yet! Frame too large!" 
                                       SEVERITY ERROR;
                                s_axis_tready_reg <= '0';
                                byte_idx <= 0;
                                lfsr_randomize <= x"FF";  -- Reset LFSR BEFORE entering RANDOMIZE
                                state <= RANDOMIZE;  -- Try to process what we have
                            END IF;
                        END IF;
                    END IF;

                -- RANDOMIZE: XOR with CCSDS LFSR sequence (pre-FEC randomization)
                -- This is a standard technique from CCSDS used to whiten data before FEC.
                -- LFSR is reset to 0xFF before entering this state (during transition)
                -- BYPASS_RANDOMIZE=TRUE: Direct copy (for testing)
                WHEN RANDOMIZE =>
                    IF byte_idx < PAYLOAD_BYTES THEN
                        IF BYPASS_RANDOMIZE THEN
                            -- BYPASS: Direct copy, no randomization
                            randomized_buffer(byte_idx) <= input_buffer(byte_idx);
                        ELSE
                            -- XOR input byte with 8 LFSR output bits
                            randomized_buffer(byte_idx) <= 
                                input_buffer(byte_idx) XOR lfsr_output_byte(lfsr_randomize);
                            -- Advance LFSR by 8 positions for next byte
                            lfsr_randomize <= lfsr_advance_8(lfsr_randomize);
                        END IF;
                        byte_idx <= byte_idx + 1;
                    ELSE
                        byte_idx <= 0;
                        state <= PREP_FEC;
                    END IF;

                ----------------------------------------------------------------------
                -- PREP_FEC: Pack randomized bytes into encoder input buffer
                -- Only start the actual encoder if NOT bypassing FEC
                ----------------------------------------------------------------------
                WHEN PREP_FEC =>
                    IF byte_idx < PAYLOAD_BYTES THEN
                        FOR j IN 0 TO 7 LOOP
                            encoder_input_buf(byte_idx*8 + j) <= randomized_buffer(byte_idx)(j);
                        END LOOP;
                        byte_idx <= byte_idx + 1;
                    ELSE
                        IF NOT BYPASS_FEC THEN
                            encoder_start <= '1';  -- Only start real encoder if not bypassing
                        END IF;
                        state <= FEC_ENCODE;
                    END IF;

                ----------------------------------------------------------------------
                -- FEC_ENCODE: Apply convolutional encoding OR duplicate bytes
                -- BYPASS_FEC=TRUE: Duplicate 134 bytes -> 268 bytes (no G1/G2 correlation)
                -- BYPASS_FEC=FALSE: Wait for K=7 convolutional encoder to complete
                ----------------------------------------------------------------------
                WHEN FEC_ENCODE =>
                    encoder_start <= '0';
                    
                    IF BYPASS_FEC THEN
                        -- BYPASS: Duplicate input bits without encoding
                        -- Output format: [copy1(1072 bits)][copy2(1072 bits)] = 2144 bits
                        -- TRUE PASSTHROUGH: No bit reversal - preserves byte patterns for testing
                        -- This allows verification that 0x00,0x01,0x02... comes out unchanged
                        FOR i IN 0 TO 1071 LOOP
                            fec_buffer(i) <= encoder_input_buf(i);           -- First copy, NOT reversed
                            fec_buffer(i + 1072) <= encoder_input_buf(i);    -- Second copy, NOT reversed
                        END LOOP;
                        
                        IF USE_BIT_INTERLEAVER THEN
                            bit_idx <= 0;
                        ELSE
                            byte_idx <= 0;
                        END IF;
                        state <= INTERLEAVE;
                        
                    ELSIF encoder_done = '1' THEN
                        -- Real FEC: Copy encoder output to fec_buffer (MSB-first to bit-buffer)
                        FOR i IN 0 TO ENCODED_BITS-1 LOOP
                            fec_buffer(i) <= encoder_output_buf(ENCODED_BITS - 1 - i);
                        END LOOP;
                        
                        IF USE_BIT_INTERLEAVER THEN
                            bit_idx <= 0;
                        ELSE
                            byte_idx <= 0;
                        END IF;
                        state <= INTERLEAVE;
                    END IF;

                ------------------------------------------------------------------------
                -- INTERLEAVE: Dual-mode implementation
                -- BYPASS_INTERLEAVE=TRUE: Direct copy (for testing)
                ------------------------------------------------------------------------
                WHEN INTERLEAVE =>
                    IF USE_BIT_INTERLEAVER THEN
                        -- BIT-LEVEL mode: Process 1 bit per clock (2144 clocks)
                        IF bit_idx < ENCODED_BITS THEN
                            IF BYPASS_INTERLEAVE THEN
                                -- BYPASS: Direct copy, no interleaving
                                interleaved_buffer(bit_idx) <= fec_buffer(bit_idx);
                            ELSE
                                -- Apply 67x32 bit interleaving
                                interleaved_buffer(interleave_address_bit(bit_idx)) <= fec_buffer(bit_idx);
                            END IF;
                            bit_idx <= bit_idx + 1;
                        ELSE
                            out_idx <= 0;
                            state <= OUTPUT;
                            m_axis_tvalid_reg <= '0';
                        END IF;
                    ELSE
                        -- BYTE-LEVEL mode: Process 1 byte per clock (268 clocks)
                        IF byte_idx < ENCODED_BYTES THEN
                            IF BYPASS_INTERLEAVE THEN
                                -- BYPASS: Direct copy, no interleaving
                                FOR j IN 0 TO 7 LOOP
                                    interleaved_buffer(byte_idx*8 + j) <= fec_buffer(byte_idx*8 + j);
                                END LOOP;
                            ELSE
                                -- Apply 67x4 byte interleaving
                                FOR j IN 0 TO 7 LOOP
                                    interleaved_buffer(interleave_address_byte(byte_idx)*8 + j) <= 
                                        fec_buffer(byte_idx*8 + j);
                                END LOOP;
                            END IF;
                            byte_idx <= byte_idx + 1;
                        ELSE
                            out_idx <= 0;
                            state <= OUTPUT;
                            m_axis_tvalid_reg <= '0';
                        END IF;
                    END IF;




                ----------------------------------------------------------------------
                -- OUTPUT: Stream interleaved bytes to modulator
                ----------------------------------------------------------------------
                -- Send encoded frame one byte at a time via AXI-Stream.
                -- Assert tlast on final byte to mark frame boundary.
                ----------------------------------------------------------------------
                WHEN OUTPUT =>
                    IF out_idx < ENCODED_BYTES THEN
                        IF m_axis_tready = '1' OR m_axis_tvalid_reg = '0' THEN
                            -- Pack 8 bits from interleaved_buffer into output byte
                            FOR j IN 0 TO 7 LOOP
                                out_bit_idx := out_idx*8 + j;
                                m_axis_tdata_reg(j) <= interleaved_buffer(out_bit_idx);
                            END LOOP;
                            m_axis_tvalid_reg <= '1';
                            
                            -- Assert tlast on final byte (AXI-Stream frame boundary)
                            IF out_idx = ENCODED_BYTES - 1 THEN
                                m_axis_tlast_reg <= '1';
                            ELSE
                                m_axis_tlast_reg <= '0';
                            END IF;
                            
                            out_idx <= out_idx + 1;
                        END IF;
                    ELSE

                        -- Frame output complete
                        IF m_axis_tready = '1' THEN
                            m_axis_tvalid_reg <= '0';
                            m_axis_tlast_reg <= '0';
                            
                            -- Pre-set ready for next frame BEFORE going to IDLE
                            -- This ensures s_axis_tready is already high when we
                            -- enter IDLE, preventing one-clock delay in handshake
                            s_axis_tready_reg <= '1';
                            
                            frames_encoded_reg <= frames_encoded_reg + 1;
                            collect_idx <= 0;
                            state <= IDLE;
                        END IF;
                    END IF;
                    
            END CASE;

        END IF;
    END PROCESS;

END ARCHITECTURE rtl;
