# ip
source ../hdl/scripts/adi_env.tcl
source $ad_hdl_dir/library/scripts/adi_ip_xilinx.tcl

adi_ip_create msk_top

# Register ALL VHDL-2008 files first with read_vhdl -vhdl2008
# Order matters: dependencies before modules that use them
read_vhdl -vhdl2008 "../rdl/src/axi4lite_intf_pkg.vhd"
read_vhdl -vhdl2008 "../rdl/src/reg_utils.vhd"
read_vhdl "../rdl/outputs/rtl/msk_top_regs_pkg.vhd"
read_vhdl -vhdl2008 "../rdl/outputs/rtl/msk_top_regs.vhd"
read_vhdl -vhdl2008 "../src/conv_encoder_k7.vhd"
read_vhdl -vhdl2008 "../src/viterbi_decoder_k7_simple.vhd"
read_vhdl -vhdl2008 "../src/viterbi_decoder_k7_soft.vhd"
read_vhdl -vhdl2008 "../src/ov_frame_encoder.vhd"
read_vhdl -vhdl2008 "../src/ov_frame_decoder.vhd"
read_vhdl -vhdl2008 "../src/ov_frame_decoder_soft.vhd"

# Register all non-VHDL-2008 files
adi_ip_files msk_top [list \
  "../msk_demodulator/src/costas_loop.vhd" \
  "../pi_controller/src/pi_controller.vhd" \
  "../lowpass_ema/src/lowpass_ema.vhd" \
  "../power_detector/src/power_detector.vhd" \
  "../msk_demodulator/src/msk_demodulator.vhd" \
  "../msk_modulator/src/msk_modulator.vhd" \
  "../src/cdc_resync.vhd" \
  "../src/pulse_detect.vhd" \
  "../src/data_capture.vhd" \
  "../src/msk_top.vhd" \
  "../src/msk_top_csr.vhd" \
  "../src/axis_dma_adapter.vhd" \
  "../src/axis_async_fifo.vhd" \
  "../src/byte_to_bit_deserializer.vhd" \
  "../src/frame_sync_detector.vhd" \
  "../src/frame_sync_detector_soft.vhd" \
  "../nco/src/nco.vhd" \
  "../prbs/src/prbs_gen.vhd" \
  "../prbs/src/prbs_mon.vhd" \
  "../nco/src/sin_cos_lut.vhd" ]

# Configure IP properties
adi_ip_properties msk_top

# Remove auto-inferred ADI custom bus interfaces before defining proper AXI-Stream
set core [ipx::current_core]
foreach intf {rx s_axis tx} {
    if {[ipx::get_bus_interfaces $intf -of_objects $core] ne ""} {
        ipx::remove_bus_interface $intf $core
    }
}

# TX AXIS slave interface (from DMA to MSK)
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

# when DMA was clocked by 254 MHz clock
#adi_add_bus_clock "s_axis_aclk" "m_axis" "s_axis_aresetn"

# To clock DMA at 100 MHz so that our dual clock rx FIFO works
adi_add_bus_clock "m_axis_aclk" "m_axis"

ipx::save_core [ipx::current_core]
