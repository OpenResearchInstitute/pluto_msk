# LibreSDR XC7Z020-CLG400 Pin Constraints
# Extracted from hz12opensource/libresdr hdl.diff patch

# =============================================================================
# Clock Constraints
# =============================================================================

# AD9363 LVDS RX clock (125 MHz max)
create_clock -name rx_clk -period 8.000 [get_ports rx_clk_in_p]

# PS7 fabric clocks
create_clock -name clk_fpga_0 -period 10 [get_pins "i_system_wrapper/system_i/sys_ps7/inst/PS7_i/FCLKCLK[0]"]
create_clock -name clk_fpga_1 -period 5 [get_pins "i_system_wrapper/system_i/sys_ps7/inst/PS7_i/FCLKCLK[1]"]

# SPI clock
create_clock -name spi0_clk -period 40 [get_pins -hier */EMIOSPI0SCLKO]

# =============================================================================
# AD9363 LVDS Interface - Bank 34 (2.5V)
# =============================================================================

# RX Clock (differential)
set_property -dict {PACKAGE_PIN N20 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports rx_clk_in_p]
set_property -dict {PACKAGE_PIN P20 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports rx_clk_in_n]

# RX Frame (differential)
set_property -dict {PACKAGE_PIN U18 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports rx_frame_in_p]
set_property -dict {PACKAGE_PIN U19 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports rx_frame_in_n]

# RX Data (differential) [5:0]
set_property -dict {PACKAGE_PIN V20 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_p[0]}]
set_property -dict {PACKAGE_PIN W20 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_n[0]}]
set_property -dict {PACKAGE_PIN T20 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_p[1]}]
set_property -dict {PACKAGE_PIN U20 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_n[1]}]
set_property -dict {PACKAGE_PIN R16 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_p[2]}]
set_property -dict {PACKAGE_PIN R17 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_n[2]}]
set_property -dict {PACKAGE_PIN V17 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_p[3]}]
set_property -dict {PACKAGE_PIN V18 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_n[3]}]
set_property -dict {PACKAGE_PIN W18 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_p[4]}]
set_property -dict {PACKAGE_PIN W19 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_n[4]}]
set_property -dict {PACKAGE_PIN Y18 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_p[5]}]
set_property -dict {PACKAGE_PIN Y19 IOSTANDARD LVDS_25 DIFF_TERM 1} [get_ports {rx_data_in_n[5]}]

# TX Clock (differential)
set_property -dict {PACKAGE_PIN N18 IOSTANDARD LVDS_25} [get_ports tx_clk_out_p]
set_property -dict {PACKAGE_PIN P19 IOSTANDARD LVDS_25} [get_ports tx_clk_out_n]

# TX Frame (differential)
set_property -dict {PACKAGE_PIN Y16 IOSTANDARD LVDS_25} [get_ports tx_frame_out_p]
set_property -dict {PACKAGE_PIN Y17 IOSTANDARD LVDS_25} [get_ports tx_frame_out_n]

# TX Data (differential) [5:0]
set_property -dict {PACKAGE_PIN W14 IOSTANDARD LVDS_25} [get_ports {tx_data_out_p[0]}]
set_property -dict {PACKAGE_PIN Y14 IOSTANDARD LVDS_25} [get_ports {tx_data_out_n[0]}]
set_property -dict {PACKAGE_PIN W15 IOSTANDARD LVDS_25} [get_ports {tx_data_out_p[1]}]
set_property -dict {PACKAGE_PIN W16 IOSTANDARD LVDS_25} [get_ports {tx_data_out_n[1]}]
set_property -dict {PACKAGE_PIN U14 IOSTANDARD LVDS_25} [get_ports {tx_data_out_p[2]}]
set_property -dict {PACKAGE_PIN U15 IOSTANDARD LVDS_25} [get_ports {tx_data_out_n[2]}]
set_property -dict {PACKAGE_PIN T16 IOSTANDARD LVDS_25} [get_ports {tx_data_out_p[3]}]
set_property -dict {PACKAGE_PIN U17 IOSTANDARD LVDS_25} [get_ports {tx_data_out_n[3]}]
set_property -dict {PACKAGE_PIN V12 IOSTANDARD LVDS_25} [get_ports {tx_data_out_p[4]}]
set_property -dict {PACKAGE_PIN W13 IOSTANDARD LVDS_25} [get_ports {tx_data_out_n[4]}]
set_property -dict {PACKAGE_PIN T12 IOSTANDARD LVDS_25} [get_ports {tx_data_out_p[5]}]
set_property -dict {PACKAGE_PIN U12 IOSTANDARD LVDS_25} [get_ports {tx_data_out_n[5]}]

# =============================================================================
# AD9363 Control Signals
# =============================================================================

