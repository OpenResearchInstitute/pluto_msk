####################################################################################
## Copyright (c) 2018 - 2023 Analog Devices, Inc.
### SPDX short identifier: BSD-1-Clause
## Auto-generated, do not modify!
####################################################################################
#make PROJECT_NAME=e310

PROJECT_NAME ?= e310

export PROJECT_NAME

M_DEPS += ../../../../adi-hdl/library/common/ad_iobuf.v
M_DEPS += ../../../../adi-hdl/library/axi_ad9361/axi_ad9361_delay.tcl
M_DEPS += ip_cores
LIB_DEPS += xilinx/util_clkdiv
LIB_DEPS += axi_ad9361
LIB_DEPS += util_rfifo
LIB_DEPS += util_wfifo

M_DEPS += msk_top
M_DEPS += ../../src/msk_top.vhd
M_DEPS += ../../src/ov_frame_encoder.vhd
M_DEPS += ../../src/conv_encoder_k7.vhd
M_DEPS += ../../src/axis_async_fifo.vhd
M_DEPS += ../../src/axis_dma_adapter.vhd
M_DEPS += ../../msk_demodulator/src/msk_demodulator.vhd

include ../../../../adi-hdl/projects/scripts/project-xilinx.mk

DEST = ../../../../../../tezuka_fw/board/tezuka/$(PROJECT_NAME)/bitstream


ip_cores:
	$(MAKE) -C ../../../../ip

msk_top:
	make -C ../../library

install :
	bash -c "cp -f $(PROJECT_NAME).sdk/system_top.xsa $(DEST)/maia-iio/"
	bash -c "rm -rf build"
	bash -c "xsct create_fsbl_project.tcl $(PROJECT_NAME)"
	bash -c "cp -f build/sdk/fsbl/Release/fsbl.elf $(DEST)/"
	bash "./all_overclock.sh"
	bash -c "cp -f build/sdk/fsbl/Release/fsbl*.elf $(DEST)/overclock/"
	bash -c "git describe > $(DEST)/overclock/bit.txt"
.PHONY: ip_cores install

all: ip_cores install
