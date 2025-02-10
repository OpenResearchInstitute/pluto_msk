# ip
#   "src/axi_ctrlif.vhd" 

source ../hdl/scripts/adi_env.tcl
source $ad_hdl_dir/library/scripts/adi_ip_xilinx.tcl

adi_ip_create msk_top

read_vhdl -library "desyrdl" "../rdl/vhdl/desyrdl/pkg_desyrdl_common.vhd"

#set_property FILE_TYPE {VHDL 2008} [get_files $ad_hdl_dir/library/msk_top/src/*.vhd]
adi_ip_files msk_top [list \
  "../rdl/vhdl/msk_top_regs/msk_top_regs_decoder_axi4l.vhd" \
  "../rdl/vhdl/msk_top_regs/pkg_msk_top_regs.vhd" \
  "../rdl/vhdl/msk_top_regs/msk_top_regs.vhd" \
  "../msk_demodulator/src/costas_loop.vhd" \
  "../pi_controller/src/pi_controller.vhd" \
  "../lowpass_ema/src/lowpass_ema.vhd" \
  "../power_detector/src/power_detector.vhd" \
  "../msk_demodulator/src/msk_demodulator.vhd" \
  "../msk_modulator/src/msk_modulator.vhd" \
  "../src/msk_top.vhd" \
  "../src/msk_top_csr.vhd" \
  "../nco/src/nco.vhd" \
  "../prbs/src/prbs_gen.vhd" \
  "../prbs/src/prbs_mon.vhd" \
  "../nco/src/sin_cos_lut.vhd" ]

# use this command if we have AXI lite interface for register control
adi_ip_properties msk_top


adi_add_bus "s_axis" "slave" \
  "xilinx.com:interface:axis_rtl:1.0" \
  "xilinx.com:interface:axis:1.0" \
  [list {"s_axis_ready" "TREADY"} \
    {"s_axis_valid" "TVALID"} \
    {"s_axis_data" "TDATA"} \
  ]
adi_add_bus_clock "s_axis_aclk" "s_axis" "s_axis_aresetn"


ipx::save_core [ipx::current_core]

