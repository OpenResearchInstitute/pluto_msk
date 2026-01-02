------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
--  _______                             ________                                            ______
--  __  __ \________ _____ _______      ___  __ \_____ _____________ ______ ___________________  /_
--  _  / / /___  __ \_  _ \__  __ \     __  /_/ /_  _ \__  ___/_  _ \_  __ `/__  ___/_  ___/__  __ \
--  / /_/ / __  /_/ //  __/_  / / /     _  _, _/ /  __/_(__  ) /  __// /_/ / _  /    / /__  _  / / /
--  \____/  _  .___/ \___/ /_/ /_/      /_/ |_|  \___/ /____/  \___/ \__,_/  /_/     \___/  /_/ /_/
--          /_/
--                   ________                _____ _____ _____         _____
--                   ____  _/_______ __________  /____(_)__  /_____  ____  /______
--                    __  /  __  __ \__  ___/_  __/__  / _  __/_  / / /_  __/_  _ \
--                   __/ /   _  / / /_(__  ) / /_  _  /  / /_  / /_/ / / /_  /  __/
--                   /___/   /_/ /_/ /____/  \__/  /_/   \__/  \__,_/  \__/  \___/
--
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
-- Copyright
------------------------------------------------------------------------------------------------------
--
-- Copyright 2025 by Open Research Institute
--
------------------------------------------------------------------------------------------------------
-- License
------------------------------------------------------------------------------------------------------
--
-- This source describes Open Hardware and is licensed under the CERN-OHL-W v2.
--
-- You may redistribute and modify this source and make products using it under
-- the terms of the CERN-OHL-W v2 (https://ohwr.org/cern_ohl_w_v2.txt).
--
-- This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
-- OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.
-- Please see the CERN-OHL-W v2 for applicable conditions.
--
------------------------------------------------------------------------------------------------------
-- Block name and description
------------------------------------------------------------------------------------------------------
--
-- Opulent Voice Protocol Frame Decoder - DUAL MODE (Bit-level or Byte-level Deinterleaver)
--
-- This module implements the RX path processing for OVP frames (reverse of encoder):
--   1. Collects 268 bytes of encoded data from AXI-Stream input
--   2. Deinterleaves using bit-level (67x32) or byte-level (67x4) based on generic
--   3. Applies FEC decoding via Viterbi decoder
--   4. Derandomizes (XOR with same fixed sequence)
--   5. Outputs 134 bytes of payload via AXI-Stream
--
-- UPDATED (2025-12-16): Re-enabled bit-level deinterleaver support for protocol compliance
--   USE_BIT_INTERLEAVER = TRUE  : 67x32 bit-level (correct protocol)
--   USE_BIT_INTERLEAVER = FALSE : 67x4 byte-level (PlutoSDR compatibility)
--
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY ov_frame_decoder IS 
    GENERIC (
        PAYLOAD_BYTES       : NATURAL := 134;   -- Output frame size
        ENCODED_BYTES       : NATURAL := 268;   -- Input frame size
        ENCODED_BITS        : NATURAL := 2144;  -- Encoded bits (268 * 8)
        BYTE_WIDTH          : NATURAL := 8;
        USE_BIT_INTERLEAVER : BOOLEAN := TRUE   -- TRUE=bit-level(67x32), FALSE=byte-level(67x4)
    );
    PORT (
        clk             : IN  std_logic;
        aresetn         : IN  std_logic;
        
        -- Input AXI-Stream (268-byte encoded frames)
        s_axis_tdata    : IN  std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        s_axis_tvalid   : IN  std_logic;
        s_axis_tready   : OUT std_logic;
        s_axis_tlast    : IN  std_logic;
        
        -- Output AXI-Stream (134-byte payload frames)
        m_axis_tdata    : OUT std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        m_axis_tvalid   : OUT std_logic;
        m_axis_tready   : IN  std_logic;
        m_axis_tlast    : OUT std_logic;
        
        -- Status outputs
        frames_decoded  : OUT std_logic_vector(31 DOWNTO 0);
        decoder_active  : OUT std_logic;
        
        -- Debug outputs for hardware visibility
        debug_state         : OUT std_logic_vector(2 DOWNTO 0);
        debug_viterbi_start : OUT std_logic;
        debug_viterbi_busy  : OUT std_logic;
        debug_viterbi_done  : OUT std_logic
    );
END ENTITY ov_frame_decoder;

ARCHITECTURE rtl OF ov_frame_decoder IS

    -- State machine
    TYPE state_t IS (IDLE, COLLECT, EXTRACT, DEINTERLEAVE, PREP_FEC_DECODE, FEC_DECODE, DERANDOMIZE, OUTPUT);
    SIGNAL state : state_t := IDLE;
    
    -- Circular collection buffer - use block RAM style
    CONSTANT COLLECT_SIZE : NATURAL := 512;
    TYPE collect_buffer_t IS ARRAY(0 TO COLLECT_SIZE-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    SIGNAL collect_buffer : collect_buffer_t;
    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF collect_buffer : SIGNAL IS "block";
    SIGNAL collect_idx : NATURAL RANGE 0 TO COLLECT_SIZE-1;
    
    -- Buffer types
    TYPE byte_buffer_t IS ARRAY(0 TO PAYLOAD_BYTES-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    TYPE encoded_byte_buffer_t IS ARRAY(0 TO ENCODED_BYTES-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    TYPE bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic;
    
    -- Processing buffers
    SIGNAL input_buffer         : encoded_byte_buffer_t;  -- 268 bytes extracted from circular buffer
    SIGNAL input_bits           : bit_buffer_t;           -- 2144 bits unpacked (for bit-level mode)
    SIGNAL deinterleaved_bits   : bit_buffer_t;           -- 2144 bits after bit-level deinterleaving
    SIGNAL deinterleaved_buffer : encoded_byte_buffer_t;  -- 268 bytes after byte-level deinterleaving
    SIGNAL fec_decoded_buffer   : byte_buffer_t;
    SIGNAL output_buffer        : byte_buffer_t;
    
    -- Index counters
    SIGNAL byte_idx : NATURAL RANGE 0 TO ENCODED_BYTES;
    SIGNAL bit_idx  : NATURAL RANGE 0 TO ENCODED_BITS;
    SIGNAL out_idx  : NATURAL RANGE 0 TO PAYLOAD_BYTES;
    
    -- Frame counter
    SIGNAL frame_count : UNSIGNED(31 DOWNTO 0) := (OTHERS => '0');
    
    -- Output holding registers
    SIGNAL m_tdata_reg  : std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    SIGNAL m_tvalid_reg : std_logic;
    SIGNAL m_tlast_reg  : std_logic;
    
    -- OVP Randomizer sequence (same as encoder)
    TYPE randomizer_t IS ARRAY(0 TO PAYLOAD_BYTES-1) OF std_logic_vector(7 DOWNTO 0);
    CONSTANT RANDOMIZER_SEQUENCE : randomizer_t := (
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
    
    -- Viterbi decoder signals
    SIGNAL decoder_start      : std_logic := '0';
    SIGNAL decoder_busy       : std_logic;
    SIGNAL decoder_done       : std_logic;
    SIGNAL decoder_input_g1   : std_logic_vector(2143 DOWNTO 0);
    SIGNAL decoder_input_g2   : std_logic_vector(2143 DOWNTO 0);
    SIGNAL decoder_output_buf : std_logic_vector(1071 DOWNTO 0);
    
    -- Prevent optimization
    ATTRIBUTE dont_touch : STRING;
    ATTRIBUTE dont_touch OF U_DECODER : LABEL IS "true";
    ATTRIBUTE ram_style OF input_bits : SIGNAL IS "block";
    ATTRIBUTE ram_style OF deinterleaved_bits : SIGNAL IS "block";

    ----------------------------------------------------------------------------
    -- BIT-LEVEL DEINTERLEAVER (67x32) - Reverse of encoder's bit interleave
    ----------------------------------------------------------------------------
    -- Encoder: output_pos = (input_pos mod 32) * 67 + (input_pos / 32)
    -- Decoder (reverse): given output_pos j, find input_pos i
    --   col = j / 67,  row = j mod 67
    --   input_pos = row * 32 + col
    ----------------------------------------------------------------------------
    FUNCTION reverse_deinterleave_bit(addr : NATURAL) RETURN NATURAL IS
        CONSTANT ROWS : NATURAL := 67;
        CONSTANT COLS : NATURAL := 32;
        VARIABLE row : NATURAL;
        VARIABLE col : NATURAL;
    BEGIN
        col := addr / ROWS;      -- 0-31
        row := addr MOD ROWS;    -- 0-66
        RETURN row * COLS + col;
    END FUNCTION;
    ----------------------------------------------------------------------------
    -- FORWARD INTERLEAVE ADDRESS (needed for correct deinterleaving)
    -- This is the SAME function the encoder uses - we read from where it wrote
    ----------------------------------------------------------------------------
    FUNCTION interleave_address_bit(bit_addr : NATURAL) RETURN NATURAL IS
        CONSTANT NUM_ROWS : NATURAL := 67;
        CONSTANT NUM_COLS : NATURAL := 32;
        VARIABLE row, col : NATURAL;
    BEGIN
        row := bit_addr / NUM_COLS;
        col := bit_addr MOD NUM_COLS;
        RETURN col * NUM_ROWS + row;
    END FUNCTION;



    ----------------------------------------------------------------------------
    -- BYTE-LEVEL DEINTERLEAVER (67x4) - Reverse of encoder's byte interleave
    ----------------------------------------------------------------------------
    FUNCTION reverse_deinterleave_byte(addr : NATURAL) RETURN NATURAL IS
        CONSTANT ROWS : NATURAL := 67;
        CONSTANT COLS : NATURAL := 4;
        VARIABLE row : NATURAL;
        VARIABLE col : NATURAL;
    BEGIN
        row := addr / COLS;     -- 0-66 (output row)
        col := addr MOD COLS;   -- 0-3  (output column)
        RETURN col * ROWS + row;
    END FUNCTION;

BEGIN

    -- Viterbi Decoder Instantiation
    U_DECODER : ENTITY work.viterbi_decoder_k7_simple
        GENERIC MAP (
            PAYLOAD_BITS    => PAYLOAD_BYTES * 8,
            ENCODED_BITS    => ENCODED_BYTES * 8,
            TRACEBACK_DEPTH => 35
        )
        PORT MAP (
            clk           => clk,
            aresetn       => aresetn,
            start         => decoder_start,
            busy          => decoder_busy,
            done          => decoder_done,
            input_bits_g1 => decoder_input_g1,
            input_bits_g2 => decoder_input_g2,
            output_bits   => decoder_output_buf
        );

    -- Output assignments
    m_axis_tdata  <= m_tdata_reg;
    m_axis_tvalid <= m_tvalid_reg;
    m_axis_tlast  <= m_tlast_reg;
    
    frames_decoded <= std_logic_vector(frame_count);
    
    -- Debug output assignments
    debug_viterbi_start <= decoder_start;
    debug_viterbi_busy  <= decoder_busy;
    debug_viterbi_done  <= decoder_done;
    
    -- State encoding for debug (3 bits for 8 states)
    WITH state SELECT debug_state <=
        "000" WHEN IDLE,
        "001" WHEN COLLECT,
        "010" WHEN EXTRACT,
        "011" WHEN DEINTERLEAVE,
        "100" WHEN PREP_FEC_DECODE,
        "101" WHEN FEC_DECODE,
        "110" WHEN DERANDOMIZE,
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
                frame_count <= (OTHERS => '0');
                s_axis_tready <= '0';
                m_tvalid_reg <= '0';
                m_tlast_reg <= '0';
                decoder_active <= '0';
                decoder_start <= '0';
                
            ELSE
                CASE state IS
                
                    WHEN IDLE =>
                        decoder_active <= '0';
                        s_axis_tready <= '0';
                        m_tvalid_reg <= '0';
                        collect_idx <= 0;
                        
                        IF s_axis_tvalid = '1' THEN
                            state <= COLLECT;
                            s_axis_tready <= '1';
                        END IF;
                    
                    WHEN COLLECT =>
                        s_axis_tready <= '1';
                        
                        IF s_axis_tvalid = '1' THEN
                            collect_buffer(collect_idx) <= s_axis_tdata;
                            
                            IF collect_idx < COLLECT_SIZE - 1 THEN
                                collect_idx <= collect_idx + 1;
                            ELSE
                                collect_idx <= 0;
                            END IF;
                            
                            IF s_axis_tlast = '1' THEN
                                s_axis_tready <= '0';
                                byte_idx <= 0;
                                state <= EXTRACT;
                            END IF;
                        END IF;
                    
                    WHEN EXTRACT =>
                        IF byte_idx < ENCODED_BYTES THEN
                            extract_start := (collect_idx - ENCODED_BYTES + COLLECT_SIZE) MOD COLLECT_SIZE;
                            input_buffer(byte_idx) <= collect_buffer((extract_start + byte_idx) MOD COLLECT_SIZE);
                            byte_idx <= byte_idx + 1;
                        ELSE
                            IF USE_BIT_INTERLEAVER THEN
                                -- Unpack bytes to bits for bit-level deinterleaving
                                FOR i IN 0 TO ENCODED_BYTES - 1 LOOP
                                    FOR j IN 0 TO 7 LOOP
                                        input_bits(i*8 + j) <= input_buffer(i)(j);
                                    END LOOP;
                                END LOOP;
                                bit_idx <= 0;
                            ELSE
                                byte_idx <= 0;
                            END IF;
                            state <= DEINTERLEAVE;
                            decoder_active <= '1';
                        END IF;
                    
                    -- DEINTERLEAVE: Reverse the interleaving (bit-level or byte-level)
                    WHEN DEINTERLEAVE =>
                        IF USE_BIT_INTERLEAVER THEN
                            -- BIT-LEVEL mode: Process 1 bit per clock (2144 clocks)
                            IF bit_idx < ENCODED_BITS THEN
                                deinterleaved_bits(bit_idx) <= input_bits(interleave_address_bit(bit_idx));
                                bit_idx <= bit_idx + 1;
                            ELSE
                                byte_idx <= 0;
                                state <= PREP_FEC_DECODE;
                            END IF;
                        ELSE
                            -- BYTE-LEVEL mode: Process 1 byte per clock (268 clocks)
                            IF byte_idx < ENCODED_BYTES THEN
                                -- Read from reverse-computed address, write sequentially
                                deinterleaved_buffer(byte_idx) <= input_buffer(reverse_deinterleave_byte(byte_idx));
                                byte_idx <= byte_idx + 1;
                            ELSE
                                byte_idx <= 0;
                                state <= PREP_FEC_DECODE;
                            END IF;
                        END IF;
                    
                    -- PREP_FEC_DECODE: Unpack deinterleaved data to G1/G2 bit streams
                    WHEN PREP_FEC_DECODE =>
                        IF USE_BIT_INTERLEAVER THEN
                            -- Bit-level mode: deinterleaved_bits already contains bit stream
                            -- Extract G1 (even positions) and G2 (odd positions)
                            FOR i IN 0 TO ENCODED_BITS/2 - 1 LOOP
                                decoder_input_g1(i) <= deinterleaved_bits(i*2);
                                decoder_input_g2(i) <= deinterleaved_bits(i*2 + 1);
                            END LOOP;
                        ELSE
                            -- Byte-level mode: unpack bytes to g1/g2 streams
                            -- Each byte contributes 4 bits to g1 (even bit positions) and 4 bits to g2 (odd bit positions)
                            FOR i IN 0 TO ENCODED_BYTES - 1 LOOP
                                decoder_input_g1(i*4 + 0) <= deinterleaved_buffer(i)(0);
                                decoder_input_g1(i*4 + 1) <= deinterleaved_buffer(i)(2);
                                decoder_input_g1(i*4 + 2) <= deinterleaved_buffer(i)(4);
                                decoder_input_g1(i*4 + 3) <= deinterleaved_buffer(i)(6);
                                decoder_input_g2(i*4 + 0) <= deinterleaved_buffer(i)(1);
                                decoder_input_g2(i*4 + 1) <= deinterleaved_buffer(i)(3);
                                decoder_input_g2(i*4 + 2) <= deinterleaved_buffer(i)(5);
                                decoder_input_g2(i*4 + 3) <= deinterleaved_buffer(i)(7);
                            END LOOP;
                        END IF;
                        
                        -- Start Viterbi and wait for busy acknowledgment
                        decoder_start <= '1';
                        IF decoder_busy = '1' THEN
                            state <= FEC_DECODE;
                        END IF;

                    WHEN FEC_DECODE =>
                        decoder_start <= '0';
                        IF decoder_done = '1' THEN
                            -- Unpack decoded bits to bytes (reverse order for encoder compatibility)
                            FOR i IN 0 TO PAYLOAD_BYTES-1 LOOP
                                FOR j IN 0 TO 7 LOOP
                                    fec_decoded_buffer(i)(j) <= decoder_output_buf(PAYLOAD_BYTES*8 - 1 - i*8 - j);
                                END LOOP;
                            END LOOP;
                            byte_idx <= 0;
                            state <= DERANDOMIZE;
                        END IF;

                    WHEN DERANDOMIZE =>
                        IF byte_idx < PAYLOAD_BYTES THEN
                            output_buffer(byte_idx) <= 
                                fec_decoded_buffer(byte_idx) XOR RANDOMIZER_SEQUENCE(byte_idx);
                            byte_idx <= byte_idx + 1;
                        ELSE
                            out_idx <= 0;
                            state <= OUTPUT;
                        END IF;
                    
                    WHEN OUTPUT =>
                        IF out_idx < PAYLOAD_BYTES THEN
                            m_tdata_reg <= output_buffer(out_idx);
                            m_tvalid_reg <= '1';
                            
                            IF out_idx = PAYLOAD_BYTES - 1 THEN
                                m_tlast_reg <= '1';
                            ELSE
                                m_tlast_reg <= '0';
                            END IF;
                            
                            IF m_axis_tready = '1' OR m_tvalid_reg = '0' THEN
                                out_idx <= out_idx + 1;
                            END IF;
                        ELSE
                            m_tvalid_reg <= '0';
                            m_tlast_reg <= '0';
                            frame_count <= frame_count + 1;
                            state <= IDLE;
                        END IF;
                        
                END CASE;
            END IF;
        END IF;
    END PROCESS decoder_fsm;

END ARCHITECTURE rtl;
