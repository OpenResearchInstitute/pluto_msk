# create board design
# LibreSDR with MSK Modem Integration
# Based on pluto MSK design adapted for LibreSDR LVDS interface
#
##############################################################################
# CLOCK DIVIDER MODIFICATION
##############################################################################
# In LVDS mode, AD9361 DATA_CLK (l_clk) runs at 245.76 MHz (4x sample rate).
# The MSK modem expects to run at the sample rate (61.44 MHz).
# This design uses a BUFR-based clock divider to create the correct clock.
#
# Changes from original:
#   1. Added clk_div_by4 module instantiation
#   2. msk_top/clk connected to divided clock (61.44 MHz)
#   3. msk_top/s_axis_aclk stays at l_clk (245 MHz) for DMA interface
#   4. tx_valid and rx_svalid tied to VCC (every divided clock cycle is valid)
#
# To revert: Search for "CLOCK_DIVIDER" comments
##############################################################################

source $ad_hdl_dir/projects/common/xilinx/adi_fir_filter_bd.tcl

# Add MSK IP repository
set_property ip_repo_paths [list $ad_hdl_dir/library ../../library] [current_fileset]
update_ip_catalog

# default ports

create_bd_intf_port -mode Master -vlnv xilinx.com:interface:ddrx_rtl:1.0 ddr
create_bd_intf_port -mode Master -vlnv xilinx.com:display_processing_system7:fixedio_rtl:1.0 fixed_io

create_bd_port -dir O spi0_csn_2_o
create_bd_port -dir O spi0_csn_1_o
create_bd_port -dir O spi0_csn_0_o
create_bd_port -dir I spi0_csn_i
create_bd_port -dir I spi0_clk_i
create_bd_port -dir O spi0_clk_o
create_bd_port -dir I spi0_sdo_i
create_bd_port -dir O spi0_sdo_o
create_bd_port -dir I spi0_sdi_i

create_bd_port -dir I -from 24 -to 0 gpio_i
create_bd_port -dir O -from 24 -to 0 gpio_o
create_bd_port -dir O -from 24 -to 0 gpio_t

create_bd_port -dir O spi_csn_o
create_bd_port -dir I spi_csn_i
create_bd_port -dir I spi_clk_i
create_bd_port -dir O spi_clk_o
create_bd_port -dir I spi_sdo_i
create_bd_port -dir O spi_sdo_o
create_bd_port -dir I spi_sdi_i

# instance: sys_ps7

ad_ip_instance processing_system7 sys_ps7

# ps7 settings

ad_ip_parameter sys_ps7 CONFIG.PCW_PRESET_BANK0_VOLTAGE {LVCMOS 3.3V}
ad_ip_parameter sys_ps7 CONFIG.PCW_PRESET_BANK1_VOLTAGE {LVCMOS 2.5V}
ad_ip_parameter sys_ps7 CONFIG.PCW_PACKAGE_NAME clg400
ad_ip_parameter sys_ps7 CONFIG.PCW_GPIO_MIO_GPIO_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_ENET0_PERIPHERAL_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_ENET0_ENET0_IO "MIO 16 .. 27"
ad_ip_parameter sys_ps7 CONFIG.PCW_ENET0_GRP_MDIO_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_ENET0_GRP_MDIO_IO "MIO 52 .. 53"
ad_ip_parameter sys_ps7 CONFIG.PCW_ENET_RESET_SELECT "Separate reset pins"
ad_ip_parameter sys_ps7 CONFIG.PCW_ENET0_RESET_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_ENET0_RESET_IO "MIO 46"
ad_ip_parameter sys_ps7 CONFIG.PCW_USE_S_AXI_HP1 1
ad_ip_parameter sys_ps7 CONFIG.PCW_USE_S_AXI_HP2 1
ad_ip_parameter sys_ps7 CONFIG.PCW_EN_CLK1_PORT 1
ad_ip_parameter sys_ps7 CONFIG.PCW_EN_RST1_PORT 1
ad_ip_parameter sys_ps7 CONFIG.PCW_FPGA0_PERIPHERAL_FREQMHZ 100.0
ad_ip_parameter sys_ps7 CONFIG.PCW_FPGA1_PERIPHERAL_FREQMHZ 200.0
ad_ip_parameter sys_ps7 CONFIG.PCW_CRYSTAL_PERIPHERAL_FREQMHZ 50
ad_ip_parameter sys_ps7 CONFIG.PCW_GPIO_EMIO_GPIO_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_GPIO_EMIO_GPIO_IO 25
ad_ip_parameter sys_ps7 CONFIG.PCW_SPI1_PERIPHERAL_ENABLE 0
ad_ip_parameter sys_ps7 CONFIG.PCW_I2C0_PERIPHERAL_ENABLE 0
ad_ip_parameter sys_ps7 CONFIG.PCW_SD0_PERIPHERAL_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_SDIO_PERIPHERAL_FREQMHZ 50
ad_ip_parameter sys_ps7 CONFIG.PCW_UART0_PERIPHERAL_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_UART0_UART0_IO {MIO 14 .. 15}
ad_ip_parameter sys_ps7 CONFIG.PCW_I2C1_PERIPHERAL_ENABLE 0
ad_ip_parameter sys_ps7 CONFIG.PCW_QSPI_PERIPHERAL_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_QSPI_GRP_SINGLE_SS_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_SPI0_PERIPHERAL_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_SPI0_SPI0_IO EMIO
ad_ip_parameter sys_ps7 CONFIG.PCW_TTC0_PERIPHERAL_ENABLE 0
ad_ip_parameter sys_ps7 CONFIG.PCW_USE_FABRIC_INTERRUPT 1
ad_ip_parameter sys_ps7 CONFIG.PCW_USB0_PERIPHERAL_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_GPIO_MIO_GPIO_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_GPIO_MIO_GPIO_IO MIO
ad_ip_parameter sys_ps7 CONFIG.PCW_USB0_RESET_IO {MIO 47}
ad_ip_parameter sys_ps7 CONFIG.PCW_USB0_RESET_ENABLE 1
ad_ip_parameter sys_ps7 CONFIG.PCW_IRQ_F2P_INTR 1
ad_ip_parameter sys_ps7 CONFIG.PCW_IRQ_F2P_MODE REVERSE
ad_ip_parameter sys_ps7 CONFIG.PCW_MIO_0_PULLUP {enabled}
ad_ip_parameter sys_ps7 CONFIG.PCW_MIO_9_PULLUP {enabled}
ad_ip_parameter sys_ps7 CONFIG.PCW_MIO_10_PULLUP {enabled}
ad_ip_parameter sys_ps7 CONFIG.PCW_MIO_11_PULLUP {enabled}
ad_ip_parameter sys_ps7 CONFIG.PCW_MIO_48_PULLUP {enabled}
ad_ip_parameter sys_ps7 CONFIG.PCW_MIO_49_PULLUP {disabled}
ad_ip_parameter sys_ps7 CONFIG.PCW_MIO_53_PULLUP {enabled}
ad_ip_parameter sys_ps7 CONFIG.PCW_APU_PERIPHERAL_FREQMHZ 750

