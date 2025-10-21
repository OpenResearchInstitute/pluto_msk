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

    -- Define sync word as a 24-bit vector
    CONSTANT SYNC_WORD : std_logic_vector(23 DOWNTO 0) := "101010101111111100010001";    

    SIGNAL shift_reg         : std_logic_vector(7 DOWNTO 0);
    SIGNAL bit_counter       : integer range 0 to 31;
    SIGNAL last_byte         : std_logic;
    SIGNAL ready_int         : std_logic;
    
    TYPE state_t IS (IDLE, SENDING_SYNC, SHIFTING_DATA);
    SIGNAL state             : state_t;

BEGIN

    s_axis_tready <= ready_int;

    deserializer_proc: PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF init = '1' THEN
                state <= IDLE;
                tx_data <= '0';
                bit_counter <= 0;
                shift_reg <= (OTHERS => '0');
                frame_complete <= '0';
                last_byte <= '0';
                ready_int <= '0';
                
            ELSE
                frame_complete <= '0';
                
                CASE state IS
                    
                    WHEN IDLE =>
                        tx_data <= '0';
                        bit_counter <= 0;
                        ready_int <= '1';
                        
                        IF s_axis_tvalid = '1' THEN
                            state <= SENDING_SYNC;
                            ready_int <= '0';
                            bit_counter <= 0;
                        END IF;
                        
                    WHEN SENDING_SYNC =>
                        IF tx_req = '1' THEN
                            -- Output bit from sync word (LSB first)
                            tx_data <= SYNC_WORD(bit_counter);
                            
                            IF bit_counter = 23 THEN
                                -- Sync word complete
                                bit_counter <= 0;
                                state <= SHIFTING_DATA;
                                ready_int <= '1';
                            ELSE
                                bit_counter <= bit_counter + 1;
                            END IF;
                        END IF;
                        
                    WHEN SHIFTING_DATA =>
                        IF s_axis_tvalid = '1' AND ready_int = '1' THEN
                            shift_reg <= s_axis_tdata;
                            last_byte <= s_axis_tlast;
                            bit_counter <= 0;
                            ready_int <= '0';
                        END IF;
                        
                        IF tx_req = '1' AND ready_int = '0' THEN
                            tx_data <= shift_reg(0);
                            shift_reg <= '0' & shift_reg(7 DOWNTO 1);
                            
                            IF bit_counter = 7 THEN
                                bit_counter <= 0;
                                
                                IF last_byte = '1' THEN
                                    frame_complete <= '1';
                                    last_byte <= '0';
                                    state <= IDLE;
                                ELSE
                                    ready_int <= '1';
                                END IF;
                            ELSE
                                bit_counter <= bit_counter + 1;
                            END IF;
                        END IF;
                        
                    WHEN OTHERS =>
                        state <= IDLE;
                        
                END CASE;
                
            END IF;
        END IF;
    END PROCESS deserializer_proc;

END ARCHITECTURE rtl;
