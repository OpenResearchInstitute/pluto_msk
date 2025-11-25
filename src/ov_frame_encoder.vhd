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
-- Opulent Voice Protocol Frame Encoder
--
-- This module implements the TX path processing for OVP frames:
--   1. Collects 134 bytes of payload from AXI-Stream input
--   2. Applies randomization (XOR with fixed sequence)
--   3. Applies FEC (rate 1/2 convolutional encoding via conv_encoder_k7)
--   4. Applies interleaving (67x32 row-column BIT interleaver)
--   5. Outputs 268 bytes (2144 bits) via AXI-Stream
--
-- FIX (2025-11-24): Restored bit-level 67x32 interleaving
--                   Byte-level interleaving broke protocol compatibility
--                   Now processes 8 bits/clock for throughput (not 1 bit/clock)
--
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY ov_frame_encoder IS 
    GENERIC (
        PAYLOAD_BYTES   : NATURAL := 134;   -- Input frame size
        ENCODED_BYTES   : NATURAL := 268;   -- Output frame size (after FEC)
        ENCODED_BITS    : NATURAL := 2144;  -- Encoded bits (268 * 8)
        BYTE_WIDTH      : NATURAL := 8
    );
    PORT (
        clk             : IN  std_logic;
        aresetn         : IN  std_logic;
        
        -- Input AXI-Stream (134-byte frames from async FIFO)
        s_axis_tdata    : IN  std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        s_axis_tvalid   : IN  std_logic;
        s_axis_tready   : OUT std_logic;
        s_axis_tlast    : IN  std_logic;
        
        -- Output AXI-Stream (268-byte frames to deserializer)
        m_axis_tdata    : OUT std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        m_axis_tvalid   : OUT std_logic;
        m_axis_tready   : IN  std_logic;
        m_axis_tlast    : OUT std_logic;
        
        -- Status outputs
        frames_encoded  : OUT std_logic_vector(31 DOWNTO 0);
        encoder_active  : OUT std_logic
    );
END ENTITY ov_frame_encoder;

