--------------------------------------------------------------------------------
-- OV Frame Decoder with Soft-Decision Viterbi
-- ov_frame_decoder_soft.vhd
--------------------------------------------------------------------------------
-- Open Research Institute - Opulent Voice Protocol
--
-- ROLE IN RECEIVE CHAIN:
--   This module reverses the encoding performed by ov_frame_encoder.
--   frame_sync_detector_soft provides 268 bytes of data, or hard values,
--   and 2144 bits of soft decision information, or soft values. These
--   two streams of data are used to produce 134 bytes of baseband frame
--   data (Opulent Voice Frame) to the rx_async_fifo, which then 
--   delivers it to the processor side through a buffer refill call.
--
--------------------------------------------------------------------------------
-- PROCESSING PIPELINE (9 states):
--
--   State            │ Description                           │ Cycles
--   ─────────────────┼───────────────────────────────────────┼─────────
--   IDLE             │ Wait for frame data                   │ 1
--   COLLECT_BYTES    │ Receive 268 bytes                     │ 268
--   COLLECT_SOFT     │ Receive 2144 3-bit soft values        │ 2144
--   EXTRACT          │ Unpack bytes to 2144-bit array        │ 268
--   DEINTERLEAVE     │ Reverse 67×32 bit shuffle             │ 2144
--   PREP_FEC_DECODE  │ Pack G1/G2 soft streams, start Viterbi│ 1
--   FEC_DECODE       │ Wait for Viterbi completion           │ ~2000
--   DERANDOMIZE      │ XOR with CCSDS LFSR                   │ 134
--   OUTPUT           │ Stream 134 decoded bytes              │ 134
--
--   Total: ~5000 cycles per frame at 61.44 MHz ≈ 81 µs
--   Frame period: 40 ms (plenty of margin)
--
--------------------------------------------------------------------------------
-- 67×32 BIT DEINTERLEAVING:
--
--   The encoder writes bits column-wise into a 67-row × 32-column matrix,
--   then reads row-wise. We reverse this. Given linear output position,
--   we find the interleaved source position.
--
--   For deinterleaved position p:
--     row = p / 32
--     col = p MOD 32
--     interleaved_source = col * 67 + row
--
--   This spreads burst errors across 67 bits in the deinterleaved stream,
--   well within the Viterbi decoder's correction capability.
--
--   SOFT VALUE HANDLING:
--   Soft values arrive in MSB-first byte order (matching transmission).
--   The soft_deinterleave_address function combines interleave position lookup
--   and MSB-first byte-to-bit correction.
--
--------------------------------------------------------------------------------
-- SOFT VITERBI DECODER:
--
--   Constraint length: K=7 (64 states)
--   Code rate: r=1/2 (G1=171 octal, G2=133 octal)
--   Traceback depth: 35 (5 * constraint length)
--   Soft width: 3 bits per symbol
--
--   Input format (after deinterleaving):
--     Bit 0: G1[0], Bit 1: G2[0], Bit 2: G1[1], Bit 3: G2[1], ...
--     Packed into separate G1 and G2 vectors for the decoder
--
--   Coding gain: ~2-3 dB over hard decision at BER=10^-5
--
--------------------------------------------------------------------------------
-- CCSDS LFSR DERANDOMIZATION:
--
--   Polynomial: x^8 + x^7 + x^5 + x^3 + 1 (CCSDS standard)
--   Initial state: 0xFF (all ones)
--   Period: 255 bits
--
--   Applied AFTER FEC decoding (reverses encoder's pre-FEC randomization).
--   Purpose: Ensure bit transitions even with constant input data,
--   preventing spectral spurs from repetitive patterns.
--
--   Each byte: output_byte = fec_decoded_byte XOR lfsr_output_byte
--
--------------------------------------------------------------------------------
-- DUAL INPUT STREAMS:
--
--   Stream 1 is on s_axis_* and is 268 bytes long.
--     This is hard decision bytes from frame_sync_detector.
--     It is used for BYPASS_FEC mode and bit extraction.
--     It arrives first.
--
--   Stream 2 is on s_axis_soft_bit_* and is 2144 × 3-bit values long.
--     This is quantized soft decisions from frame_sync_detector.
--     It arrives immediately after Stream 1 completes.
--     000 = strong 0, 111 = strong 1, 011 = erasure
--
--   Both streams must arrive for each frame. The decoder waits for
--   s_axis_tlast on bytes, then collects soft values until
--   s_axis_soft_bit_tlast or count reaches 2144.
--
--------------------------------------------------------------------------------
-- BYPASS MODES (for debugging):
--
--   BYPASS_RANDOMIZE: Skip LFSR derandomization
--     Use when encoder has BYPASS_RANDOMIZE=TRUE
--     Direct copy from FEC output to final output
--
--   BYPASS_FEC: Skip Viterbi decoding
--     Takes first 134 bytes (1072 bits) from deinterleaved stream
--     Useful for testing interleaver without FEC complexity
--     Must match encoder's BYPASS_FEC setting
--
--   BYPASS_INTERLEAVE: Skip 67×32 deinterleaving
--     Direct copy of bits (no matrix transpose)
--     Must match encoder's BYPASS_INTERLEAVE setting
--
--   CRITICAL: Bypass settings MUST match between encoder and decoder!
--
--------------------------------------------------------------------------------
-- RESOURCE USAGE:
--
--   Block RAM:
--     collect_buffer: 268 × 8 bits
--     soft_buffer: 2144 × 3 bits
--     input_bits: 2144 × 1 bit
--     deinterleaved_bits: 2144 × 1 bit
--     deinterleaved_soft: 2144 × 3 bits
--     Viterbi path memory: 64 states × 35 depth × ~7 bits
--
--   DSP: None (all logic-based)
--   LUTs: ~2000 (dominated by Viterbi ACS units)
--
--------------------------------------------------------------------------------
-- GENERICS:
--
--   PAYLOAD_BYTES    : Decoded output size (134 for Opulent Voice)
--   ENCODED_BYTES    : Input frame size (268 = 134 × 2)
--   ENCODED_BITS     : Total bits (2144 = 268 × 8)
--   BYTE_WIDTH       : Always 8
--   SOFT_WIDTH       : Bits per soft value (3)
--   BYPASS_RANDOMIZE : Skip LFSR (must match encoder)
--   BYPASS_FEC       : Skip Viterbi (must match encoder)
--   BYPASS_INTERLEAVE: Skip deinterleaver (must match encoder)
--
--------------------------------------------------------------------------------
-- DEBUG OUTPUTS:
--
--   debug_state        : Current state (0-8, see state encoding below)
--   debug_viterbi_start: Pulses when Viterbi decoder starts
--   debug_viterbi_busy : High while Viterbi is processing
--   debug_viterbi_done : Pulses when Viterbi completes
--   debug_path_metric  : Final path metric (lower = more confident decode)
--
--   State encoding:
--     0000 = IDLE
--     0001 = COLLECT_BYTES
--     0010 = COLLECT_SOFT
--     0011 = EXTRACT
--     0100 = DEINTERLEAVE
--     0101 = PREP_FEC_DECODE
--     0110 = FEC_DECODE
--     0111 = DERANDOMIZE
--     1000 = OUTPUT
--
--------------------------------------------------------------------------------
-- TIMING:
--
--   Clock: 61.44 MHz (PlutoSDR modem clock)
--   Reset: Active-low asynchronous (aresetn)
--   Latency: ~5000 cycles from first input byte to first output byte
--   Throughput: One 134-byte frame per ~81 µs (frame period is 40 ms)
--
--------------------------------------------------------------------------------
-- VERSION HISTORY:
--
--   v1: Initial implementation with hard-decision Viterbi
--   v2: Added soft-decision Viterbi support
--   v3: Removed byte-level interleaver (unused, bit-level only)
--   v4: Cleaned up dead code, improved documentation
--
--------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY ov_frame_decoder_soft IS
    GENERIC (
        PAYLOAD_BYTES       : NATURAL := 134;
        ENCODED_BYTES       : NATURAL := 268;
        ENCODED_BITS        : NATURAL := 2144;
        BYTE_WIDTH          : NATURAL := 8;
        SOFT_WIDTH          : NATURAL := 3;
        -- Debug bypass controls (must match encoder settings!)
        BYPASS_RANDOMIZE    : BOOLEAN := FALSE;  -- TRUE=skip pre-FEC LFSR derandomization
        BYPASS_FEC          : BOOLEAN := FALSE;  -- TRUE=skip Viterbi, take first 134 bytes
        BYPASS_INTERLEAVE   : BOOLEAN := FALSE   -- TRUE=skip 67x32 bit deinterleaving
    );
    PORT (
        clk                 : IN  std_logic;
        aresetn             : IN  std_logic;
        
        -- AXI-Stream input (hard bytes from frame_sync_detector)
        s_axis_tdata        : IN  std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        s_axis_tvalid       : IN  std_logic;
        s_axis_tready       : OUT std_logic;
        s_axis_tlast        : IN  std_logic;
        
        -- Soft decision input (bit-level, from frame_sync_detector)
        -- Arrives as a burst of 2144 3-bit values AFTER the 268 bytes
        s_axis_soft_bit_tdata   : IN  std_logic_vector(SOFT_WIDTH-1 DOWNTO 0);
        s_axis_soft_bit_tvalid  : IN  std_logic;
        s_axis_soft_bit_tready  : OUT std_logic;
        s_axis_soft_bit_tlast   : IN  std_logic;
        
        -- AXI-Stream output (decoded payload)
        m_axis_tdata        : OUT std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        m_axis_tvalid       : OUT std_logic;
        m_axis_tready       : IN  std_logic;
        m_axis_tlast        : OUT std_logic;
        
        -- Status
        frames_decoded      : OUT std_logic_vector(31 DOWNTO 0);
        decoder_active      : OUT std_logic;
        
        -- Debug
        debug_state         : OUT std_logic_vector(3 DOWNTO 0);  -- 4 bits for future expansion
        debug_viterbi_start : OUT std_logic;
        debug_viterbi_busy  : OUT std_logic;
        debug_viterbi_done  : OUT std_logic;
        debug_path_metric   : OUT std_logic_vector(15 DOWNTO 0)
    );
END ENTITY ov_frame_decoder_soft;

ARCHITECTURE rtl OF ov_frame_decoder_soft IS

    ------------------------------------------------------------------------------
    -- CCSDS LFSR Functions (for DERANDOMIZE - standard pre-FEC randomization)
    ------------------------------------------------------------------------------
    -- Polynomial: x^8 + x^7 + x^5 + x^3 + 1 (CCSDS standard randomizer)
    -- Period: 255 bits
    ------------------------------------------------------------------------------
    
    -- Generate 8 output bits from LFSR (for byte-level XOR in DERANDOMIZE)
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

    -- Constants
    CONSTANT PAYLOAD_BITS : NATURAL := PAYLOAD_BYTES * 8;  -- 1072
    CONSTANT NUM_SYMBOLS  : NATURAL := ENCODED_BITS / 2;   -- 1072
    
    -- State machine (9 states)
    TYPE state_t IS (IDLE, COLLECT_BYTES, COLLECT_SOFT, EXTRACT, 
                     DEINTERLEAVE, PREP_FEC_DECODE, FEC_DECODE, DERANDOMIZE, OUTPUT);
    SIGNAL state : state_t := IDLE;
    
    -- Linear buffer for collecting bytes (sized to exactly what we need)
    TYPE collect_buffer_t IS ARRAY(0 TO ENCODED_BYTES-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    SIGNAL collect_buffer : collect_buffer_t;
    SIGNAL collect_idx : NATURAL RANGE 0 TO ENCODED_BYTES;
    
    -- Soft value buffer (one 3-bit value per bit, 2144 total)
    TYPE soft_bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic_vector(SOFT_WIDTH-1 DOWNTO 0);
    SIGNAL soft_buffer : soft_bit_buffer_t;
    SIGNAL soft_idx : NATURAL RANGE 0 TO ENCODED_BITS-1;
    
    -- Extracted data buffers
    TYPE byte_buffer_t IS ARRAY(0 TO PAYLOAD_BYTES-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    TYPE bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic;
    
    SIGNAL input_bits           : bit_buffer_t;
    SIGNAL deinterleaved_bits   : bit_buffer_t;
    SIGNAL deinterleaved_soft   : soft_bit_buffer_t;  -- Soft values after deinterleaving
    SIGNAL fec_decoded_buffer   : byte_buffer_t;
    SIGNAL output_buffer        : byte_buffer_t;
    
    -- CCSDS LFSR register (for DERANDOMIZE only)
    SIGNAL lfsr_derandomize   : std_logic_vector(7 DOWNTO 0) := x"FF";
    
    -- Viterbi decoder signals
    SIGNAL decoder_start        : std_logic := '0';
    SIGNAL decoder_busy         : std_logic;
    SIGNAL decoder_done         : std_logic;
    SIGNAL decoder_input_soft_g1 : std_logic_vector(NUM_SYMBOLS * SOFT_WIDTH - 1 DOWNTO 0);
    SIGNAL decoder_input_soft_g2 : std_logic_vector(NUM_SYMBOLS * SOFT_WIDTH - 1 DOWNTO 0);
    SIGNAL decoder_output_buf   : std_logic_vector(PAYLOAD_BITS-1 DOWNTO 0);
    SIGNAL decoder_path_metric  : std_logic_vector(15 DOWNTO 0);
    
    -- Processing indices
    SIGNAL byte_idx             : NATURAL RANGE 0 TO ENCODED_BYTES;
    SIGNAL bit_idx              : NATURAL RANGE 0 TO ENCODED_BITS;
    SIGNAL out_idx              : NATURAL RANGE 0 TO PAYLOAD_BYTES;
    
    -- Frame counter
    SIGNAL frame_count          : unsigned(31 DOWNTO 0) := (OTHERS => '0');
    
    -- Output registers
    SIGNAL m_tdata_reg          : std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    SIGNAL m_tvalid_reg         : std_logic := '0';
    SIGNAL m_tlast_reg          : std_logic := '0';
    
    -- Attributes
    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF collect_buffer : SIGNAL IS "block";
    ATTRIBUTE ram_style OF soft_buffer : SIGNAL IS "block";
    ATTRIBUTE ram_style OF input_bits : SIGNAL IS "block";
    ATTRIBUTE ram_style OF deinterleaved_bits : SIGNAL IS "block";
    ATTRIBUTE ram_style OF deinterleaved_soft : SIGNAL IS "block";
    
    ATTRIBUTE dont_touch : STRING;
    ATTRIBUTE dont_touch OF U_DECODER : LABEL IS "true";

    ----------------------------------------------------------------------------
    -- Bit-level interleave address function (67x32 matrix)
    ----------------------------------------------------------------------------
    FUNCTION interleave_address_bit(linear_idx : NATURAL) RETURN NATURAL IS
        CONSTANT ROWS : NATURAL := 67;
        CONSTANT COLS : NATURAL := 32;
        VARIABLE row, col : NATURAL;
    BEGIN
        row := linear_idx / COLS;
        col := linear_idx MOD COLS;
        RETURN col * ROWS + row;
    END FUNCTION;
    
    ----------------------------------------------------------------------------
    -- Soft buffer deinterleave address function
    -- Given deinterleaved bit index, returns the soft_buffer index containing it.
    -- soft_buffer is in ARRIVAL order (MSB-first byte transmission).
    -- This combines interleave lookup with MSB-first byte correction.
    --
    -- Arrival order: bits arrive as bytes transmitted MSB-first
    --   arrival[0] = byte 0, bit 7 = interleaved[7]
    --   arrival[1] = byte 0, bit 6 = interleaved[6]
    --   arrival[7] = byte 0, bit 0 = interleaved[0]
    --   arrival[8] = byte 1, bit 7 = interleaved[15]
    --   etc.
    --
    -- To get deinterleaved bit i:
    --   1. Find interleaved position: interleave_address_bit(i)
    --   2. Convert to arrival position: byte*8 + (7 - bit_in_byte)
    ----------------------------------------------------------------------------
    FUNCTION soft_deinterleave_address(deint_idx : NATURAL) RETURN NATURAL IS
        VARIABLE interleaved_pos : NATURAL;
        VARIABLE byte_num : NATURAL;
        VARIABLE bit_in_byte : NATURAL;
    BEGIN
        -- First find which interleaved position has the deinterleaved bit
        interleaved_pos := interleave_address_bit(deint_idx);
        -- Convert interleaved position to arrival position (MSB-first correction)
        byte_num := interleaved_pos / 8;
        bit_in_byte := interleaved_pos MOD 8;
        RETURN byte_num * 8 + (7 - bit_in_byte);
    END FUNCTION;

BEGIN

    -- Soft Viterbi Decoder Instantiation
    U_DECODER : ENTITY work.viterbi_decoder_k7_soft
        GENERIC MAP (
            PAYLOAD_BITS    => PAYLOAD_BITS,
            ENCODED_BITS    => ENCODED_BITS,
            TRACEBACK_DEPTH => 35,
            SOFT_WIDTH      => SOFT_WIDTH
        )
        PORT MAP (
            clk              => clk,
            aresetn          => aresetn,
            start            => decoder_start,
            busy             => decoder_busy,
            done             => decoder_done,
            input_soft_g1    => decoder_input_soft_g1,
            input_soft_g2    => decoder_input_soft_g2,
            output_bits      => decoder_output_buf,
            debug_path_metric => decoder_path_metric
        );

    -- Output assignments
    m_axis_tdata  <= m_tdata_reg;
    m_axis_tvalid <= m_tvalid_reg;
    m_axis_tlast  <= m_tlast_reg;
    
    frames_decoded <= std_logic_vector(frame_count);
    
    -- Debug outputs
    debug_viterbi_busy <= decoder_busy;
    debug_path_metric  <= decoder_path_metric;

    -- Main state machine
    PROCESS(clk, aresetn)
    BEGIN
        IF aresetn = '0' THEN
            state <= IDLE;
            collect_idx <= 0;
            soft_idx <= 0;
            byte_idx <= 0;
            bit_idx <= 0;
            out_idx <= 0;
            m_tvalid_reg <= '0';
            m_tlast_reg <= '0';
            frame_count <= (OTHERS => '0');
            decoder_start <= '0';
            debug_viterbi_start <= '0';
            debug_viterbi_done <= '0';
            lfsr_derandomize <= x"FF";
            
        ELSIF rising_edge(clk) THEN
            decoder_start <= '0';
            debug_viterbi_start <= '0';
            debug_viterbi_done <= '0';
            
            CASE state IS
                
                ----------------------------------------------------------
                -- IDLE: Wait for frame data
                ----------------------------------------------------------
                WHEN IDLE =>
                    m_tvalid_reg <= '0';
                    m_tlast_reg <= '0';
                    
                    IF s_axis_tvalid = '1' THEN
                        collect_buffer(0) <= s_axis_tdata;
                        collect_idx <= 1;
                        state <= COLLECT_BYTES;
                    END IF;
                    
                ----------------------------------------------------------
                -- COLLECT_BYTES: Receive 268 bytes into linear buffer
                ----------------------------------------------------------
                WHEN COLLECT_BYTES =>
                    IF s_axis_tvalid = '1' THEN
                        collect_buffer(collect_idx) <= s_axis_tdata;
                        
                        IF s_axis_tlast = '1' THEN
                            soft_idx <= 0;
                            state <= COLLECT_SOFT;
                        ELSE
                            collect_idx <= collect_idx + 1;
                        END IF;
                    END IF;
                    
                ----------------------------------------------------------
                -- COLLECT_SOFT: Receive 2144 soft bit values
                ----------------------------------------------------------
                WHEN COLLECT_SOFT =>
                    IF s_axis_soft_bit_tvalid = '1' THEN
                        soft_buffer(soft_idx) <= s_axis_soft_bit_tdata;
                        
                        IF s_axis_soft_bit_tlast = '1' OR soft_idx = ENCODED_BITS - 1 THEN
                            byte_idx <= 0;
                            state <= EXTRACT;
                        ELSE
                            soft_idx <= soft_idx + 1;
                        END IF;
                    END IF;
                    
                ----------------------------------------------------------
                -- EXTRACT: Unpack bytes from collect_buffer to bit array
                -- Data is stored linearly at indices 0 to ENCODED_BYTES-1
                ----------------------------------------------------------
                WHEN EXTRACT =>
                    IF byte_idx < ENCODED_BYTES THEN
                        -- Unpack to bit array (MSB-first per byte)
                        FOR j IN 0 TO 7 LOOP
                            input_bits(byte_idx*8 + j) <= collect_buffer(byte_idx)(7-j);
                        END LOOP;
                        
                        byte_idx <= byte_idx + 1;
                    ELSE
                        bit_idx <= 0;
                        state <= DEINTERLEAVE;
                    END IF;
                    
                ----------------------------------------------------------
                -- DEINTERLEAVE: Reverse 67x32 bit interleaving
                -- Also deinterleave soft values for Viterbi
                -- BYPASS_INTERLEAVE=TRUE: Direct copy (must match encoder!)
                ----------------------------------------------------------
WHEN DEINTERLEAVE =>
    IF bit_idx < ENCODED_BITS THEN
        IF BYPASS_INTERLEAVE THEN
            -- BYPASS: Direct copy, no deinterleaving
            deinterleaved_bits(bit_idx) <= input_bits(bit_idx);
            deinterleaved_soft(bit_idx) <= soft_buffer(bit_idx);
        ELSE
            -- Apply inverse 67x32 bit deinterleaving
            deinterleaved_bits(bit_idx) <= 
                input_bits(interleave_address_bit(bit_idx));
            deinterleaved_soft(bit_idx) <= 
                soft_buffer(soft_deinterleave_address(bit_idx));
        END IF;
        bit_idx <= bit_idx + 1;
    ELSE
        byte_idx <= 0;
        state <= PREP_FEC_DECODE;
    END IF;                    
                ----------------------------------------------------------
                -- PREP_FEC_DECODE: Pack soft G1/G2 and start decoder
                -- BYPASS_FEC=TRUE: Skip packing, go straight to extraction
                ----------------------------------------------------------
                WHEN PREP_FEC_DECODE =>
                    IF BYPASS_FEC THEN
                        -- BYPASS: Skip Viterbi, will extract first 134 bytes in FEC_DECODE
                        state <= FEC_DECODE;
                    ELSE
                        -- Real FEC: Pack soft values for Viterbi decoder
                        -- Deinterleaved stream: G1[0], G2[0], G1[1], G2[1], ...
                        FOR i IN 0 TO NUM_SYMBOLS - 1 LOOP
                            decoder_input_soft_g1((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                                deinterleaved_soft(i*2);
                            decoder_input_soft_g2((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                                deinterleaved_soft(i*2 + 1);
                        END LOOP;
                        
                        decoder_start <= '1';
                        debug_viterbi_start <= '1';
                        IF decoder_busy = '1' THEN
                            state <= FEC_DECODE;
                        END IF;
                    END IF;
                    
                ----------------------------------------------------------
                -- FEC_DECODE: Wait for Viterbi decoder OR extract first copy
                -- BYPASS_FEC=TRUE: Take first 1072 bits (134 bytes) from deinterleaved stream
                -- BYPASS_FEC=FALSE: Wait for Viterbi decoder to complete
                ----------------------------------------------------------




WHEN FEC_DECODE =>
    IF BYPASS_FEC THEN
        -- BYPASS: Extract first 134 bytes from deinterleaved stream
        -- The encoder duplicated 134 bytes -> 268 bytes
        -- First 1072 bits = first copy, second 1072 bits = second copy
        -- We just use the first copy
        --
        -- EXTRACT packed bits MSB-first: input_bits(i*8 + j) = byte(i)(7-j)
        -- So input_bits[0..7] = byte[0] bits 7,6,5,4,3,2,1,0
        -- We must reverse to recover original byte order:
        -- fec_decoded_buffer(i)(j) needs original bit j, which is at input_bits(i*8 + (7-j))
        FOR i IN 0 TO PAYLOAD_BYTES - 1 LOOP
            FOR j IN 0 TO 7 LOOP
                -- Reverse bit order to undo EXTRACT's MSB-first packing
                fec_decoded_buffer(i)(j) <= deinterleaved_bits(i*8 + (7-j));
            END LOOP;
        END LOOP;
        
        byte_idx <= 0;
        lfsr_derandomize <= x"FF";  -- Reset LFSR for derandomization
        state <= DERANDOMIZE;
                        
                    ELSIF decoder_done = '1' THEN
                        -- Real FEC: Use Viterbi decoder output
                        debug_viterbi_done <= '1';
                        
                        -- Pack decoded bits into bytes
                        -- NOTE: Bit order must match hard decoder!
                        -- decoder_output_buf is MSB-first from Viterbi traceback
                        FOR i IN 0 TO PAYLOAD_BYTES - 1 LOOP
                            FOR j IN 0 TO 7 LOOP
                                fec_decoded_buffer(i)(j) <= decoder_output_buf(PAYLOAD_BYTES*8 - 1 - i*8 - j);
                            END LOOP;
                        END LOOP;
                        
                        byte_idx <= 0;
                        lfsr_derandomize <= x"FF";  -- Reset LFSR for derandomization
                        state <= DERANDOMIZE;
                    END IF;
                    
                ----------------------------------------------------------
                -- DERANDOMIZE: XOR with CCSDS LFSR
                -- This is the standard pre-FEC randomization reversal
                -- BYPASS_RANDOMIZE=TRUE: Direct copy (must match encoder!)
                ----------------------------------------------------------
                WHEN DERANDOMIZE =>
                    IF byte_idx < PAYLOAD_BYTES THEN
                        IF BYPASS_RANDOMIZE THEN
                            -- BYPASS: Direct copy, no derandomization
                            output_buffer(byte_idx) <= fec_decoded_buffer(byte_idx);
                        ELSE
                            -- XOR with 8 LFSR output bits
                            output_buffer(byte_idx) <= 
                                fec_decoded_buffer(byte_idx) XOR lfsr_output_byte(lfsr_derandomize);
                            -- Advance LFSR by 8 positions
                            lfsr_derandomize <= lfsr_advance_8(lfsr_derandomize);
                        END IF;
                        byte_idx <= byte_idx + 1;
                    ELSE
                        out_idx <= 0;
                        frame_count <= frame_count + 1;
                        state <= OUTPUT;
                    END IF;
                    
                ----------------------------------------------------------
                -- OUTPUT: Stream decoded bytes
                ----------------------------------------------------------
                WHEN OUTPUT =>
                    IF m_axis_tready = '1' OR m_tvalid_reg = '0' THEN
                        m_tdata_reg <= output_buffer(out_idx);
                        m_tvalid_reg <= '1';
                        
                        IF out_idx = PAYLOAD_BYTES - 1 THEN
                            m_tlast_reg <= '1';
                            out_idx <= 0;
                            state <= IDLE;
                        ELSE
                            m_tlast_reg <= '0';
                            out_idx <= out_idx + 1;
                        END IF;
                    END IF;
                    
            END CASE;
        END IF;
    END PROCESS;
    
    -- Ready signals (directly active for these inputs)
    s_axis_tready <= '1' WHEN state = IDLE OR state = COLLECT_BYTES ELSE '0';
    s_axis_soft_bit_tready <= '1' WHEN state = COLLECT_SOFT ELSE '0';
    
    -- Decoder active when not idle
    decoder_active <= '0' WHEN state = IDLE ELSE '1';
    
    -- Debug state output
    debug_state <= "0000" WHEN state = IDLE ELSE
                   "0001" WHEN state = COLLECT_BYTES ELSE
                   "0010" WHEN state = COLLECT_SOFT ELSE
                   "0011" WHEN state = EXTRACT ELSE
                   "0100" WHEN state = DEINTERLEAVE ELSE
                   "0101" WHEN state = PREP_FEC_DECODE ELSE
                   "0110" WHEN state = FEC_DECODE ELSE
                   "0111" WHEN state = DERANDOMIZE ELSE
                   "1000" WHEN state = OUTPUT ELSE
                   "1111";

END ARCHITECTURE rtl;
