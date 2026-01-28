


"""
Unit Tests for the msk_top_regs register model Python Wrapper

This code was generated from the PeakRDL-python package version 2.3.0
"""






from array import array as Array

import sys
import asyncio
if sys.version_info < (3, 8):
    import asynctest  # type: ignore[import]
else:
    import unittest

import random



from ..lib import RegisterWriteVerifyError

from ..lib import AsyncCallbackSet, AsyncCallbackSetLegacy



from ..reg_model import RegModel

from ..sim_lib.dummy_callbacks import async_dummy_read as read_addr_space
from ..sim_lib.dummy_callbacks import async_dummy_write as write_addr_space
from ..sim_lib.dummy_callbacks import async_dummy_read_block as read_block_addr_space
from ..sim_lib.dummy_callbacks import async_dummy_write_block as write_block_addr_space
from ..sim_lib.dummy_callbacks import async_dummy_read_block_legacy as read_block_addr_space_alt
from ..sim_lib.dummy_callbacks import async_dummy_write_block_legacy as write_block_addr_space_alt



from ..lib import SystemRDLEnum, SystemRDLEnumEntry


async def read_callback(addr: int, width: int, accesswidth: int) -> int:
    return await read_addr_space(addr=addr, width=width, accesswidth=accesswidth)

async def read_block_callback(addr: int, width: int, accesswidth: int, length: int) -> list[int]:
    return await read_block_addr_space(addr=addr, width=width, accesswidth=accesswidth, length=length)

async def read_block_callback_alt(addr: int, width: int, accesswidth: int, length: int) -> Array:
    return await read_block_addr_space_alt(addr=addr, width=width, accesswidth=accesswidth, length=length)

async def write_callback(addr: int, width: int, accesswidth: int,  data: int) -> None:
    await write_addr_space(addr=addr, width=width, accesswidth=accesswidth, data=data)

async def write_block_callback(addr: int, width: int, accesswidth: int,  data: list[int]) -> None:
    await write_block_addr_space(addr=addr, width=width, accesswidth=accesswidth, data=data)

async def write_block_callback_alt(addr: int, width: int, accesswidth: int,  data: Array) -> None:
    await write_block_addr_space_alt(addr=addr, width=width, accesswidth=accesswidth, data=data)

def random_enum_reg_value(enum_class: type[SystemRDLEnum]) -> SystemRDLEnum:
    return random.choice(list(enum_class))


if sys.version_info < (3, 8):
    TestCaseBase = asynctest.TestCase
else:
    TestCaseBase = unittest.IsolatedAsyncioTestCase


class msk_top_regs_TestCase(TestCaseBase): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.dut = RegModel(callbacks=AsyncCallbackSet(read_callback=read_callback,
                                                          write_callback=write_callback))

    @staticmethod
    def _reverse_bits(value: int, number_bits: int) -> int:
        """

        Args:
            value: value to reverse
            number_bits: number of bits used in the value

        Returns:
            reversed valued
        """
        result = 0
        for i in range(number_bits):
            if (value >> i) & 1:
                result |= 1 << (number_bits - 1 - i)
        return result

class msk_top_regs_TestCase_BlockAccess(TestCaseBase): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.dut = RegModel(callbacks=AsyncCallbackSet(read_callback=read_callback,
                                                          write_callback=write_callback,
                                                          read_block_callback=read_block_callback,
                                                          write_block_callback=write_block_callback))

class msk_top_regs_TestCase_AltBlockAccess(TestCaseBase): # type: ignore[valid-type,misc]
    """
    Based test to use with the alternative call backs, this allow the legacy output API to be tested
    with the new callbacks and visa versa.
    """

    def setUp(self) -> None:
        self.dut = RegModel(callbacks=AsyncCallbackSetLegacy(
                                                          read_callback=read_callback,
                                                          write_callback=write_callback,
                                                          read_block_callback=read_block_callback_alt,
                                                          write_block_callback=write_block_callback_alt))




if __name__ == '__main__':
    pass



