##############################################################################
# MSK Modem Integration
##############################################################################
# Use https://analogdevicesinc.github.io/hdl/projects/fmcomms2/index.html
# Get the current list of repos
set current_repos [get_property ip_repo_paths [current_fileset]]

# Add your new path to that list
set new_repo [file normalize "../../library"]
lappend current_repos $new_repo

# Apply the updated list and refresh
set_property ip_repo_paths $current_repos [current_fileset]
update_ip_catalog


ad_ip_instance msk_top msk_top

# Override clock domain for m_axis BEFORE connections are made
# msk_top is a module reference, so Vivado infers wrong clock domain
# Tell Vivado that m_axis interface uses m_axis_aclk clock domain
# This is needed because msk_top is a module reference, not packaged IP
#set_property CONFIG.CLK_DOMAIN system_sys_ps7_0_FCLK_CLK0 [get_bd_intf_pins msk_top/m_axis]

# CLOCK_DIVIDER: MSK processing clock - use divided clock (61.44 MHz)
# This is where the NCO, modulator, demodulator all run
ad_connect  msk_top/clk util_ad9361_divclk/clk_out

# CLOCK_DIVIDER: MSK AXIS clock - keep at l_clk (245 MHz) for DMA interface
# The async FIFO inside msk_top handles CDC between s_axis_aclk and clk
# TX input (s_axis_aclk): stays at l_clk because TX DMA feeds through the 245 MHz domain
# RX output (m_axis_aclk): now at sys_cpu_clk (100 MHz) because RX DMA runs there
ad_connect  msk_top/s_axis_aclk util_ad9361_divclk/clk_out
ad_connect  msk_top/m_axis_aclk util_ad9361_divclk/clk_out

# MSK AXI-Lite register interface (100 MHz CPU clock)
ad_connect  msk_top/s_axi_aclk sys_cpu_clk
ad_connect  msk_top/s_axis_aresetn /util_ad9361_divclk_reset/peripheral_aresetn
ad_connect  msk_top/s_axi_aresetn sys_cpu_resetn

# MSK AXI-Lite register interface
ad_cpu_interconnect 0x43C00000 msk_top


# Sync registers -> AD9361 Channel 0

ad_connect msk_top/tx_enable axi_ad9361_dac_fifo/din_enable_0

ad_connect msk_top/tx_valid axi_ad9361_dac_fifo/din_valid_0
#ad_connect msk_top/tx_valid axi_ad9361_dac_fifo/din_valid_in_1

ad_connect msk_top/tx_samples_I axi_ad9361_dac_fifo/din_data_0
ad_connect msk_top/tx_samples_Q axi_ad9361_dac_fifo/din_data_1

# TX DMA Connections
ad_connect axi_ad9361_dac_dma/m_axis_data   msk_top/s_axis_tdata
ad_connect axi_ad9361_dac_dma/m_axis_valid  msk_top/s_axis_tvalid
ad_connect axi_ad9361_dac_dma/m_axis_ready  msk_top/s_axis_tready
ad_connect axi_ad9361_dac_dma/m_axis_last   msk_top/s_axis_tlast
ad_connect axi_ad9361_dac_dma/m_axis_keep   msk_top/s_axis_tkeep

# MSK RX Connects - Channel 0 I/Q from AD9361
ad_connect  msk_top/rx_samples_I util_ad9361_adc_fifo/dout_data_0
ad_connect  msk_top/rx_samples_Q util_ad9361_adc_fifo/dout_data_1
ad_connect  msk_top/rx_enable util_ad9361_adc_fifo/dout_enable_0
ad_connect  msk_top/rx_svalid util_ad9361_adc_fifo/dout_valid_0

# MSK RX AXIS to DMA - interface connection
# overwrite to 32 bit bus

ad_connect  msk_top/m_axis axi_ad9361_adc_dma/s_axis