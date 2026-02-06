# Makefile

# defaults
SIM ?= nvc
TOPLEVEL_LANG ?= vhdl
GUI = 1
SCRIPT_FILE =

ifeq ($(SIM),ghdl)
	COMPILE_ARGS = --std=08
	EXTRA_ARGS = --std=08
	SIM_ARGS = --wave=msk_top.ghw 
endif

ifeq ($(SIM),nvc)
	EXTRA_ARGS = --ieee-warnings=off
	SIM_ARGS = --wave=msk_top.ghw
endif

SRC = ../src
RDL = ../rdl/

# use VHDL_SOURCES for VHDL files
VHDL_SOURCES += $(RDL)/src/axi4lite_intf_pkg.vhd \
				$(RDL)/src/reg_utils.vhd \
				$(RDL)/outputs/rtl/msk_top_regs_pkg.vhd \
				$(RDL)/outputs/rtl/msk_top_regs.vhd \
				$(SRC)/pulse_detect.vhd \
				$(SRC)/data_capture.vhd \
				$(SRC)/cdc_resync.vhd \
				$(SRC)/frame_sync_detector_soft.vhd \
				$(SRC)/axis_async_fifo.vhd \
				$(SRC)/axis_dma_adapter.vhd \
				$(SRC)/byte_to_bit_deserializer.vhd \
				$(SRC)/axi_lite_cdc.vhd \
				$(SRC)/msk_top_csr.vhd \
				$(SRC)/conv_encoder_k7.vhd \
				$(SRC)/viterbi_decoder_k7_soft.vhd \
				$(SRC)/ov_frame_encoder.vhd \
				$(SRC)/ov_frame_decoder_soft.vhd \
				../lowpass_ema/src/lowpass_ema.vhd \
				../power_detector/src/power_detector.vhd \
				../nco/src/nco.vhd \
				../nco/src/sin_cos_lut.vhd \
				../msk_modulator/src/msk_modulator.vhd \
				../pi_controller/src/pi_controller.vhd \
				../msk_demodulator/src/costas_lock_detect.vhd \
				../msk_demodulator/src/costas_loop.vhd \
				../msk_demodulator/src/msk_demodulator.vhd \
				../prbs/src/prbs_gen.vhd \
				../prbs/src/prbs_mon.vhd \
				$(SRC)/msk_top.vhd

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
COCOTB_TOPLEVEL = msk_top

# MODULE is the basename of the Python test file
COCOTB_TEST_MODULES = msk_test

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
