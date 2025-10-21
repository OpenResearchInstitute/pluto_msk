------------------------------------------------------------------------------------------------------
-- Bit to Byte Serializer for MSK Demodulator
------------------------------------------------------------------------------------------------------
-- Collects individual bits from demodulator into 8-bit bytes
-- LSB-first ordering to match transmit side
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY bit_to_byte_serializer IS
    GENERIC (
        BYTE_WIDTH : NATURAL := 8
    );
    PORT (
        clk             : IN  std_logic;
        reset           : IN  std_logic;
        
        rx_bit          : IN  std_logic;
        rx_bit_valid    : IN  std_logic;
        
        rx_byte         : OUT std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        rx_byte_valid   : OUT std_logic
    );
END ENTITY bit_to_byte_serializer;

ARCHITECTURE rtl OF bit_to_byte_serializer IS

    SIGNAL shift_reg    : std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    SIGNAL ser_bit_counter  : unsigned(2 DOWNTO 0);
    
BEGIN

    serializer_proc: PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF reset = '1' THEN
                shift_reg <= (OTHERS => '0');
                ser_bit_counter <= (OTHERS => '0');
                rx_byte <= (OTHERS => '0');
                rx_byte_valid <= '0';
                
            ELSE
                -- Default
                rx_byte_valid <= '0';
                
                IF rx_bit_valid = '1' THEN
                    -- Shift in new bit (LSB first)
                    shift_reg <= shift_reg(BYTE_WIDTH-2 DOWNTO 0) & rx_bit;
                    
                    IF ser_bit_counter = 7 THEN
                        -- Byte complete - output it
                        rx_byte <= shift_reg(BYTE_WIDTH-2 DOWNTO 0) & rx_bit;
                        rx_byte_valid <= '1';
                        ser_bit_counter <= (OTHERS => '0');
                    ELSE
                        -- Keep counting
                        ser_bit_counter <= ser_bit_counter + 1;
                    END IF;
                END IF;
                
            END IF;
        END IF;
    END PROCESS serializer_proc;

END ARCHITECTURE rtl;
