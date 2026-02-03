# LibreSDR Support

LibreSDR is a PlutoSDR-compatible board with upgraded hardware:
- **FPGA**: XC7Z020-CLG400 (53,200 LUTs vs PlutoSDR's 17,600)
- **RF**: AD9363 (essentially the same as PlutoSDR AD9361)
- **Memory**: 1GB DDR3
- **Interface**: LVDS (vs PlutoSDR's CMOS)

## Building LibreSDR Firmware

### Prerequisites
- Vivado 2022.2 (for HDL build)
- ARM cross-compiler (arm-none-linux-gnueabihf-)

### Quick Start
```bash
# 1. Clone and init submodules
git clone --recursive https://github.com/OpenResearchInstitute/pluto_msk.git
git checkout <branch>
cd pluto_msk

or 

git clone https://github.com/OpenResearchInstitute/pluto_msk.git
git checkout <branch>
git submodule update --init --recursive
cd pluto_msk

# 2. Run LibreSDR setup
cd firmware/ori/libre
./setup_libre.sh

# 3. Build firmware (auto-builds HDL)
cd ../..
make PLATFORM=libre
```

### Using Pre-built XSA

If you have a pre-built XSA file (from CI or another build):
```bash
cd firmware
make TARGET=libre XSA_FILE=/path/to/system_top.xsa
```

### Output

Firmware files will be in `firmware/build/`:
- `libre.frm` - Main firmware image
- `boot.frm` - Boot image

### Flashing

Copy `libre.frm` to the LibreSDR mass storage device, or use DFU:
```bash
dfu-util -D build/libre.dfu -a firmware.dfu
```

# 4. Build SD Card Image
```bash
cd pluto_msk/firmware
make PLATFORM=libre sdimg
```

Copy contents of sdimg directory in build directory to an SD card and then boot from SD card. 
