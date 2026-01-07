------------------------------------------------------------------------------------------------------
-- Byte to Bit Deserializer with Sync Word Insertion
------------------------------------------------------------------------------------------------------
-- Role in the Transmit Chain:
--   This module sits between the Opulent Voice frame assembler (byte-oriented) and the 
--   MSK modulator (bit-oriented). It performs two essential functions.
--   First, it prepends the 24-bit sync word (0x02B8DB) to each frame for frame synchronization
--   at the receiver. Second, it serializes each byte into individual bits for the modulator.
--
-- Bit Ordering:
--   MSB-first throughout. Bit 7 of each byte is transmitted first, bit 0 last.
--   The sync word is transmitted starting from bit 23 (leftmost) to bit 0.
--   This matches the receiver's frame_sync_detector expectations directly. 
--   No bit reversal is needed here.
--
-- Sync Word:
--   0x02B8DB (24 bits) was selected through an exhaustive search. It has favorable 
--   autocorrelation properties with an excellent 8:1 peak to sidelobe ratio. 
--   Binary: 0000_0010_1011_1000_1101_1011
--
-- Interfaces:
--   Input:  AXI-Stream (s_axis_*) It accepts bytes from upstream frame assembler
--   Output: tx_data/tx_req, which is data and request handshake to MSK modulator.
--           tx_req high = modulator ready for next bit
--           tx_data = current bit value (updated on tx_req)
--
-- Timing Behavior:
--   Frame begins when s_axis_tvalid is seen in IDLE state.
--   Sync word is transmitted first (24 bits), then payload bytes.
--   s_axis_tlast marks final byte. Frame_complete pulses when last bit sent.
--   Returns to IDLE after frame_complete, ready for next frame.
--
-- State Machine:
--   IDLE (tvalid), to SENDING_SYNC (24 bits), to SHIFTING_DATA (tlast means we're done), to IDLE
--
-- Exiting SHIFTING_DATA:
--   The module stays in SHIFTING_DATA until the entire frame payload is transmitted.
--   This means that the frame length for this module is flexible. 
--   The sync word is specific to Opulent Voice, so it's fixed in value and length.
--   Since it is an optimal sync word, it is of good general use and therefore a
--   good place to start for anyone re-using this module. 
-- 
--   Exit occurs when BOTH conditions are met:
--     1. bit_counter = 0 (all 8 bits of current byte have been sent)
--     2. last_byte = '1' (this byte had s_axis_tlast asserted when loaded)
--
--   The last_byte flag is a registered copy of s_axis_tlast, captured at the moment
--   each byte is loaded into shift_reg. This lets us remember "this is the final byte"
--   while we spend 8 tx_req cycles shifting it out.
--
--   On frame completion:
--     - frame_complete pulses high for one clock
--     - tx_data returns to '0' 
--     - State returns to IDLE, ready for the next frame's tvalid
--
--   If last_byte = '0' when bit_counter hits 0, we simply raise ready_int to 
--   accept the next byte and keep shifting—no state change occurs.
--
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY byte_to_bit_deserializer IS
    GENERIC (
        BYTE_WIDTH : NATURAL := 8
    );
    PORT (
        clk             : IN  std_logic;
        init            : IN  std_logic;
        
        s_axis_tdata    : IN  std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        s_axis_tvalid   : IN  std_logic;
        s_axis_tready   : OUT std_logic;
        s_axis_tlast    : IN  std_logic;
        
        tx_data         : OUT std_logic;
        tx_req          : IN  std_logic;
        
        frame_complete  : OUT std_logic
    );
END ENTITY byte_to_bit_deserializer;

ARCHITECTURE rtl OF byte_to_bit_deserializer IS

    -- Sync word: 0x02B8DB sent MSB-first
    -- This is the SAME pattern the receiver expects (no bit reversal!)
    -- Bit 23 (leftmost) is sent first
    CONSTANT SYNC_WORD : std_logic_vector(23 DOWNTO 0) := "000000101011100011011011";
    --                                                        0   2   B   8   D   B
    -- 02 00000010  B8 10111000  DB 11011011 

    SIGNAL shift_reg         : std_logic_vector(7 DOWNTO 0);
    SIGNAL bit_counter       : integer range 0 to 31;
    SIGNAL last_byte         : std_logic;
    SIGNAL ready_int         : std_logic;
    SIGNAL tx_data_int       : std_logic;  -- Internal register for tx_data
    
    TYPE state_t IS (IDLE, SENDING_SYNC, SHIFTING_DATA);
    SIGNAL state             : state_t;

    ATTRIBUTE dont_touch : STRING;
    ATTRIBUTE dont_touch OF state : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF ready_int : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF last_byte : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF shift_reg : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF bit_counter : SIGNAL IS "true";


BEGIN

    s_axis_tready <= ready_int;
    tx_data <= tx_data_int;  -- Drive output from registered signal

    deserializer_proc: PROCESS(clk)
    BEGIN

        IF rising_edge(clk) THEN

            IF init = '1' THEN
                state <= IDLE;
                tx_data_int <= '0';
                bit_counter <= 0;
                shift_reg <= (OTHERS => '0');
                frame_complete <= '0';
                last_byte <= '0';
                ready_int <= '1'; --changed from 0 to 1
                
            ELSE
                frame_complete <= '0';
                
                CASE state IS
                    
                    WHEN IDLE =>
                        bit_counter <= 0;
                        ready_int <= '0'; -- don't take data in IDLE 
                        
                        IF s_axis_tvalid = '1' THEN
                            state <= SENDING_SYNC;
                            bit_counter <= 23;  -- Start from MSB (bit 23)
                            -- Pre-load first sync bit (MSB) for immediate output
                            tx_data_int <= SYNC_WORD(23);
                        END IF;
                        
                    WHEN SENDING_SYNC =>

                        IF tx_req = '1' THEN
                            -- Current bit already on tx_data_int from previous cycle
                            
                            IF bit_counter = 0 THEN
                                -- Sync word complete (just output last bit)
                                bit_counter <= 7;  -- Prepare for data bits (start at bit 7)
                                state <= SHIFTING_DATA;
                                ready_int <= '1';
                                -- Keep last sync bit on output until new byte loads
                                -- (don't force to '0' - that could cause glitch)
                            ELSE
                                -- Prepare NEXT bit for output (count down from MSB)
                                bit_counter <= bit_counter - 1;
                                tx_data_int <= SYNC_WORD(bit_counter - 1);
                            END IF;

                        END IF;
                        
                    WHEN SHIFTING_DATA =>

                        IF s_axis_tvalid = '1' AND ready_int = '1' THEN
                            shift_reg <= s_axis_tdata;
                            last_byte <= s_axis_tlast;
                            bit_counter <= 7;  -- Start from MSB (bit 7)
                            ready_int <= '0';
                            -- Pre-load first data bit (MSB)
                            tx_data_int <= s_axis_tdata(7);
                        END IF;
                        
                        IF tx_req = '1' AND ready_int = '0' THEN
                            -- Current bit already on tx_data_int
                            
                            IF bit_counter = 0 THEN
                                -- Byte complete (just sent bit 0, the LSB)
                                
                                IF last_byte = '1' THEN
                                    frame_complete <= '1';
                                    last_byte <= '0';
                                    state <= IDLE;
                                    tx_data_int <= '0';

                                ELSE
                                    bit_counter <= 7;  -- Reset for next byte
                                    ready_int <= '1';
                                    -- Keep last bit on output until new byte loads
                                    -- (don't force to '0' - that could cause glitch)
                                END IF;

                            ELSE
                                -- Prepare NEXT bit for output (count down)
                                bit_counter <= bit_counter - 1;
                                tx_data_int <= shift_reg(bit_counter - 1);
                            END IF;

                        END IF;
                        
                    WHEN OTHERS =>
                        state <= IDLE;
                        
                END CASE;
                
            END IF;

        END IF;

    END PROCESS deserializer_proc;

END ARCHITECTURE rtl;
