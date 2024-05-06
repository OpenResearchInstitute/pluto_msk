# Makefile

# defaults
SIM ?= ghdl
TOPLEVEL_LANG ?= vhdl
GUI = 1
SCRIPT_FILE =
SIM_ARGS = --wave=msk_top.ghw

SRC = ../src

VHDL_SOURCES += $(SRC)/nco.vhd $(SRC)/sin_cos_lut.vhd $(SRC)/msk_modulator.vhd $(SRC)/costas_loop.vhd $(SRC)/msk_demodulator.vhd $(SRC)/msk_top.vhd
# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = msk_top

# MODULE is the basename of the Python test file
MODULE = msk_test

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
