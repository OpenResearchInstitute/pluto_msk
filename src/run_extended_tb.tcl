create_project -force tb_extended ./tb_extended -part xc7z020clg400-2
add_files {viterbi_decoder_k7_simple.vhd viterbi_decoder_k7_soft.vhd tb_viterbi_extended.vhd}
set_property top tb_viterbi_extended [get_filesets sim_1]
set_property target_language VHDL [current_project]
launch_simulation
run all
