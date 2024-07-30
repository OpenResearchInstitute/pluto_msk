#!/bin/sh

# assert init
devmem 0x43C000008 32 0x1

# Enable PTT, Enable Loopback
devmem 0x43C00000C 32 0x3

# Bitrate NCO Frequency Word
devmem 0x43C00001C 32 0x0039D036

# F1 and F2 NCO Frequency Words
devmem 0x43C000020 32 0x04BE147A
devmem 0x43C000024 32 0x044A740D

# Low-pass filter alpha
devmem 0x43C000028 32 0x20000

# Loop PI controller gains
devmem 0x43C000028 32 0x00320014

# Tx and Rx Data Width
devmem 0x43C000030 32 0x8
devmem 0x43C000034 32 0x8

# PRBS Data Select
devmem 0x43C000038 32 0x1
# PRBS Polynomial
devmem 0x43C000040 32 0x90000000
# PRBS Initial State
devmem 0x43C00003C 40 0xFFFF
# PRBS Error Mask
devmem 0x43C000044 40 0x1

# deassert init
devmem 0x43C000008 32 0x1

# read prbs
devmem 0x43C000048
devmem 0x43C00004C
devmem 0x43C000048
devmem 0x43C00004C
devmem 0x43C000048
devmem 0x43C00004C

# resync PRBS
devmem 0x43C000038 32 0x9
devmem 0x43C000038 32 0x1

# read prbs
devmem 0x43C000048
devmem 0x43C00004C
devmem 0x43C000048
devmem 0x43C00004C
devmem 0x43C000048
devmem 0x43C00004C

