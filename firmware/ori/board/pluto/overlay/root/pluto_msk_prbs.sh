#!/bin/sh

# assert init
devmem 0x43C00008 32 0x1

# Enable PTT, Enable Loopback
devmem 0x43C0000C 32 0x3

# Bitrate NCO Frequency Word
devmem 0x43C0001C 32 0x0039D036

# Tx F1 and F2 NCO Frequency Words
devmem 0x43C00020 32 0x04BE147A
devmem 0x43C00024 32 0x044A740D

# Rx F1 and F2 NCO Frequency Words
devmem 0x43C00028 32 0x04BE147A
devmem 0x43C0002C 32 0x044A740D

# Low-pass filter alpha
devmem 0x43C00030 32 0x20000

# Loop PI controller gains
devmem 0x43C00034 32 0x01F400FA

# Tx and Rx Data Width
devmem 0x43C00038 32 0x8
devmem 0x43C0003C 32 0x8

# PRBS Data Select
devmem 0x43C00040 32 0x1
# PRBS Polynomial
devmem 0x43C00044 32 0x90000000
# PRBS Initial State
devmem 0x43C00048 32 0xFFFF
# PRBS Error Mask
devmem 0x43C0004C 32 0x1
# deassert init
devmem 0x43C00008 32 0x0

# read prbs
devmem 0x43C00050
devmem 0x43C00054
devmem 0x43C00050
devmem 0x43C00054
devmem 0x43C00050
devmem 0x43C00054

# resync PRBS
devmem 0x43C00040 32 0x9
devmem 0x43C00040 32 0x1

# read prbs
devmem 0x43C00050
devmem 0x43C00054
devmem 0x43C00050
devmem 0x43C00054
devmem 0x43C00050
devmem 0x43C00054

# Enable PTT, Enable Loopback, and RX Invert
devmem 0x43C0000C 32 0x7

# read prbs
devmem 0x43C00050
devmem 0x43C00054
devmem 0x43C00050
devmem 0x43C00054
devmem 0x43C00050
devmem 0x43C00054

# resync PRBS
devmem 0x43C00040 32 0x9
devmem 0x43C00040 32 0x1

# read prbs
devmem 0x43C00050
devmem 0x43C00054
devmem 0x43C00050
devmem 0x43C00054
devmem 0x43C00050
devmem 0x43C00054
