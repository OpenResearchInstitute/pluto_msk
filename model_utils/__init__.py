"""
Fixed-point utility functions for VHDL RTL model verification.

These helpers match VHDL signed/unsigned arithmetic behavior for
bit-accurate comparison with RTL simulation.
"""

from .utils import (
    signed,
    unsigned,
    sat_signed,
    sat_add_signed,
    shift_right_signed,
    resize_signed,
    vhdl_saturate,
)
