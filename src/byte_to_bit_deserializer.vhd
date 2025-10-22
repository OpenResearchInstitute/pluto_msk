------------------------------------------------------------------------------------------------------
-- Byte to Bit De-serializer with Sync Word Insertion
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

    -- Barker code: 0xACFA47 (produces 0xE25F35 at RX after bit reversal)
    CONSTANT SYNC_WORD : std_logic_vector(23 DOWNTO 0) := "101011001111101001000111";

    SIGNAL shift_reg         : std_logic_vector(7 DOWNTO 0);
    SIGNAL bit_counter       : integer range 0 to 31;
    SIGNAL last_byte         : std_logic;
    SIGNAL ready_int         : std_logic;
    SIGNAL tx_data_int       : std_logic;  -- Internal register for tx_data
    
    TYPE state_t IS (IDLE, SENDING_SYNC, SHIFTING_DATA);
    SIGNAL state             : state_t;

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
                ready_int <= '0';
                
            ELSE
                frame_complete <= '0';
                
                CASE state IS
                    
                    WHEN IDLE =>
                        tx_data_int <= '0';
                        bit_counter <= 0;
                        ready_int <= '1';
                        
                        IF s_axis_tvalid = '1' THEN
                            state <= SENDING_SYNC;
                            ready_int <= '0';
                            bit_counter <= 0;
                            -- Pre-load first sync bit for immediate output
                            tx_data_int <= SYNC_WORD(0);
                        END IF;
                        
                    WHEN SENDING_SYNC =>
                        IF tx_req = '1' THEN
                            -- Current bit already on tx_data_int from previous cycle
                            
                            IF bit_counter = 23 THEN
                                -- Sync word complete (just output bit 23)
                                bit_counter <= 0;
                                state <= SHIFTING_DATA;
                                ready_int <= '1';
                                tx_data_int <= '0';  -- Default for next state
                            ELSE
                                -- Prepare NEXT bit for output
                                bit_counter <= bit_counter + 1;
                                tx_data_int <= SYNC_WORD(bit_counter + 1);
                            END IF;
                        END IF;
                        
                    WHEN SHIFTING_DATA =>
                        IF s_axis_tvalid = '1' AND ready_int = '1' THEN
                            shift_reg <= s_axis_tdata;
                            last_byte <= s_axis_tlast;
                            bit_counter <= 0;
                            ready_int <= '0';
                            -- Pre-load first data bit
                            tx_data_int <= s_axis_tdata(0);
                        END IF;
                        
                        IF tx_req = '1' AND ready_int = '0' THEN
                            -- Current bit already on tx_data_int
                            shift_reg <= '0' & shift_reg(7 DOWNTO 1);
                            
                            IF bit_counter = 7 THEN
                                bit_counter <= 0;
                                
                                IF last_byte = '1' THEN
                                    frame_complete <= '1';
                                    last_byte <= '0';
                                    state <= IDLE;
                                    tx_data_int <= '0';
                                ELSE
                                    ready_int <= '1';
                                    tx_data_int <= '0';  -- Will be updated when new byte arrives
                                END IF;
                            ELSE
                                -- Prepare NEXT bit for output
                                bit_counter <= bit_counter + 1;
                                tx_data_int <= shift_reg(1);  -- Next bit after current shift
                            END IF;
                        END IF;
                        
                    WHEN OTHERS =>
                        state <= IDLE;
                        
                END CASE;
                
            END IF;
        END IF;
    END PROCESS deserializer_proc;

END ARCHITECTURE rtl;
