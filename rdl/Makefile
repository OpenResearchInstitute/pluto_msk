
#all: msk_top_regs.pdf msk_top_regs.h msk_top_regs_desy.rdl gen_files_cocotb.txt gen_files_vhdl.txt 

SRCS 		= src/regblock_udps.rdl src/msk_top_regs.rdl 

OUTDOCS 	= outputs/docs
OUTRTL  	= outputs/rtl
OUTPYTHON	= outputs/python
OUTCHEADER  = outputs/c-header

all: $(OUTDOCS)/msk_top_regs.pdf \
	 $(OUTDOCS)/msk_top_regs.md \
	 $(OUTDOCS)/html/index.html \
	 $(OUTDOCS)/msk_top_regs.docx \
	 $(OUTRTL)/msk_top_regs.vhd \
	 $(OUTPYTHON)/__init__.py \
	 $(OUTCHEADER)/msk_top_regs.h

$(OUTDOCS)/msk_top_regs.md: $(SRCS)
	peakrdl markdown $(SRCS) -o $(OUTDOCS)/msk_top_regs.md 

$(OUTDOCS)/msk_top_regs.docx: $(SRCS)
	peakrdl docx $(SRCS) -o $(OUTDOCS)/msk_top_regs.docx --title "MSK Modem Registers"

$(OUTDOCS)/html/index.html: $(SRCS)
	peakrdl html $(SRCS) -o $(OUTDOCS)/html

$(OUTCHEADER)/msk_top_regs.h: $(SRCS)
	peakrdl c-header $(SRCS) -o outputs/c-header/msk_top_regs.h

$(OUTRTL)/msk_top_regs.vhd: $(SRCS)
	peakrdl regblock-vhdl $(SRCS) -o $(OUTRTL) --cpuif axi4-lite
	@echo "Converting VHDL-2019 to VHDL-2008 for XSim compatibility..."
	perl -i -pe 's/^context ieee\.ieee_std_context;$$/use ieee.std_logic_1164.all;\nuse ieee.numeric_std.all;/' \
    outputs/rtl/msk_top_regs.vhd \
    src/axi4lite_intf_pkg.vhd \
    src/reg_utils.vhd
	@echo "Conversion complete!"


$(OUTDOCS)/msk_top_regs.pdf: $(OUTDOCS)/msk_top_regs.md 
	pandoc -o $(OUTDOCS)/msk_top_regs.pdf $(OUTDOCS)/msk_top_regs.md

$(OUTPYTHON)/__init__.py: $(SRCS)
	peakrdl python $(SRCS) --async -o $(OUTPYTHON)

clean:
	rm -rf outputs/docs/*
	rm -f outputs/c-header/*
	rm -rf outputs/python/*
	rm -f outputs/rtl/*
