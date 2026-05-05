################################################################################
# msk_modem_134byte_test.tcl
# Vivado simulation script for MSK modem with 134-byte OV frames
# Includes complete modem initialization sequence
#
# INTERLEAVER MODE: BIT-LEVEL (67x32)
# DECORRELATION: CCSDS LFSR (x^8+x^7+x^5+x^3+1)
#
# NOTE ON frame_sync_detector_soft.vhd v5 ARCHITECTURE CHANGE:
#   byte_sr has been REMOVED from the design. Byte assembly now uses a
#   VHDL VARIABLE (byte_v) inside fsm_proc. Variables are invisible to
#   the waveform viewer. The proxy signal debug_byte_v is provided:
#     - Captures the last complete assembled byte at the moment it is
#       written to circ_buffer (bit_count = 7)
#     - Updates once every 8 valid RX bits while in LOCKED state
#     - First byte of frame 0 (HUNTING->LOCKED path): should be 0x00
#       (or whatever the first payload byte is after FEC+interleave)
#     - If debug_byte_v looks scrambled, byte alignment is still off
################################################################################

# Close any existing simulation
catch {close_sim -force}

# Change to script directory for consistent relative path resolution
cd [file dirname [info script]]

set project_name "msk_axistream_debug_msb"
set project_dir "./axistream_debug_project_msb"
set part_name "xc7z010clg400-1"

# Create clean project
if {[file exists $project_dir]} {
    file delete -force $project_dir
}

create_project $project_name $project_dir -part $part_name -force
set_property target_language VHDL [current_project]
set_property simulator_language VHDL [current_project]

# VHDL-2008 configuration
set_property -name {xsim.compile.vhdl.more_options} -value {-2008} -objects [get_filesets sim_1]
set_property -name {xsim.elaborate.vhdl.more_options} -value {-2008} -objects [get_filesets sim_1]
set_property -name {xsim.simulate.runtime} -value {700ms} -objects [get_filesets sim_1]
set_property -name {xsim.simulate.log_all_signals} -value {true} -objects [get_filesets sim_1]

# File adding helper with detailed error reporting
proc safe_add_files {fileset file_list {library "work"}} {
    foreach file $file_list {
        if {[file exists $file]} {
            puts "OK Adding: $file"
            add_files -fileset $fileset -norecurse $file
            set_property file_type {VHDL 2008} [get_files $file]
            if {$library != "work"} {
                set_property library $library [get_files $file]
            }
        } else {
            puts "MISSING: $file"
            puts "  Current directory: [pwd]"
            puts "  Full path would be: [file normalize $file]"
            return 0
        }
    }
    return 1
}

################################################################################
# Add VHDL source files
################################################################################

puts "========================================"
puts "Adding VHDL source files..."
puts "Current directory: [pwd]"
puts "========================================"

# PeakRDL support packages (MUST BE FIRST!)
puts "\n--- PeakRDL Packages ---"
safe_add_files sources_1 {
    ../rdl/src/axi4lite_intf_pkg.vhd
    ../rdl/src/reg_utils.vhd
}

# CSR support components (MUST BE BEFORE msk_top_csr!)
puts "\n--- CSR Support Components ---"
safe_add_files sources_1 {
    ../src/cdc_resync.vhd
    ../src/pulse_detect.vhd
    ../src/data_capture.vhd
    ../src/axi_lite_cdc.vhd
}

# Register file infrastructure
puts "\n--- Register File & Packages ---"
safe_add_files sources_1 {
    ../rdl/outputs/rtl/msk_top_regs_pkg.vhd
    ../rdl/outputs/rtl/msk_top_regs.vhd
}

# Low-level components
puts "\n--- Low-Level Components ---"
safe_add_files sources_1 {
    ../nco/src/sin_cos_lut.vhd
    ../prbs/src/prbs_gen.vhd
    ../prbs/src/prbs_mon.vhd
    ../lowpass_ema/src/lowpass_ema.vhd
    ../nco/src/nco.vhd
    ../pi_controller/src/pi_controller.vhd
    ../power_detector/src/power_detector.vhd
}

# Modulator/Demodulator
puts "\n--- Modulator/Demodulator ---"
safe_add_files sources_1 {
    ../msk_modulator/src/msk_modulator.vhd
    ../msk_demodulator/src/costas_loop.vhd
    ../msk_demodulator/src/msk_demodulator.vhd
    ../msk_demodulator/src/costas_lock_detect.vhd
}

# TX path components
puts "\n--- TX Path Components ---"
safe_add_files sources_1 {
    ../src/axis_dma_adapter.vhd
    ../src/byte_to_bit_deserializer.vhd
    ../src/axis_async_fifo.vhd
}

# RX path components
puts "\n--- RX Path Components ---"
safe_add_files sources_1 {
    ../src/frame_sync_detector_soft.vhd
}

