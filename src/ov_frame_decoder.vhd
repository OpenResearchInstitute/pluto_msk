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
-- Opulent Voice Protocol Frame Decoder
--
-- This module implements the RX path processing for OVP frames (reverse of encoder):
--   1. Collects 268 bytes of encoded data from AXI-Stream input
--   2. Deinterleaves bits (reverse 67x32 row-column interleaver)
--   3. Applies FEC decoding (majority vote on bit pairs)
--   4. Derandomizes (XOR with same fixed sequence)
--   5. Outputs 134 bytes of payload via AXI-Stream
--
-- CIRCULAR BUFFER FIX (2025-11-20): Matching encoder's proven strategy
--                      - Collect ALL incoming bytes into circular buffer
--                      - When tlast arrives, count back 268 bytes
--                      - This handles FIFO timing issues naturally
--                      - Never try to time the "first" byte arrival
--
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY ov_frame_decoder IS 
    GENERIC (
        PAYLOAD_BYTES   : NATURAL := 134;   -- Output frame size
        ENCODED_BYTES   : NATURAL := 268;   -- Input frame size
        ENCODED_BITS    : NATURAL := 2144;  -- Encoded bits (268 * 8)
        BYTE_WIDTH      : NATURAL := 8
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
        decoder_active  : OUT std_logic
    );
END ENTITY ov_frame_decoder;