# Enable and TxNRx
set_property -dict {PACKAGE_PIN R18 IOSTANDARD LVCMOS25} [get_ports enable]
set_property -dict {PACKAGE_PIN P14 IOSTANDARD LVCMOS25} [get_ports txnrx]

# GPIO Reset and AGC
set_property -dict {PACKAGE_PIN N17 IOSTANDARD LVCMOS25} [get_ports gpio_resetb]
set_property -dict {PACKAGE_PIN P16 IOSTANDARD LVCMOS25} [get_ports gpio_en_agc]

# =============================================================================
# GPIO Status [7:0] - Bank 34 (2.5V)
# =============================================================================

set_property -dict {PACKAGE_PIN T11 IOSTANDARD LVCMOS25} [get_ports {gpio_status[0]}]
set_property -dict {PACKAGE_PIN T14 IOSTANDARD LVCMOS25} [get_ports {gpio_status[1]}]
set_property -dict {PACKAGE_PIN T15 IOSTANDARD LVCMOS25} [get_ports {gpio_status[2]}]
set_property -dict {PACKAGE_PIN T17 IOSTANDARD LVCMOS25} [get_ports {gpio_status[3]}]
set_property -dict {PACKAGE_PIN T19 IOSTANDARD LVCMOS25} [get_ports {gpio_status[4]}]
set_property -dict {PACKAGE_PIN G14 IOSTANDARD LVCMOS33} [get_ports {gpio_status[5]}]
set_property -dict {PACKAGE_PIN U13 IOSTANDARD LVCMOS25} [get_ports {gpio_status[6]}]
set_property -dict {PACKAGE_PIN V13 IOSTANDARD LVCMOS25} [get_ports {gpio_status[7]}]

# =============================================================================
# GPIO Control [3:0] - Mixed Banks
# =============================================================================

set_property -dict {PACKAGE_PIN T10 IOSTANDARD LVCMOS25} [get_ports {gpio_ctl[0]}]
set_property -dict {PACKAGE_PIN Y11 IOSTANDARD LVCMOS33} [get_ports {gpio_ctl[1]}]
set_property -dict {PACKAGE_PIN V10 IOSTANDARD LVCMOS33} [get_ports {gpio_ctl[2]}]
set_property -dict {PACKAGE_PIN U9  IOSTANDARD LVCMOS33} [get_ports {gpio_ctl[3]}]

# =============================================================================
# I2C Interface - Bank 35 (3.3V)
# =============================================================================

set_property -dict {PACKAGE_PIN M15 IOSTANDARD LVCMOS33 PULLUP true} [get_ports iic_scl]
set_property -dict {PACKAGE_PIN K16 IOSTANDARD LVCMOS33 PULLUP true} [get_ports iic_sda]

# =============================================================================
# SPI Interface (AD9363) - Bank 34 (2.5V)
# =============================================================================

set_property -dict {PACKAGE_PIN P18 IOSTANDARD LVCMOS25} [get_ports spi_csn]
set_property -dict {PACKAGE_PIN R14 IOSTANDARD LVCMOS25} [get_ports spi_clk]
set_property -dict {PACKAGE_PIN P15 IOSTANDARD LVCMOS25} [get_ports spi_mosi]
set_property -dict {PACKAGE_PIN R19 IOSTANDARD LVCMOS25} [get_ports spi_miso]

# =============================================================================
# PL SPI Interface - Bank 35 (3.3V)
# =============================================================================

set_property -dict {PACKAGE_PIN K14 IOSTANDARD LVCMOS33} [get_ports pl_spi_clk_o]
set_property -dict {PACKAGE_PIN J14 IOSTANDARD LVCMOS33} [get_ports pl_spi_miso]
set_property -dict {PACKAGE_PIN N15 IOSTANDARD LVCMOS33} [get_ports pl_spi_mosi]

# =============================================================================
# Timing Exceptions
# =============================================================================

# False paths for GPIO outputs from axi_ad9361
set_false_path -from [get_pins i_system_wrapper/system_i/axi_ad9361/inst/i_tdd/i_tdd_control/tdd_enable_reg/C]
set_false_path -from [get_pins i_system_wrapper/system_i/axi_ad9361/inst/i_tdd/i_tdd_control/tdd_tx_only_reg/C]
set_false_path -from [get_pins i_system_wrapper/system_i/axi_ad9361/inst/i_tdd/i_tdd_control/tdd_rx_only_reg/C]
set_false_path -from [get_pins i_system_wrapper/system_i/axi_ad9361/inst/i_tdd/i_tdd_control/tdd_gated_tx_dmapath_reg/C]
set_false_path -from [get_pins i_system_wrapper/system_i/axi_ad9361/inst/i_tdd/i_tdd_control/tdd_gated_rx_dmapath_reg/C]
