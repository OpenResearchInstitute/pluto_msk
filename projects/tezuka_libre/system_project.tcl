set IGNORE_VERSION_CHECK 1

source ../../../../adi-hdl/scripts/adi_env.tcl
source $ad_hdl_dir/projects/scripts/adi_project_xilinx.tcl
source $ad_hdl_dir/projects/scripts/adi_board.tcl
source ../../../tezuka_env.tcl

if { [info exists ::env(PROJECT_NAME)] } {
  set project_name $::env(PROJECT_NAME)
} else {
  set project_name "e310"
}

if {[file exists $project_name]} {
    file delete -force $project_name
}

if [regexp "e310" $project_name] {
     set p_device "xc7z020clg400-2"
   }

if [regexp "libre" $project_name] {
     set p_device "xc7z020clg400-2"
   }

adi_project $project_name

adi_project_files $project_name [list \
  "$::tezuka_hdl_dir/boards/$project_name/system_top.v" \
  "$::tezuka_hdl_dir/boards/$project_name/system_constr.xdc" \
  "$ad_hdl_dir/library/common/ad_iobuf.v"]


# use improved implementation strategy for best timing results
set_property strategy Performance_ExplorePostRoutePhysOpt [get_runs impl_1]
set_property is_enabled false [get_files  *system_sys_ps7_0.xdc]

adi_project_run $project_name
source $ad_hdl_dir/library/axi_ad9361/axi_ad9361_delay.tcl