ARCHITECTURE rtl OF ov_frame_decoder IS

    -- State machine - ADDED EXTRACT STATE
    TYPE state_t IS (IDLE, COLLECT, EXTRACT, DEINTERLEAVE, PREP_FEC_DECODE, FEC_DECODE, DERANDOMIZE, OUTPUT);
    SIGNAL state : state_t := IDLE;
    
    -- Circular collection buffer (2x encoded size for safety)
    CONSTANT COLLECT_SIZE : NATURAL := 512;
    TYPE collect_buffer_t IS ARRAY(0 TO COLLECT_SIZE-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    SIGNAL collect_buffer : collect_buffer_t;
    SIGNAL collect_idx : NATURAL RANGE 0 TO COLLECT_SIZE-1;
    
    -- Buffer types
    TYPE byte_buffer_t IS ARRAY(0 TO PAYLOAD_BYTES-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    TYPE encoded_byte_buffer_t IS ARRAY(0 TO ENCODED_BYTES-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    TYPE bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic;
    
    -- Processing buffers
    SIGNAL input_buffer         : encoded_byte_buffer_t;  -- 268 bytes extracted from circular buffer
    SIGNAL deinterleaved_buffer : bit_buffer_t := (OTHERS => '0');
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

    -- Deinterleaver address calculation (reverse of interleaver)
    FUNCTION deinterleave_address(addr : NATURAL) RETURN NATURAL IS
        CONSTANT ROWS : NATURAL := 67;
        CONSTANT COLS : NATURAL := 32;
        VARIABLE row : NATURAL;
        VARIABLE col : NATURAL;
    BEGIN
        row := addr MOD ROWS;
        col := addr / ROWS;
        RETURN row * COLS + col;
    END FUNCTION;

BEGIN

    -- Viterbi Decoder Instantiation (Hard Decision)
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

    -- Main FSM with Circular Buffer Collection
    decoder_fsm : PROCESS(clk)
        VARIABLE extract_start : INTEGER;
        VARIABLE extract_end : INTEGER;
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
                
                    -- IDLE: Ready to start collecting
                    WHEN IDLE =>
                        decoder_active <= '0';
                        s_axis_tready <= '0';  -- Keep tready LOW in IDLE
                        m_tvalid_reg <= '0';
                        collect_idx <= 0;
                        
                        IF s_axis_tvalid = '1' THEN
                            state <= COLLECT;
                            s_axis_tready <= '1';  -- Set tready HIGH when entering COLLECT
                        END IF;
                    
                    -- COLLECT: Continuously store ALL incoming bytes into circular buffer
                    WHEN COLLECT =>
                        s_axis_tready <= '1';  -- Maintain tready HIGH during collection
                        
                        IF s_axis_tvalid = '1' THEN
                            -- Store byte at current circular buffer position
                            collect_buffer(collect_idx) <= s_axis_tdata;
                            
                            -- Debug: Report first few bytes
                            IF collect_idx < 5 THEN
                                REPORT "COLLECT: collect_idx=" & INTEGER'IMAGE(collect_idx) & 
                                       " data=0x" & INTEGER'IMAGE(to_integer(unsigned(s_axis_tdata))) &
                                       " tlast=" & STD_LOGIC'IMAGE(s_axis_tlast)(2);
                            END IF;
                            
                            -- Check for tlast
                            IF s_axis_tlast = '1' THEN
                                REPORT "COLLECT: tlast at collect_idx=" & INTEGER'IMAGE(collect_idx);
                                
                                -- Move to EXTRACT state to count back 268 bytes
                                s_axis_tready <= '0';
                                byte_idx <= 0;
                                state <= EXTRACT;
                            ELSE
                                -- Advance circular buffer pointer (wrap around)
                                IF collect_idx = COLLECT_SIZE - 1 THEN
                                    collect_idx <= 0;
                                ELSE
                                    collect_idx <= collect_idx + 1;
                                END IF;
                            END IF;
                        END IF;
                    
                    -- EXTRACT: Count back ENCODED_BYTES from where tlast arrived
                    WHEN EXTRACT =>
                        IF byte_idx < ENCODED_BYTES THEN
                            -- Calculate which byte in collect_buffer to read
                            -- If collect_idx = 267, we want bytes [0:267]
                            -- If collect_idx = 300, we want bytes [33:300]
                            extract_start := (collect_idx + 1) - ENCODED_BYTES;
                            extract_end := collect_idx;
                            
                            -- Copy byte from circular buffer (with modulo wraparound)
                            input_buffer(byte_idx) <= collect_buffer((extract_start + byte_idx) MOD COLLECT_SIZE);
                            
                            IF byte_idx < 5 THEN
                                REPORT "EXTRACT[" & INTEGER'IMAGE(byte_idx) & 
                                       "] from collect_buffer[" & 
                                       INTEGER'IMAGE((extract_start + byte_idx) MOD COLLECT_SIZE) & 
                                       "] = 0x" & 
                                       INTEGER'IMAGE(to_integer(unsigned(collect_buffer((extract_start + byte_idx) MOD COLLECT_SIZE))));
                            END IF;
                            
                            byte_idx <= byte_idx + 1;
                        ELSE
                            REPORT "EXTRACT complete, " & INTEGER'IMAGE(ENCODED_BYTES) & " bytes copied";
                            byte_idx <= 0;
                            bit_idx <= 0;
                            state <= DEINTERLEAVE;
                            decoder_active <= '1';
                        END IF;
                    
                    -- DEINTERLEAVE: Reverse the row-column shuffle
                    WHEN DEINTERLEAVE =>
                        IF bit_idx < ENCODED_BITS THEN
                            -- Unpack input_buffer bytes to bits
                            deinterleaved_buffer(deinterleave_address(bit_idx)) <= 
                                input_buffer(bit_idx / 8)(bit_idx MOD 8);
                            bit_idx <= bit_idx + 1;
                        ELSE
                            REPORT "DEINTERLEAVE complete";
                            byte_idx <= 0;
                            bit_idx <= 0;
                            state <= PREP_FEC_DECODE;
                        END IF;
                    
                    -- PREP_FEC_DECODE: Separate deinterleaved bits into G1 and G2 streams
                    WHEN PREP_FEC_DECODE =>
                        FOR i IN 0 TO ENCODED_BITS/2 - 1 LOOP
                            decoder_input_g1(i) <= deinterleaved_buffer(i*2);
                            decoder_input_g2(i) <= deinterleaved_buffer(i*2 + 1);
                        END LOOP;
                        decoder_start <= '1';
                        state <= FEC_DECODE;

                    WHEN FEC_DECODE =>
                        decoder_start <= '0';
                        IF decoder_done = '1' THEN
                            -- Unpack decoded bits in REVERSE order to match encoder's bit reversal
                            -- Viterbi traceback produces bits in reverse order, compensating for
                            -- conv encoder's MSB-first processing, but we need to reverse again
                            -- to match how encoder packed the input
                            FOR i IN 0 TO PAYLOAD_BYTES-1 LOOP
                                FOR j IN 0 TO 7 LOOP
                                    fec_decoded_buffer(i)(j) <= decoder_output_buf(PAYLOAD_BYTES*8 - 1 - i*8 - j);
                                END LOOP;
                            END LOOP;
                            byte_idx <= 0;
                            state <= DERANDOMIZE;
                        END IF;

                    -- DERANDOMIZE: XOR with same sequence (inverse operation)
                    WHEN DERANDOMIZE =>
                        IF byte_idx < PAYLOAD_BYTES THEN
                            output_buffer(byte_idx) <= 
                                fec_decoded_buffer(byte_idx) XOR RANDOMIZER_SEQUENCE(byte_idx);
                            
                            IF byte_idx < 5 THEN
                                REPORT "DERANDOMIZE[" & INTEGER'IMAGE(byte_idx) &
                                       "] fec=" & INTEGER'IMAGE(to_integer(unsigned(fec_decoded_buffer(byte_idx)))) &
                                       " rand=" & INTEGER'IMAGE(to_integer(unsigned(RANDOMIZER_SEQUENCE(byte_idx)))) &
                                       " out=" & INTEGER'IMAGE(to_integer(unsigned(fec_decoded_buffer(byte_idx) XOR RANDOMIZER_SEQUENCE(byte_idx))));
                            END IF;
                            
                            byte_idx <= byte_idx + 1;
                        ELSE
                            REPORT "DERANDOMIZE complete";
                            out_idx <= 0;
                            state <= OUTPUT;
                        END IF;
                    
                    -- OUTPUT: Send bytes to next stage (FIXED AXI-Stream handshaking)
                    WHEN OUTPUT =>
                        IF out_idx < PAYLOAD_BYTES THEN
                            -- Present current data
                            m_tdata_reg <= output_buffer(out_idx);
                            m_tvalid_reg <= '1';
                            
                            IF out_idx < 5 THEN
                                REPORT "DECODER OUTPUT byte " & INTEGER'IMAGE(out_idx) & " = " &
                                       INTEGER'IMAGE(to_integer(unsigned(output_buffer(out_idx))));
                            END IF;
                            
                            -- Set tlast on final byte
                            IF out_idx = PAYLOAD_BYTES - 1 THEN
                                m_tlast_reg <= '1';
                            ELSE
                                m_tlast_reg <= '0';
                            END IF;
                            
                            -- Advance on handshake OR on first presentation (tvalid was 0)
                            IF m_axis_tready = '1' OR m_tvalid_reg = '0' THEN
                                out_idx <= out_idx + 1;
                            END IF;
                        ELSE
                            -- Frame complete
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
