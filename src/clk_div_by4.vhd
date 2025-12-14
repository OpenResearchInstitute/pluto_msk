------------------------------------------------------------------------------------------------------
-- Clock Divider by 4 using counter + BUFG
------------------------------------------------------------------------------------------------------
-- Divides 245.76 MHz l_clk to 61.44 MHz for MSK modem on LibreSDR
-- Uses a 2-bit counter and BUFG for global clock distribution
--
-- BUFR cannot be used because it's limited to ~3200 slices in one clock region,
-- but the MSK modem has 23,000+ flops on this clock.
------------------------------------------------------------------------------------------------------

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

library UNISIM;
use UNISIM.VComponents.all;

entity clk_div_by4 is
    port (
        clk_in  : in  std_logic;  -- 245.76 MHz from axi_ad9361/l_clk
        clk_out : out std_logic   -- 61.44 MHz divided clock
    );
end entity clk_div_by4;

architecture rtl of clk_div_by4 is
    signal counter    : unsigned(1 downto 0) := "00";
    signal clk_div_ff : std_logic := '0';
    signal clk_div_bufg : std_logic;
    
    attribute DONT_TOUCH : string;
    attribute DONT_TOUCH of counter : signal is "TRUE";
    attribute DONT_TOUCH of clk_div_ff : signal is "TRUE";
begin

    -- Divide by 4 using toggle flip-flop
    -- Counter counts 0,1,2,3,0,1,2,3...
    -- Output toggles when counter wraps (every 4 clocks)
    process(clk_in)
    begin
        if rising_edge(clk_in) then
            counter <= counter + 1;
            if counter = "01" then
                clk_div_ff <= '1';
            elsif counter = "11" then
                clk_div_ff <= '0';
            end if;
        end if;
    end process;

    -- BUFG for global clock distribution
    U_BUFG : BUFG
        port map (
            I => clk_div_ff,
            O => clk_div_bufg
        );
    
    clk_out <= clk_div_bufg;

end architecture rtl;