ARCHITECTURE rtl OF ov_frame_encoder IS

    -- State machine (no PACK_FEC needed with bit-level interleaving)
    TYPE state_t IS (IDLE, COLLECT, EXTRACT, RANDOMIZE, PREP_FEC, FEC_ENCODE, INTERLEAVE, OUTPUT);
    SIGNAL state : state_t := IDLE;
    
    -- Buffer types
    TYPE byte_buffer_t IS ARRAY(0 TO PAYLOAD_BYTES-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    TYPE bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic;

    -- Circular collection buffer (larger than needed to handle any transients)
    CONSTANT COLLECT_SIZE : NATURAL := 256;
    TYPE collect_buffer_t IS ARRAY(0 TO COLLECT_SIZE-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    SIGNAL collect_buffer : collect_buffer_t;
    
    -- Processing buffers
    SIGNAL input_buffer       : byte_buffer_t;
    SIGNAL randomized_buffer  : byte_buffer_t;
    SIGNAL fec_buffer         : bit_buffer_t := (OTHERS => '0');
    SIGNAL interleaved_buffer : bit_buffer_t := (OTHERS => '0');  -- BIT-level buffer!

    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF interleaved_buffer : SIGNAL IS "distributed";
    
    -- Index counters
    SIGNAL collect_idx : NATURAL RANGE 0 TO COLLECT_SIZE;
    SIGNAL byte_idx    : NATURAL RANGE 0 TO PAYLOAD_BYTES;
    SIGNAL bit_idx     : NATURAL RANGE 0 TO ENCODED_BITS;
    SIGNAL out_idx     : NATURAL RANGE 0 TO ENCODED_BYTES;
    
    -- Frame counter
    SIGNAL frame_count : UNSIGNED(31 DOWNTO 0) := (OTHERS => '0');
    
    -- Output holding registers
    SIGNAL m_tdata_reg  : std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    SIGNAL m_tvalid_reg : std_logic;
    SIGNAL m_tlast_reg  : std_logic;
    
    -- OVP Randomizer sequence (from OVP spec)
    TYPE randomizer_t IS ARRAY(0 TO PAYLOAD_BYTES-1) OF std_logic_vector(7 DOWNTO 0);
    -- OVP Randomizer sequence (from protocol spec - must match decoder!)
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

    -- Convolutional encoder signals (matches conv_encoder_k7 interface)
    SIGNAL encoder_start      : std_logic := '0';
    SIGNAL encoder_busy       : std_logic;
    SIGNAL encoder_done       : std_logic;
    SIGNAL encoder_input_buf  : std_logic_vector(1071 DOWNTO 0);  -- 134*8
    SIGNAL encoder_output_buf : std_logic_vector(2143 DOWNTO 0);  -- 268*8
    
    -- BIT-LEVEL interleaver address calculation (67 rows x 32 cols)
    -- This is the CORRECT algorithm - scatters bits across byte boundaries
    FUNCTION interleave_address(addr : NATURAL) RETURN NATURAL IS
        CONSTANT ROWS : NATURAL := 67;
        CONSTANT COLS : NATURAL := 32;
        VARIABLE row : NATURAL;
        VARIABLE col : NATURAL;
    BEGIN
        row := addr / COLS;
        col := addr MOD COLS;
        RETURN col * ROWS + row;
    END FUNCTION;
    
BEGIN

    -- Convolutional Encoder Instantiation (using YOUR actual component)
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

    -- Connect output registers to ports
    m_axis_tdata  <= m_tdata_reg;
    m_axis_tvalid <= m_tvalid_reg;
    m_axis_tlast  <= m_tlast_reg;
    
    frames_encoded <= std_logic_vector(frame_count);
    encoder_active <= '1' WHEN state /= IDLE ELSE '0';
    
    -- Ready to accept data when IDLE or COLLECT
    s_axis_tready <= '1' WHEN (state = IDLE OR state = COLLECT) AND aresetn = '1' ELSE '0';
    
    -- Main FSM
    encoder_fsm: PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF aresetn = '0' THEN
                state <= IDLE;
                collect_idx <= 0;
                byte_idx <= 0;
                bit_idx <= 0;
                out_idx <= 0;
                m_tvalid_reg <= '0';
                m_tlast_reg <= '0';
                encoder_start <= '0';
                frame_count <= (OTHERS => '0');
            ELSE
                CASE state IS
                    -- IDLE: Wait for start of frame
                    WHEN IDLE =>
                        m_tvalid_reg <= '0';
                        m_tlast_reg <= '0';
                        encoder_start <= '0';
                        
                        IF s_axis_tvalid = '1' THEN
                            collect_buffer(0) <= s_axis_tdata;
                            collect_idx <= 1;
                            state <= COLLECT;
                        END IF;
                    
                    -- COLLECT: Gather bytes until tlast
                    WHEN COLLECT =>
                        IF s_axis_tvalid = '1' THEN
                            collect_buffer(collect_idx MOD COLLECT_SIZE) <= s_axis_tdata;
                            collect_idx <= collect_idx + 1;
                            
                            IF s_axis_tlast = '1' THEN
                                byte_idx <= 0;
                                state <= EXTRACT;
                            END IF;
                        END IF;
                    
                    -- EXTRACT: Pull last 134 bytes from circular buffer
                    WHEN EXTRACT =>
                        IF byte_idx < PAYLOAD_BYTES THEN
                            input_buffer(byte_idx) <= 
                                collect_buffer((collect_idx - PAYLOAD_BYTES + byte_idx) MOD COLLECT_SIZE);
                            byte_idx <= byte_idx + 1;
                        ELSE
                            byte_idx <= 0;
                            state <= RANDOMIZE;
                        END IF;
                    
                    -- RANDOMIZE: XOR with randomizer sequence
                    WHEN RANDOMIZE =>
                        IF byte_idx < PAYLOAD_BYTES THEN
                            randomized_buffer(byte_idx) <= 
                                input_buffer(byte_idx) XOR RANDOMIZER_SEQUENCE(byte_idx);
                            byte_idx <= byte_idx + 1;
                        ELSE
                            byte_idx <= 0;
                            state <= PREP_FEC;
                        END IF;
                    
                    -- PREP_FEC: Pack bytes into encoder input vector
                    WHEN PREP_FEC =>
                        FOR i IN 0 TO PAYLOAD_BYTES-1 LOOP
                            FOR j IN 0 TO 7 LOOP
                                encoder_input_buf(i*8 + j) <= randomized_buffer(i)(j);
                            END LOOP;
                        END LOOP;
                        encoder_start <= '1';
                        state <= FEC_ENCODE;
                    
                    -- FEC_ENCODE: Wait for convolutional encoder to complete
                    WHEN FEC_ENCODE =>
                        encoder_start <= '0';
                        IF encoder_done = '1' THEN
                            -- Unpack encoded bits into fec_buffer
                            FOR i IN 0 TO ENCODED_BITS-1 LOOP
                                fec_buffer(i) <= encoder_output_buf(ENCODED_BITS - 1 - i);  -- MSB-first
                            END LOOP;
                            bit_idx <= 0;
                            state <= INTERLEAVE;
                        END IF;
                    
                    -- INTERLEAVE: Bit-level 67x32 interleaving
                    -- Process 8 bits per clock for throughput (268 clocks total)
                    WHEN INTERLEAVE =>
                        IF bit_idx < ENCODED_BITS THEN
                            -- Write 8 bits in parallel to their interleaved positions
                            interleaved_buffer(interleave_address(bit_idx + 0)) <= fec_buffer(bit_idx + 0);
                            interleaved_buffer(interleave_address(bit_idx + 1)) <= fec_buffer(bit_idx + 1);
                            interleaved_buffer(interleave_address(bit_idx + 2)) <= fec_buffer(bit_idx + 2);
                            interleaved_buffer(interleave_address(bit_idx + 3)) <= fec_buffer(bit_idx + 3);
                            interleaved_buffer(interleave_address(bit_idx + 4)) <= fec_buffer(bit_idx + 4);
                            interleaved_buffer(interleave_address(bit_idx + 5)) <= fec_buffer(bit_idx + 5);
                            interleaved_buffer(interleave_address(bit_idx + 6)) <= fec_buffer(bit_idx + 6);
                            interleaved_buffer(interleave_address(bit_idx + 7)) <= fec_buffer(bit_idx + 7);
                            bit_idx <= bit_idx + 8;
                        ELSE
                            out_idx <= 0;
                            state <= OUTPUT;
                            m_tvalid_reg <= '0';
                        END IF;
                    
                    -- OUTPUT: Send 268 bytes via AXI-Stream
                    -- Pack 8 bits from interleaved buffer into each output byte
                    WHEN OUTPUT =>
                        IF out_idx < ENCODED_BYTES THEN
                            m_tdata_reg(0) <= interleaved_buffer(out_idx * 8 + 0);
                            m_tdata_reg(1) <= interleaved_buffer(out_idx * 8 + 1);
                            m_tdata_reg(2) <= interleaved_buffer(out_idx * 8 + 2);
                            m_tdata_reg(3) <= interleaved_buffer(out_idx * 8 + 3);
                            m_tdata_reg(4) <= interleaved_buffer(out_idx * 8 + 4);
                            m_tdata_reg(5) <= interleaved_buffer(out_idx * 8 + 5);
                            m_tdata_reg(6) <= interleaved_buffer(out_idx * 8 + 6);
                            m_tdata_reg(7) <= interleaved_buffer(out_idx * 8 + 7);
                            
                            m_tvalid_reg <= '1';
                            IF out_idx = (ENCODED_BYTES - 1) THEN
                                m_tlast_reg <= '1';
                            ELSE
                                m_tlast_reg <= '0';
                            END IF;
                            
                            IF m_axis_tready = '1' THEN
                                IF out_idx = (ENCODED_BYTES - 1) THEN
                                    frame_count <= frame_count + 1;
                                    state <= IDLE;
                                    m_tvalid_reg <= '0';
                                ELSE
                                    out_idx <= out_idx + 1;
                                END IF;
                            END IF;
                        END IF;
                        
                END CASE;
            END IF;
        END IF;
    END PROCESS encoder_fsm;

END ARCHITECTURE rtl;