# FEC encoder/decoder - MUST BE BEFORE OV frame encoder/decoder!
puts "\n--- FEC Encoder/Decoder (K=7 Viterbi) ---"
safe_add_files sources_1 {
    ../src/conv_encoder_k7.vhd
    ../src/viterbi_decoder_k7_soft.vhd
}

# OV Frame encoder/decoder
puts "\n--- OV Frame Encoder/Decoder (134->268->134 bytes) ---"
puts "    Using BIT-LEVEL interleaver (67x32)"
puts "    With CCSDS LFSR decorrelation (spur fix)"
safe_add_files sources_1 {
    ../src/ov_frame_encoder.vhd
    ../src/ov_frame_decoder_soft.vhd
}

# CSR wrapper
puts "\n--- CSR Wrapper ---"
safe_add_files sources_1 {
    ../src/msk_top_csr.vhd
}

# Top level
puts "\n--- Top Level ---"
safe_add_files sources_1 {
    ../src/msk_top.vhd
}

# Testbench
puts "\n--- Testbench ---"
safe_add_files sim_1 {
    ./tb_msk_modem_134byte.vhd
}

puts "\n========================================"
puts "File addition complete"
puts "========================================"

################################################################################
# Simulation settings
################################################################################

puts "\nConfiguring simulation..."
update_compile_order -fileset sources_1
update_compile_order -fileset sim_1

set_property top tb_msk_modem_134byte [get_filesets sim_1]
set_property top_lib work [get_filesets sim_1]

################################################################################
# Launch simulation
################################################################################

puts "\n========================================"
puts "Launching behavioral simulation..."
puts "========================================"

if {[catch {launch_simulation -simset sim_1 -mode behavioral} result]} {
    puts "Simulation launch failed: $result"
    return
}

puts "Simulation launched successfully"

################################################################################
# Add key signals to waveform
################################################################################

puts "\nSetting up waveform..."

# Create waveform groups
add_wave_group {Test_Control}
add_wave_group {Initialization}
add_wave_group {TX_Path}
add_wave_group {AXI-Stream_TX}
add_wave_group {RF_Loopback}
add_wave_group {RX_Path}
add_wave_group {AXI-Stream_RX}
add_wave_group {Status}

# Test Control signals
add_wave -into {Test_Control} /tb_msk_modem_134byte/test_phase
add_wave -into {Test_Control} /tb_msk_modem_134byte/start_sending
add_wave -into {Test_Control} /tb_msk_modem_134byte/tx_frame_count
add_wave -into {Test_Control} /tb_msk_modem_134byte/rx_frame_count
add_wave -into {Test_Control} /tb_msk_modem_134byte/test_complete
add_wave -into {Test_Control} /tb_msk_modem_134byte/sim_done

# Initialization signals
add_wave -into {Initialization} /tb_msk_modem_134byte/s_axi_aresetn
add_wave -into {Initialization} /tb_msk_modem_134byte/s_axi_awaddr
add_wave -into {Initialization} /tb_msk_modem_134byte/s_axi_awvalid
add_wave -into {Initialization} /tb_msk_modem_134byte/s_axi_awready
add_wave -into {Initialization} /tb_msk_modem_134byte/s_axi_wdata
add_wave -into {Initialization} /tb_msk_modem_134byte/s_axi_wvalid
add_wave -into {Initialization} /tb_msk_modem_134byte/s_axi_wready
add_wave -into {Initialization} /tb_msk_modem_134byte/s_axi_bvalid

# TX Path
add_wave -into {TX_Path} /tb_msk_modem_134byte/tx_enable
add_wave -into {TX_Path} /tb_msk_modem_134byte/tx_valid

# AXI-Stream TX
add_wave -into {AXI-Stream_TX} /tb_msk_modem_134byte/s_axis_aresetn
add_wave -into {AXI-Stream_TX} /tb_msk_modem_134byte/s_axis_tvalid
add_wave -into {AXI-Stream_TX} /tb_msk_modem_134byte/s_axis_tready
add_wave -into {AXI-Stream_TX} -radix hex /tb_msk_modem_134byte/s_axis_tdata
add_wave -into {AXI-Stream_TX} /tb_msk_modem_134byte/s_axis_tlast
add_wave -into {AXI-Stream_TX} /tb_msk_modem_134byte/s_axis_tkeep

# RF Loopback
add_wave -into {RF_Loopback} -radix hex /tb_msk_modem_134byte/tx_samples_I
add_wave -into {RF_Loopback} -radix hex /tb_msk_modem_134byte/tx_samples_Q
add_wave -into {RF_Loopback} -radix hex /tb_msk_modem_134byte/rx_samples_I
add_wave -into {RF_Loopback} -radix hex /tb_msk_modem_134byte/rx_samples_Q

