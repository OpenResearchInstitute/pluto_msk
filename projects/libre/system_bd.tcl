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
# CLOCK_DIVIDER: Using 1R1T mode as required by LibreSDR device tree
ad_ip_parameter axi_ad9361 CONFIG.MODE_1R1T 1
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
ad_connect  msk_top/s_axis_aclk axi_ad9361/l_clk

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
    CONFIG.Depth {1} \
    CONFIG.DefaultData {0000000000000000} \
    CONFIG.AsyncInitVal {0000000000000000} \
] [get_bd_cells tx_i_sync]

create_bd_cell -type ip -vlnv xilinx.com:ip:c_shift_ram:12.0 tx_q_sync
set_property -dict [list \
    CONFIG.Width {16} \
    CONFIG.Depth {1} \
    CONFIG.DefaultData {0000000000000000} \
    CONFIG.AsyncInitVal {0000000000000000} \
] [get_bd_cells tx_q_sync]

# Clock sync registers with l_clk (245 MHz)
ad_connect axi_ad9361/l_clk tx_i_sync/CLK
ad_connect axi_ad9361/l_clk tx_q_sync/CLK

# MSK outputs -> sync registers
ad_connect msk_top/tx_samples_I tx_i_sync/D
ad_connect msk_top/tx_samples_Q tx_q_sync/D

# Sync registers -> AD9361
ad_connect tx_i_sync/Q axi_ad9361/dac_data_i0
ad_connect tx_q_sync/Q axi_ad9361/dac_data_q0

ad_connect  msk_top/tx_enable axi_ad9361/dac_enable_i0

# CLOCK_DIVIDER: tx_valid tied HIGH - every 61.44 MHz clock cycle is a valid sample
# (Previously connected to dac_valid_i0 which pulses in l_clk domain)
ad_connect  msk_top/tx_valid VCC

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
ad_connect  msk_top/rx_svalid VCC

# MSK RX AXIS to DMA - interface connection
ad_connect  msk_top/m_axis axi_ad9361_adc_dma/s_axis
