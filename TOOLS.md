# PLUTO_MSK Design Tool Requirements and Suggestions

## Simulation

### Simulators

For simulating the design a VHDL simulator with VHDL-2008 support is required. The following simulators are supported, other simulators should work well.

* [NVC](https://www.nickg.me.uk/nvc/) - Supports cocotb testbench
* [GHDL](https://ghdl.github.io/ghdl/) - Supports cocotb testbench
* [XSIM](https://www.xilinx.com/support/documents/sw_manuals/xilinx2022_1/ug900-vivado-logic-simulation.pdf) - Vivado simulator - supports VHDL testbench

### Testbenches

Cocotb and VHDL are used for testbenches. Cocotb dependencies are:

* [cocotb](https://docs.cocotb.org/en/stable/) - version 2.x is required
* Python 3.6.2+
* GNU Make 3+

### Waveforms

* [gtkwave](https://gtkwave.github.io/gtkwave/index.html)
* [Vivado](https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado.html)

Other waveform viewers maybe used, but may not have all the features supported by gtkwave, analog waveforms in particular.

* [Surfer](https://surfer-project.org)

### Linter

* [vhdl-linter](https://github.com/vhdl-linter/vhdl-linter) - VHDL syntax checker and coding guidelines checking


## SystemRDL

[SystemRDL](https://www.accellera.org/downloads/standards/systemrdl) is used for configuration and status register description. The following tools are required:

* [PeakRDL](https://peakrdl.readthedocs.io/en/latest/) - Suite of SystemRDL tools to generate RTL, verification artificacts, and documentation from the SystemRDL code.

    * [PeakRDL-docx](https://pypi.org/project/peakrdl-docx) - docx documentation generator
    * [PeakRDL-markdown](https://peakrdl-markdown.readthedocs.io/) - markdown documentation generator
    * [PeakRDL-regblock-VHDL](https://peakrdl-regblock-vhdl.readthedocs.io/) - VHDL RTL generator

## Synthesis

* [Vivado](https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado.html) - synthesis and P&R for Xilinx/AMD Zynq series FPGAs

## Source Code Control

* [git](https://git-scm.com) - version control system
    * CLI available on Linux and macOS
    * Various GUI interfaces available on all platforms

## Documentation Tools

* [draw.io](https://www.drawio.com) - block diagram editor
* [Wavedrom](https://wavedrom.com) - timing diagram editor
* [Markdown](https://www.markdownguide.org) - Light weight documentation markup language
* [Asciidoctor](https://asciidoctor.org) - Documentation markup language
* [MathJax]

# Editors and IDEs

Any editing solution will work. If you don't have an established workflow the following options may be useful.

* [VSCode](https://code.visualstudio.com) or [VSCodium](https://vscodium.com) with the following extensions
    * [AsciiDoc] - if using AsciiDoctor
    * [SystemRDL] - for SystemRDL syntax highlighting - (For VSCodium must be installed from .vsix file)
    * [VaporView] - Waveform display
    * [Surfer] - Waveform display
    * [Claude Code] - for AI agent integration

