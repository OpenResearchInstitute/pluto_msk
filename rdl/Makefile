
all: msk_top_regs.pdf msk_top_regs.h gen_files_cocotb.txt gen_files_vhdl.txt 

gen_files_cocotb.txt : msk_top_regs_desy.rdl
	desyrdl -i msk_top_regs_desy.rdl -f cocotb

gen_files_vhdl.txt : msk_top_regs_desy.rdl
	desyrdl -i msk_top_regs_desy.rdl -f vhdl

msk_top_regs_desy.rdl : msk_top_regs.rdl msk_top_regs.pl
	rm msk_top_regs_desy.rdl
	./msk_top_regs.pl msk_top_regs.rdl > msk_top_regs_desy.rdl

msk_top_regs.md: msk_top_regs.rdl
	peakrdl markdown msk_top_regs.rdl -o msk_top_regs.md 

msk_top_regs.h: msk_top_regs.rdl
	peakrdl c-header msk_top_regs.rdl -o msk_top_regs.h

msk_top_regs.pdf: msk_top_regs.md
	pandoc -o msk_top_regs.pdf msk_top_regs.md
