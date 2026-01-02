------------------------------------------------------------------------------------------------------
-- Clock Divider by 4 with Pulse Stretchers
------------------------------------------------------------------------------------------------------
-- Divides 245.76 MHz l_clk to 61.44 MHz for MSK modem on LibreSDR
-- Also stretches dac_valid and adc_valid pulses from 1 to 2 l_clk cycles
-- so msk_top (running at 61.44 MHz) doesn't miss them
------------------------------------------------------------------------------------------------------
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
library UNISIM;
use UNISIM.VComponents.all;

entity clk_div_by4 is
    port (
        clk_in        : in  std_logic;  -- 245.76 MHz from axi_ad9361/l_clk
        clk_out       : out std_logic;  -- 61.44 MHz divided clock
        
        -- TX pulse stretcher
        dac_valid_in  : in  std_logic;  -- 1 l_clk cycle pulse from AD9361
        dac_valid_out : out std_logic;  -- 2 l_clk cycles stretched for msk_top
        
        -- RX pulse stretcher
        adc_valid_in  : in  std_logic;  -- 1 l_clk cycle pulse from AD9361
        adc_valid_out : out std_logic;  -- 2 l_clk cycles stretched for msk_top
        
        -- Debug ports
        dbg_counter   : out std_logic_vector(1 downto 0);
        dbg_clk_ff    : out std_logic
    );
end entity clk_div_by4;

architecture rtl of clk_div_by4 is
    signal counter      : unsigned(1 downto 0) := "00";
    signal clk_div_ff   : std_logic := '0';
    signal clk_div_bufg : std_logic;
    signal dac_valid_d1 : std_logic := '0';
    signal dac_valid_d2 : std_logic := '0';
    signal adc_valid_d1 : std_logic := '0';
    signal adc_valid_d2 : std_logic := '0';
    
    attribute DONT_TOUCH : string;
    attribute DONT_TOUCH of counter : signal is "TRUE";
    attribute DONT_TOUCH of clk_div_ff : signal is "TRUE";
    
    attribute MARK_DEBUG : string;
    attribute MARK_DEBUG of counter : signal is "TRUE";
    attribute MARK_DEBUG of clk_div_ff : signal is "TRUE";
begin

    process(clk_in)
    begin
        if rising_edge(clk_in) then
            -- Clock divider: count 0,1,2,3,0,1,2,3...
            counter <= counter + 1;
            if counter = "01" then
                clk_div_ff <= '1';
            elsif counter = "11" then
                clk_div_ff <= '0';
            end if;
            
            -- Pulse stretchers: 2-stage delay
            dac_valid_d1 <= dac_valid_in;
            dac_valid_d2 <= dac_valid_d1;
            adc_valid_d1 <= adc_valid_in;
            adc_valid_d2 <= adc_valid_d1;
        end if;
    end process;

    -- Stretched pulses: 3 cycles wide (covers phases 0, 1, 2)
    --dac_valid_out <= dac_valid_in OR dac_valid_d1 OR dac_valid_d2;
    --adc_valid_out <= adc_valid_in OR adc_valid_d1 OR adc_valid_d2;
    -- TEMPORARY: bypass stretcher, hardcode high (equivalent to VCC)
    dac_valid_out <= '1';
    adc_valid_out <= '1';

    -- BUFG for global clock distribution
    U_BUFG : BUFG
        port map (
            I => clk_div_ff,
            O => clk_div_bufg
        );
    
    clk_out <= clk_div_bufg;
    
    -- Debug outputs
    dbg_counter <= std_logic_vector(counter);
    dbg_clk_ff  <= clk_div_ff;
    
end architecture rtl;