# DDR MT41K256M16 HA-125 (32M, 16bit, 8banks)

ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_ACT_DDR_FREQ_MHZ 525
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_PARTNO {Custom}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_BANK_ADDR_COUNT {3}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_ROW_ADDR_COUNT {15}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_COL_ADDR_COUNT {10}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_CL {7}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_CWL {5}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_T_RCD {7}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_T_RP {7}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_T_RC {48.91}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_T_RAS_MIN {35.0}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_T_FAW {40.0}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_DQS_TO_CLK_DELAY_0 {0.048}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_DQS_TO_CLK_DELAY_1 {0.050}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_BOARD_DELAY0 {0.241}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_BOARD_DELAY1 {0.240}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_ECC {Disabled}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_BUS_WIDTH {32 Bit}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_DRAM_WIDTH {16 Bits}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_DEVICE_CAPACITY {4096 MBits}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_SPEED_BIN {DDR3_1066F}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_TRAIN_WRITE_LEVEL {1}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_TRAIN_READ_GATE {1}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_TRAIN_DATA_EYE {1}
ad_ip_parameter sys_ps7 CONFIG.PCW_UIPARAM_DDR_USE_INTERNAL_VREF {0}

ad_ip_instance xlconcat sys_concat_intc
ad_ip_parameter sys_concat_intc CONFIG.NUM_PORTS 16

ad_ip_instance proc_sys_reset sys_rstgen
ad_ip_parameter sys_rstgen CONFIG.C_EXT_RST_WIDTH 1

# system reset/clock definitions

# add external spi

ad_ip_instance axi_quad_spi axi_spi
ad_ip_parameter axi_spi CONFIG.C_USE_STARTUP 0
ad_ip_parameter axi_spi CONFIG.C_NUM_SS_BITS 1
ad_ip_parameter axi_spi CONFIG.C_SCK_RATIO 8

ad_connect  sys_cpu_clk sys_ps7/FCLK_CLK0
ad_connect  sys_200m_clk sys_ps7/FCLK_CLK1
ad_connect  sys_cpu_reset sys_rstgen/peripheral_reset
ad_connect  sys_cpu_resetn sys_rstgen/peripheral_aresetn
ad_connect  sys_cpu_clk sys_rstgen/slowest_sync_clk
ad_connect  sys_rstgen/ext_reset_in sys_ps7/FCLK_RESET0_N

# interface connections

ad_connect  ddr sys_ps7/DDR
ad_connect  gpio_i sys_ps7/GPIO_I
ad_connect  gpio_o sys_ps7/GPIO_O
ad_connect  gpio_t sys_ps7/GPIO_T
ad_connect  fixed_io sys_ps7/FIXED_IO

# ps7 spi connections

ad_connect  spi0_csn_2_o sys_ps7/SPI0_SS2_O
ad_connect  spi0_csn_1_o sys_ps7/SPI0_SS1_O
ad_connect  spi0_csn_0_o sys_ps7/SPI0_SS_O
ad_connect  spi0_csn_i sys_ps7/SPI0_SS_I
ad_connect  spi0_clk_i sys_ps7/SPI0_SCLK_I
ad_connect  spi0_clk_o sys_ps7/SPI0_SCLK_O
ad_connect  spi0_sdo_i sys_ps7/SPI0_MOSI_I
ad_connect  spi0_sdo_o sys_ps7/SPI0_MOSI_O
ad_connect  spi0_sdi_i sys_ps7/SPI0_MISO_I

# axi spi connections

ad_connect  sys_cpu_clk  axi_spi/ext_spi_clk
ad_connect  spi_csn_i  axi_spi/ss_i
ad_connect  spi_csn_o  axi_spi/ss_o
ad_connect  spi_clk_i  axi_spi/sck_i
ad_connect  spi_clk_o  axi_spi/sck_o
ad_connect  spi_sdo_i  axi_spi/io0_i
ad_connect  spi_sdo_o  axi_spi/io0_o
ad_connect  spi_sdi_i  axi_spi/io1_i

# interrupts

ad_connect  sys_concat_intc/dout sys_ps7/IRQ_F2P
ad_connect  sys_concat_intc/In15 GND
ad_connect  sys_concat_intc/In14 GND
ad_connect  sys_concat_intc/In13 GND
ad_connect  sys_concat_intc/In12 GND
ad_connect  sys_concat_intc/In11 GND
ad_connect  sys_concat_intc/In10 GND
ad_connect  sys_concat_intc/In9 GND
ad_connect  sys_concat_intc/In8 GND
ad_connect  sys_concat_intc/In7 GND
ad_connect  sys_concat_intc/In6 GND
ad_connect  sys_concat_intc/In5 GND
ad_connect  sys_concat_intc/In4 GND
ad_connect  sys_concat_intc/In3 GND
ad_connect  sys_concat_intc/In2 GND
ad_connect  sys_concat_intc/In1 GND
ad_connect  sys_concat_intc/In0 GND

# iic

create_bd_intf_port -mode Master -vlnv xilinx.com:interface:iic_rtl:1.0 iic_main

ad_ip_instance axi_iic axi_iic_main

ad_connect  iic_main axi_iic_main/iic
ad_cpu_interconnect 0x41600000 axi_iic_main
ad_cpu_interrupt ps-15 mb-15 axi_iic_main/iic2intc_irpt

# ad9361

create_bd_port -dir I rx_clk_in_p
create_bd_port -dir I rx_clk_in_n
create_bd_port -dir I rx_frame_in_p
create_bd_port -dir I rx_frame_in_n
create_bd_port -dir I -from 5 -to 0 rx_data_in_p
create_bd_port -dir I -from 5 -to 0 rx_data_in_n

create_bd_port -dir O tx_clk_out_p
create_bd_port -dir O tx_clk_out_n
create_bd_port -dir O tx_frame_out_p
create_bd_port -dir O tx_frame_out_n
create_bd_port -dir O -from 5 -to 0 tx_data_out_p
create_bd_port -dir O -from 5 -to 0 tx_data_out_n

create_bd_port -dir O enable
create_bd_port -dir O txnrx
create_bd_port -dir I up_enable
create_bd_port -dir I up_txnrx

# ad9361 core
ad_ip_instance axi_ad9361 axi_ad9361
ad_ip_parameter axi_ad9361 CONFIG.ID 0
ad_ip_parameter axi_ad9361 CONFIG.CMOS_OR_LVDS_N 0

# This place is horrible
ad_ip_parameter axi_ad9361 CONFIG.MODE_1R1T 0
ad_ip_parameter axi_ad9361 CONFIG.ADC_INIT_DELAY 30

