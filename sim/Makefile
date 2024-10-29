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
	SIM_ARGS = --wave=msk_top.ghw
endif

SRC = ../src
RDL = ../rdl/vhdl/msk_top_regs

VHDL_SOURCES_desyrdl = ../rdl/vhdl/desyrdl/pkg_desyrdl_common.vhd

VHDL_LIB_ORDER = desyrdl

# use VHDL_SOURCES for VHDL files
VHDL_SOURCES += $(RDL)/msk_top_regs_decoder_axi4l.vhd \
				$(RDL)/pkg_msk_top_regs.vhd \
				$(RDL)/msk_top_regs.vhd \
				$(SRC)/msk_top_csr.vhd \
				../nco/src/nco.vhd \
				../nco/src/sin_cos_lut.vhd \
				../msk_modulator/src/msk_modulator.vhd \
				../pi_controller/src/pi_controller.vhd \
				../msk_demodulator/src/costas_loop.vhd \
				../msk_demodulator/src/msk_demodulator.vhd \
				../prbs/src/prbs_gen.vhd \
				../prbs/src/prbs_mon.vhd \
				$(SRC)/msk_top.vhd

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = msk_top

# MODULE is the basename of the Python test file
MODULE = msk_test

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
