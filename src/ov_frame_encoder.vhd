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
--   3. Applies FEC (rate 1/2 convolutional - currently simple bit duplication)
--   4. Applies interleaving (67x32 row-column interleaver)
--   5. Outputs 268 bytes (2144 bits) via AXI-Stream
--
-- The module is designed to maintain timing for 40ms frame periods.
--
-- BUGFIX (2025-11-16): Fixed first-byte-lost issue in IDLE?COLLECT transition
--                      Now stores first byte immediately when transitioning states
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

    -- State machine
    TYPE state_t IS (IDLE, COLLECT, RANDOMIZE, FEC_ENCODE, INTERLEAVE, OUTPUT);
    SIGNAL state : state_t := IDLE;
    
    -- Buffer types
    TYPE byte_buffer_t IS ARRAY(0 TO PAYLOAD_BYTES-1) OF std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    TYPE bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic;
    
    -- Processing buffers
    SIGNAL input_buffer       : byte_buffer_t;
    SIGNAL randomized_buffer  : byte_buffer_t;
    SIGNAL fec_buffer         : bit_buffer_t := (OTHERS => '0');  -- Initialize to prevent 'U'
    SIGNAL interleaved_buffer : bit_buffer_t := (OTHERS => '0');  -- Initialize to prevent 'U'
    
    -- Index counters
    SIGNAL byte_idx : NATURAL RANGE 0 TO PAYLOAD_BYTES;
    SIGNAL bit_idx  : NATURAL RANGE 0 TO ENCODED_BITS;
    SIGNAL out_idx  : NATURAL RANGE 0 TO ENCODED_BYTES;
    
    -- Frame counter
    SIGNAL frame_count : UNSIGNED(31 DOWNTO 0) := (OTHERS => '0');
    
    -- Output holding registers
    SIGNAL m_tdata_reg  : std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    SIGNAL m_tvalid_reg : std_logic;
    SIGNAL m_tlast_reg  : std_logic;
    
    -- OVP Randomizer sequence (from OVP spec)
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
    
    -- Interleaver address calculation (67 rows x 32 cols)
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

    -- Connect output registers to ports
    m_axis_tdata  <= m_tdata_reg;
    m_axis_tvalid <= m_tvalid_reg;
    m_axis_tlast  <= m_tlast_reg;
    
    frames_encoded <= std_logic_vector(frame_count);
    
    -- Main FSM
    encoder_fsm: PROCESS(clk, aresetn)
    BEGIN
        IF aresetn = '0' THEN
            state <= IDLE;
            byte_idx <= 0;
            bit_idx <= 0;
            out_idx <= 0;
            s_axis_tready <= '0';
            m_tvalid_reg <= '0';
            m_tlast_reg <= '0';
            frame_count <= (OTHERS => '0');
            
        ELSIF rising_edge(clk) THEN
            IF aresetn = '1' THEN
                CASE state IS
                
                    -- IDLE: Wait for incoming data
                    WHEN IDLE =>
                        encoder_active <= '0';
                        s_axis_tready <= '0';  -- Keep tready LOW to prevent premature handshakes
                        m_tvalid_reg <= '0';
                        byte_idx <= 0;
                        
                        IF s_axis_tvalid = '1' THEN
                            -- Data is waiting, transition to COLLECT and assert tready
                            state <= COLLECT;
                            encoder_active <= '1';
                            s_axis_tready <= '1';  -- Assert tready ONLY when transitioning
                        END IF;
                    
                    -- COLLECT: Gather ALL bytes (0 through 133)
                    WHEN COLLECT =>
                        -- DON'T touch tready - it was set to '1' during IDLE transition
                        -- Leave it alone to prevent FIFO synchronization issues
                        
                        IF s_axis_tvalid = '1' AND s_axis_tready = '1' THEN
                            -- Store the incoming byte
                            input_buffer(byte_idx) <= s_axis_tdata;
                            REPORT "ENCODER: Stored byte at byte_idx=" & INTEGER'IMAGE(byte_idx) & 
                                   " data=" & INTEGER'IMAGE(to_integer(unsigned(s_axis_tdata))) & 
                                   " tlast=" & STD_LOGIC'IMAGE(s_axis_tlast)(2);
                            
                            -- Check tlast FIRST
                            IF s_axis_tlast = '1' THEN
                                REPORT "ENCODER: Received tlast. Total bytes stored = " & 
                                       INTEGER'IMAGE(byte_idx + 1);
                                
                                IF byte_idx + 1 /= PAYLOAD_BYTES THEN
                                    REPORT "ENCODER: WARNING! Expected " & INTEGER'IMAGE(PAYLOAD_BYTES) & 
                                           " bytes but got " & INTEGER'IMAGE(byte_idx + 1) severity warning;
                                END IF;
                                
                                byte_idx <= 0;
                                state <= RANDOMIZE;
                                s_axis_tready <= '0';  -- Deassert when done
                                
                            ELSIF byte_idx >= PAYLOAD_BYTES - 1 THEN
                                -- Just stored the last expected byte but no tlast
                                REPORT "ENCODER: ERROR! Stored " & INTEGER'IMAGE(byte_idx + 1) & 
                                       " bytes but no tlast received" severity error;
                                byte_idx <= 0;
                                state <= IDLE;
                                s_axis_tready <= '0';  -- Deassert on error
                            ELSE
                                -- Continue to next byte
                                byte_idx <= byte_idx + 1;
                                -- DON'T touch tready!
                            END IF;
                        END IF;
                    
                    -- RANDOMIZE: XOR with sequence
                    WHEN RANDOMIZE =>
                        IF byte_idx < PAYLOAD_BYTES THEN
                            randomized_buffer(byte_idx) <= 
                                input_buffer(byte_idx) XOR RANDOMIZER_SEQUENCE(byte_idx);
                            
                            -- Debug: Report first 5 bytes
                            IF byte_idx < 5 THEN
                                REPORT "RANDOMIZE[" & INTEGER'IMAGE(byte_idx) &
                                       "] input=" & INTEGER'IMAGE(to_integer(unsigned(input_buffer(byte_idx)))) &
                                       " rand=" & INTEGER'IMAGE(to_integer(unsigned(RANDOMIZER_SEQUENCE(byte_idx)))) &
                                       " out=" & INTEGER'IMAGE(to_integer(unsigned(input_buffer(byte_idx) XOR RANDOMIZER_SEQUENCE(byte_idx))));
                            END IF;
                            
                            byte_idx <= byte_idx + 1;
                        ELSE
                            REPORT "RANDOMIZE complete, " & INTEGER'IMAGE(PAYLOAD_BYTES) & " bytes processed";
                            byte_idx <= 0;
                            bit_idx <= 0;
                            state <= FEC_ENCODE;
                        END IF;
                    
                    -- FEC_ENCODE: Duplicate each bit (rate 1/2)
                    WHEN FEC_ENCODE =>
                        IF byte_idx < PAYLOAD_BYTES THEN
                            -- Process one source bit at a time (produces 2 output bits)
                            IF bit_idx < 8 THEN
                                -- Duplicate bit (bit_idx) from current byte
                                fec_buffer(byte_idx * 16 + bit_idx * 2)     <= randomized_buffer(byte_idx)(bit_idx);
                                fec_buffer(byte_idx * 16 + bit_idx * 2 + 1) <= randomized_buffer(byte_idx)(bit_idx);
                                bit_idx <= bit_idx + 1;
                            ELSE
                                -- Done with this byte, move to next
                                -- Debug: Report first byte's FEC output
                                IF byte_idx = 0 THEN
                                    REPORT "FEC_ENCODE byte 0 produces 16 bits: " &
                                           std_logic'IMAGE(fec_buffer(0)) & std_logic'IMAGE(fec_buffer(1)) & " " &
                                           std_logic'IMAGE(fec_buffer(2)) & std_logic'IMAGE(fec_buffer(3)) & " " &
                                           std_logic'IMAGE(fec_buffer(4)) & std_logic'IMAGE(fec_buffer(5)) & " " &
                                           std_logic'IMAGE(fec_buffer(6)) & std_logic'IMAGE(fec_buffer(7)) & " " &
                                           std_logic'IMAGE(fec_buffer(8)) & std_logic'IMAGE(fec_buffer(9)) & " " &
                                           std_logic'IMAGE(fec_buffer(10)) & std_logic'IMAGE(fec_buffer(11)) & " " &
                                           std_logic'IMAGE(fec_buffer(12)) & std_logic'IMAGE(fec_buffer(13)) & " " &
                                           std_logic'IMAGE(fec_buffer(14)) & std_logic'IMAGE(fec_buffer(15));
                                END IF;
                                bit_idx <= 0;
                                byte_idx <= byte_idx + 1;
                            END IF;
                        ELSE
                            REPORT "FEC_ENCODE complete, " & INTEGER'IMAGE(ENCODED_BITS) & " bits produced";
                            byte_idx <= 0;
                            bit_idx <= 0;
                            state <= INTERLEAVE;
                        END IF;
                    
                    -- INTERLEAVE: Shuffle bits via row-column interleaver
                    WHEN INTERLEAVE =>
                        IF bit_idx < ENCODED_BITS THEN
                            interleaved_buffer(interleave_address(bit_idx)) <= fec_buffer(bit_idx);
                            bit_idx <= bit_idx + 1;
                        ELSE
                            REPORT "INTERLEAVE complete";
                            bit_idx <= 0;
                            out_idx <= 0;
                            state <= OUTPUT;
                        END IF;
                    
                    -- OUTPUT: Send bytes to deserializer




                    WHEN OUTPUT =>
                        IF m_axis_tready = '1' OR m_tvalid_reg = '0' THEN
                            IF out_idx < ENCODED_BYTES THEN
                                -- Pack 8 bits into a byte
                                m_tdata_reg(0) <= interleaved_buffer(out_idx * 8 + 0);
                                m_tdata_reg(1) <= interleaved_buffer(out_idx * 8 + 1);
                                m_tdata_reg(2) <= interleaved_buffer(out_idx * 8 + 2);
                                m_tdata_reg(3) <= interleaved_buffer(out_idx * 8 + 3);
                                m_tdata_reg(4) <= interleaved_buffer(out_idx * 8 + 4);
                                m_tdata_reg(5) <= interleaved_buffer(out_idx * 8 + 5);
                                m_tdata_reg(6) <= interleaved_buffer(out_idx * 8 + 6);
                                m_tdata_reg(7) <= interleaved_buffer(out_idx * 8 + 7);
                                
                                m_tvalid_reg <= '1';
                                
                                -- Debug reports...
                                IF out_idx < 5 THEN
                                    REPORT "OUTPUT[" & INTEGER'IMAGE(out_idx) & "] bits: " &
                                           std_logic'IMAGE(interleaved_buffer(out_idx * 8 + 7)) &
                                           std_logic'IMAGE(interleaved_buffer(out_idx * 8 + 6)) &
                                           std_logic'IMAGE(interleaved_buffer(out_idx * 8 + 5)) &
                                           std_logic'IMAGE(interleaved_buffer(out_idx * 8 + 4)) &
                                           std_logic'IMAGE(interleaved_buffer(out_idx * 8 + 3)) &
                                           std_logic'IMAGE(interleaved_buffer(out_idx * 8 + 2)) &
                                           std_logic'IMAGE(interleaved_buffer(out_idx * 8 + 1)) &
                                           std_logic'IMAGE(interleaved_buffer(out_idx * 8 + 0));
                                END IF;
                                
                                -- Set tlast on final byte
                                IF out_idx = ENCODED_BYTES - 1 THEN
                                    m_tlast_reg <= '1';
                                ELSE
                                    m_tlast_reg <= '0';
                                END IF;
                                
                                out_idx <= out_idx + 1;
                            ELSE
                                -- Frame complete
                                m_tvalid_reg <= '0';
                                m_tlast_reg <= '0';
                                frame_count <= frame_count + 1;
                                state <= IDLE;
                            END IF;
                        END IF;









                END CASE;
            END IF;
        END IF;
    END PROCESS encoder_fsm;

END ARCHITECTURE rtl;
