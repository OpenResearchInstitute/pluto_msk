--------------------------------------------------------------------------------
-- ov_frame_decoder_soft.vhd
--
-- Opulent Voice Frame Decoder with Soft-Decision Viterbi Decoding
--
-- This module decodes OV protocol frames using soft-decision Viterbi decoding
-- for improved performance at low SNR.
--
-- Changes from ov_frame_decoder:
--   1. Added soft input port for 3-bit quantized soft values
--   2. Added soft value buffer (2144 × 3 bits)
--   3. Soft deinterleaving
--   4. Uses viterbi_decoder_k7_soft instead of viterbi_decoder_k7_simple
--
-- Soft Value Convention:
--   0 = strong '0', 7 = strong '1', 3-4 = uncertain
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
        USE_BIT_INTERLEAVER : BOOLEAN := TRUE
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
        debug_state         : OUT std_logic_vector(2 DOWNTO 0);
        debug_viterbi_start : OUT std_logic;
        debug_viterbi_busy  : OUT std_logic;
        debug_viterbi_done  : OUT std_logic;
        debug_path_metric   : OUT std_logic_vector(15 DOWNTO 0)
    );
END ENTITY ov_frame_decoder_soft;

ARCHITECTURE rtl OF ov_frame_decoder_soft IS

    -- Constants
    CONSTANT PAYLOAD_BITS : NATURAL := PAYLOAD_BYTES * 8;  -- 1072
    CONSTANT NUM_SYMBOLS  : NATURAL := ENCODED_BITS / 2;   -- 1072
    
    -- State machine
    TYPE state_t IS (IDLE, COLLECT_BYTES, COLLECT_SOFT, EXTRACT, DEINTERLEAVE, PREP_FEC_DECODE, FEC_DECODE, DERANDOMIZE, OUTPUT);
    SIGNAL state : state_t := IDLE;
    
    -- Circular buffer for bytes
    CONSTANT COLLECT_SIZE : NATURAL := 512;
    TYPE collect_buffer_t IS ARRAY(0 TO COLLECT_SIZE-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    SIGNAL collect_buffer : collect_buffer_t;
    SIGNAL collect_idx : NATURAL RANGE 0 TO COLLECT_SIZE-1;
    
    -- Soft value buffer (one 3-bit value per bit, 2144 total)
    TYPE soft_bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic_vector(SOFT_WIDTH-1 DOWNTO 0);
    SIGNAL soft_buffer : soft_bit_buffer_t;
    SIGNAL soft_idx : NATURAL RANGE 0 TO ENCODED_BITS-1;
    
    -- Extracted data buffers
    TYPE byte_buffer_t IS ARRAY(0 TO PAYLOAD_BYTES-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    TYPE encoded_byte_buffer_t IS ARRAY(0 TO ENCODED_BYTES-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    TYPE bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic;
    
    SIGNAL input_buffer         : encoded_byte_buffer_t;
    SIGNAL input_bits           : bit_buffer_t;
    SIGNAL deinterleaved_bits   : bit_buffer_t;
    SIGNAL deinterleaved_soft   : soft_bit_buffer_t;  -- Soft values after deinterleaving
    SIGNAL fec_decoded_buffer   : byte_buffer_t;
    SIGNAL output_buffer        : byte_buffer_t;
    
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
    
    ----------------------------------------------------------------------------
    -- Derandomizer LFSR sequence (must match encoder!)
    ----------------------------------------------------------------------------
    FUNCTION get_rand_byte(byte_num : NATURAL) RETURN std_logic_vector IS
        TYPE rand_lut_t IS ARRAY(0 TO 133) OF std_logic_vector(7 DOWNTO 0);
        CONSTANT RAND_LUT : rand_lut_t := (
            x"A3", x"81", x"5C", x"C4", x"C9", x"08", x"0E", x"53",
            x"CC", x"A1", x"FB", x"29", x"9E", x"4F", x"16", x"E0",
            x"97", x"4E", x"2B", x"57", x"12", x"A7", x"3F", x"C2",
            x"4D", x"6B", x"0F", x"08", x"30", x"46", x"11", x"56",
            x"0D", x"1A", x"13", x"E7", x"50", x"97", x"61", x"F3",
            x"BE", x"E3", x"99", x"B0", x"64", x"39", x"22", x"2C",
            x"F0", x"09", x"E1", x"86", x"CF", x"73", x"59", x"C2",
            x"5C", x"8E", x"E3", x"D7", x"3F", x"70", x"D4", x"27",
            x"C2", x"E0", x"81", x"92", x"DA", x"FC", x"CA", x"5A",
            x"80", x"42", x"83", x"15", x"0F", x"A2", x"9E", x"15",
            x"9C", x"8B", x"DB", x"A4", x"46", x"1C", x"10", x"9F",
            x"B3", x"47", x"6C", x"5E", x"15", x"12", x"1F", x"AD",
            x"38", x"3D", x"03", x"BA", x"90", x"8D", x"BE", x"D3",
            x"65", x"23", x"32", x"B8", x"AB", x"10", x"62", x"7E",
            x"C6", x"26", x"7C", x"13", x"C9", x"65", x"3D", x"15",
            x"15", x"ED", x"35", x"F4", x"57", x"F5", x"58", x"11",
            x"9D", x"8E", x"E8", x"34", x"C9", x"59"
        );
    BEGIN
        IF byte_num < 134 THEN
            RETURN RAND_LUT(byte_num);
        ELSE
            RETURN x"00";
        END IF;
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
    decoder_active <= '1' WHEN state /= IDLE ELSE '0';
    
    debug_path_metric <= decoder_path_metric;
    debug_viterbi_busy <= decoder_busy;
    
    WITH state SELECT debug_state <=
        "000" WHEN IDLE,
        "001" WHEN COLLECT_BYTES,
        "010" WHEN COLLECT_SOFT,
        "011" WHEN EXTRACT,
        "100" WHEN DEINTERLEAVE,
        "101" WHEN PREP_FEC_DECODE,
        "110" WHEN FEC_DECODE,
        "111" WHEN DERANDOMIZE,
        "111" WHEN OUTPUT;

    -- Main FSM
    decoder_fsm : PROCESS(clk)
        VARIABLE extract_start : INTEGER;
    BEGIN
        IF rising_edge(clk) THEN
            IF aresetn = '0' THEN
                state <= IDLE;
                byte_idx <= 0;
                bit_idx <= 0;
                out_idx <= 0;
                collect_idx <= 0;
                soft_idx <= 0;
                decoder_start <= '0';
                frame_count <= (OTHERS => '0');
                m_tvalid_reg <= '0';
                m_tlast_reg <= '0';
                s_axis_tready <= '0';
                s_axis_soft_bit_tready <= '0';
                debug_viterbi_start <= '0';
                debug_viterbi_done <= '0';
                
            ELSE
                -- Defaults
                decoder_start <= '0';
                debug_viterbi_start <= '0';
                debug_viterbi_done <= '0';
                
                CASE state IS
                    WHEN IDLE =>
                        m_tvalid_reg <= '0';
                        m_tlast_reg <= '0';
                        s_axis_tready <= '0';
                        s_axis_soft_bit_tready <= '0';
                        
                        IF s_axis_tvalid = '1' THEN
                            collect_idx <= 0;
                            s_axis_tready <= '1';
                            state <= COLLECT_BYTES;
                        END IF;
                    
                    ----------------------------------------------------------
                    -- COLLECT_BYTES: Receive 268 bytes from frame_sync_detector
                    ----------------------------------------------------------
                    WHEN COLLECT_BYTES =>
                        s_axis_tready <= '1';
                        s_axis_soft_bit_tready <= '0';
                        
                        IF s_axis_tvalid = '1' THEN
                            collect_buffer(collect_idx) <= s_axis_tdata;
                            
                            IF collect_idx < COLLECT_SIZE - 1 THEN
                                collect_idx <= collect_idx + 1;
                            ELSE
                                collect_idx <= 0;
                            END IF;
                            
                            IF s_axis_tlast = '1' THEN
                                s_axis_tready <= '0';
                                soft_idx <= 0;
                                s_axis_soft_bit_tready <= '1';
                                state <= COLLECT_SOFT;
                            END IF;
                        END IF;
                    
                    ----------------------------------------------------------
                    -- COLLECT_SOFT: Receive 2144 3-bit soft values
                    ----------------------------------------------------------
                    WHEN COLLECT_SOFT =>
                        s_axis_tready <= '0';
                        s_axis_soft_bit_tready <= '1';
                        
                        IF s_axis_soft_bit_tvalid = '1' THEN
                            soft_buffer(soft_idx) <= s_axis_soft_bit_tdata;
                            
                            IF s_axis_soft_bit_tlast = '1' OR soft_idx = ENCODED_BITS - 1 THEN
                                s_axis_soft_bit_tready <= '0';
                                byte_idx <= 0;
                                state <= EXTRACT;
                            ELSE
                                soft_idx <= soft_idx + 1;
                            END IF;
                        END IF;
                    
                    ----------------------------------------------------------
                    -- EXTRACT: Extract bytes from circular buffer
                    ----------------------------------------------------------
                    WHEN EXTRACT =>
                        extract_start := (collect_idx - ENCODED_BYTES + COLLECT_SIZE) MOD COLLECT_SIZE;
                        input_buffer(byte_idx) <= collect_buffer((extract_start + byte_idx) MOD COLLECT_SIZE);
                        
                        IF byte_idx < ENCODED_BYTES - 1 THEN
                            byte_idx <= byte_idx + 1;
                        ELSE
                            byte_idx <= 0;
                            
                            IF USE_BIT_INTERLEAVER THEN
                                -- Unpack bytes to bits
                                FOR i IN 0 TO ENCODED_BYTES - 1 LOOP
                                    FOR j IN 0 TO 7 LOOP
                                        input_bits(i*8 + j) <= input_buffer(i)(j);
                                    END LOOP;
                                END LOOP;
                            END IF;
                            
                            bit_idx <= 0;
                            state <= DEINTERLEAVE;
                        END IF;
                    
                    ----------------------------------------------------------
                    -- DEINTERLEAVE: Reverse interleaving for bits and soft values
                    ----------------------------------------------------------
                    WHEN DEINTERLEAVE =>
                        IF USE_BIT_INTERLEAVER THEN
                            -- BIT-LEVEL mode: Process 1 bit per clock (2144 clocks)
                            -- soft_buffer is in arrival order (MSB-first bytes)
                            -- Use soft_deinterleave_address to get correct position
                            IF bit_idx < ENCODED_BITS THEN
                                deinterleaved_bits(bit_idx) <= input_bits(interleave_address_bit(bit_idx));
                                deinterleaved_soft(bit_idx) <= soft_buffer(soft_deinterleave_address(bit_idx));
                                bit_idx <= bit_idx + 1;
                            ELSE
                                byte_idx <= 0;
                                state <= PREP_FEC_DECODE;
                            END IF;
                        ELSE
                            -- BYTE-LEVEL mode: Process 1 bit per clock for soft path
                            IF bit_idx < ENCODED_BITS THEN
                                deinterleaved_bits(bit_idx) <= input_bits(bit_idx);
                                deinterleaved_soft(bit_idx) <= soft_buffer(bit_idx);
                                bit_idx <= bit_idx + 1;
                            ELSE
                                byte_idx <= 0;
                                state <= PREP_FEC_DECODE;
                            END IF;
                        END IF;
                    
                    ----------------------------------------------------------
                    -- PREP_FEC_DECODE: Pack soft G1/G2 and start decoder
                    ----------------------------------------------------------
                    WHEN PREP_FEC_DECODE =>
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
                    
                    ----------------------------------------------------------
                    -- FEC_DECODE: Wait for Viterbi decoder
                    ----------------------------------------------------------
                    WHEN FEC_DECODE =>
                        IF decoder_done = '1' THEN
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
                            state <= DERANDOMIZE;
                        END IF;
                    
                    ----------------------------------------------------------
                    -- DERANDOMIZE: XOR with LFSR sequence
                    ----------------------------------------------------------
                    WHEN DERANDOMIZE =>
                        FOR i IN 0 TO PAYLOAD_BYTES - 1 LOOP
                            output_buffer(i) <= fec_decoded_buffer(i) XOR get_rand_byte(i);
                        END LOOP;
                        
                        out_idx <= 0;
                        frame_count <= frame_count + 1;
                        state <= OUTPUT;
                    
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
        END IF;
    END PROCESS;

END ARCHITECTURE rtl;
