if { [info exists ::env(PROJECT_NAME)] } {
  set project_name $::env(PROJECT_NAME)
} else {
  set project_name "e310"
}

# enable E310 specific settings
if { $project_name eq "e310" } {
  set e310 "e310"
}

if { $project_name eq "libre" } {
  set lvds "lvds"
}


source $::tezuka_hdl_dir/common/xilinx_init.tcl
source $::tezuka_hdl_dir/boards/$project_name/ps7.tcl
source $::tezuka_hdl_dir/boards/$project_name/ports.tcl
#source $::tezuka_hdl_dir/common/xilinx_ad9361.tcl
source $::tezuka_hdl_dir/common/xilinx_ad9361_no_pack.tcl
source $::tezuka_hdl_dir/common/maia.tcl
source  msk.tcl
#source $::tezuka_hdl_dir/common/maiafirtoiq.tcl
#source $::tezuka_hdl_dir/common/maiaffttoiq.tcl
#source $::tezuka_hdl_dir/common/minimal.tcl
#source $::tezuka_hdl_dir/boards/$project_name/vcxo_ctrl.tcl
#source $::tezuka_hdl_dir/common/sweeper.tcl
#source $::tezuka_hdl_dir/common/cs12_cs8.tcl