# TDD, DDS, and more
ad_ip_parameter axi_ad9361 CONFIG.TDD_DISABLE 1
ad_ip_parameter axi_ad9361 CONFIG.DAC_DDS_DISABLE 1
ad_ip_parameter axi_ad9361 CONFIG.ADC_DCFILTER_DISABLE 1
ad_ip_parameter axi_ad9361 CONFIG.ADC_IQCORRECTION_DISABLE 1
ad_ip_parameter axi_ad9361 CONFIG.DAC_IQCORRECTION_DISABLE 1

# Enable user ports for direct MSK connection
ad_ip_parameter axi_ad9361 CONFIG.DAC_USERPORTS_DISABLE 0
ad_ip_parameter axi_ad9361 CONFIG.ADC_USERPORTS_DISABLE 0

# DAC DMA - TX data from PS to MSK
ad_ip_instance axi_dmac axi_ad9361_dac_dma
ad_ip_parameter axi_ad9361_dac_dma CONFIG.DMA_TYPE_SRC 0
ad_ip_parameter axi_ad9361_dac_dma CONFIG.DMA_TYPE_DEST 1
ad_ip_parameter axi_ad9361_dac_dma CONFIG.CYCLIC 0
ad_ip_parameter axi_ad9361_dac_dma CONFIG.AXI_SLICE_SRC 0
ad_ip_parameter axi_ad9361_dac_dma CONFIG.AXI_SLICE_DEST 0
ad_ip_parameter axi_ad9361_dac_dma CONFIG.DMA_2D_TRANSFER 0
ad_ip_parameter axi_ad9361_dac_dma CONFIG.DMA_DATA_WIDTH_DEST 32

# ADC DMA - RX data from MSK to PS (AXIS interface)
ad_ip_instance axi_dmac axi_ad9361_adc_dma
ad_ip_parameter axi_ad9361_adc_dma CONFIG.DMA_TYPE_SRC 1
ad_ip_parameter axi_ad9361_adc_dma CONFIG.DMA_TYPE_DEST 0
ad_ip_parameter axi_ad9361_adc_dma CONFIG.CYCLIC 0
ad_ip_parameter axi_ad9361_adc_dma CONFIG.SYNC_TRANSFER_START 0
ad_ip_parameter axi_ad9361_adc_dma CONFIG.AXI_SLICE_SRC 0
ad_ip_parameter axi_ad9361_adc_dma CONFIG.AXI_SLICE_DEST 0
ad_ip_parameter axi_ad9361_adc_dma CONFIG.DMA_2D_TRANSFER 0
ad_ip_parameter axi_ad9361_adc_dma CONFIG.DMA_DATA_WIDTH_SRC 32

# connections

ad_connect  rx_clk_in_p axi_ad9361/rx_clk_in_p
ad_connect  rx_clk_in_n axi_ad9361/rx_clk_in_n
ad_connect  rx_frame_in_p axi_ad9361/rx_frame_in_p
ad_connect  rx_frame_in_n axi_ad9361/rx_frame_in_n
ad_connect  rx_data_in_p axi_ad9361/rx_data_in_p
ad_connect  rx_data_in_n axi_ad9361/rx_data_in_n
ad_connect  tx_clk_out_p axi_ad9361/tx_clk_out_p
ad_connect  tx_clk_out_n axi_ad9361/tx_clk_out_n
ad_connect  tx_frame_out_p axi_ad9361/tx_frame_out_p
ad_connect  tx_frame_out_n axi_ad9361/tx_frame_out_n
ad_connect  tx_data_out_p axi_ad9361/tx_data_out_p
ad_connect  tx_data_out_n axi_ad9361/tx_data_out_n
ad_connect  enable axi_ad9361/enable
ad_connect  txnrx axi_ad9361/txnrx
ad_connect  up_enable axi_ad9361/up_enable
ad_connect  up_txnrx axi_ad9361/up_txnrx

ad_connect  axi_ad9361/tdd_sync GND
ad_connect  sys_200m_clk axi_ad9361/delay_clk
ad_connect  axi_ad9361/l_clk axi_ad9361/clk

# Logic OR for reset
ad_ip_instance util_vector_logic logic_or_1 [list \
  C_OPERATION {or} \
  C_SIZE 1]

ad_connect  logic_or_1/Op1  axi_ad9361/rst
ad_connect  logic_or_1/Op2  GND

# DMA clock connections - these stay at l_clk (245 MHz)
ad_connect  axi_ad9361/l_clk axi_ad9361_adc_dma/s_axis_aclk
ad_connect  axi_ad9361/l_clk axi_ad9361_dac_dma/m_axis_aclk

# Tie off unused signals
ad_connect GND axi_ad9361/adc_dovf
ad_connect GND axi_ad9361/dac_dunf

# interconnects

ad_cpu_interconnect 0x79020000 axi_ad9361
ad_cpu_interconnect 0x7C400000 axi_ad9361_adc_dma
ad_cpu_interconnect 0x7C420000 axi_ad9361_dac_dma
ad_cpu_interconnect 0x7C430000 axi_spi

ad_ip_parameter sys_ps7 CONFIG.PCW_USE_S_AXI_HP1 {1}
ad_connect sys_cpu_clk sys_ps7/S_AXI_HP1_ACLK
ad_connect axi_ad9361_adc_dma/m_dest_axi sys_ps7/S_AXI_HP1

create_bd_addr_seg -range 0x40000000 -offset 0x00000000 \
                    [get_bd_addr_spaces axi_ad9361_adc_dma/m_dest_axi] \
                    [get_bd_addr_segs sys_ps7/S_AXI_HP1/HP1_DDR_LOWOCM] \
                    SEG_sys_ps7_HP1_DDR_LOWOCM

ad_ip_parameter sys_ps7 CONFIG.PCW_USE_S_AXI_HP2 {1}
ad_connect sys_cpu_clk sys_ps7/S_AXI_HP2_ACLK
ad_connect axi_ad9361_dac_dma/m_src_axi sys_ps7/S_AXI_HP2

create_bd_addr_seg -range 0x40000000 -offset 0x00000000 \
                    [get_bd_addr_spaces axi_ad9361_dac_dma/m_src_axi] \
                    [get_bd_addr_segs sys_ps7/S_AXI_HP2/HP2_DDR_LOWOCM] \
                    SEG_sys_ps7_HP2_DDR_LOWOCM

ad_connect sys_cpu_clk axi_ad9361_dac_dma/m_src_axi_aclk
ad_connect sys_cpu_clk axi_ad9361_adc_dma/m_dest_axi_aclk
ad_connect sys_cpu_resetn axi_ad9361_adc_dma/m_dest_axi_aresetn
ad_connect sys_cpu_resetn axi_ad9361_dac_dma/m_src_axi_aresetn

# interrupts

ad_cpu_interrupt ps-13 mb-13 axi_ad9361_adc_dma/irq
ad_cpu_interrupt ps-12 mb-12 axi_ad9361_dac_dma/irq
ad_cpu_interrupt ps-11 mb-11 axi_spi/ip2intc_irpt


