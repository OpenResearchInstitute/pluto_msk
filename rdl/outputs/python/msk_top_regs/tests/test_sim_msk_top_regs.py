


"""
Unit Tests for the msk_top_regs register model Python Wrapper

This code was generated from the PeakRDL-python package version 1.4.0
"""


from typing import Union, cast

import sys
import asyncio
import unittest
from unittest.mock import Mock

import random


from ..sim_lib.register import Register,MemoryRegister
from ..sim_lib.field import Field

from ._msk_top_regs_sim_test_base import msk_top_regs_SimTestCase, msk_top_regs_SimTestCase_BlockAccess
from ._msk_top_regs_sim_test_base import __name__ as base_name
from ._msk_top_regs_test_base import random_enum_reg_value


from ..lib import SystemRDLEnum


class msk_top_regs_single_access(msk_top_regs_SimTestCase): # type: ignore[valid-type,misc]

    async def test_register_read_and_write(self) -> None:
        """
        Walk the register map and check every register can be read and written to correctly
        """
        # test access operations (read and/or write) to register:
        # msk_top_regs.Hash_ID_Low
        with self.subTest(msg='register: msk_top_regs.Hash_ID_Low'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Hash_ID_Low')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Hash_ID_Low.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Hash_ID_Low.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.Hash_ID_Low.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Hash_ID_High
        with self.subTest(msg='register: msk_top_regs.Hash_ID_High'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Hash_ID_High')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Hash_ID_High.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Hash_ID_High.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.Hash_ID_High.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Init
        with self.subTest(msg='register: msk_top_regs.MSK_Init'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Init')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Init.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Init.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.MSK_Init.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.MSK_Init.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.MSK_Init.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.MSK_Init.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.MSK_Init.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Control
        with self.subTest(msg='register: msk_top_regs.MSK_Control'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.MSK_Control.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.MSK_Control.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.MSK_Control.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.MSK_Control.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.MSK_Control.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Status
        with self.subTest(msg='register: msk_top_regs.MSK_Status'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Status')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Status.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Status.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.MSK_Status.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Bit_Count
        with self.subTest(msg='register: msk_top_regs.Tx_Bit_Count'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Tx_Bit_Count')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Bit_Count.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Bit_Count.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.Tx_Bit_Count.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Bit_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Bit_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Bit_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.Tx_Bit_Count.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Enable_Count
        with self.subTest(msg='register: msk_top_regs.Tx_Enable_Count'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Tx_Enable_Count')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Enable_Count.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Enable_Count.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.Tx_Enable_Count.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Enable_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Enable_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Enable_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.Tx_Enable_Count.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Fb_FreqWord
        with self.subTest(msg='register: msk_top_regs.Fb_FreqWord'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Fb_FreqWord')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Fb_FreqWord.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Fb_FreqWord.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.Fb_FreqWord.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Fb_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Fb_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Fb_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.Fb_FreqWord.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.TX_F1_FreqWord
        with self.subTest(msg='register: msk_top_regs.TX_F1_FreqWord'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.TX_F1_FreqWord')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.TX_F1_FreqWord.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.TX_F1_FreqWord.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.TX_F1_FreqWord.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.TX_F1_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.TX_F1_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.TX_F1_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.TX_F1_FreqWord.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.TX_F2_FreqWord
        with self.subTest(msg='register: msk_top_regs.TX_F2_FreqWord'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.TX_F2_FreqWord')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.TX_F2_FreqWord.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.TX_F2_FreqWord.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.TX_F2_FreqWord.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.TX_F2_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.TX_F2_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.TX_F2_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.TX_F2_FreqWord.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.RX_F1_FreqWord
        with self.subTest(msg='register: msk_top_regs.RX_F1_FreqWord'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.RX_F1_FreqWord')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.RX_F1_FreqWord.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.RX_F1_FreqWord.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.RX_F1_FreqWord.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.RX_F1_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.RX_F1_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.RX_F1_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.RX_F1_FreqWord.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.RX_F2_FreqWord
        with self.subTest(msg='register: msk_top_regs.RX_F2_FreqWord'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.RX_F2_FreqWord')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.RX_F2_FreqWord.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.RX_F2_FreqWord.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.RX_F2_FreqWord.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.RX_F2_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.RX_F2_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.RX_F2_FreqWord.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.RX_F2_FreqWord.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_0
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Config_0')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_0.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_0.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.LPF_Config_0.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Config_0.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Config_0.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Config_0.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.LPF_Config_0.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_1
        with self.subTest(msg='register: msk_top_regs.LPF_Config_1'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Config_1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_1.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_1.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.LPF_Config_1.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Config_1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Config_1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Config_1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.LPF_Config_1.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Data_Width
        with self.subTest(msg='register: msk_top_regs.Tx_Data_Width'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Tx_Data_Width')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Data_Width.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Data_Width.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.Tx_Data_Width.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Data_Width.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Data_Width.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Data_Width.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.Tx_Data_Width.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Rx_Data_Width
        with self.subTest(msg='register: msk_top_regs.Rx_Data_Width'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Rx_Data_Width')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Rx_Data_Width.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Rx_Data_Width.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.Rx_Data_Width.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Rx_Data_Width.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Rx_Data_Width.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Rx_Data_Width.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.Rx_Data_Width.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Control
        with self.subTest(msg='register: msk_top_regs.PRBS_Control'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Control.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Control.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.PRBS_Control.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Control.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Control.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Control.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.PRBS_Control.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Initial_State
        with self.subTest(msg='register: msk_top_regs.PRBS_Initial_State'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Initial_State')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Initial_State.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Initial_State.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.PRBS_Initial_State.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Initial_State.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Initial_State.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Initial_State.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.PRBS_Initial_State.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Polynomial
        with self.subTest(msg='register: msk_top_regs.PRBS_Polynomial'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Polynomial')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Polynomial.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Polynomial.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.PRBS_Polynomial.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Polynomial.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Polynomial.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Polynomial.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.PRBS_Polynomial.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Error_Mask
        with self.subTest(msg='register: msk_top_regs.PRBS_Error_Mask'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Error_Mask')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Error_Mask.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Error_Mask.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.PRBS_Error_Mask.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Error_Mask.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Error_Mask.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Error_Mask.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.PRBS_Error_Mask.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Bit_Count
        with self.subTest(msg='register: msk_top_regs.PRBS_Bit_Count'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Bit_Count')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Bit_Count.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Bit_Count.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.PRBS_Bit_Count.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Bit_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Bit_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Bit_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.PRBS_Bit_Count.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Error_Count
        with self.subTest(msg='register: msk_top_regs.PRBS_Error_Count'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Error_Count')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Error_Count.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Error_Count.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.PRBS_Error_Count.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Error_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Error_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.PRBS_Error_Count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.PRBS_Error_Count.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Accum_F1
        with self.subTest(msg='register: msk_top_regs.LPF_Accum_F1'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Accum_F1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Accum_F1.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Accum_F1.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.LPF_Accum_F1.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Accum_F1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Accum_F1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Accum_F1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.LPF_Accum_F1.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Accum_F2
        with self.subTest(msg='register: msk_top_regs.LPF_Accum_F2'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Accum_F2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Accum_F2.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Accum_F2.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.LPF_Accum_F2.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Accum_F2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Accum_F2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Accum_F2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.LPF_Accum_F2.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.axis_xfer_count
        with self.subTest(msg='register: msk_top_regs.axis_xfer_count'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.axis_xfer_count')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.axis_xfer_count.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.axis_xfer_count.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.axis_xfer_count.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.axis_xfer_count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.axis_xfer_count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.axis_xfer_count.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.axis_xfer_count.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Rx_Sample_Discard
        with self.subTest(msg='register: msk_top_regs.Rx_Sample_Discard'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Rx_Sample_Discard')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Rx_Sample_Discard.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Rx_Sample_Discard.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.Rx_Sample_Discard.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Rx_Sample_Discard.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Rx_Sample_Discard.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Rx_Sample_Discard.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.Rx_Sample_Discard.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_2
        with self.subTest(msg='register: msk_top_regs.LPF_Config_2'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Config_2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_2.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_2.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.LPF_Config_2.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Config_2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Config_2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.LPF_Config_2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.LPF_Config_2.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.f1_nco_adjust
        with self.subTest(msg='register: msk_top_regs.f1_nco_adjust'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.f1_nco_adjust')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.f1_nco_adjust.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.f1_nco_adjust.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.f1_nco_adjust.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f1_nco_adjust.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f1_nco_adjust.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f1_nco_adjust.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.f1_nco_adjust.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.f2_nco_adjust
        with self.subTest(msg='register: msk_top_regs.f2_nco_adjust'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.f2_nco_adjust')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.f2_nco_adjust.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.f2_nco_adjust.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.f2_nco_adjust.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f2_nco_adjust.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f2_nco_adjust.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f2_nco_adjust.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.f2_nco_adjust.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.f1_error
        with self.subTest(msg='register: msk_top_regs.f1_error'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.f1_error')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.f1_error.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.f1_error.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.f1_error.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f1_error.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f1_error.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f1_error.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.f1_error.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.f2_error
        with self.subTest(msg='register: msk_top_regs.f2_error'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.f2_error')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.f2_error.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.f2_error.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.f2_error.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f2_error.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f2_error.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.f2_error.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.f2_error.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Sync_Ctrl
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Tx_Sync_Ctrl')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Sync_Ctrl.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Sync_Ctrl.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Sync_Ctrl.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Sync_Cnt
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Cnt'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Tx_Sync_Cnt')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Sync_Cnt.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Sync_Cnt.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.Tx_Sync_Cnt.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Sync_Cnt.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Sync_Cnt.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.Tx_Sync_Cnt.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.Tx_Sync_Cnt.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.lowpass_ema_alpha1
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha1'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.lowpass_ema_alpha1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.lowpass_ema_alpha1.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.lowpass_ema_alpha1.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.lowpass_ema_alpha1.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.lowpass_ema_alpha1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.lowpass_ema_alpha1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.lowpass_ema_alpha1.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.lowpass_ema_alpha1.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.lowpass_ema_alpha2
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha2'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.lowpass_ema_alpha2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.lowpass_ema_alpha2.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.lowpass_ema_alpha2.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.lowpass_ema_alpha2.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.lowpass_ema_alpha2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.lowpass_ema_alpha2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.lowpass_ema_alpha2.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.lowpass_ema_alpha2.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.rx_power
        with self.subTest(msg='register: msk_top_regs.rx_power'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.rx_power')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_power.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_power.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.rx_power.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.rx_power.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.rx_power.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.rx_power.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.rx_power.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.tx_async_fifo_rd_wr_ptr
        with self.subTest(msg='register: msk_top_regs.tx_async_fifo_rd_wr_ptr'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.tx_async_fifo_rd_wr_ptr')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.tx_async_fifo_rd_wr_ptr.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.tx_async_fifo_rd_wr_ptr.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.tx_async_fifo_rd_wr_ptr.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.tx_async_fifo_rd_wr_ptr.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.tx_async_fifo_rd_wr_ptr.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.tx_async_fifo_rd_wr_ptr.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.tx_async_fifo_rd_wr_ptr.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.rx_async_fifo_rd_wr_ptr
        with self.subTest(msg='register: msk_top_regs.rx_async_fifo_rd_wr_ptr'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.rx_async_fifo_rd_wr_ptr')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_async_fifo_rd_wr_ptr.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_async_fifo_rd_wr_ptr.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.rx_async_fifo_rd_wr_ptr.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.rx_async_fifo_rd_wr_ptr.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.rx_async_fifo_rd_wr_ptr.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.rx_async_fifo_rd_wr_ptr.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.rx_async_fifo_rd_wr_ptr.read(), random_value)
            
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.rx_frame_sync_status
        with self.subTest(msg='register: msk_top_regs.rx_frame_sync_status'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.rx_frame_sync_status')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            register_read_callback = Mock()
            register_write_callback = Mock()

            # register read checks
            # update the value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_frame_sync_status.read(), random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_frame_sync_status.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.value = random_value
            sim_register.read_callback = None
            sim_register.write_callback = None
            self.assertEqual(await self.dut.rx_frame_sync_status.read(), random_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()

            

            # register write checks
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.rx_frame_sync_status.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            # up to now the callback should not have been called
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.rx_frame_sync_status.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            register_write_callback.assert_called_once_with(value=random_value)
            register_read_callback.assert_not_called()
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            await self.dut.rx_frame_sync_status.write(random_value)  # type: ignore[union-attr]
            self.assertEqual(sim_register.value, random_value)
            self.assertEqual(await self.dut.rx_frame_sync_status.read(), random_value)
            
            

        

    async def test_field_read_and_write(self) -> None:
        """
        Walk the register map and check every field can be read and written to correctly
        """
        random_field_value: Union[int, SystemRDLEnum]
        # test access operations (read and/or write) to register:
        # msk_top_regs.Hash_ID_Low.hash_id_lo
        with self.subTest(msg='field: msk_top_regs.Hash_ID_Low.hash_id_lo'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Hash_ID_Low')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Hash_ID_Low.hash_id_lo')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Hash_ID_Low.hash_id_lo.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.Hash_ID_Low.hash_id_lo.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Hash_ID_Low.hash_id_lo.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Hash_ID_Low.hash_id_lo.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Hash_ID_High.hash_id_hi
        with self.subTest(msg='field: msk_top_regs.Hash_ID_High.hash_id_hi'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Hash_ID_High')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Hash_ID_High.hash_id_hi')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Hash_ID_High.hash_id_hi.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.Hash_ID_High.hash_id_hi.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Hash_ID_High.hash_id_hi.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Hash_ID_High.hash_id_hi.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Init.txrxinit
        with self.subTest(msg='field: msk_top_regs.MSK_Init.txrxinit'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Init')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Init.txrxinit')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Init.txrxinit.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFE) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.MSK_Init.txrxinit.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Init.txrxinit.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Init.txrxinit.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Init.txrxinit.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Init.txrxinit.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Init.txrxinit.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Init.txinit
        with self.subTest(msg='field: msk_top_regs.MSK_Init.txinit'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Init')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Init.txinit')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Init.txinit.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFD) | (random_field_value << 1))
            
            self.assertEqual(await self.dut.MSK_Init.txinit.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Init.txinit.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Init.txinit.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Init.txinit.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Init.txinit.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Init.txinit.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Init.rxinit
        with self.subTest(msg='field: msk_top_regs.MSK_Init.rxinit'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Init')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Init.rxinit')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Init.rxinit.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFB) | (random_field_value << 2))
            
            self.assertEqual(await self.dut.MSK_Init.rxinit.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Init.rxinit.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Init.rxinit.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Init.rxinit.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Init.rxinit.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Init.rxinit.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Control.ptt
        with self.subTest(msg='field: msk_top_regs.MSK_Control.ptt'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Control.ptt')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.ptt.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFE) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.MSK_Control.ptt.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Control.ptt.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.ptt.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.ptt.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.ptt.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.ptt.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Control.loopback_ena
        with self.subTest(msg='field: msk_top_regs.MSK_Control.loopback_ena'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Control.loopback_ena')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.loopback_ena.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFD) | (random_field_value << 1))
            
            self.assertEqual(await self.dut.MSK_Control.loopback_ena.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Control.loopback_ena.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.loopback_ena.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.loopback_ena.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.loopback_ena.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.loopback_ena.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Control.rx_invert
        with self.subTest(msg='field: msk_top_regs.MSK_Control.rx_invert'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Control.rx_invert')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.rx_invert.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFB) | (random_field_value << 2))
            
            self.assertEqual(await self.dut.MSK_Control.rx_invert.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Control.rx_invert.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.rx_invert.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.rx_invert.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.rx_invert.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.rx_invert.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Control.clear_counts
        with self.subTest(msg='field: msk_top_regs.MSK_Control.clear_counts'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Control.clear_counts')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x8) >> 3
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.clear_counts.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFF7) | (random_field_value << 3))
            
            self.assertEqual(await self.dut.MSK_Control.clear_counts.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x8) >> 3
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Control.clear_counts.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x8) >> 3
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.clear_counts.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.clear_counts.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.clear_counts.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.clear_counts.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Control.diff_encoder_loopback
        with self.subTest(msg='field: msk_top_regs.MSK_Control.diff_encoder_loopback'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Control.diff_encoder_loopback')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x10) >> 4
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.diff_encoder_loopback.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFEF) | (random_field_value << 4))
            
            self.assertEqual(await self.dut.MSK_Control.diff_encoder_loopback.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x10) >> 4
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Control.diff_encoder_loopback.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x10) >> 4
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Control.diff_encoder_loopback.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.diff_encoder_loopback.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFEF) | (0x10 & (random_field_value << 4)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.diff_encoder_loopback.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFEF) | (0x10 & (random_field_value << 4)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFEF) | (0x10 & (random_field_value << 4)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.MSK_Control.diff_encoder_loopback.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFEF) | (0x10 & (random_field_value << 4)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Status.demod_sync_lock
        with self.subTest(msg='field: msk_top_regs.MSK_Status.demod_sync_lock'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Status')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Status.demod_sync_lock')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Status.demod_sync_lock.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFE) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.MSK_Status.demod_sync_lock.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Status.demod_sync_lock.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Status.demod_sync_lock.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Status.tx_enable
        with self.subTest(msg='field: msk_top_regs.MSK_Status.tx_enable'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Status')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Status.tx_enable')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Status.tx_enable.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFD) | (random_field_value << 1))
            
            self.assertEqual(await self.dut.MSK_Status.tx_enable.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Status.tx_enable.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Status.tx_enable.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Status.rx_enable
        with self.subTest(msg='field: msk_top_regs.MSK_Status.rx_enable'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Status')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Status.rx_enable')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Status.rx_enable.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFB) | (random_field_value << 2))
            
            self.assertEqual(await self.dut.MSK_Status.rx_enable.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Status.rx_enable.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x4) >> 2
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Status.rx_enable.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Status.tx_axis_valid
        with self.subTest(msg='field: msk_top_regs.MSK_Status.tx_axis_valid'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.MSK_Status')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.MSK_Status.tx_axis_valid')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x8) >> 3
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Status.tx_axis_valid.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFF7) | (random_field_value << 3))
            
            self.assertEqual(await self.dut.MSK_Status.tx_axis_valid.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x8) >> 3
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.MSK_Status.tx_axis_valid.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x8) >> 3
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.MSK_Status.tx_axis_valid.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Bit_Count.data
        with self.subTest(msg='field: msk_top_regs.Tx_Bit_Count.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Tx_Bit_Count')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Tx_Bit_Count.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Bit_Count.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.Tx_Bit_Count.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Tx_Bit_Count.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Bit_Count.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.Tx_Bit_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.Tx_Bit_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.Tx_Bit_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Enable_Count.data
        with self.subTest(msg='field: msk_top_regs.Tx_Enable_Count.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Tx_Enable_Count')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Tx_Enable_Count.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Enable_Count.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.Tx_Enable_Count.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Tx_Enable_Count.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Enable_Count.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.Tx_Enable_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.Tx_Enable_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.Tx_Enable_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Fb_FreqWord.config_data
        with self.subTest(msg='field: msk_top_regs.Fb_FreqWord.config_data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Fb_FreqWord')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Fb_FreqWord.config_data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Fb_FreqWord.config_data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.Fb_FreqWord.config_data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Fb_FreqWord.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Fb_FreqWord.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.Fb_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.Fb_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.Fb_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.TX_F1_FreqWord.config_data
        with self.subTest(msg='field: msk_top_regs.TX_F1_FreqWord.config_data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.TX_F1_FreqWord')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.TX_F1_FreqWord.config_data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.TX_F1_FreqWord.config_data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.TX_F1_FreqWord.config_data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.TX_F1_FreqWord.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.TX_F1_FreqWord.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.TX_F1_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.TX_F1_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.TX_F1_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.TX_F2_FreqWord.config_data
        with self.subTest(msg='field: msk_top_regs.TX_F2_FreqWord.config_data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.TX_F2_FreqWord')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.TX_F2_FreqWord.config_data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.TX_F2_FreqWord.config_data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.TX_F2_FreqWord.config_data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.TX_F2_FreqWord.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.TX_F2_FreqWord.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.TX_F2_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.TX_F2_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.TX_F2_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.RX_F1_FreqWord.config_data
        with self.subTest(msg='field: msk_top_regs.RX_F1_FreqWord.config_data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.RX_F1_FreqWord')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.RX_F1_FreqWord.config_data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.RX_F1_FreqWord.config_data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.RX_F1_FreqWord.config_data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.RX_F1_FreqWord.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.RX_F1_FreqWord.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.RX_F1_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.RX_F1_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.RX_F1_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.RX_F2_FreqWord.config_data
        with self.subTest(msg='field: msk_top_regs.RX_F2_FreqWord.config_data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.RX_F2_FreqWord')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.RX_F2_FreqWord.config_data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.RX_F2_FreqWord.config_data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.RX_F2_FreqWord.config_data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.RX_F2_FreqWord.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.RX_F2_FreqWord.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.RX_F2_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.RX_F2_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.RX_F2_FreqWord.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_0.lpf_freeze
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.lpf_freeze'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Config_0')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.LPF_Config_0.lpf_freeze')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_0.lpf_freeze.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFE) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.LPF_Config_0.lpf_freeze.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.LPF_Config_0.lpf_freeze.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_0.lpf_freeze.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.LPF_Config_0.lpf_freeze.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.LPF_Config_0.lpf_freeze.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.LPF_Config_0.lpf_freeze.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_0.lpf_zero
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.lpf_zero'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Config_0')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.LPF_Config_0.lpf_zero')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_0.lpf_zero.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFD) | (random_field_value << 1))
            
            self.assertEqual(await self.dut.LPF_Config_0.lpf_zero.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.LPF_Config_0.lpf_zero.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_0.lpf_zero.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.LPF_Config_0.lpf_zero.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.LPF_Config_0.lpf_zero.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.LPF_Config_0.lpf_zero.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_0.prbs_reserved
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.prbs_reserved'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Config_0')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.LPF_Config_0.prbs_reserved')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFC) >> 2
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_0.prbs_reserved.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x3F+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFF03) | (random_field_value << 2))
            
            self.assertEqual(await self.dut.LPF_Config_0.prbs_reserved.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFC) >> 2
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.LPF_Config_0.prbs_reserved.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFC) >> 2
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_0.prbs_reserved.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x3F+1)
            
            await self.dut.LPF_Config_0.prbs_reserved.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF03) | (0xFC & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x3F+1)
            
            await self.dut.LPF_Config_0.prbs_reserved.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF03) | (0xFC & (random_field_value << 2)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFF03) | (0xFC & (random_field_value << 2)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x3F+1)
            
            await self.dut.LPF_Config_0.prbs_reserved.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF03) | (0xFC & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_0.lpf_alpha
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.lpf_alpha'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Config_0')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.LPF_Config_0.lpf_alpha')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF00) >> 8
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_0.lpf_alpha.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFF) | (random_field_value << 8))
            
            self.assertEqual(await self.dut.LPF_Config_0.lpf_alpha.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF00) >> 8
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.LPF_Config_0.lpf_alpha.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF00) >> 8
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_0.lpf_alpha.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.LPF_Config_0.lpf_alpha.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF) | (0xFFFFFF00 & (random_field_value << 8)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.LPF_Config_0.lpf_alpha.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF) | (0xFFFFFF00 & (random_field_value << 8)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFF) | (0xFFFFFF00 & (random_field_value << 8)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.LPF_Config_0.lpf_alpha.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF) | (0xFFFFFF00 & (random_field_value << 8)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_1.i_gain
        with self.subTest(msg='field: msk_top_regs.LPF_Config_1.i_gain'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Config_1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.LPF_Config_1.i_gain')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_1.i_gain.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFF000000) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.LPF_Config_1.i_gain.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.LPF_Config_1.i_gain.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_1.i_gain.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.LPF_Config_1.i_gain.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.LPF_Config_1.i_gain.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.LPF_Config_1.i_gain.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_1.i_shift
        with self.subTest(msg='field: msk_top_regs.LPF_Config_1.i_shift'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Config_1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.LPF_Config_1.i_shift')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF000000) >> 24
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_1.i_shift.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFF) | (random_field_value << 24))
            
            self.assertEqual(await self.dut.LPF_Config_1.i_shift.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF000000) >> 24
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.LPF_Config_1.i_shift.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF000000) >> 24
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_1.i_shift.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.LPF_Config_1.i_shift.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF) | (0xFF000000 & (random_field_value << 24)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.LPF_Config_1.i_shift.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF) | (0xFF000000 & (random_field_value << 24)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFF) | (0xFF000000 & (random_field_value << 24)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.LPF_Config_1.i_shift.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF) | (0xFF000000 & (random_field_value << 24)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Data_Width.data_width
        with self.subTest(msg='field: msk_top_regs.Tx_Data_Width.data_width'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Tx_Data_Width')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Tx_Data_Width.data_width')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Data_Width.data_width.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFF00) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.Tx_Data_Width.data_width.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Tx_Data_Width.data_width.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Data_Width.data_width.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Tx_Data_Width.data_width.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Tx_Data_Width.data_width.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Tx_Data_Width.data_width.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Rx_Data_Width.data_width
        with self.subTest(msg='field: msk_top_regs.Rx_Data_Width.data_width'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Rx_Data_Width')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Rx_Data_Width.data_width')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Rx_Data_Width.data_width.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFF00) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.Rx_Data_Width.data_width.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Rx_Data_Width.data_width.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Rx_Data_Width.data_width.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Rx_Data_Width.data_width.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Rx_Data_Width.data_width.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Rx_Data_Width.data_width.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Control.prbs_sel
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_sel'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.PRBS_Control.prbs_sel')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Control.prbs_sel.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFE) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.PRBS_Control.prbs_sel.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.PRBS_Control.prbs_sel.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Control.prbs_sel.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_sel.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_sel.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_sel.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Control.prbs_error_insert
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_error_insert'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.PRBS_Control.prbs_error_insert')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_error_insert.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_error_insert.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_error_insert.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Control.prbs_clear
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_clear'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.PRBS_Control.prbs_clear')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_clear.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_clear.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_clear.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFB) | (0x4 & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Control.prbs_manual_sync
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_manual_sync'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.PRBS_Control.prbs_manual_sync')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_manual_sync.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_manual_sync.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.PRBS_Control.prbs_manual_sync.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFF7) | (0x8 & (random_field_value << 3)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Control.prbs_reserved
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_reserved'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.PRBS_Control.prbs_reserved')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFF0) >> 4
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Control.prbs_reserved.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFF000F) | (random_field_value << 4))
            
            self.assertEqual(await self.dut.PRBS_Control.prbs_reserved.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFF0) >> 4
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.PRBS_Control.prbs_reserved.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFF0) >> 4
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Control.prbs_reserved.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFF+1)
            
            await self.dut.PRBS_Control.prbs_reserved.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFF000F) | (0xFFF0 & (random_field_value << 4)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFF+1)
            
            await self.dut.PRBS_Control.prbs_reserved.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFF000F) | (0xFFF0 & (random_field_value << 4)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFF000F) | (0xFFF0 & (random_field_value << 4)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFF+1)
            
            await self.dut.PRBS_Control.prbs_reserved.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFF000F) | (0xFFF0 & (random_field_value << 4)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Control.prbs_sync_threshold
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_sync_threshold'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Control')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.PRBS_Control.prbs_sync_threshold')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFF0000) >> 16
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Control.prbs_sync_threshold.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFF) | (random_field_value << 16))
            
            self.assertEqual(await self.dut.PRBS_Control.prbs_sync_threshold.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFF0000) >> 16
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.PRBS_Control.prbs_sync_threshold.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFF0000) >> 16
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Control.prbs_sync_threshold.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFF+1)
            
            await self.dut.PRBS_Control.prbs_sync_threshold.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFF) | (0xFFFF0000 & (random_field_value << 16)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFF+1)
            
            await self.dut.PRBS_Control.prbs_sync_threshold.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFF) | (0xFFFF0000 & (random_field_value << 16)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFF) | (0xFFFF0000 & (random_field_value << 16)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFF+1)
            
            await self.dut.PRBS_Control.prbs_sync_threshold.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFF) | (0xFFFF0000 & (random_field_value << 16)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Initial_State.config_data
        with self.subTest(msg='field: msk_top_regs.PRBS_Initial_State.config_data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Initial_State')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.PRBS_Initial_State.config_data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Initial_State.config_data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.PRBS_Initial_State.config_data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.PRBS_Initial_State.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Initial_State.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Initial_State.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Initial_State.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Initial_State.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Polynomial.config_data
        with self.subTest(msg='field: msk_top_regs.PRBS_Polynomial.config_data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Polynomial')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.PRBS_Polynomial.config_data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Polynomial.config_data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.PRBS_Polynomial.config_data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.PRBS_Polynomial.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Polynomial.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Polynomial.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Polynomial.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Polynomial.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Error_Mask.config_data
        with self.subTest(msg='field: msk_top_regs.PRBS_Error_Mask.config_data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Error_Mask')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.PRBS_Error_Mask.config_data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Error_Mask.config_data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.PRBS_Error_Mask.config_data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.PRBS_Error_Mask.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Error_Mask.config_data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Error_Mask.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Error_Mask.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Error_Mask.config_data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Bit_Count.data
        with self.subTest(msg='field: msk_top_regs.PRBS_Bit_Count.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Bit_Count')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.PRBS_Bit_Count.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Bit_Count.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.PRBS_Bit_Count.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.PRBS_Bit_Count.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Bit_Count.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Bit_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Bit_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Bit_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Error_Count.data
        with self.subTest(msg='field: msk_top_regs.PRBS_Error_Count.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.PRBS_Error_Count')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.PRBS_Error_Count.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Error_Count.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.PRBS_Error_Count.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.PRBS_Error_Count.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.PRBS_Error_Count.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Error_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Error_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.PRBS_Error_Count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Accum_F1.data
        with self.subTest(msg='field: msk_top_regs.LPF_Accum_F1.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Accum_F1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.LPF_Accum_F1.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Accum_F1.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.LPF_Accum_F1.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.LPF_Accum_F1.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Accum_F1.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.LPF_Accum_F1.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.LPF_Accum_F1.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.LPF_Accum_F1.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Accum_F2.data
        with self.subTest(msg='field: msk_top_regs.LPF_Accum_F2.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Accum_F2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.LPF_Accum_F2.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Accum_F2.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.LPF_Accum_F2.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.LPF_Accum_F2.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Accum_F2.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.LPF_Accum_F2.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.LPF_Accum_F2.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.LPF_Accum_F2.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.axis_xfer_count.data
        with self.subTest(msg='field: msk_top_regs.axis_xfer_count.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.axis_xfer_count')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.axis_xfer_count.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.axis_xfer_count.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.axis_xfer_count.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.axis_xfer_count.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.axis_xfer_count.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.axis_xfer_count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.axis_xfer_count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.axis_xfer_count.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Rx_Sample_Discard.rx_sample_discard
        with self.subTest(msg='field: msk_top_regs.Rx_Sample_Discard.rx_sample_discard'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Rx_Sample_Discard')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Rx_Sample_Discard.rx_sample_discard')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Rx_Sample_Discard.rx_sample_discard.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFF00) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.Rx_Sample_Discard.rx_sample_discard.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Rx_Sample_Discard.rx_sample_discard.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Rx_Sample_Discard.rx_sample_discard.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Rx_Sample_Discard.rx_sample_discard.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Rx_Sample_Discard.rx_sample_discard.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Rx_Sample_Discard.rx_sample_discard.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF00) | (0xFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Rx_Sample_Discard.rx_nco_discard
        with self.subTest(msg='field: msk_top_regs.Rx_Sample_Discard.rx_nco_discard'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Rx_Sample_Discard')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Rx_Sample_Discard.rx_nco_discard')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF00) >> 8
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Rx_Sample_Discard.rx_nco_discard.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFF00FF) | (random_field_value << 8))
            
            self.assertEqual(await self.dut.Rx_Sample_Discard.rx_nco_discard.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF00) >> 8
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Rx_Sample_Discard.rx_nco_discard.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF00) >> 8
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Rx_Sample_Discard.rx_nco_discard.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Rx_Sample_Discard.rx_nco_discard.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFF00FF) | (0xFF00 & (random_field_value << 8)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Rx_Sample_Discard.rx_nco_discard.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFF00FF) | (0xFF00 & (random_field_value << 8)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFF00FF) | (0xFF00 & (random_field_value << 8)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.Rx_Sample_Discard.rx_nco_discard.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFF00FF) | (0xFF00 & (random_field_value << 8)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_2.p_gain
        with self.subTest(msg='field: msk_top_regs.LPF_Config_2.p_gain'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Config_2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.LPF_Config_2.p_gain')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_2.p_gain.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFF000000) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.LPF_Config_2.p_gain.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.LPF_Config_2.p_gain.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_2.p_gain.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.LPF_Config_2.p_gain.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.LPF_Config_2.p_gain.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.LPF_Config_2.p_gain.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_2.p_shift
        with self.subTest(msg='field: msk_top_regs.LPF_Config_2.p_shift'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.LPF_Config_2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.LPF_Config_2.p_shift')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF000000) >> 24
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_2.p_shift.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFF) | (random_field_value << 24))
            
            self.assertEqual(await self.dut.LPF_Config_2.p_shift.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF000000) >> 24
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.LPF_Config_2.p_shift.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFF000000) >> 24
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.LPF_Config_2.p_shift.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.LPF_Config_2.p_shift.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF) | (0xFF000000 & (random_field_value << 24)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.LPF_Config_2.p_shift.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF) | (0xFF000000 & (random_field_value << 24)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFF) | (0xFF000000 & (random_field_value << 24)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFF+1)
            
            await self.dut.LPF_Config_2.p_shift.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFF) | (0xFF000000 & (random_field_value << 24)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.f1_nco_adjust.data
        with self.subTest(msg='field: msk_top_regs.f1_nco_adjust.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.f1_nco_adjust')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.f1_nco_adjust.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.f1_nco_adjust.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.f1_nco_adjust.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.f1_nco_adjust.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.f1_nco_adjust.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f1_nco_adjust.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f1_nco_adjust.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f1_nco_adjust.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.f2_nco_adjust.data
        with self.subTest(msg='field: msk_top_regs.f2_nco_adjust.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.f2_nco_adjust')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.f2_nco_adjust.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.f2_nco_adjust.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.f2_nco_adjust.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.f2_nco_adjust.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.f2_nco_adjust.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f2_nco_adjust.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f2_nco_adjust.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f2_nco_adjust.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.f1_error.data
        with self.subTest(msg='field: msk_top_regs.f1_error.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.f1_error')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.f1_error.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.f1_error.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.f1_error.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.f1_error.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.f1_error.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f1_error.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f1_error.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f1_error.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.f2_error.data
        with self.subTest(msg='field: msk_top_regs.f2_error.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.f2_error')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.f2_error.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.f2_error.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.f2_error.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.f2_error.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.f2_error.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f2_error.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f2_error.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.f2_error.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Tx_Sync_Ctrl')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.tx_sync_ena.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFE) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.tx_sync_ena.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.tx_sync_ena.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.tx_sync_ena.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.Tx_Sync_Ctrl.tx_sync_ena.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.Tx_Sync_Ctrl.tx_sync_ena.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.Tx_Sync_Ctrl.tx_sync_ena.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFE) | (0x1 & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Sync_Ctrl.tx_sync_force
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_force'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Tx_Sync_Ctrl')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Tx_Sync_Ctrl.tx_sync_force')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.tx_sync_force.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFD) | (random_field_value << 1))
            
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.tx_sync_force.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.tx_sync_force.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Sync_Ctrl.tx_sync_force.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.Tx_Sync_Ctrl.tx_sync_force.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.Tx_Sync_Ctrl.tx_sync_force.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x1+1)
            
            await self.dut.Tx_Sync_Ctrl.tx_sync_force.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFFFFFD) | (0x2 & (random_field_value << 1)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.Tx_Sync_Cnt')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Sync_Cnt.tx_sync_cnt.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFF000000) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.Tx_Sync_Cnt.tx_sync_cnt.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.Tx_Sync_Cnt.tx_sync_cnt.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.Tx_Sync_Cnt.tx_sync_cnt.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.Tx_Sync_Cnt.tx_sync_cnt.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.Tx_Sync_Cnt.tx_sync_cnt.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.Tx_Sync_Cnt.tx_sync_cnt.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF000000) | (0xFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.lowpass_ema_alpha1.alpha
        with self.subTest(msg='field: msk_top_regs.lowpass_ema_alpha1.alpha'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.lowpass_ema_alpha1')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.lowpass_ema_alpha1.alpha')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x3FFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.lowpass_ema_alpha1.alpha.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x3FFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFC0000) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.lowpass_ema_alpha1.alpha.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x3FFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.lowpass_ema_alpha1.alpha.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x3FFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.lowpass_ema_alpha1.alpha.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x3FFFF+1)
            
            await self.dut.lowpass_ema_alpha1.alpha.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFC0000) | (0x3FFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x3FFFF+1)
            
            await self.dut.lowpass_ema_alpha1.alpha.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFC0000) | (0x3FFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFC0000) | (0x3FFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x3FFFF+1)
            
            await self.dut.lowpass_ema_alpha1.alpha.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFC0000) | (0x3FFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.lowpass_ema_alpha2.alpha
        with self.subTest(msg='field: msk_top_regs.lowpass_ema_alpha2.alpha'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.lowpass_ema_alpha2')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.lowpass_ema_alpha2.alpha')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x3FFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.lowpass_ema_alpha2.alpha.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x3FFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFC0000) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.lowpass_ema_alpha2.alpha.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x3FFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.lowpass_ema_alpha2.alpha.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x3FFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.lowpass_ema_alpha2.alpha.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x3FFFF+1)
            
            await self.dut.lowpass_ema_alpha2.alpha.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFC0000) | (0x3FFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x3FFFF+1)
            
            await self.dut.lowpass_ema_alpha2.alpha.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFC0000) | (0x3FFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFFFC0000) | (0x3FFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x3FFFF+1)
            
            await self.dut.lowpass_ema_alpha2.alpha.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFFFC0000) | (0x3FFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.rx_power.data
        with self.subTest(msg='field: msk_top_regs.rx_power.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.rx_power')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.rx_power.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x7FFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_power.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x7FFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFF800000) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.rx_power.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x7FFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.rx_power.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x7FFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_power.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x7FFFFF+1)
            
            await self.dut.rx_power.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF800000) | (0x7FFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x7FFFFF+1)
            
            await self.dut.rx_power.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF800000) | (0x7FFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFF800000) | (0x7FFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x7FFFFF+1)
            
            await self.dut.rx_power.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFF800000) | (0x7FFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.tx_async_fifo_rd_wr_ptr.data
        with self.subTest(msg='field: msk_top_regs.tx_async_fifo_rd_wr_ptr.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.tx_async_fifo_rd_wr_ptr')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.tx_async_fifo_rd_wr_ptr.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.tx_async_fifo_rd_wr_ptr.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.tx_async_fifo_rd_wr_ptr.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.tx_async_fifo_rd_wr_ptr.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.tx_async_fifo_rd_wr_ptr.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.tx_async_fifo_rd_wr_ptr.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.tx_async_fifo_rd_wr_ptr.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.tx_async_fifo_rd_wr_ptr.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.rx_async_fifo_rd_wr_ptr.data
        with self.subTest(msg='field: msk_top_regs.rx_async_fifo_rd_wr_ptr.data'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.rx_async_fifo_rd_wr_ptr')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.rx_async_fifo_rd_wr_ptr.data')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_async_fifo_rd_wr_ptr.data.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x0) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.rx_async_fifo_rd_wr_ptr.data.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.rx_async_fifo_rd_wr_ptr.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFFFFFFFF) >> 0
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_async_fifo_rd_wr_ptr.data.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.rx_async_fifo_rd_wr_ptr.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.rx_async_fifo_rd_wr_ptr.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFFFF+1)
            
            await self.dut.rx_async_fifo_rd_wr_ptr.data.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x0) | (0xFFFFFFFF & (random_field_value << 0)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.rx_frame_sync_status.frame_sync_locked
        with self.subTest(msg='field: msk_top_regs.rx_frame_sync_status.frame_sync_locked'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.rx_frame_sync_status')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.rx_frame_sync_status.frame_sync_locked')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_sync_locked.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFE) | (random_field_value << 0))
            
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_sync_locked.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_sync_locked.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x1) >> 0
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_sync_locked.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # msk_top_regs.rx_frame_sync_status.frame_buffer_overflow
        with self.subTest(msg='field: msk_top_regs.rx_frame_sync_status.frame_buffer_overflow'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.rx_frame_sync_status')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.rx_frame_sync_status.frame_buffer_overflow')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_buffer_overflow.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x1+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFFFFFFFD) | (random_field_value << 1))
            
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_buffer_overflow.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_buffer_overflow.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x2) >> 1
                
            random_field_value = self._reverse_bits(value=random_field_value, number_bits=1)
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_buffer_overflow.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            

        # test access operations (read and/or write) to register:
        # msk_top_regs.rx_frame_sync_status.frames_received
        with self.subTest(msg='field: msk_top_regs.rx_frame_sync_status.frames_received'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.rx_frame_sync_status')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.rx_frame_sync_status.frames_received')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x3FFFFFC) >> 2
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_frame_sync_status.frames_received.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0xFC000003) | (random_field_value << 2))
            
            self.assertEqual(await self.dut.rx_frame_sync_status.frames_received.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x3FFFFFC) >> 2
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.rx_frame_sync_status.frames_received.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0x3FFFFFC) >> 2
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_frame_sync_status.frames_received.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.rx_frame_sync_status.frames_received.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFC000003) | (0x3FFFFFC & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.rx_frame_sync_status.frames_received.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFC000003) | (0x3FFFFFC & (random_field_value << 2)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0xFC000003) | (0x3FFFFFC & (random_field_value << 2)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0xFFFFFF+1)
            
            await self.dut.rx_frame_sync_status.frames_received.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0xFC000003) | (0x3FFFFFC & (random_field_value << 2)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        # test access operations (read and/or write) to register:
        # msk_top_regs.rx_frame_sync_status.frame_sync_errors
        with self.subTest(msg='field: msk_top_regs.rx_frame_sync_status.frame_sync_errors'):
            sim_register = self.sim.register_by_full_name('msk_top_regs.rx_frame_sync_status')
            self.assertIsInstance(sim_register, (Register,MemoryRegister))
            sim_field = self.sim.field_by_full_name('msk_top_regs.rx_frame_sync_status.frame_sync_errors')
            self.assertIsInstance(sim_field, Field)
            register_read_callback = Mock()
            register_write_callback = Mock()
            field_read_callback = Mock()
            field_write_callback = Mock()

            # register read checks
            # update the register value via the backdoor in the simulator
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFC000000) >> 26
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_sync_errors.read(), random_field_value)
            # update the field value via the backdoor in the simulator
            previous_register_value = random_value
            random_field_value = random.randrange(0, 0x3F+1)
            sim_field.value = random_field_value
            self.assertEqual(sim_register.value, (previous_register_value & 0x3FFFFFF) | (random_field_value << 26))
            
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_sync_errors.read(), random_field_value)
            # hook up the call backs to check they work correctly
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFC000000) >> 26
                
            
            sim_register.value = random_value
            sim_register.read_callback = register_read_callback
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = field_read_callback
            sim_field.write_callback = field_write_callback
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_sync_errors.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_called_once_with(value=random_value)
            field_write_callback.assert_not_called()
            field_read_callback.assert_called_once_with(value=random_field_value)
            
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.read_callback = None
            sim_register.write_callback = None
            sim_field.read_callback = None
            sim_field.write_callback = None
            random_value = random.randrange(0, 0xFFFFFFFF+1)
            random_field_value = (random_value & 0xFC000000) >> 26
                
            
            sim_register.value = random_value
            self.assertEqual(await self.dut.rx_frame_sync_status.frame_sync_errors.read(), random_field_value)
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

            # register write checks
            # update the register value via the backdoor in the simulator, then perform a field
            # write and make sure it is updated
            inital_reg_random_value = random.randrange(0, 0xFFFFFFFF+1)
            sim_register.value = inital_reg_random_value
            
            random_field_value = random.randrange(0, 0x3F+1)
            
            await self.dut.rx_frame_sync_status.frame_sync_errors.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x3FFFFFF) | (0xFC000000 & (random_field_value << 26)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # hook up the call backs
            sim_register.read_callback = None
            sim_register.write_callback = register_write_callback
            sim_field.read_callback = None
            sim_field.write_callback = field_write_callback
            random_field_value = random.randrange(0, 0x3F+1)
            
            await self.dut.rx_frame_sync_status.frame_sync_errors.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x3FFFFFF) | (0xFC000000 & (random_field_value << 26)))
            register_write_callback.assert_called_once_with(value=(reg_random_value & 0x3FFFFFF) | (0xFC000000 & (random_field_value << 26)))
            field_write_callback.assert_called_once_with(value=random_field_value)
            
            register_read_callback.assert_not_called()
            field_read_callback.assert_not_called()
            reg_random_value = sim_register.value
            # revert the callbacks and check again
            register_write_callback.reset_mock()
            register_read_callback.reset_mock()
            field_write_callback.reset_mock()
            field_read_callback.reset_mock()
            sim_register.write_callback = None
            sim_field.write_callback = None
            random_field_value = random.randrange(0, 0x3F+1)
            
            await self.dut.rx_frame_sync_status.frame_sync_errors.write(random_field_value) # type: ignore[arg-type]
            self.assertEqual(sim_register.value, (inital_reg_random_value & 0x3FFFFFF) | (0xFC000000 & (random_field_value << 26)))
            
            register_write_callback.assert_not_called()
            register_read_callback.assert_not_called()
            field_write_callback.assert_not_called()
            field_read_callback.assert_not_called()
            

        


    



class msk_top_regs_block_access(msk_top_regs_SimTestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    

if __name__ == '__main__':

    if sys.version_info < (3, 8):
        asynctest.main()
    else:
        unittest.main()