# RX Path
add_wave -into {RX_Path} /tb_msk_modem_134byte/rx_enable
add_wave -into {RX_Path} /tb_msk_modem_134byte/rx_svalid

# AXI-Stream RX
add_wave -into {AXI-Stream_RX} /tb_msk_modem_134byte/m_axis_tvalid
add_wave -into {AXI-Stream_RX} /tb_msk_modem_134byte/m_axis_tready
add_wave -into {AXI-Stream_RX} -radix hex /tb_msk_modem_134byte/m_axis_tdata
add_wave -into {AXI-Stream_RX} /tb_msk_modem_134byte/m_axis_tlast

# Status
add_wave -into {Status} /tb_msk_modem_134byte/frame_sync_locked
add_wave -into {Status} -radix unsigned /tb_msk_modem_134byte/frames_received
add_wave -into {Status} -radix unsigned /tb_msk_modem_134byte/frame_sync_errors
add_wave -into {Status} /tb_msk_modem_134byte/frame_buffer_overflow

################################################################################
# TLAST DEBUG SIGNALS - Complete pipeline trace
################################################################################

# DMA Adapter output (Stage 1)
add_wave_group {Stage_1:_DMA_Adapter_Output}
add_wave -into {Stage_1:_DMA_Adapter_Output} /tb_msk_modem_134byte/DUT/adapter_tvalid
add_wave -into {Stage_1:_DMA_Adapter_Output} /tb_msk_modem_134byte/DUT/adapter_tready
add_wave -into {Stage_1:_DMA_Adapter_Output} -radix hex /tb_msk_modem_134byte/DUT/adapter_tdata
add_wave -into {Stage_1:_DMA_Adapter_Output} /tb_msk_modem_134byte/DUT/adapter_tlast

# Async FIFO Write Side (Stage 2a)
add_wave_group {Stage_2a:_FIFO_Write_Side}
add_wave -into {Stage_2a:_FIFO_Write_Side} /tb_msk_modem_134byte/DUT/u_async_fifo/s_axis_tvalid
add_wave -into {Stage_2a:_FIFO_Write_Side} /tb_msk_modem_134byte/DUT/u_async_fifo/tready_int
add_wave -into {Stage_2a:_FIFO_Write_Side} -radix hex /tb_msk_modem_134byte/DUT/u_async_fifo/s_axis_tdata
add_wave -into {Stage_2a:_FIFO_Write_Side} /tb_msk_modem_134byte/DUT/u_async_fifo/s_axis_tlast
add_wave -into {Stage_2a:_FIFO_Write_Side} -radix unsigned /tb_msk_modem_134byte/DUT/u_async_fifo/wr_ptr_bin
add_wave -into {Stage_2a:_FIFO_Write_Side} /tb_msk_modem_134byte/DUT/u_async_fifo/full_int

# Async FIFO CDC (Stage 2b)
add_wave_group {Stage_2b:_FIFO_CDC}
add_wave -into {Stage_2b:_FIFO_CDC} -radix hex /tb_msk_modem_134byte/DUT/u_async_fifo/wr_ptr_gray
add_wave -into {Stage_2b:_FIFO_CDC} -radix hex /tb_msk_modem_134byte/DUT/u_async_fifo/wr_ptr_gray_sync1
add_wave -into {Stage_2b:_FIFO_CDC} -radix hex /tb_msk_modem_134byte/DUT/u_async_fifo/wr_ptr_gray_sync2
add_wave -into {Stage_2b:_FIFO_CDC} -radix hex /tb_msk_modem_134byte/DUT/u_async_fifo/rd_ptr_gray

# Async FIFO Read Side (Stage 2c)
add_wave_group {Stage_2c:_FIFO_Read_Side}
add_wave -into {Stage_2c:_FIFO_Read_Side} /tb_msk_modem_134byte/DUT/u_async_fifo/tvalid_int
add_wave -into {Stage_2c:_FIFO_Read_Side} /tb_msk_modem_134byte/DUT/u_async_fifo/m_axis_tready
add_wave -into {Stage_2c:_FIFO_Read_Side} -radix hex /tb_msk_modem_134byte/DUT/u_async_fifo/m_axis_tdata
add_wave -into {Stage_2c:_FIFO_Read_Side} /tb_msk_modem_134byte/DUT/u_async_fifo/m_axis_tlast
add_wave -into {Stage_2c:_FIFO_Read_Side} -radix unsigned /tb_msk_modem_134byte/DUT/u_async_fifo/rd_ptr_bin

