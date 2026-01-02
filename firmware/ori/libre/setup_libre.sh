#!/bin/bash
# Setup script to install LibreSDR support files into submodules
# Run this after cloning the repo and initializing submodules

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIRMWARE_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"

echo "=========================================="
echo "LibreSDR Setup for pluto_msk"
echo "=========================================="

echo "Installing Linux device tree and config..."
cp "$SCRIPT_DIR/linux-dts/zynq-libre.dts" "$FIRMWARE_DIR/linux/arch/arm/boot/dts/"
cp "$SCRIPT_DIR/linux-dts/zynq-libre.dtsi" "$FIRMWARE_DIR/linux/arch/arm/boot/dts/"
cp "$SCRIPT_DIR/linux-configs/zynq_libre_linux_defconfig" "$FIRMWARE_DIR/linux/arch/arm/configs/"

echo "Installing U-Boot device tree and config..."
cp "$SCRIPT_DIR/uboot-dts/zynq-libre-sdr.dts" "$FIRMWARE_DIR/u-boot-xlnx/arch/arm/dts/"
cp "$SCRIPT_DIR/uboot-configs/zynq_libre_defconfig" "$FIRMWARE_DIR/u-boot-xlnx/configs/"

# Add zynq-libre-sdr.dtb to U-Boot DTS Makefile if not present
if ! grep -q "zynq-libre-sdr.dtb" "$FIRMWARE_DIR/u-boot-xlnx/arch/arm/dts/Makefile"; then
    sed -i '/zynq-pluto-sdr.dtb/a\	zynq-libre-sdr.dtb \\' "$FIRMWARE_DIR/u-boot-xlnx/arch/arm/dts/Makefile"
    echo "  Added zynq-libre-sdr.dtb to U-Boot DTS Makefile"
fi

echo "Installing Buildroot config..."
cp "$SCRIPT_DIR/buildroot-configs/zynq_libre_defconfig" "$FIRMWARE_DIR/buildroot/configs/"

echo ""
echo "=========================================="
echo "LibreSDR setup complete!"
echo "=========================================="
echo ""
echo "To build LibreSDR firmware:"
echo ""
echo "  Option 1 - Build HDL first (requires Vivado, ~30 min):"
echo "    cd pluto_msk/projects/libre && make"
echo "    cd pluto_msk/firmware"
echo "    make PLATFORM=libre"
echo ""
echo "  Option 1a - Build SD Card Image Files"
echo "    cd pluto_msk/firmware"
echo "    make PLATFORM=libre sdimg"
echo ""
echo "  Option 2 - Use pre-built XSA:"
echo "    cd pluto_msk/firmware"
echo "    make PLATFORM=libre XSA_FILE=/path/to/system_top.xsa"
echo ""
