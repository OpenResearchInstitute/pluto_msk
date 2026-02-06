# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Minimum Shift Keying (MSK) modem for the Opulent Voice (OPV) protocol, targeting the ADALM-Pluto SDR (Analog Devices AD9361 + Xilinx Zynq Z-7010). It is structured as an out-of-tree module that integrates with the ADI HDL reference design. The modem and DSP blocks are written in VHDL; the testbench uses cocotb (Python) with the NVC or GHDL simulator.

## Build Commands

### Prerequisites
- Vivado 2022.2 (expected at `/opt/Xilinx/Vivado/2022.2/`; symlink if installed elsewhere)
- For simulation: cocotb, NVC (default) or GHDL, Python 3 with numpy/matplotlib
- For register generation: PeakRDL toolchain (`peakrdl` CLI with regblock-vhdl, markdown, python, c-header, html, docx plugins), pandoc

### FPGA Bitstream (Pluto target)
```bash
source /opt/Xilinx/Vivado/2022.2/settings64.sh
cd projects/pluto && make
```
This first builds the msk_top IP library (`library/`), then synthesizes the Vivado project. Log: `projects/pluto/pluto_vivado.log`.

### Libre target (alternate board)
```bash
cd projects/libre && make
```

### Firmware (full Pluto image with Linux)
```bash
cd firmware
make                    # full build (bitstream + u-boot + linux + rootfs)
make PLATFORM=libre     # libre variant
make PLATFORM=libre sdimg  # SD card image
```

### Simulation (cocotb)
```bash
cd sim
make                    # run with NVC (default), GUI enabled
make SIM=ghdl           # run with GHDL instead
```
The testbench is `sim/msk_test.py`. Waveform output: `sim/msk_top.ghw` (viewable in GTKWave; save files: `msk_top_nvc.gtkw`, `msk_top_ghdl.gtkw`).

### Register Map (PeakRDL)
```bash
cd rdl && make          # generates VHDL, Python, C header, docs from RDL
cd rdl && make clean    # remove generated outputs
```

## Architecture

### Top-Level Integration
- `projects/pluto/system_bd.tcl` — Vivado block design that wires msk_top into the ADI Pluto reference design (AD9361 + DMA + PS7). The custom IP repo is set via `ip_repo_paths` to include `library/`.
- `projects/pluto/system_top.v` — Verilog top-level wrapper (Zynq PS + PL).
- `projects/pluto/system_constr.xdc` — Pin constraints.
- `library/msk_top_ip.tcl` — Vivado IP packager script. Defines the msk_top IP core, registers VHDL sources, and configures AXI-Stream bus interfaces (s_axis slave for TX, m_axis master for RX). **When adding new VHDL source files, they must be added here** as well as in `sim/Makefile`.

### Modem Core (`src/`)
- `msk_top.vhd` — Top-level modem entity. Instantiates modulator, demodulator, NCOs, PRBS, frame encoder/decoder, FIFOs, and CSR bridge. AXI4-Lite register interface + AXI-Stream data interfaces.
- `msk_top_csr.vhd` — Configuration/Status Register bridge (connects PeakRDL-generated register block to modem internals).

**TX datapath:** AXI-Stream FIFO → OV Frame Encoder → Byte-to-Bit Deserializer → MSK Modulator → DAC samples
**RX datapath:** ADC samples → MSK Demodulator → Frame Sync Detector → OV Frame Decoder → AXI-Stream FIFO

Key src modules:
- `ov_frame_encoder.vhd` / `ov_frame_decoder_soft.vhd` — Opulent Voice framing (134→268 byte encoding with convolutional coding)
- `conv_encoder_k7.vhd` / `viterbi_decoder_k7_soft.vhd` — Rate 1/2, K=7 convolutional codec
- `frame_sync_detector_soft.vhd` — Sync word detection with soft decision support
- `axis_async_fifo.vhd` — Dual-clock FIFO for clock domain crossing between DMA and modem
- `byte_to_bit_deserializer.vhd` — Converts byte-wide AXI-Stream to serial bit stream for modulator

### Submodules (ORI RTL Library)
Each is a standalone repo with its own `src/` directory:
- `msk_modulator/` — MSK modulation (I/Q with offset bit timing, continuous phase)
- `msk_demodulator/` — MSK demodulation with Costas loop carrier recovery (`costas_loop.vhd`, `costas_lock_detect.vhd`)
- `nco/` — Numerically Controlled Oscillator with sin/cos LUT
- `pi_controller/` — Proportional-Integral controller (used in Costas loop)
- `lowpass_ema/` — Exponential Moving Average low-pass filter
- `power_detector/` — Signal power measurement
- `prbs/` — Pseudo-Random Bit Sequence generator and monitor (BER testing)

### Register Map (`rdl/`)
Register definitions in SystemRDL (`rdl/src/msk_top_regs.rdl`). PeakRDL generates:
- VHDL register block → `rdl/outputs/rtl/`
- Python register model → `rdl/outputs/python/` (used by cocotb testbench via symlink `sim/msk_top_regs`)
- C header → `rdl/outputs/c-header/`
- Documentation → `rdl/outputs/docs/`

The generated VHDL requires a post-processing step (VHDL-2019 → VHDL-2008 conversion) handled automatically by the RDL Makefile.

### Register Base Address
Modem registers are memory-mapped at `0x43C00000` (AXI4-Lite). See `README.md` for the full register map or `rdl/outputs/docs/` for generated documentation.

## Key Conventions

- VHDL standard: VHDL-2008 (simulation uses `--std=08` for GHDL). Some files in `rdl/src/` use VHDL-2008 features and are read with `-vhdl2008` in Vivado.
- Source file compilation order matters — dependencies must appear before dependent files in both `sim/Makefile` and `library/msk_top_ip.tcl`.
- The cocotb testbench imports the PeakRDL-generated Python register model; if registers change, regenerate with `cd rdl && make`.
- HDL submodule pin is intentionally on `hdl_2022_r2` branch — do not change without good reason.
- The `hdl/` submodule is the full Analog Devices HDL reference design; modifications should be avoided.
