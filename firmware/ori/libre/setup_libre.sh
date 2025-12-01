#!/bin/bash
# Setup script to install LibreSDR support files into submodules
# Run this after cloning the repo and initializing submodules

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIRMWARE_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"

echo "Installing LibreSDR files..."

# Linux device tree and config
cp "$SCRIPT_DIR/linux-dts/zynq-libre.dts" "$FIRMWARE_DIR/linux/arch/arm/boot/dts/"
cp "$SCRIPT_DIR/linux-dts/zynq-libre.dtsi" "$FIRMWARE_DIR/linux/arch/arm/boot/dts/"
cp "$SCRIPT_DIR/linux-configs/zynq_libre_linux_defconfig" "$FIRMWARE_DIR/linux/arch/arm/configs/"

# U-Boot device tree and config
cp "$SCRIPT_DIR/uboot-dts/zynq-libre-sdr.dts" "$FIRMWARE_DIR/u-boot-xlnx/arch/arm/dts/"
cp "$SCRIPT_DIR/uboot-configs/zynq_libre_defconfig" "$FIRMWARE_DIR/u-boot-xlnx/configs/"

# Add zynq-libre-sdr.dtb to U-Boot DTS Makefile if not present
if ! grep -q "zynq-libre-sdr.dtb" "$FIRMWARE_DIR/u-boot-xlnx/arch/arm/dts/Makefile"; then
    sed -i '/zynq-pluto-sdr.dtb/a\	zynq-libre-sdr.dtb \\' "$FIRMWARE_DIR/u-boot-xlnx/arch/arm/dts/Makefile"
    echo "Added zynq-libre-sdr.dtb to U-Boot DTS Makefile"
fi

# Buildroot config
cp "$SCRIPT_DIR/buildroot-configs/zynq_libre_defconfig" "$FIRMWARE_DIR/buildroot/configs/"

echo "LibreSDR setup complete!"
echo "Build with: make TARGET=libre"
