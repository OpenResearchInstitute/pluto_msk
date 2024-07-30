#!/bin/sh

# assert init
devmem 0x43C00008 32 0x1

# Enable PTT, Enable Loopback
devmem 0x43C0000C 32 0x3

# Bitrate NCO Frequency Word
devmem 0x43C0001C 32 0x0039D036

# F1 and F2 NCO Frequency Words
devmem 0x43C00020 32 0x04BE147A
devmem 0x43C00024 32 0x044A740D

# Low-pass filter alpha
devmem 0x43C00028 32 0x20000

# Loop PI controller gains
devmem 0x43C00028 32 0x00320014

# Tx and Rx Data Width
devmem 0x43C00030 32 0x8
devmem 0x43C00034 32 0x8

# PRBS Data Select
devmem 0x43C00038 32 0x1
# PRBS Polynomial
devmem 0x43C00040 32 0x90000000
# PRBS Initial State
devmem 0x43C0003C 32 0xFFFF
# PRBS Error Mask
devmem 0x43C00044 32 0x1
# deassert init
devmem 0x43C00008 32 0x0

# read prbs
devmem 0x43C00048
devmem 0x43C0004C
devmem 0x43C00048
devmem 0x43C0004C
devmem 0x43C00048
devmem 0x43C0004C

# resync PRBS
devmem 0x43C00038 32 0x9
devmem 0x43C00038 32 0x1

# read prbs
devmem 0x43C00048
devmem 0x43C0004C
devmem 0x43C00048
devmem 0x43C0004C
devmem 0x43C00048
devmem 0x43C0004C

# Enable PTT, Enable Loopback, and RX Invert
devmem 0x43C0000C 32 0x7

# read prbs
devmem 0x43C00048
devmem 0x43C0004C
devmem 0x43C00048
devmem 0x43C0004C
devmem 0x43C00048
devmem 0x43C0004C

# resync PRBS
devmem 0x43C00038 32 0x9
devmem 0x43C00038 32 0x1

# read prbs
devmem 0x43C00048
devmem 0x43C0004C
devmem 0x43C00048
devmem 0x43C0004C
devmem 0x43C00048
devmem 0x43C0004C
