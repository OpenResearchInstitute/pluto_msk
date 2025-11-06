
#all: msk_top_regs.pdf msk_top_regs.h msk_top_regs_desy.rdl gen_files_cocotb.txt gen_files_vhdl.txt 

SRCS 		= src/regblock_udps.rdl src/msk_top_regs.rdl 

OUTDOCS 	= outputs/docs
OUTRTL  	= outputs/rtl
OUTPYTHON	= outputs/python
OUTCHEADER  = outputs/c-header

all: $(OUTDOCS)/msk_top_regs.pdf \
	 $(OUTDOCS)/msk_top_regs.md \
	 $(OUTDOCS)/html/index.html \
	 $(OUTRTL)/msk_top_regs.vhd \
	 $(OUTPYTHON)/__init__.py \
	 $(OUTCHEADER)/msk_top_regs.h

$(OUTDOCS)/msk_top_regs.md: $(SRCS)
	peakrdl markdown $(SRCS) -o $(OUTDOCS)/msk_top_regs.md 

$(OUTDOCS)/html/index.html: $(SRCS)
	peakrdl html $(SRCS) -o $(OUTDOCS)/html

$(OUTCHEADER)/msk_top_regs.h: $(SRCS)
	peakrdl c-header $(SRCS) -o outputs/c-header/msk_top_regs.h

$(OUTRTL)/msk_top_regs.vhd: $(SRCS)
	peakrdl regblock-vhdl $(SRCS) -o $(OUTRTL) --cpuif axi4-lite

$(OUTDOCS)/msk_top_regs.pdf: $(OUTDOCS)/html/index.html
	pandoc -o $(OUTDOCS)/msk_top_regs.pdf $(OUTDOCS)/html/index.html --pdf-engine=weasyprint --css=$(OUTDOCS)/html/css/theme.css

$(OUTPYTHON)/__init__.py: $(SRCS)
	peakrdl python $(SRCS) --async -o $(OUTPYTHON)

clean:
	rm -r outputs/docs/*
	rm outputs/c-header/*
	rm -r outputs/python/*
	rm outputs/rtl/*
