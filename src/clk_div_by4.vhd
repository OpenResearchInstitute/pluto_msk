------------------------------------------------------------------------------------------------------
-- Clock Divider by 4 using BUFR
------------------------------------------------------------------------------------------------------
-- Divides 245.76 MHz l_clk to 61.44 MHz for MSK modem
-- Uses BUFR primitive which maintains phase alignment with input clock
--
-- CRITICAL: BUFR output is phase-aligned with l_clk, meaning the rising edge
-- of clk_out occurs at the same time as every 4th rising edge of clk_in.
-- This ensures proper timing for AD9361 DAC/ADC interface.
------------------------------------------------------------------------------------------------------

library IEEE;
use IEEE.std_logic_1164.all;

library UNISIM;
use UNISIM.VComponents.all;

entity clk_div_by4 is
    port (
        clk_in  : in  std_logic;  -- 245.76 MHz from axi_ad9361/l_clk
        clk_out : out std_logic   -- 61.44 MHz divided clock
    );
end entity clk_div_by4;

architecture rtl of clk_div_by4 is
    -- Preserve the clock divider from optimization
    attribute DONT_TOUCH : string;
    attribute DONT_TOUCH of U_BUFR : label is "TRUE";
begin

    -- BUFR divides the clock by 4
    -- BUFR is a regional clock buffer that provides low-skew distribution
    -- The divided clock maintains phase alignment with the input
    U_BUFR : BUFR
        generic map (
            BUFR_DIVIDE => "4",        -- Divide by 4: 245.76 -> 61.44 MHz
            SIM_DEVICE  => "7SERIES"   -- Zynq 7020 is 7-series
        )
        port map (
            I   => clk_in,
            CE  => '1',                -- Always enabled
            CLR => '0',                -- No async clear
            O   => clk_out
        );

end architecture rtl;