##############################################################################
# CLOCK_DIVIDER: Clock divider for MSK modem (245.76 MHz -> 61.44 MHz)
##############################################################################
# Uses BUFR primitive to divide l_clk by 4.
# This provides a phase-aligned 61.44 MHz clock for the MSK modem.
# The BUFR output edges align with every 4th l_clk edge, ensuring proper
# timing for DAC/ADC data which is stable for 4 l_clk cycles per sample.
##############################################################################

# Add the clock divider source file to the project before creating the BD cell
add_files -norecurse ../../src/clk_div_by4.vhd
update_compile_order -fileset sources_1

create_bd_cell -type module -reference clk_div_by4 clk_divider
ad_connect axi_ad9361/l_clk clk_divider/clk_in


##############################################################################
# MSK Modem Integration
##############################################################################

ad_ip_instance msk_top msk_top

# CLOCK_DIVIDER: MSK processing clock - use divided clock (61.44 MHz)
# This is where the NCO, modulator, demodulator all run
ad_connect  msk_top/clk clk_divider/clk_out

# CLOCK_DIVIDER: MSK AXIS clock - keep at l_clk (245 MHz) for DMA interface
# The async FIFO inside msk_top handles CDC between s_axis_aclk and clk
# TX input (s_axis_aclk): stays at l_clk because TX DMA feeds through the 245 MHz domain
# RX output (m_axis_aclk): now at sys_cpu_clk (100 MHz) because RX DMA runs there
ad_connect  msk_top/s_axis_aclk axi_ad9361/l_clk
ad_connect  msk_top/m_axis_aclk sys_cpu_clk


# MSK AXI-Lite register interface (100 MHz CPU clock)
ad_connect  msk_top/s_axi_aclk sys_cpu_clk
ad_connect  msk_top/s_axis_aresetn sys_cpu_resetn
ad_connect  msk_top/s_axi_aresetn sys_cpu_resetn

# MSK AXI-Lite register interface
ad_cpu_interconnect 0x43C00000 msk_top

# MSK TX Connects - Channel 0 I/Q to AD9361
# CLOCK_DIVIDER: TX samples need to be synchronized from clk_div4 to l_clk domain
# The msk_top outputs change on clk_div4 edges, but AD9361 samples on l_clk.
# Without sync, the DAC might catch glitches during transitions.

# Create sync registers for TX I/Q (resample clk_div4 outputs to l_clk)
create_bd_cell -type ip -vlnv xilinx.com:ip:c_shift_ram:12.0 tx_i_sync
set_property -dict [list \
    CONFIG.Width {16} \
    CONFIG.Depth {2} \
    CONFIG.DefaultData {0000000000000000} \
    CONFIG.AsyncInitVal {0000000000000000} \
] [get_bd_cells tx_i_sync]

create_bd_cell -type ip -vlnv xilinx.com:ip:c_shift_ram:12.0 tx_q_sync
set_property -dict [list \
    CONFIG.Width {16} \
    CONFIG.Depth {2} \
    CONFIG.DefaultData {0000000000000000} \
    CONFIG.AsyncInitVal {0000000000000000} \
] [get_bd_cells tx_q_sync]

# Clock sync registers with l_clk (245 MHz)
ad_connect axi_ad9361/l_clk tx_i_sync/CLK
ad_connect axi_ad9361/l_clk tx_q_sync/CLK

# MSK outputs -> sync registers
ad_connect msk_top/tx_samples_I tx_i_sync/D
ad_connect msk_top/tx_samples_Q tx_q_sync/D

# Sync registers -> AD9361 Channel 0
ad_connect tx_i_sync/Q axi_ad9361/dac_data_i0
ad_connect tx_q_sync/Q axi_ad9361/dac_data_q0
ad_connect msk_top/tx_enable axi_ad9361/dac_enable_i0
#ad_connect msk_top/tx_enable axi_ad9361/dac_enable_q0

#The dac_enable_* signals are outputs from axi_ad9361 indicating 
#which channels are active (set by software). 
#Not connecting dac_enable_q0 doesn't disable Q.
#It just means nobody reads that status signal.

# Sync registers -> AD9361 Channel 1 (duplicate for LVDS interleaving)
ad_connect tx_i_sync/Q axi_ad9361/dac_data_i1
ad_connect tx_q_sync/Q axi_ad9361/dac_data_q1
#ad_connect msk_top/tx_enable axi_ad9361/dac_enable_i1
#ad_connect msk_top/tx_enable axi_ad9361/dac_enable_q1

# CLOCK_DIVIDER: tx_valid tied HIGH - every 61.44 MHz clock cycle is a valid sample
# (Previously connected to dac_valid_i0 which pulses in l_clk domain)
#ad_connect  msk_top/tx_valid VCC

# ok that was a bad idea maybe, connect it back
# TX side - connect to actual DAC valid, using pulse stretcher.
ad_connect axi_ad9361/dac_valid_i0 clk_divider/dac_valid_in
ad_connect clk_divider/dac_valid_out msk_top/tx_valid

# TX DMA Connections
ad_connect axi_ad9361_dac_dma/m_axis_data   msk_top/s_axis_tdata
ad_connect axi_ad9361_dac_dma/m_axis_valid  msk_top/s_axis_tvalid
ad_connect axi_ad9361_dac_dma/m_axis_ready  msk_top/s_axis_tready
ad_connect axi_ad9361_dac_dma/m_axis_last   msk_top/s_axis_tlast
ad_connect axi_ad9361_dac_dma/m_axis_keep   msk_top/s_axis_tkeep

# MSK RX Connects - Channel 0 I/Q from AD9361
ad_connect  msk_top/rx_samples_I axi_ad9361/adc_data_i0
ad_connect  msk_top/rx_samples_Q axi_ad9361/adc_data_q0
ad_connect  msk_top/rx_enable axi_ad9361/adc_enable_i0

# CLOCK_DIVIDER: rx_svalid tied HIGH - every 61.44 MHz clock cycle is a valid sample
# (Previously connected to adc_valid_i0 which pulses in l_clk domain)
#ad_connect  msk_top/rx_svalid VCC

# Ok that might have been a bad idea. Connect it back, using pulse stretcher.
ad_connect axi_ad9361/adc_valid_i0 clk_divider/adc_valid_in
ad_connect clk_divider/adc_valid_out msk_top/rx_svalid

# MSK RX AXIS to DMA - interface connection
ad_connect  msk_top/m_axis axi_ad9361_adc_dma/s_axis

