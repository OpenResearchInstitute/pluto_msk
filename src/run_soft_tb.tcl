create_project -force tb_soft_viterbi ./tb_soft_viterbi -part xc7z020clg400-2

add_files {viterbi_decoder_k7_simple.vhd viterbi_decoder_k7_soft.vhd tb_viterbi_soft.vhd}

set_property top tb_viterbi_soft [get_filesets sim_1]
set_property target_language VHDL [current_project]

launch_simulation
run all
