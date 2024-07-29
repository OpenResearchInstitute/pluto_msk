# Makefile

# defaults
SIM ?= nvc
TOPLEVEL_LANG ?= vhdl
GUI = 1
SCRIPT_FILE =

ifeq ($(SIM),ghdl)
	COMPILE_ARGS = --std=08
endif

SIM_ARGS = --wave=msk_top.ghw

SRC = ../src

VHDL_SOURCES += ../nco/src/nco.vhd \
				../nco/src/sin_cos_lut.vhd \
				../msk_modulator/src/msk_modulator.vhd \
				../pi_controller/src/pi_controller.vhd \
				../msk_demodulator/src/costas_loop.vhd \
				../msk_demodulator/src/msk_demodulator.vhd \
				../prbs/src/prbs_gen.vhd \
				../prbs/src/prbs_mon.vhd \
				$(SRC)/msk_top.vhd

# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = msk_top

# MODULE is the basename of the Python test file
MODULE = msk_test

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