##############################################################################
# ILA Debug Core - Deserializer Monitoring
##############################################################################
# Captures deserializer signals in clk_div4 domain (61 MHz).
# 
# Probes:
#   probe0: tx_data_bit    - bit output to modulator
#   probe1: tx_req         - modulator requesting next bit
#   probe2: encoder_tvalid - encoder has data available
#   probe3: encoder_tready - deserializer ready for byte
#   probe4: frame_complete - end of frame marker
#
# At 61 MHz with 16384 samples, we get ~268us of capture (~6.8 frames).
# At 61 MHz with 32768 samples, we get more time fails to place (over on BRAM)
# Look for patterns at byte boundaries (every 8 tx_req pulses).
##############################################################################
#create_bd_cell -type ip -vlnv xilinx.com:ip:ila:6.2 ila_msk_tx
#set_property -dict [list \
#    CONFIG.C_PROBE0_WIDTH {1} \
#    CONFIG.C_PROBE1_WIDTH {1} \
#    CONFIG.C_PROBE2_WIDTH {1} \
#    CONFIG.C_PROBE3_WIDTH {1} \
#    CONFIG.C_PROBE4_WIDTH {1} \
#    CONFIG.C_PROBE5_WIDTH {8} \
#    CONFIG.C_NUM_OF_PROBES {6} \
#    CONFIG.C_DATA_DEPTH {16384} \
#    CONFIG.C_TRIGIN_EN {false} \
#    CONFIG.C_EN_STRG_QUAL {1} \
#    CONFIG.ALL_PROBE_SAME_MU_CNT {2} \
#] [get_bd_cells ila_msk_tx]
## Clock ILA with clk_div4 (61 MHz) - deserializer clock domain
#ad_connect clk_divider/clk_out ila_msk_tx/clk
## Probe 0: tx_data_bit - the bit going to modulator
#ad_connect msk_top/dbg_tx_data_bit ila_msk_tx/probe0
## Probe 1: tx_req - when modulator requests a bit
#ad_connect msk_top/dbg_tx_req ila_msk_tx/probe1
## Probe 2: encoder_tvalid - data available from encoder
#ad_connect msk_top/dbg_encoder_tvalid ila_msk_tx/probe2
## Probe 3: encoder_tready - deserializer ready for data
#ad_connect msk_top/dbg_encoder_tready ila_msk_tx/probe3
## Probe 4: frame_complete - end of frame marker
#ad_connect msk_top/dbg_frame_complete ila_msk_tx/probe4
## Probe 5: encoder_tdata - 8-bit data from encoder to deserializer
#ad_connect msk_top/dbg_encoder_tdata ila_msk_tx/probe5




##############################################################################
# ILA Debug Core - TX DAC Path Monitoring  
##############################################################################
# Add this after the existing ila_msk_tx section in system_bd.tcl
# Probes the I/Q samples going to the AD9361
##############################################################################
create_bd_cell -type ip -vlnv xilinx.com:ip:ila:6.2 ila_dac_tx
set_property -dict [list \
    CONFIG.C_MONITOR_TYPE {Native} \
    CONFIG.C_NUM_OF_PROBES {21} \
    CONFIG.C_PROBE0_WIDTH {16} \
    CONFIG.C_PROBE1_WIDTH {16} \
    CONFIG.C_PROBE2_WIDTH {16} \
    CONFIG.C_PROBE3_WIDTH {16} \
    CONFIG.C_PROBE4_WIDTH {1} \
    CONFIG.C_PROBE5_WIDTH {1} \
    CONFIG.C_PROBE6_WIDTH {1} \
    CONFIG.C_PROBE7_WIDTH {1} \
    CONFIG.C_PROBE8_WIDTH {1} \
    CONFIG.C_PROBE9_WIDTH {1} \
    CONFIG.C_PROBE10_WIDTH {1} \
    CONFIG.C_PROBE11_WIDTH {1} \
    CONFIG.C_PROBE12_WIDTH {1} \
    CONFIG.C_PROBE13_WIDTH {1} \
    CONFIG.C_PROBE14_WIDTH {1} \
    CONFIG.C_PROBE15_WIDTH {1} \
    CONFIG.C_PROBE16_WIDTH {16} \
    CONFIG.C_PROBE17_WIDTH {16} \
    CONFIG.C_PROBE18_WIDTH {1} \
    CONFIG.C_PROBE19_WIDTH {1} \
    CONFIG.C_PROBE20_WIDTH {1} \
    CONFIG.C_DATA_DEPTH {4096} \
    CONFIG.C_TRIGIN_EN {false} \
    CONFIG.C_EN_STRG_QUAL {1} \
    CONFIG.ALL_PROBE_SAME_MU_CNT {2} \
] [get_bd_cells ila_dac_tx]

# Clock with l_clk (245 MHz) - same as AD9361 interface
ad_connect axi_ad9361/l_clk ila_dac_tx/clk

# TX Path - Channel 0
# Probe 0: TX I samples from msk_top (before CDC)
ad_connect msk_top/tx_samples_I ila_dac_tx/probe0

# Probe 1: TX Q samples from msk_top (before CDC)  
ad_connect msk_top/tx_samples_Q ila_dac_tx/probe1

# Probe 2: TX I after CDC sync (going to AD9361)
ad_connect tx_i_sync/Q ila_dac_tx/probe2

# Probe 3: TX Q after CDC sync (going to AD9361)
ad_connect tx_q_sync/Q ila_dac_tx/probe3

# Probe 4: TX enable signal
ad_connect msk_top/tx_enable ila_dac_tx/probe4

# Probe 5: dac_valid_i0
ad_connect axi_ad9361/dac_valid_i0 ila_dac_tx/probe5

# Probe 6: dac_valid_q0
ad_connect axi_ad9361/dac_valid_q0 ila_dac_tx/probe6

# Probe 7: dac_enable_i0
ad_connect axi_ad9361/dac_enable_i0 ila_dac_tx/probe7

# Probe 8: dac_enable_q0
ad_connect axi_ad9361/dac_enable_q0 ila_dac_tx/probe8

# Probe 9: dac_r1_mode - KEY: shows if in 1R1T mode
ad_connect axi_ad9361/dac_r1_mode ila_dac_tx/probe9

# Probe 10: dac_sync_out
ad_connect axi_ad9361/dac_sync_out ila_dac_tx/probe10

# TX Path - Channel 1
# Probe 11: dac_valid_i1
ad_connect axi_ad9361/dac_valid_i1 ila_dac_tx/probe11

# Probe 12: dac_valid_q1
ad_connect axi_ad9361/dac_valid_q1 ila_dac_tx/probe12

# Probe 13: dac_enable_i1
ad_connect axi_ad9361/dac_enable_i1 ila_dac_tx/probe13

# Probe 14: dac_enable_q1
ad_connect axi_ad9361/dac_enable_q1 ila_dac_tx/probe14

# RX Path - Raw ADC data
# Probe 15: adc_enable_i0
ad_connect axi_ad9361/adc_enable_i0 ila_dac_tx/probe15

# Probe 16: ADC I data raw from AD9361
ad_connect axi_ad9361/adc_data_i0 ila_dac_tx/probe16

# Probe 17: ADC Q data raw from AD9361
ad_connect axi_ad9361/adc_data_q0 ila_dac_tx/probe17

# Probe 18: adc_valid_i0
ad_connect axi_ad9361/adc_valid_i0 ila_dac_tx/probe18

