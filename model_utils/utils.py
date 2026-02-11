"""
Fixed-point utility functions for VHDL RTL model verification.

These helpers match VHDL signed/unsigned arithmetic behavior for
bit-accurate comparison with RTL simulation.
"""


def signed(val, width):
    """Sign-extend an integer to `width` bits (VHDL signed semantics)."""
    mask = (1 << width) - 1
    val = val & mask
    if val >= (1 << (width - 1)):
        val -= (1 << width)
    return val


def unsigned(val, width):
    """Mask an integer to `width` bits (VHDL unsigned semantics)."""
    return val & ((1 << width) - 1)


def sat_signed(val, width):
    """Saturate a value to fit in `width`-bit signed range."""
    max_pos = (1 << (width - 1)) - 1
    max_neg = -(1 << (width - 1))
    if val > max_pos:
        return max_pos
    elif val < max_neg:
        return max_neg
    return val


def sat_add_signed(a, b, width):
    """Saturating signed addition matching VHDL overflow detection.

    Uses the RTL pattern: overflow when MSB and MSB-1 of sum disagree.
    """
    result = signed(a, width) + signed(b, width)
    return sat_signed(result, width)


def shift_right_signed(val, shift, width):
    """Arithmetic right shift for signed value of `width` bits."""
    val = signed(val, width)
    if shift <= 0:
        return val
    return val >> shift


def resize_signed(val, from_width, to_width):
    """Resize a signed value (sign-extend or truncate)."""
    val = signed(val, from_width)
    return signed(val, to_width)


def vhdl_saturate(val, width):
    """Match VHDL saturation pattern used in costas_loop and pi_controller.

    Checks if MSB and MSB-1 disagree (overflow indicator):
      - MSB=0, MSB-1=1 -> positive overflow -> clamp to MAX_POS
      - MSB=1, MSB-1=0 -> negative overflow -> clamp to MAX_NEG
    """
    mask = (1 << width) - 1
    uval = val & mask
    msb = (uval >> (width - 1)) & 1
    msb_1 = (uval >> (width - 2)) & 1

    max_pos = 1 << (width - 2)  # 2^(W-2)
    max_neg = -(1 << (width - 2))  # -2^(W-2), which is 3<<(W-2) in unsigned

    if msb == 0 and msb_1 == 1:
        return max_pos
    elif msb == 1 and msb_1 == 0:
        return max_neg
    else:
        return signed(val, width)
