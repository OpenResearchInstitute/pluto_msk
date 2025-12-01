------------------------------------------------------------------------------------------------------
-- Byte to Bit De-serializer with Sync Word Insertion
------------------------------------------------------------------------------------------------------
-- MODIFIED: Now uses MSB-first bit ordering (standard serial convention)
-- Sends bit 7 first, then bit 6, 5, 4, 3, 2, 1, 0
-- Sync word updated to match MSB-first ordering
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

--    ATTRIBUTE dont_touch : STRING;
--    ATTRIBUTE dont_touch OF state : SIGNAL IS "true";
--    ATTRIBUTE dont_touch OF ready_int : SIGNAL IS "true";
--    ATTRIBUTE dont_touch OF last_byte : SIGNAL IS "true";
--    ATTRIBUTE dont_touch OF shift_reg : SIGNAL IS "true";
--    ATTRIBUTE dont_touch OF bit_counter : SIGNAL IS "true";


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
                        --tx_data_int <= '0'; --AI!!! caused spurious extra byte in first frame
                        bit_counter <= 0;
                        ready_int <= '0'; -- AI!!! don't take data in IDLE 
                        
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
                                tx_data_int <= '0';  -- Default for next state
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
                                    tx_data_int <= '0';  -- Will be updated when new byte arrives
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
