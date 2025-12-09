####################################################################################
## Copyright (c) 2018 - 2023 Analog Devices, Inc.
### SPDX short identifier: BSD-1-Clause
## Auto-generated, do not modify!
####################################################################################
export ADI_IGNORE_VERSION_CHECK = 1
export ADI_GENERATE_UTILIZATION = 1
PROJECT_NAME := libre

M_DEPS += ../../hdl/projects/common/xilinx/adi_fir_filter_constr.xdc
M_DEPS += ../../hdl/projects/common/xilinx/adi_fir_filter_bd.tcl
M_DEPS += ../../hdl/library/util_cdc/sync_bits.v
M_DEPS += ../../hdl/library/common/util_pulse_gen.v
M_DEPS += ../../hdl/library/common/ad_iobuf.v
M_DEPS += ../../hdl/library/common/ad_bus_mux.v
M_DEPS += ../../hdl/library/axi_tdd/scripts/axi_tdd.tcl
M_DEPS += ../../hdl/library/axi_ad9361/axi_ad9361_delay.tcl
M_DEPS += msk_top
M_DEPS += ../../src/msk_top.vhd
M_DEPS += ../../src/ov_frame_encoder.vhd
M_DEPS += ../../src/conv_encoder_k7.vhd
M_DEPS += ../../src/axis_async_fifo.vhd
M_DEPS += ../../src/axis_dma_adapter.vhd
M_DEPS += ../../msk_demodulator/src/msk_demodulator.vhd
M_DEPS += system_bd.tcl
M_DEPS += system_constr.xdc

LIB_DEPS += axi_ad9361
LIB_DEPS += axi_dmac
LIB_DEPS += axi_tdd
LIB_DEPS += util_pack/util_cpack2
LIB_DEPS += util_pack/util_upack2

include ../../hdl/projects/scripts/project-xilinx.mk

msk_top:
	make -C ../../library