# Probe 19: adc_valid_q0
ad_connect axi_ad9361/adc_valid_q0 ila_dac_tx/probe19

# Probe 20: adc_enable_q0
ad_connect axi_ad9361/adc_enable_q0 ila_dac_tx/probe20







##############################################################################
# FUTURE DEBUG: Comprehensive MSK Datapath ILA
##############################################################################
# Uncomment this section to add a second ILA for internal datapath debugging.
# This ILA runs at the modem clock (61.44 MHz) to capture the bit-level signals.
#
# OBSERVATION POINTS IN TX PATH:
# ─────────────────────────────────────────────────────────────────────────────
# 1. FIFO output (after CDC from PS clock to modem clock):
#    - fifo_tdata[7:0]    : Byte from async FIFO
#    - fifo_tvalid        : FIFO has data
#    - fifo_tready        : Encoder ready to accept
#    - fifo_tlast         : Frame boundary marker
#
# 2. Encoder output (after FEC, interleaving):
#    - encoder_tdata[7:0] : Encoded byte to deserializer
#    - encoder_tvalid     : Encoder has data
#    - encoder_tready     : Deserializer ready
#    - encoder_tlast      : Encoded frame boundary
#    - encoder_debug_state[2:0] : Encoder FSM state
#
# 3. Deserializer output (byte-to-bit conversion):
#    - tx_data_bit        : Current bit to modulator
#    - tx_req             : Modulator requesting next bit (tclk pulse)
#    - frame_complete     : End of frame marker
#
# 4. Modulator internals (if needed):
#    - tclk               : Bit clock from NCO
#    - tx_samples_I[15:0] : I samples (already in ila_dac_tx)
#    - tx_samples_Q[15:0] : Q samples (already in ila_dac_tx)
#
# SIGNALS ACTIVE IN CURRENT ila_dac_tx (245 MHz, l_clk domain):
#    - probe0: tx_samples_I[15:0]  - I samples before CDC
#    - probe1: tx_samples_Q[15:0]  - Q samples before CDC
#    - probe2: tx_i_sync/Q[15:0]   - I samples after CDC (to AD9361)
#    - probe3: tx_q_sync/Q[15:0]   - Q samples after CDC (to AD9361)
#    - probe4: tx_enable           - TX enable signal
#
# TO DEBUG 3375 Hz SPURS (16-bit periodicity):
# If the problem is us, then it is likely to be
# in the encoder to deserializer handshaking.
# Enable ila_msk_tx below to capture bit-level timing.
# ─────────────────────────────────────────────────────────────────────────────

create_bd_cell -type ip -vlnv xilinx.com:ip:ila:6.2 ila_msk_tx
set_property -dict [list \
    CONFIG.C_MONITOR_TYPE {Native} \
    CONFIG.C_NUM_OF_PROBES {10} \
    CONFIG.C_PROBE0_WIDTH {1} \
    CONFIG.C_PROBE1_WIDTH {1} \
    CONFIG.C_PROBE2_WIDTH {1} \
    CONFIG.C_PROBE3_WIDTH {1} \
    CONFIG.C_PROBE4_WIDTH {8} \
    CONFIG.C_PROBE5_WIDTH {1} \
    CONFIG.C_PROBE6_WIDTH {8} \
    CONFIG.C_PROBE7_WIDTH {1} \
    CONFIG.C_PROBE8_WIDTH {1} \
    CONFIG.C_PROBE9_WIDTH {3} \
    CONFIG.C_DATA_DEPTH {16384} \
    CONFIG.C_TRIGIN_EN {false} \
    CONFIG.C_EN_STRG_QUAL {1} \
    CONFIG.ALL_PROBE_SAME_MU_CNT {2} \
] [get_bd_cells ila_msk_tx]

# Clock with divided clock (61.44 MHz) - modem clock domain
ad_connect clk_divider/clk_out ila_msk_tx/clk

# Probe 0: tx_data_bit - bit output to modulator
ad_connect msk_top/dbg_tx_data_bit ila_msk_tx/probe0

# Probe 1: tx_req - modulator requesting next bit (tclk)
ad_connect msk_top/dbg_tx_req ila_msk_tx/probe1

# Probe 2: encoder_tvalid - encoder has data available
ad_connect msk_top/dbg_encoder_tvalid ila_msk_tx/probe2

# Probe 3: encoder_tready - deserializer ready for byte
ad_connect msk_top/dbg_encoder_tready ila_msk_tx/probe3

# Probe 4: encoder_tdata - encoded byte data
ad_connect msk_top/dbg_encoder_tdata ila_msk_tx/probe4

# Probe 5: frame_complete - end of frame marker
ad_connect msk_top/dbg_frame_complete ila_msk_tx/probe5

# Probe 6: fifo_tdata - data from async FIFO (now exposed in msk_top)
ad_connect msk_top/dbg_fifo_tdata ila_msk_tx/probe6

# Probe 7: fifo_tvalid - FIFO has data (now exposed in msk_top)
ad_connect msk_top/dbg_fifo_tvalid ila_msk_tx/probe7

# Probe 8: fifo_tready - encoder ready for FIFO data (now exposed in msk_top)
ad_connect msk_top/dbg_fifo_tready ila_msk_tx/probe8

# Probe 9: encoder_debug_state - encoder FSM state (now exposed in msk_top)
ad_connect msk_top/dbg_encoder_state ila_msk_tx/probe9




##############################################################################
# ILA Debug Core - Randomizer Monitoring
##############################################################################
#create_bd_cell -type ip -vlnv xilinx.com:ip:ila:6.2 ila_randomizer
#set_property -dict [list \
#    CONFIG.C_MONITOR_TYPE {Native} \
#    CONFIG.C_NUM_OF_PROBES {5} \
#    CONFIG.C_PROBE0_WIDTH {8} \
#    CONFIG.C_PROBE1_WIDTH {8} \
#    CONFIG.C_PROBE2_WIDTH {8} \
#    CONFIG.C_PROBE3_WIDTH {1} \
#    CONFIG.C_PROBE4_WIDTH {3} \
#    CONFIG.C_DATA_DEPTH {16384} \
#    CONFIG.C_TRIGIN_EN {false} \
#    CONFIG.C_EN_STRG_QUAL {1} \
#    CONFIG.ALL_PROBE_SAME_MU_CNT {2} \
#] [get_bd_cells ila_randomizer]
#
#ad_connect clk_divider/clk_out ila_randomizer/clk
#
## Probe 0: LFSR state (should cycle through values, NOT stuck at FF)
#ad_connect msk_top/dbg_lfsr_state ila_randomizer/probe0
#
## Probe 1: Input byte (before XOR)
#ad_connect msk_top/dbg_input_byte ila_randomizer/probe1
#
## Probe 2: Randomized byte (after XOR) - should be input XOR lfsr_output
#ad_connect msk_top/dbg_rand_byte ila_randomizer/probe2
#
## Probe 3: Randomize active (trigger on rising edge to capture start)
#ad_connect msk_top/dbg_rand_active ila_randomizer/probe3
#
## Probe 4: Encoder state
#ad_connect msk_top/dbg_encoder_state ila_randomizer/probe4




