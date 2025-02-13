source ../../hdl/scripts/adi_env.tcl
source $ad_hdl_dir/projects/scripts/adi_project_xilinx.tcl
source $ad_hdl_dir/projects/scripts/adi_board.tcl

adi_project_create pluto 0 {} "xc7z010clg225-1"

adi_project_files pluto [list \
  "system_top.v" \
  "system_constr.xdc" \
  "$ad_hdl_dir/library/common/ad_iobuf.v"]

set_property is_enabled false [get_files  *system_sys_ps7_0.xdc]
adi_project_run pluto
source $ad_hdl_dir/library/axi_ad9361/axi_ad9361_delay.tcl

source ../../scripts/batch_insert_ila.tcl

if {[info exists ::env(DEBUG_CORE)]} {
   set DEBUG_CORE $::env(DEBUG_CORE)
} elseif {![info exists DEBUG_CORE]} {
   set DEBUG_CORE 0
}

if {$DEBUG_CORE == 1} {
  open_checkpoint pluto.runs/impl_1/system_top.dcp
  batch_insert_ila 2048
  opt_design
  read_checkpoint -incremental pluto.runs/impl_1/system_top_routed.dcp
  place_design
  route_design
  write_checkpoint
  rename bitstream
  write_bitstream
}
