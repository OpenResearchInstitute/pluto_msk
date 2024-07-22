####################################################################################
## Copyright (c) 2018 - 2023 Analog Devices, Inc.
### SPDX short identifier: BSD-1-Clause
## Auto-generated, do not modify!
####################################################################################
export ADI_IGNORE_VERSION_CHECK = 1
PROJECT_NAME := pluto

M_DEPS += ../../hdl/projects/common/xilinx/adi_fir_filter_constr.xdc
M_DEPS += ../../hdl/projects/common/xilinx/adi_fir_filter_bd.tcl
M_DEPS += ../../hdl/library//util_cdc/sync_bits.v
M_DEPS += ../../hdl/library/common/util_pulse_gen.v
M_DEPS += ../../hdl/library/common/ad_iobuf.v
M_DEPS += ../../hdl/library/common/ad_bus_mux.v
M_DEPS += ../../hdl/library/axi_tdd/scripts/axi_tdd.tcl
M_DEPS += ../../hdl/library/axi_ad9361/axi_ad9361_delay.tcl
M_DEPS += msk_top

M_VIVADO := vivado -mode batch -source

LIB_DEPS += axi_ad9361
LIB_DEPS += axi_dmac
LIB_DEPS += axi_tdd
LIB_DEPS += util_pack/util_cpack2
LIB_DEPS += util_pack/util_upack2
#LIB_DEPS += msk_top

include ../../hdl/projects/scripts/project-xilinx.mk


msk_top: 
	make -C ../../library clean
	make -C ../../library 