##############################################################################
# ILA Debug Core #1: FEC Encoder Verification
##############################################################################
# PURPOSE: Prove the convolutional encoder is actually engaged
#
# WHAT TO LOOK FOR:
#   - encoder_state should show FEC_ENCODE state (value 4 or "100")
#   - encoder_tdata should show variety (NOT constant 0xFF or 0x00)
#   - If using bypass, tdata should match input pattern
#   - With real FEC, tdata should look "random" (encoded)
#
# TRIGGER SUGGESTION:
#   - Trigger on encoder_state == FEC_ENCODE (value 4)
#   - Or trigger on encoder_tvalid rising edge
#
# NOTE: To verify FEC is truly engaged (not bypassed), we need to expose
# the conv_encoder_k7 internal signals. See "ADDITIONAL PORTS NEEDED" below.
##############################################################################

create_bd_cell -type ip -vlnv xilinx.com:ip:ila:6.2 ila_fec_verify
set_property -dict [list \
    CONFIG.C_MONITOR_TYPE {Native} \
    CONFIG.C_NUM_OF_PROBES {13} \
    CONFIG.C_PROBE0_WIDTH {3} \
    CONFIG.C_PROBE1_WIDTH {8} \
    CONFIG.C_PROBE2_WIDTH {1} \
    CONFIG.C_PROBE3_WIDTH {1} \
    CONFIG.C_PROBE4_WIDTH {8} \
    CONFIG.C_PROBE5_WIDTH {1} \
    CONFIG.C_PROBE6_WIDTH {1} \
    CONFIG.C_PROBE7_WIDTH {1} \
    CONFIG.C_PROBE8_WIDTH {1} \
    CONFIG.C_PROBE9_WIDTH {1} \
    CONFIG.C_PROBE10_WIDTH {1} \
    CONFIG.C_PROBE11_WIDTH {1} \
    CONFIG.C_PROBE12_WIDTH {1} \
    CONFIG.C_DATA_DEPTH {16384} \
    CONFIG.C_TRIGIN_EN {false} \
    CONFIG.C_EN_STRG_QUAL {1} \
    CONFIG.ALL_PROBE_SAME_MU_CNT {2} \
] [get_bd_cells ila_fec_verify]

# Clock - use same clock as encoder (PS clock divided)
ad_connect clk_divider/clk_out ila_fec_verify/clk

# Probe 0: Encoder state machine (3 bits)
#   IDLE=0, COLLECT=1, RANDOMIZE=2, WAIT_ENCODER=3, FEC_ENCODE=4, INTERLEAVE=5, OUTPUT=6
ad_connect msk_top/dbg_encoder_state ila_fec_verify/probe0

# Probe 1: Encoder output data (8 bits) - what's being transmitted
ad_connect msk_top/dbg_encoder_tdata ila_fec_verify/probe1

# Probe 2: Encoder tvalid - encoder has data available
ad_connect msk_top/dbg_encoder_tvalid ila_fec_verify/probe2

# Probe 3: Encoder tready - deserializer ready for byte
ad_connect msk_top/dbg_encoder_tready ila_fec_verify/probe3

# Probe 4: FIFO data (8 bits) - data from PS before encoding
ad_connect msk_top/dbg_fifo_tdata ila_fec_verify/probe4

# Probe 5: FIFO tvalid - FIFO has data
ad_connect msk_top/dbg_fifo_tvalid ila_fec_verify/probe5

# Probe 6: FIFO tready - encoder ready to accept
ad_connect msk_top/dbg_fifo_tready ila_fec_verify/probe6

# Probe 7: Frame complete signal
ad_connect msk_top/dbg_frame_complete ila_fec_verify/probe7

# Probe 8: Convolutional encoder start pulse
ad_connect msk_top/dbg_conv_start ila_fec_verify/probe8

# Probe 9: Convolutional encoder busy (HIGH during encoding)
ad_connect msk_top/dbg_conv_busy ila_fec_verify/probe9

# Probe 10: Convolutional encoder done pulse
ad_connect msk_top/dbg_conv_done ila_fec_verify/probe10

# Probe 11 and 12: dac_enable_i0 and dac_enable_q0
ad_connect axi_ad9361/dac_enable_i0 ila_fec_verify/probe11

ad_connect axi_ad9361/dac_enable_q0 ila_fec_verify/probe12


##############################################################################
# ADDITIONAL PORTS NEEDED (to truly verify FEC engagement)
##############################################################################
# To see INSIDE the convolutional encoder, add these to msk_top.vhd:
#
#   -- In port declaration:
#   dbg_conv_encoder_start  : OUT std_logic;
#   dbg_conv_encoder_busy   : OUT std_logic;
#   dbg_conv_encoder_done   : OUT std_logic;
#   dbg_conv_shift_reg      : OUT std_logic_vector(5 DOWNTO 0);
#
# Then wire from ov_frame_encoder's conv_encoder_k7 instance.
#
# With those signals, add probes:
#   CONFIG.C_PROBE8_WIDTH {1}   -- conv_start
#   CONFIG.C_PROBE9_WIDTH {1}   -- conv_busy  
#   CONFIG.C_PROBE10_WIDTH {1}  -- conv_done
#   CONFIG.C_PROBE11_WIDTH {6}  -- shift_reg (K=7, 6 memory elements)
#
# Then connect:
#   ad_connect msk_top/dbg_conv_encoder_start ila_fec_verify/probe8
#   ad_connect msk_top/dbg_conv_encoder_busy  ila_fec_verify/probe9
#   ad_connect msk_top/dbg_conv_encoder_done  ila_fec_verify/probe10
#   ad_connect msk_top/dbg_conv_shift_reg     ila_fec_verify/probe11
#
# KEY VERIFICATION:
#   - conv_start should pulse once per frame
#   - conv_busy should be HIGH for ~1072 cycles (rate 1/2 encoder)
#   - shift_reg should show activity (NOT stuck at 000000)
#   - If shift_reg never changes, FEC is bypassed!
##############################################################################





##############################################################################
# ILA Debug Core #2: RX Soft Value Calibration
##############################################################################
# PURPOSE: Observe actual demodulator soft value distribution to calibrate
#          the quantization thresholds in frame_sync_detector_soft.vhd
#
# CURRENT THRESHOLDS (in quantize_soft function):
#   Strong '1':  soft < -300  -> "111"
#   Medium '1':  soft < -150  -> "101"
#   Weak '1':    soft < -50   -> "100"
#   Erasure:     -50 to +50   -> "011"
#   Weak '0':    soft < +150  -> "010"
#   Medium '0':  soft < +300  -> "001"
#   Strong '0':  soft >= +300 -> "000"
#
# CALIBRATION PROCEDURE:
#   1. Run loopback test with randomizer ON
#   2. Trigger on rx_bit_valid rising edge (continuous capture)
#   3. Look at rx_data_soft values - note the actual min/max range
#   4. Adjust thresholds proportionally to observed range
#
# POLARITY (msk_demodulator convention):
#   Negative soft values -> '1' bit
#   Positive soft values -> '0' bit
##############################################################################

