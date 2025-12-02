


"""
Unit Tests for the msk_top_regs register model Python Wrapper

This code was generated from the PeakRDL-python package version 1.4.0
"""


import sys
import asyncio
if sys.version_info < (3, 8):
    import asynctest  # type: ignore[import]
else:
    import unittest



from ..lib import RegisterWriteVerifyError

from ..lib import AsyncCallbackSet


from ._msk_top_regs_test_base import msk_top_regs_TestCase, msk_top_regs_TestCase_BlockAccess

from ..reg_model.msk_top_regs import msk_top_regs_cls
from ..sim.msk_top_regs import msk_top_regs_simulator_cls

class msk_top_regs_SimTestCase(msk_top_regs_TestCase): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.sim = msk_top_regs_simulator_cls(address=0)
        self.dut = msk_top_regs_cls(callbacks=AsyncCallbackSet(read_callback=self.sim.read,
                                                          write_callback=self.sim.write))

class msk_top_regs_SimTestCase_BlockAccess(msk_top_regs_TestCase_BlockAccess): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.sim = msk_top_regs_simulator_cls(address=0)
        self.dut = msk_top_regs_cls(callbacks=AsyncCallbackSet(read_callback=self.sim.read,
                                                          write_callback=self.sim.write,
                                                          read_block_callback=self.sim.read_block,
                                                          write_block_callback=self.sim.write_block))




if __name__ == '__main__':
    pass