####################################################################################
## Copyright (c) 2018 - 2023 Analog Devices, Inc.
### SPDX short identifier: BSD-1-Clause
## Auto-generated, do not modify!
####################################################################################

PROJECT_NAME := libre
M_DEPS += ../../../hdl/library/common/ad_iobuf.v
M_DEPS += ../../../hdl/library/axi_ad9361/axi_ad9361_delay.tcl

LIB_DEPS += xilinx/util_clkdiv
LIB_DEPS += axi_ad9361
LIB_DEPS += util_rfifo
LIB_DEPS += util_wfifo


M_DEPS += msk_top
M_DEPS += ../../../src/msk_top.vhd
M_DEPS += ../../../src/ov_frame_encoder.vhd
M_DEPS += ../../../src/conv_encoder_k7.vhd
M_DEPS += ../../../src/axis_async_fifo.vhd
M_DEPS += ../../../src/axis_dma_adapter.vhd
M_DEPS += ../../../msk_demodulator/src/msk_demodulator.vhd
M_DEPS += ../common/system_bd.tcl
M_DEPS += system_constr.xdc

include ../../../hdl/projects/scripts/project-xilinx.mk

msk_top:
	make -C ../../../library