create_bd_cell -type ip -vlnv xilinx.com:ip:ila:6.2 ila_rx_soft
set_property -dict [list \
    CONFIG.C_MONITOR_TYPE {Native} \
    CONFIG.C_NUM_OF_PROBES {11} \
    CONFIG.C_PROBE0_WIDTH {16} \
    CONFIG.C_PROBE1_WIDTH {1} \
    CONFIG.C_PROBE2_WIDTH {32} \
    CONFIG.C_PROBE3_WIDTH {32} \
    CONFIG.C_PROBE4_WIDTH {3} \
    CONFIG.C_PROBE5_WIDTH {1} \
    CONFIG.C_PROBE6_WIDTH {1} \
    CONFIG.C_PROBE7_WIDTH {1} \
    CONFIG.C_PROBE8_WIDTH {1} \
    CONFIG.C_PROBE9_WIDTH {12} \
    CONFIG.C_PROBE10_WIDTH {16} \
    CONFIG.C_DATA_DEPTH {16384} \
    CONFIG.C_TRIGIN_EN {false} \
    CONFIG.C_EN_STRG_QUAL {1} \
    CONFIG.ALL_PROBE_SAME_MU_CNT {2} \
] [get_bd_cells ila_rx_soft]

# Clock - use RX clock (same as demodulator)
# NOTE: May need to adjust based on your clock structure
ad_connect clk_divider/clk_out ila_rx_soft/clk

# Probe 0: rx_data_soft (16-bit signed) - THE KEY SIGNAL FOR CALIBRATION
#   Watch the actual range of values here!
#   If values are ±2000 but thresholds are ±300, you're under-utilizing soft info
ad_connect msk_top/dbg_rx_data_soft ila_rx_soft/probe0

# Probe 1: rx_bit_valid - valid pulse for each demodulated bit
#   Use this as trigger for continuous capture
ad_connect msk_top/dbg_rx_bit_valid ila_rx_soft/probe1

# Probe 2: Correlation value (32-bit signed) - current sync correlation
#   Watch this to understand HUNTING_THRESHOLD setting
ad_connect msk_top/dbg_rx_sync_correlation ila_rx_soft/probe2

# Probe 3: Peak correlation (32-bit) - highest correlation seen
#   Set HUNTING_THRESHOLD to ~75% of this value
ad_connect msk_top/dbg_rx_sync_corr_peak ila_rx_soft/probe3

# Probe 4: Frame sync state (3 bits)
#   HUNTING=1, LOCKED=2, OUTPUT_DATA=3, OUTPUT_SOFT=4
ad_connect msk_top/dbg_rx_sync_state ila_rx_soft/probe4

# Probe 5: Bit correlation (decorrelated bit)
ad_connect msk_top/dbg_rx_bit_corr ila_rx_soft/probe5

# Probe 6: tx_req (bit clock reference for timing)
ad_connect msk_top/dbg_tx_req ila_rx_soft/probe6

# Probe 7: External rx_svalid from ADC interface
ad_connect msk_top/dbg_rx_svalid_in ila_rx_soft/probe7

# Probe 8: Internal rx_sample_clk to demodulator  
ad_connect msk_top/dbg_rx_sample_clk ila_rx_soft/probe8

# Probe 9: Actual sample data going to demodulator (12 bits)
ad_connect msk_top/dbg_rx_samples_dec ila_rx_soft/probe9

# Probe 10: sample data from the ADC before it gets to msk_top
ad_connect msk_top/dbg_rx_samples_I_raw ila_rx_soft/probe10

##############################################################################
# THRESHOLD CALIBRATION QUICK REFERENCE
##############################################################################
#
# After capturing, note the observed rx_data_soft range:
#
# | Observed Range | Suggested Thresholds                    |
# |----------------|-----------------------------------------|
# | ±300 (current) | -300, -150, -50, +50, +150, +300        |
# | ±1000          | -900, -500, -150, +150, +500, +900      |
# | ±2000          | -1800, -1000, -300, +300, +1000, +1800  |
# | ±4000          | -3600, -2000, -600, +600, +2000, +3600  |
# | ±8000          | -7200, -4000, -1200, +1200, +4000, +7200|
#
# Rule of thumb for symmetric thresholds:
#   - Erasure zone: ±(max * 0.075)  -- center 15% of range
#   - Weak zone:    ±(max * 0.25)   -- next 35%
#   - Medium zone:  ±(max * 0.50)   -- next 50%
#   - Strong zone:  beyond medium   -- top ~15%
#
# HUNTING_THRESHOLD calibration:
#   Expected peak correlation ? 24 × average(|soft_max|)
#   Set HUNTING_THRESHOLD = 0.70 × expected_peak
#   Set LOCKED_THRESHOLD  = 0.40 × expected_peak
#
# Example: If soft values range ±2000
#   Expected peak = 24 × 2000 = 48,000
#   HUNTING_THRESHOLD = 0.70 × 48000 = 33,600
#   LOCKED_THRESHOLD  = 0.40 × 48000 = 19,200
#
##############################################################################
# WHAT TO LOOK FOR IN ILA CAPTURE
##############################################################################
#
# 1. rx_data_soft distribution:
#    - Should see values spanning the full ± range
#    - Should be roughly symmetric around 0
#    - If biased, check randomizer is ON
#
# 2. Correlation behavior:
#    - Should see spikes at sync word locations
#    - Peak should be ~24 × soft amplitude
#    - If correlation never exceeds threshold, frame sync won't lock
#
# 3. State machine:
#    - Should see HUNTING -> LOCKED transition when sync is found
#    - If stuck in HUNTING, correlation threshold too high
#
# TROUBLESHOOTING:
#   - All soft values near 0?       -> Demodulator not running
#   - Soft values very small (±10)? -> Signal too weak or wrong freq
#   - Asymmetric distribution?      -> DC offset or polarity issue
#   - Never locks?                  -> Lower HUNTING_THRESHOLD
#   - Locks then loses lock?        -> Raise LOCKED_THRESHOLD
#
##############################################################################








##############################################################################
# LVDS SIGNALS (External - requires scope/logic analyzer)
##############################################################################
# These are physical pins going to the AD9361 chip:
#   tx_clk_out_p/n   : TX clock to AD9361
#   tx_frame_out_p/n : TX frame signal
#   tx_data_out_p/n  : TX data (6-bit DDR)
#
# Cannot probe with ILA - need external test equipment.
# The axi_ad9361 IP handles the LVDS serialization internally.
##############################################################################
