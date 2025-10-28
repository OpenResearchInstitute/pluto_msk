# ip
#   "src/axi_ctrlif.vhd" 

source ../hdl/scripts/adi_env.tcl
source $ad_hdl_dir/library/scripts/adi_ip_xilinx.tcl

adi_ip_create msk_top

read_vhdl -vhdl2008 "../rdl/src/axi4lite_intf_pkg.vhd"
read_vhdl -vhdl2008 "../rdl/src/reg_utils.vhd"
read_vhdl "../rdl/outputs/rtl/msk_top_regs_pkg.vhd"
read_vhdl -vhdl2008 "../rdl/outputs/rtl/msk_top_regs.vhd"

#set_property FILE_TYPE {VHDL 2008} [get_files $ad_hdl_dir/library/msk_top/src/*.vhd]
adi_ip_files msk_top [list \
  "../msk_demodulator/src/costas_loop.vhd" \
  "../pi_controller/src/pi_controller.vhd" \
  "../lowpass_ema/src/lowpass_ema.vhd" \
  "../power_detector/src/power_detector.vhd" \
  "../msk_demodulator/src/msk_demodulator.vhd" \
  "../msk_modulator/src/msk_modulator.vhd" \
  "../src/msk_top.vhd" \
  "../src/msk_top_csr.vhd" \
  "../src/axis_dma_adapter.vhd" \
  "../src/axis_async_fifo.vhd" \
  "../src/byte_to_bit_deserializer.vhd" \
  "../src/bit_to_byte_serializer.vhd" \
  "../src/frame_sync_detector.vhd" \
  "../nco/src/nco.vhd" \
  "../prbs/src/prbs_gen.vhd" \
  "../prbs/src/prbs_mon.vhd" \
  "../nco/src/sin_cos_lut.vhd" ]

# use this command if we have AXI lite interface for register control
adi_ip_properties msk_top


# Remove auto-inferred ADI custom bus interfaces before defining proper AXI-Stream
set core [ipx::current_core]
foreach intf {rx s_axis tx} {
    if {[ipx::get_bus_interfaces $intf -of_objects $core] ne ""} {
        ipx::remove_bus_interface $intf $core
    }
}


adi_add_bus "s_axis" "slave" \
  "xilinx.com:interface:axis_rtl:1.0" \
  "xilinx.com:interface:axis:1.0" \
  [list \
    {"s_axis_ready" "TREADY"} \
    {"s_axis_valid" "TVALID"} \
    {"s_axis_data" "TDATA"} \
    {"s_axis_tlast" "TLAST"} \
    {"s_axis_tkeep" "TKEEP"}]

adi_add_bus_clock "s_axis_aclk" "s_axis" "s_axis_aresetn"

# RX AXIS master interface (from MSK to DMA)
adi_add_bus "m_axis" "master" \
  "xilinx.com:interface:axis_rtl:1.0" \
  "xilinx.com:interface:axis:1.0" \
  [list \
    {"m_axis_tready" "TREADY"} \
    {"m_axis_tvalid" "TVALID"} \
    {"m_axis_tdata" "TDATA"} \
    {"m_axis_tlast" "TLAST"}]

# m_axis shares the same clock as the demodulator
adi_add_bus_clock "s_axis_aclk" "m_axis" "s_axis_aresetn"

ipx::save_core [ipx::current_core]

ipx::save_core [ipx::current_core]

