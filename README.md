# An Opulent Voice MSK Modem for the ADALM-Pluto SDR Platform

Keywords: #MSK #SDR #Pluto #Opulent-Voice

This is a Minimum Shift Keying (MSK) modem for [Opulent Voice](https://www.openresearch.institute/2022/07/30/opulent-voice-digital-voice-and-data-protocol-update/) (OPV) targeted to Analog Devices [ADALM-Pluto](https://wiki.analog.com/university/tools/pluto/users/intro) SDR Platform. This repository provides a top-level design to be included in Pluto's [AMD Zync Z-7010 SoC](https://www.amd.com/en/products/adaptive-socs-and-fpgas/soc/zynq-7000.html). The modem and supporting functions are included from ORI's RTL library, and can be used in any FPGA development as well as non-OPV protocols. This repository can serve as a starting point/guide for targeting the MSK modem to other FPGA based SDR platforms.

The following ORI library components are used as submodules to this repository:

1. [msk_modulator](https://github.com/OpenResearchInstitute/msk_modulator)
2. [msk_demodulator](https://github.com/OpenResearchInstitute/msk_demodulator)
3. [nco](https://github.com/OpenResearchInstitute/nco)
4. [pi_controller](https://github.com/OpenResearchInstitute/pi_controller)
5. [prbs](https://github.com/OpenResearchInstitute/prbs)

## Building

1. git clone --recursive https://github.com/OpenResearchInstitute/pluto_msk
2. cd pluto_msk/project/pluto
3. source /opt/Xilinx/Vivado/2022.2/settings64.sh
4. make 

## MSK Modem Architecture


## Development Quickstart


## Roadmap


## Contributors

## ADI add custom IP

https://wiki.analog.com/resources/fpga/docs/hdl/creating_new_ip_guide