# FIFO to Encoder (Stage 3)
add_wave_group {Stage_3:_FIFO_to_Encoder}
add_wave -into {Stage_3:_FIFO_to_Encoder} /tb_msk_modem_134byte/DUT/fifo_tvalid
add_wave -into {Stage_3:_FIFO_to_Encoder} /tb_msk_modem_134byte/DUT/fifo_tready
add_wave -into {Stage_3:_FIFO_to_Encoder} -radix hex /tb_msk_modem_134byte/DUT/fifo_tdata
add_wave -into {Stage_3:_FIFO_to_Encoder} /tb_msk_modem_134byte/DUT/fifo_tlast

################################################################################
# ENCODER STATE MACHINE
# States: IDLE(0) -> COLLECT(1) -> RANDOMIZE(2) -> PREP_FEC(3) ->
#         FEC_ENCODE(4) -> INTERLEAVE(5) -> OUTPUT(6)
################################################################################

add_wave_group {Stage_4:_Encoder_State_Machine}
add_wave -into {Stage_4:_Encoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_encoder/state
add_wave -into {Stage_4:_Encoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_encoder/collect_idx
add_wave -into {Stage_4:_Encoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_encoder/byte_idx
add_wave -into {Stage_4:_Encoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_encoder/bit_idx
add_wave -into {Stage_4:_Encoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_encoder/out_idx
add_wave -into {Stage_4:_Encoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_encoder/s_axis_tvalid
add_wave -into {Stage_4:_Encoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_encoder/s_axis_tready
add_wave -into {Stage_4:_Encoder_State_Machine} -radix hex /tb_msk_modem_134byte/DUT/u_ov_encoder/s_axis_tdata
add_wave -into {Stage_4:_Encoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_encoder/s_axis_tlast
add_wave -into {Stage_4:_Encoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_encoder/encoder_active

# Encoder LFSR
add_wave_group {Stage_4a:_Encoder_LFSR}
add_wave -into {Stage_4a:_Encoder_LFSR} -radix hex /tb_msk_modem_134byte/DUT/u_ov_encoder/lfsr_randomize

# Encoder FEC
add_wave_group {Stage_4b:_Encoder_FEC}
add_wave -into {Stage_4b:_Encoder_FEC} /tb_msk_modem_134byte/DUT/u_ov_encoder/encoder_start
add_wave -into {Stage_4b:_Encoder_FEC} /tb_msk_modem_134byte/DUT/u_ov_encoder/encoder_busy
add_wave -into {Stage_4b:_Encoder_FEC} /tb_msk_modem_134byte/DUT/u_ov_encoder/encoder_done

# Encoder to Deserializer (Stage 5)
add_wave_group {Stage_5:_Encoder_to_Deserializer}
add_wave -into {Stage_5:_Encoder_to_Deserializer} /tb_msk_modem_134byte/DUT/encoder_tvalid
add_wave -into {Stage_5:_Encoder_to_Deserializer} /tb_msk_modem_134byte/DUT/encoder_tready
add_wave -into {Stage_5:_Encoder_to_Deserializer} -radix hex /tb_msk_modem_134byte/DUT/encoder_tdata
add_wave -into {Stage_5:_Encoder_to_Deserializer} /tb_msk_modem_134byte/DUT/encoder_tlast
add_wave -into {Stage_5:_Encoder_to_Deserializer} /tb_msk_modem_134byte/DUT/tx_encoder_active
add_wave -into {Stage_5:_Encoder_to_Deserializer} -radix unsigned /tb_msk_modem_134byte/DUT/tx_frames_encoded

# Deserializer (Stage 6)
add_wave_group {Stage_6:_Deserializer}
add_wave -into {Stage_6:_Deserializer} /tb_msk_modem_134byte/DUT/u_deserializer/state
add_wave -into {Stage_6:_Deserializer} /tb_msk_modem_134byte/DUT/u_deserializer/bit_counter
add_wave -into {Stage_6:_Deserializer} /tb_msk_modem_134byte/DUT/u_deserializer/ready_int
add_wave -into {Stage_6:_Deserializer} -radix hex /tb_msk_modem_134byte/DUT/u_deserializer/shift_reg
add_wave -into {Stage_6:_Deserializer} /tb_msk_modem_134byte/DUT/u_deserializer/tx_data_int
add_wave -into {Stage_6:_Deserializer} /tb_msk_modem_134byte/DUT/tx_data_bit
add_wave -into {Stage_6:_Deserializer} /tb_msk_modem_134byte/DUT/tx_req
add_wave -into {Stage_6:_Deserializer} /tb_msk_modem_134byte/DUT/frame_complete
add_wave -into {Stage_6:_Deserializer} /tb_msk_modem_134byte/DUT/u_deserializer/last_byte
add_wave -into {Stage_6:_Deserializer} /tb_msk_modem_134byte/DUT/tx_bit_counter

# Modulator (Stage 7)
add_wave_group {Stage_7:_Modulator}
add_wave -into {Stage_7:_Modulator} /tb_msk_modem_134byte/DUT/tx_data_bit_d1
add_wave -into {Stage_7:_Modulator} /tb_msk_modem_134byte/DUT/tx_data_bit_d2
add_wave -into {Stage_7:_Modulator} /tb_msk_modem_134byte/DUT/tx_enable
add_wave -into {Stage_7:_Modulator} /tb_msk_modem_134byte/DUT/tx_valid
add_wave -into {Stage_7:_Modulator} -radix hex /tb_msk_modem_134byte/DUT/tx_samples_I_int
add_wave -into {Stage_7:_Modulator} -radix hex /tb_msk_modem_134byte/DUT/tx_samples_Q_int

# Demodulator (Stage 8)
add_wave_group {Stage_8:_Demodulator}
add_wave -into {Stage_8:_Demodulator} /tb_msk_modem_134byte/DUT/rx_enable
add_wave -into {Stage_8:_Demodulator} /tb_msk_modem_134byte/DUT/rx_svalid
add_wave -into {Stage_8:_Demodulator} /tb_msk_modem_134byte/DUT/rx_bit
add_wave -into {Stage_8:_Demodulator} /tb_msk_modem_134byte/DUT/rx_bit_valid
add_wave -into {Stage_8:_Demodulator} /tb_msk_modem_134byte/DUT/rx_bit_corr
add_wave -into {Stage_8:_Demodulator} /tb_msk_modem_134byte/DUT/demod_sync_lock

# F1 Costas Lock Detection (Stage 8a)
add_wave_group {Stage_8a:_Costas_Lock_F1}
add_wave -into {Stage_8a:_Costas_Lock_F1} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/cst_lock
add_wave -into {Stage_8a:_Costas_Lock_F1} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/cst_unlock
add_wave -into {Stage_8a:_Costas_Lock_F1} -radix unsigned /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/cst_lock_time
add_wave -into {Stage_8a:_Costas_Lock_F1} -radix hex /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/cst_lock_thresh
add_wave -into {Stage_8a:_Costas_Lock_F1} -radix unsigned /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/cst_lock_count
add_wave -into {Stage_8a:_Costas_Lock_F1} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/tclk
add_wave -into {Stage_8a:_Costas_Lock_F1} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/acc_valid
add_wave -into {Stage_8a:_Costas_Lock_F1} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/init
add_wave -into {Stage_8a:_Costas_Lock_F1} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/cst_i_acc
add_wave -into {Stage_8a:_Costas_Lock_F1} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/cst_q_acc

# F1 Lock Detection Internals (Stage 8b)
add_wave_group {Stage_8b:_Lock_Detect_F1_Internals}
add_wave -into {Stage_8b:_Lock_Detect_F1_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/i_sqr
add_wave -into {Stage_8b:_Lock_Detect_F1_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/q_sqr
add_wave -into {Stage_8b:_Lock_Detect_F1_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/acc_i
add_wave -into {Stage_8b:_Lock_Detect_F1_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/acc_q
add_wave -into {Stage_8b:_Lock_Detect_F1_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/acc_iq_delta
add_wave -into {Stage_8b:_Lock_Detect_F1_Internals} -radix unsigned /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/icntr
add_wave -into {Stage_8b:_Lock_Detect_F1_Internals} -radix unsigned /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/tcntr
add_wave -into {Stage_8b:_Lock_Detect_F1_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/lock
add_wave -into {Stage_8b:_Lock_Detect_F1_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/lock_d
add_wave -into {Stage_8b:_Lock_Detect_F1_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f1/u_lock_detect/lock_once

# F2 Costas Lock Detection (Stage 8c)
add_wave_group {Stage_8c:_Costas_Lock_F2}
add_wave -into {Stage_8c:_Costas_Lock_F2} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/cst_lock
add_wave -into {Stage_8c:_Costas_Lock_F2} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/cst_unlock
add_wave -into {Stage_8c:_Costas_Lock_F2} -radix unsigned /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/cst_lock_time
add_wave -into {Stage_8c:_Costas_Lock_F2} -radix hex /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/cst_lock_thresh
add_wave -into {Stage_8c:_Costas_Lock_F2} -radix unsigned /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/cst_lock_count
add_wave -into {Stage_8c:_Costas_Lock_F2} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/tclk
add_wave -into {Stage_8c:_Costas_Lock_F2} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/acc_valid
add_wave -into {Stage_8c:_Costas_Lock_F2} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/init
add_wave -into {Stage_8c:_Costas_Lock_F2} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/cst_i_acc
add_wave -into {Stage_8c:_Costas_Lock_F2} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/cst_q_acc

# F2 Lock Detection Internals (Stage 8d)
add_wave_group {Stage_8d:_Lock_Detect_F2_Internals}
add_wave -into {Stage_8d:_Lock_Detect_F2_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/i_sqr
add_wave -into {Stage_8d:_Lock_Detect_F2_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/q_sqr
add_wave -into {Stage_8d:_Lock_Detect_F2_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/acc_i
add_wave -into {Stage_8d:_Lock_Detect_F2_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/acc_q
add_wave -into {Stage_8d:_Lock_Detect_F2_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/acc_iq_delta
add_wave -into {Stage_8d:_Lock_Detect_F2_Internals} -radix unsigned /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/icntr
add_wave -into {Stage_8d:_Lock_Detect_F2_Internals} -radix unsigned /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/tcntr
add_wave -into {Stage_8d:_Lock_Detect_F2_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/lock
add_wave -into {Stage_8d:_Lock_Detect_F2_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/lock_d
add_wave -into {Stage_8d:_Lock_Detect_F2_Internals} /tb_msk_modem_134byte/DUT/u_dem/U_f2/u_lock_detect/lock_once

# Top-level Lock Status (Stage 8e)
add_wave_group {Stage_8e:_Lock_Status_Summary}
add_wave -into {Stage_8e:_Lock_Status_Summary} /tb_msk_modem_134byte/DUT/cst_lock_f1
add_wave -into {Stage_8e:_Lock_Status_Summary} /tb_msk_modem_134byte/DUT/cst_unlock_f1
add_wave -into {Stage_8e:_Lock_Status_Summary} -radix unsigned /tb_msk_modem_134byte/DUT/cst_lock_time_f1
add_wave -into {Stage_8e:_Lock_Status_Summary} /tb_msk_modem_134byte/DUT/cst_lock_f2
add_wave -into {Stage_8e:_Lock_Status_Summary} /tb_msk_modem_134byte/DUT/cst_unlock_f2
add_wave -into {Stage_8e:_Lock_Status_Summary} -radix unsigned /tb_msk_modem_134byte/DUT/cst_lock_time_f2
add_wave -into {Stage_8e:_Lock_Status_Summary} -radix unsigned /tb_msk_modem_134byte/DUT/symbol_lock_count
add_wave -into {Stage_8e:_Lock_Status_Summary} -radix hex /tb_msk_modem_134byte/DUT/symbol_lock_threshold

# Frame Sync Detector (Stage 9)
add_wave_group {Stage_9:_Frame_Sync_Detector}
add_wave -into {Stage_9:_Frame_Sync_Detector} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/state
add_wave -into {Stage_9:_Frame_Sync_Detector} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/lock_status
add_wave -into {Stage_9:_Frame_Sync_Detector} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/frame_byte_count
add_wave -into {Stage_9:_Frame_Sync_Detector} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/frame_ready
add_wave -into {Stage_9:_Frame_Sync_Detector} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/frame_ack
add_wave -into {Stage_9:_Frame_Sync_Detector} -radix unsigned /tb_msk_modem_134byte/DUT/u_rx_frame_sync/consecutive_good

# Correlator Debug (Stage 9b)
add_wave_group {Stage_9b:_Correlator_Debug}
add_wave -into {Stage_9b:_Correlator_Debug} /tb_msk_modem_134byte/DUT/rx_sync_correlation
add_wave -into {Stage_9b:_Correlator_Debug} /tb_msk_modem_134byte/DUT/rx_sync_corr_peak
add_wave -into {Stage_9b:_Correlator_Debug} /tb_msk_modem_134byte/DUT/rx_sync_soft_current
add_wave -into {Stage_9b:_Correlator_Debug} /tb_msk_modem_134byte/DUT/rx_sync_bit_count
add_wave -into {Stage_9b:_Correlator_Debug} /tb_msk_modem_134byte/DUT/rx_data_soft

################################################################################
# Stage_9c: Frame Sync Detector Internals (v5 registered-input architecture)
#
# ARCHITECTURE CHANGE FROM PREVIOUS VERSION:
#   byte_sr REMOVED - was a signal in shift_proc, caused cross-process latency
#   byte_v  ADDED   - local VARIABLE in fsm_proc, not waveform-visible directly
#
# PROXY SIGNAL for byte assembly observation:
#   debug_byte_v = last complete byte written to circ_buffer
#              Updated once per byte (every 8 valid bits in LOCKED state)
#              If this is wrong, byte alignment is broken
#              Expected: matches encoded/interleaved payload bytes
#
# KEY BYTE ALIGNMENT INVARIANTS TO CHECK:
#   HUNTING->LOCKED entry clock:
#     rx_bit_r = P(0)         <- first payload bit, captured into byte_v directly
#     bit_count will be 1     <- one bit pre-loaded
#     frame_soft_idx will be 1 <- soft[0] captured for P(0)
#
#   VSYNC->LOCKED entry clock:
#     rx_bit_r = SYNC[0]      <- last sync bit (NOT payload)
#     bit_count will be 0     <- byte_v empty, P(0) arrives next clock
#     frame_soft_idx will be 0 <- P(0) soft captured on first LOCKED clock
################################################################################

add_wave_group {Stage_9c:_Frame_Sync_Internals}
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/rx_bit_valid_r
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/rx_bit_r
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/soft_r
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/corr
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/corr_prev
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/corr_peak

# --- byte_sr REMOVED from design in v5 ---
# byte assembly is now done via a local VARIABLE (byte_v) inside fsm_proc.
# Variables are not visible to the simulator waveform viewer.
# Use debug_byte_v as the proxy: it captures byte_v at each circ_buffer write.

add_wave -into {Stage_9c:_Frame_Sync_Internals} -radix hex /tb_msk_modem_134byte/DUT/u_rx_frame_sync/debug_byte_v
# ^ Expect: correct encoded payload bytes, MSB-first assembly, no sync contamination

add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/bit_count
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/sync_bit_count
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/wr_ptr
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/frame_start_ptr
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/frame_byte_count
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/frame_soft_idx
add_wave -into {Stage_9c:_Frame_Sync_Internals} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/missed_sync_count

# Soft shift register (Stage 9d)
add_wave_group {Stage_9d:_Soft_Shift_Register}
add_wave -into {Stage_9d:_Soft_Shift_Register} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/soft_sr
add_wave -into {Stage_9d:_Soft_Shift_Register} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/soft_output_active
add_wave -into {Stage_9d:_Soft_Shift_Register} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/soft_output_count
add_wave -into {Stage_9d:_Soft_Shift_Register} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/soft_tvalid_int
add_wave -into {Stage_9d:_Soft_Shift_Register} /tb_msk_modem_134byte/DUT/u_rx_frame_sync/soft_tlast_int

# Soft bit stream (Stage 9e)
add_wave_group {Stage_9e:_Soft_Bit_Stream}
add_wave -into {Stage_9e:_Soft_Bit_Stream} -radix unsigned /tb_msk_modem_134byte/DUT/sync_det_soft_tdata
add_wave -into {Stage_9e:_Soft_Bit_Stream} /tb_msk_modem_134byte/DUT/sync_det_soft_tvalid
add_wave -into {Stage_9e:_Soft_Bit_Stream} /tb_msk_modem_134byte/DUT/sync_det_soft_tready
add_wave -into {Stage_9e:_Soft_Bit_Stream} /tb_msk_modem_134byte/DUT/sync_det_soft_tlast

################################################################################
# DECODER
################################################################################

# Soft Decoder State Machine (Stage 10)
add_wave_group {Stage_10:_Soft_Decoder_State_Machine}
add_wave -into {Stage_10:_Soft_Decoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_decoder/state
add_wave -into {Stage_10:_Soft_Decoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_decoder/collect_idx
add_wave -into {Stage_10:_Soft_Decoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_decoder/soft_idx
add_wave -into {Stage_10:_Soft_Decoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_decoder/byte_idx
add_wave -into {Stage_10:_Soft_Decoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_decoder/bit_idx
add_wave -into {Stage_10:_Soft_Decoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_decoder/out_idx
add_wave -into {Stage_10:_Soft_Decoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_decoder/s_axis_tvalid
add_wave -into {Stage_10:_Soft_Decoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_decoder/s_axis_tready
add_wave -into {Stage_10:_Soft_Decoder_State_Machine} -radix hex /tb_msk_modem_134byte/DUT/u_ov_decoder/s_axis_tdata
add_wave -into {Stage_10:_Soft_Decoder_State_Machine} /tb_msk_modem_134byte/DUT/u_ov_decoder/s_axis_tlast
add_wave -into {Stage_10:_Soft_Decoder_State_Machine} /tb_msk_modem_134byte/DUT/rx_decoder_active

# Decoder LFSR (Stage 10a)
add_wave_group {Stage_10a:_Decoder_LFSR}
add_wave -into {Stage_10a:_Decoder_LFSR} -radix hex /tb_msk_modem_134byte/DUT/u_ov_decoder/lfsr_derandomize

# Soft input collection (Stage 10b)
add_wave_group {Stage_10b:_Soft_Input_Collection}
add_wave -into {Stage_10b:_Soft_Input_Collection} /tb_msk_modem_134byte/DUT/u_ov_decoder/s_axis_soft_bit_tvalid
add_wave -into {Stage_10b:_Soft_Input_Collection} /tb_msk_modem_134byte/DUT/u_ov_decoder/s_axis_soft_bit_tready
add_wave -into {Stage_10b:_Soft_Input_Collection} -radix unsigned /tb_msk_modem_134byte/DUT/u_ov_decoder/s_axis_soft_bit_tdata
add_wave -into {Stage_10b:_Soft_Input_Collection} /tb_msk_modem_134byte/DUT/u_ov_decoder/s_axis_soft_bit_tlast

# Soft Viterbi internals (Stage 10c)
add_wave_group {Stage_10c:_Soft_Viterbi}
add_wave -into {Stage_10c:_Soft_Viterbi} /tb_msk_modem_134byte/DUT/u_ov_decoder/U_DECODER/start
add_wave -into {Stage_10c:_Soft_Viterbi} /tb_msk_modem_134byte/DUT/u_ov_decoder/U_DECODER/busy
add_wave -into {Stage_10c:_Soft_Viterbi} /tb_msk_modem_134byte/DUT/u_ov_decoder/U_DECODER/done
add_wave -into {Stage_10c:_Soft_Viterbi} /tb_msk_modem_134byte/DUT/u_ov_decoder/U_DECODER/state
add_wave -into {Stage_10c:_Soft_Viterbi} /tb_msk_modem_134byte/DUT/u_ov_decoder/U_DECODER/time_step
add_wave -into {Stage_10c:_Soft_Viterbi} /tb_msk_modem_134byte/DUT/u_ov_decoder/U_DECODER/best_metric

# Soft G1/G2 (Stage 10d)
add_wave_group {Stage_10d:_Soft_G1_G2}
add_wave -into {Stage_10d:_Soft_G1_G2} -radix hex /tb_msk_modem_134byte/DUT/u_ov_decoder/decoder_input_soft_g1
add_wave -into {Stage_10d:_Soft_G1_G2} -radix hex /tb_msk_modem_134byte/DUT/u_ov_decoder/decoder_input_soft_g2

# Decoder to RX FIFO (Stage 11)
add_wave_group {Stage_11:_Decoder_to_RX_FIFO}
add_wave -into {Stage_11:_Decoder_to_RX_FIFO} /tb_msk_modem_134byte/DUT/decoder_tvalid
add_wave -into {Stage_11:_Decoder_to_RX_FIFO} /tb_msk_modem_134byte/DUT/decoder_tready
add_wave -into {Stage_11:_Decoder_to_RX_FIFO} -radix hex /tb_msk_modem_134byte/DUT/decoder_tdata
add_wave -into {Stage_11:_Decoder_to_RX_FIFO} /tb_msk_modem_134byte/DUT/decoder_tlast

# RX FIFO Status (Stage 12)
add_wave_group {Stage_12:_RX_FIFO_Status}
add_wave -into {Stage_12:_RX_FIFO_Status} /tb_msk_modem_134byte/DUT/rx_async_fifo_prog_full
add_wave -into {Stage_12:_RX_FIFO_Status} /tb_msk_modem_134byte/DUT/rx_async_fifo_prog_empty
add_wave -into {Stage_12:_RX_FIFO_Status} /tb_msk_modem_134byte/DUT/rx_async_fifo_wr_ptr
add_wave -into {Stage_12:_RX_FIFO_Status} /tb_msk_modem_134byte/DUT/rx_async_fifo_rd_ptr

################################################################################
# Run simulation
################################################################################

puts ""
puts "========================================"
puts "RUNNING MSK MODEM TEST"
puts "134-byte OV frames, 10 frames total"
puts "========================================"
puts ""
puts "frame_sync_detector_soft v5 changes:"
puts "  REMOVED: byte_sr (was in shift_proc, caused SYNC bit contamination)"
puts "  ADDED:   byte_v variable in fsm_proc (no cross-process dependency)"
puts "  ADDED:   debug_byte_v signal (proxy for byte_v in waveform viewer)"
puts "  FIXED:   soft_frame_buf[0] now captures P(0) on HUNTING->LOCKED path"
puts ""
puts "Key debug signals in Stage_9c:"
puts "  debug_byte_v: last complete assembled byte (hex)"
puts "                updates every 8 valid bits while LOCKED"
puts "                check MSB-first order and no sync contamination"
puts "  bit_count: should be 1 after HUNTING->LOCKED, 0 after VSYNC->LOCKED"
puts "  frame_soft_idx: should be 1 after HUNTING->LOCKED, 0 after VSYNC->LOCKED"
puts ""
puts "TX data pattern:"
puts "  Frame 0: 0x00 -> 0x85  (after FEC+interleave will look scrambled)"
puts "  Frame 1: 0x80 -> 0x05  (alternates every frame)"
puts "  Frames 2..9: repeats"
puts "========================================"

# Run for full test duration (10 frames x ~40ms + overhead)
run 700 ms

wave zoom full

puts ""
puts "Simulation complete!"
puts ""
puts "SUCCESS criteria:"
puts "  test_phase = TEST_COMPLETE"
puts "  tx_frame_count = 10"
puts "  rx_frame_count = 10"
puts "  frame_sync_locked = 1"
puts "  'SUCCESS! All 10 frames transmitted and verified!'"
