
all : gen_files_adoc.txt gen_files_cocotb.txt gen_files_vhdl.txt

gen_files_adoc.txt : msk_top_regs.rdl
	desyrdl -i msk_top_regs.rdl -f adoc

gen_files_cocotb.txt : msk_top_regs.rdl
	desyrdl -i msk_top_regs.rdl -f cocotb

gen_files_vhdl.txt : msk_top_regs.rdl
	desyrdl -i msk_top_regs.rdl -f vhdl