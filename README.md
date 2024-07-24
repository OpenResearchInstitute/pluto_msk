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
In oder to build fpga bitstream, you need to install first Vivado. Recommended version is 2022.2. In this documentation vivado installtion path is assumed to be /opt/Xilinx/Vivado. If it is on an other directory, change the path (for example /tools/Xilinx/Vivado on keroppi) 
### First, clone this repo with all submodules
git clone --recursive https://github.com/OpenResearchInstitute/pluto_msk
### building bitstream only
1. cd pluto_msk/projects/pluto/
2. source /opt/Xilinx/Vivado/2022.2/settings64.sh
3. make
### complete firmware
1. Check if your vivado path is correct on this line https://github.com/OpenResearchInstitute/pluto_msk/blob/871bd130de0e6d462138bc6d2981b1c65897a0ca/firmware/Makefile#L19 
2. cd pluto_msk/firmware
3. make

## MSK Modem Architecture

### Control and Status Registers

The control and status registers (CSR) are organized as an array. 

|Directionality | Array Address | Name          | Summary |
| ------------- | ------------- |------------- | ------------- |
| output |csr_array(0) | HASH_ID | set to 0xaaaa5555 in the hardware |
| input |csr_array(1)(0) | init | initializes or is part of initialization for many blocks |
| input |csr_array(2)(0) | ptt | push to talk |
| input |csr_array(3)(0) | loopback_ena | loopback enable |
| input |csr_array(3)(31) | rx_invert | rx_bit_corr takes the value of rx_bit when rx_invert is 0 and rx_bit_corr takes the value of NOT rx_bit when rx_invert is 1 |
| input |csr_array(4) | freq_word_ft | value of the frequency for symbol time (mapped to freq_word_tclk) |
| input |csr_array(5) | freq_word_f1 | value of the frequency for the lower MSK tone |
| input |csr_array(6) | freq_word_f2 | value of the frequency for the higher MSK tone |
||csr_array(7)(15:0) |  lpf_i_gain | low pass filter gain value |
||csr_array(7)(31:16) | lpf_p_gain| low pass filter gain value |
||csr_array(8)(0) | lpf_freeze| low pass filter value |
||csr_array(8)(1) | lpf_zero| low pass filter value |
||csr_array(8)(31:16) | lpf_alpha| low pass filter value |
| input |csr_array(9)(7:0) | tx_data_w| sets bit width in transmitter parallel to serial circuit |
| input |csr_array(10)(7:0) | rx_data_w| sets bit width in receiver serial to parallel circuit |
| input |csr_array(11)(0) | prbs_sel| pseudo random bit sequence select |
||csr_array(11)(1) | prbs_err_insert| pseudo random bit sequence error insert (?) |
| input |csr_array(12) | prbs_poly| pseudo random bit sequence polynomial |
| input |csr_array(13) | prbs_initial| pseudo random bit sequence initial value |
||csr_array(14) | prbs_err_mask| pseudo random bit sequence error mask |
||csr_array(15)(0) | prbs_clear| pseudo random bit sequence clear |
||csr_array(15)(1) | prbs_sync| pseudo random bit sequence sync |


## Development Quickstart

Here is a set of instructions for getting this minimum shift keying (MSK) transceiver implementation to work on a PLUTO SDR. 

Clone this pluto_msk repository.

```
git clone --recursive https://github.com/OpenResearchInstitute/pluto_msk.git
```

The repository should clone to the latest stable PLUTO firmware release commit. Here is an example of how to change to another branch of the hdl reference design. hdl_2022_r2 was used for VHDL development. Don't change branches of hdl unless you have to.

```
/pluto_msk/hdl$ git checkout hdl_2022_r2 
Previous HEAD position was 1978df298 axi_dac_interpolate: Improve the ctrl logic
branch 'hdl_2022_r2' set up to track 'origin/hdl_2022_r2'.
Switched to a new branch 'hdl_2022_r2'
```

If you are working on ORI virtual machine, then source the version of Vivado needed as follows. 

```$ source /tools/Xilinx/Vivado/2022.2/settings.sh```

You can check which version of Vivado is currently being used as follows. 

```
$ which vivado
/tools/Xilinx/Vivado/2022.2/bin/vivado
```
Change directories to the PLUTO project directory and run make. 

```
/hdl/projects/pluto$ make
```
A useful log file for information, warnings, and errors is pluto_vivado.log

This repository is organized as an out of tree module.

Key lines in system_bd.tcl are:

https://github.com/OpenResearchInstitute/pluto_msk/blob/942aa516f8cc30af73a5a0c9ce3f8266012989e8/projects/pluto/system_bd.tcl#L7-19

```
set_property ip_repo_paths [list $ad_hdl_dir/library ../../library]  [current_fileset]
update_ip_catalog
```
The ip_repo_paths property lets us create a custom IP catalog for use with Vivado. It defines the path to one or more directories containing user-defined intellectual property (IP), like our blocks. The specified directories, and any sub-directories, are searched for files to add to the Vivado IP catalog. The property is assigned to the current fileset of the current project. 

ip_repo_paths will look for a <component>.xml file, where <component> is the name of the IP to add to the catalog. This XML file lists the files that define the module. Subdirectories are searched through. We don't have to list out each individual module's <component>.xml.

Where does our component.xml file come from? It's create by the msk_top_ip.tcl file. A version can be found here:
https://github.com/OpenResearchInstitute/pluto_msk/blob/main/library/msk_top_ip.tcl

Setting the ip_repo_paths property needs to be followed by update_ip_catalog. 

Example syntax:

```
set_property IP_REPO_PATHS {c:/Data/Designs C:/myIP} [current_fileset]
update_ip_catalog
```


## Roadmap


## Contributors

## ADI add custom IP

https://wiki.analog.com/resources/fpga/docs/hdl/creating_new_ip_guide
