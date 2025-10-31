


"""
Unit Tests for the msk_top_regs register model Python Wrapper

This code was generated from the PeakRDL-python package version 1.4.0
"""
from typing import Union,Iterable
from array import array as Array

import sys
import asyncio
import unittest
from unittest.mock import patch, call

import random
from itertools import combinations, chain
import math


from ..lib import RegisterWriteVerifyError, UnsupportedWidthError

from ..reg_model.msk_top_regs import msk_top_regs_cls




from ..lib import FieldAsyncReadOnly, FieldAsyncWriteOnly, FieldAsyncReadWrite
from ..lib import WritableAsyncRegister, ReadableAsyncRegister
from ..lib import RegAsyncReadWrite, RegAsyncReadOnly, RegAsyncWriteOnly
from ..lib import RegAsyncReadWriteArray, RegAsyncReadOnlyArray, RegAsyncWriteOnlyArray
from ..lib import MemoryAsyncReadOnly, MemoryAsyncWriteOnly, MemoryAsyncReadWrite
from ..lib import MemoryAsyncReadOnlyArray, MemoryAsyncWriteOnlyArray, MemoryAsyncReadWriteArray
from ..lib import AsyncAddressMap, AsyncRegFile
from ..lib import AsyncAddressMapArray, AsyncRegFileArray
from ..lib import AsyncMemory



from ..lib import Field
from ..lib import Reg

from ..lib import SystemRDLEnum, SystemRDLEnumEntry


from ._msk_top_regs_test_base import msk_top_regs_TestCase, msk_top_regs_TestCase_BlockAccess, msk_top_regs_TestCase_AltBlockAccess
from ._msk_top_regs_test_base import __name__ as base_name
from ._msk_top_regs_test_base import random_enum_reg_value



class msk_top_regs_single_access(msk_top_regs_TestCase): # type: ignore[valid-type,misc]

    def test_inst_name(self)  -> None:
        """
        Walk the address map and check the inst name has been correctly populated
        """
        with self.subTest(msg='node: msk_top_regs.Hash_ID_Low'):
            self.assertEqual(self.dut.Hash_ID_Low.inst_name, 'Hash_ID_Low') # type: ignore[union-attr]
            self.assertEqual(self.dut.Hash_ID_Low.full_inst_name, 'msk_top_regs.Hash_ID_Low')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Hash_ID_High'):
            self.assertEqual(self.dut.Hash_ID_High.inst_name, 'Hash_ID_High') # type: ignore[union-attr]
            self.assertEqual(self.dut.Hash_ID_High.full_inst_name, 'msk_top_regs.Hash_ID_High')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Init'):
            self.assertEqual(self.dut.MSK_Init.inst_name, 'MSK_Init') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Init.full_inst_name, 'msk_top_regs.MSK_Init')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control'):
            self.assertEqual(self.dut.MSK_Control.inst_name, 'MSK_Control') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Control.full_inst_name, 'msk_top_regs.MSK_Control')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Status'):
            self.assertEqual(self.dut.MSK_Status.inst_name, 'MSK_Status') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Status.full_inst_name, 'msk_top_regs.MSK_Status')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Fb_FreqWord'):
            self.assertEqual(self.dut.Fb_FreqWord.inst_name, 'Fb_FreqWord') # type: ignore[union-attr]
            self.assertEqual(self.dut.Fb_FreqWord.full_inst_name, 'msk_top_regs.Fb_FreqWord')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.TX_F1_FreqWord'):
            self.assertEqual(self.dut.TX_F1_FreqWord.inst_name, 'TX_F1_FreqWord') # type: ignore[union-attr]
            self.assertEqual(self.dut.TX_F1_FreqWord.full_inst_name, 'msk_top_regs.TX_F1_FreqWord')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.TX_F2_FreqWord'):
            self.assertEqual(self.dut.TX_F2_FreqWord.inst_name, 'TX_F2_FreqWord') # type: ignore[union-attr]
            self.assertEqual(self.dut.TX_F2_FreqWord.full_inst_name, 'msk_top_regs.TX_F2_FreqWord')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.RX_F1_FreqWord'):
            self.assertEqual(self.dut.RX_F1_FreqWord.inst_name, 'RX_F1_FreqWord') # type: ignore[union-attr]
            self.assertEqual(self.dut.RX_F1_FreqWord.full_inst_name, 'msk_top_regs.RX_F1_FreqWord')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.RX_F2_FreqWord'):
            self.assertEqual(self.dut.RX_F2_FreqWord.inst_name, 'RX_F2_FreqWord') # type: ignore[union-attr]
            self.assertEqual(self.dut.RX_F2_FreqWord.full_inst_name, 'msk_top_regs.RX_F2_FreqWord')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_0'):
            self.assertEqual(self.dut.LPF_Config_0.inst_name, 'LPF_Config_0') # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_0.full_inst_name, 'msk_top_regs.LPF_Config_0')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_1'):
            self.assertEqual(self.dut.LPF_Config_1.inst_name, 'LPF_Config_1') # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_1.full_inst_name, 'msk_top_regs.LPF_Config_1')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Data_Width'):
            self.assertEqual(self.dut.Tx_Data_Width.inst_name, 'Tx_Data_Width') # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Data_Width.full_inst_name, 'msk_top_regs.Tx_Data_Width')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Data_Width'):
            self.assertEqual(self.dut.Rx_Data_Width.inst_name, 'Rx_Data_Width') # type: ignore[union-attr]
            self.assertEqual(self.dut.Rx_Data_Width.full_inst_name, 'msk_top_regs.Rx_Data_Width')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control'):
            self.assertEqual(self.dut.PRBS_Control.inst_name, 'PRBS_Control') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Control.full_inst_name, 'msk_top_regs.PRBS_Control')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Initial_State'):
            self.assertEqual(self.dut.PRBS_Initial_State.inst_name, 'PRBS_Initial_State') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Initial_State.full_inst_name, 'msk_top_regs.PRBS_Initial_State')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Polynomial'):
            self.assertEqual(self.dut.PRBS_Polynomial.inst_name, 'PRBS_Polynomial') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Polynomial.full_inst_name, 'msk_top_regs.PRBS_Polynomial')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Error_Mask'):
            self.assertEqual(self.dut.PRBS_Error_Mask.inst_name, 'PRBS_Error_Mask') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Error_Mask.full_inst_name, 'msk_top_regs.PRBS_Error_Mask')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard'):
            self.assertEqual(self.dut.Rx_Sample_Discard.inst_name, 'Rx_Sample_Discard') # type: ignore[union-attr]
            self.assertEqual(self.dut.Rx_Sample_Discard.full_inst_name, 'msk_top_regs.Rx_Sample_Discard')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_2'):
            self.assertEqual(self.dut.LPF_Config_2.inst_name, 'LPF_Config_2') # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_2.full_inst_name, 'msk_top_regs.LPF_Config_2')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl'):
            self.assertEqual(self.dut.Tx_Sync_Ctrl.inst_name, 'Tx_Sync_Ctrl') # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Ctrl.full_inst_name, 'msk_top_regs.Tx_Sync_Ctrl')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Cnt'):
            self.assertEqual(self.dut.Tx_Sync_Cnt.inst_name, 'Tx_Sync_Cnt') # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Cnt.full_inst_name, 'msk_top_regs.Tx_Sync_Cnt')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha1'):
            self.assertEqual(self.dut.lowpass_ema_alpha1.inst_name, 'lowpass_ema_alpha1') # type: ignore[union-attr]
            self.assertEqual(self.dut.lowpass_ema_alpha1.full_inst_name, 'msk_top_regs.lowpass_ema_alpha1')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha2'):
            self.assertEqual(self.dut.lowpass_ema_alpha2.inst_name, 'lowpass_ema_alpha2') # type: ignore[union-attr]
            self.assertEqual(self.dut.lowpass_ema_alpha2.full_inst_name, 'msk_top_regs.lowpass_ema_alpha2')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Hash_ID_Low.hash_id_lo'):
            self.assertEqual(self.dut.Hash_ID_Low.hash_id_lo.inst_name, 'hash_id_lo') # type: ignore[union-attr]
            self.assertEqual(self.dut.Hash_ID_Low.hash_id_lo.full_inst_name, 'msk_top_regs.Hash_ID_Low.hash_id_lo')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Hash_ID_High.hash_id_hi'):
            self.assertEqual(self.dut.Hash_ID_High.hash_id_hi.inst_name, 'hash_id_hi') # type: ignore[union-attr]
            self.assertEqual(self.dut.Hash_ID_High.hash_id_hi.full_inst_name, 'msk_top_regs.Hash_ID_High.hash_id_hi')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Init.txrxinit'):
            self.assertEqual(self.dut.MSK_Init.txrxinit.inst_name, 'txrxinit') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Init.txrxinit.full_inst_name, 'msk_top_regs.MSK_Init.txrxinit')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Init.txinit'):
            self.assertEqual(self.dut.MSK_Init.txinit.inst_name, 'txinit') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Init.txinit.full_inst_name, 'msk_top_regs.MSK_Init.txinit')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Init.rxinit'):
            self.assertEqual(self.dut.MSK_Init.rxinit.inst_name, 'rxinit') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Init.rxinit.full_inst_name, 'msk_top_regs.MSK_Init.rxinit')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control.ptt'):
            self.assertEqual(self.dut.MSK_Control.ptt.inst_name, 'ptt') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Control.ptt.full_inst_name, 'msk_top_regs.MSK_Control.ptt')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control.loopback_ena'):
            self.assertEqual(self.dut.MSK_Control.loopback_ena.inst_name, 'loopback_ena') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Control.loopback_ena.full_inst_name, 'msk_top_regs.MSK_Control.loopback_ena')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control.rx_invert'):
            self.assertEqual(self.dut.MSK_Control.rx_invert.inst_name, 'rx_invert') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Control.rx_invert.full_inst_name, 'msk_top_regs.MSK_Control.rx_invert')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control.clear_counts'):
            self.assertEqual(self.dut.MSK_Control.clear_counts.inst_name, 'clear_counts') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Control.clear_counts.full_inst_name, 'msk_top_regs.MSK_Control.clear_counts')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control.diff_encoder_loopback'):
            self.assertEqual(self.dut.MSK_Control.diff_encoder_loopback.inst_name, 'diff_encoder_loopback') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Control.diff_encoder_loopback.full_inst_name, 'msk_top_regs.MSK_Control.diff_encoder_loopback')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Status.demod_sync_lock'):
            self.assertEqual(self.dut.MSK_Status.demod_sync_lock.inst_name, 'demod_sync_lock') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Status.demod_sync_lock.full_inst_name, 'msk_top_regs.MSK_Status.demod_sync_lock')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Status.tx_enable'):
            self.assertEqual(self.dut.MSK_Status.tx_enable.inst_name, 'tx_enable') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Status.tx_enable.full_inst_name, 'msk_top_regs.MSK_Status.tx_enable')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Status.rx_enable'):
            self.assertEqual(self.dut.MSK_Status.rx_enable.inst_name, 'rx_enable') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Status.rx_enable.full_inst_name, 'msk_top_regs.MSK_Status.rx_enable')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Status.tx_axis_valid'):
            self.assertEqual(self.dut.MSK_Status.tx_axis_valid.inst_name, 'tx_axis_valid') # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Status.tx_axis_valid.full_inst_name, 'msk_top_regs.MSK_Status.tx_axis_valid')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Fb_FreqWord.config_data'):
            self.assertEqual(self.dut.Fb_FreqWord.config_data.inst_name, 'config_data') # type: ignore[union-attr]
            self.assertEqual(self.dut.Fb_FreqWord.config_data.full_inst_name, 'msk_top_regs.Fb_FreqWord.config_data')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.TX_F1_FreqWord.config_data'):
            self.assertEqual(self.dut.TX_F1_FreqWord.config_data.inst_name, 'config_data') # type: ignore[union-attr]
            self.assertEqual(self.dut.TX_F1_FreqWord.config_data.full_inst_name, 'msk_top_regs.TX_F1_FreqWord.config_data')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.TX_F2_FreqWord.config_data'):
            self.assertEqual(self.dut.TX_F2_FreqWord.config_data.inst_name, 'config_data') # type: ignore[union-attr]
            self.assertEqual(self.dut.TX_F2_FreqWord.config_data.full_inst_name, 'msk_top_regs.TX_F2_FreqWord.config_data')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.RX_F1_FreqWord.config_data'):
            self.assertEqual(self.dut.RX_F1_FreqWord.config_data.inst_name, 'config_data') # type: ignore[union-attr]
            self.assertEqual(self.dut.RX_F1_FreqWord.config_data.full_inst_name, 'msk_top_regs.RX_F1_FreqWord.config_data')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.RX_F2_FreqWord.config_data'):
            self.assertEqual(self.dut.RX_F2_FreqWord.config_data.inst_name, 'config_data') # type: ignore[union-attr]
            self.assertEqual(self.dut.RX_F2_FreqWord.config_data.full_inst_name, 'msk_top_regs.RX_F2_FreqWord.config_data')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_freeze'):
            self.assertEqual(self.dut.LPF_Config_0.lpf_freeze.inst_name, 'lpf_freeze') # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_0.lpf_freeze.full_inst_name, 'msk_top_regs.LPF_Config_0.lpf_freeze')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_zero'):
            self.assertEqual(self.dut.LPF_Config_0.lpf_zero.inst_name, 'lpf_zero') # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_0.lpf_zero.full_inst_name, 'msk_top_regs.LPF_Config_0.lpf_zero')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.prbs_reserved'):
            self.assertEqual(self.dut.LPF_Config_0.prbs_reserved.inst_name, 'prbs_reserved') # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_0.prbs_reserved.full_inst_name, 'msk_top_regs.LPF_Config_0.prbs_reserved')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_alpha'):
            self.assertEqual(self.dut.LPF_Config_0.lpf_alpha.inst_name, 'lpf_alpha') # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_0.lpf_alpha.full_inst_name, 'msk_top_regs.LPF_Config_0.lpf_alpha')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_1.i_gain'):
            self.assertEqual(self.dut.LPF_Config_1.i_gain.inst_name, 'i_gain') # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_1.i_gain.full_inst_name, 'msk_top_regs.LPF_Config_1.i_gain')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_1.i_shift'):
            self.assertEqual(self.dut.LPF_Config_1.i_shift.inst_name, 'i_shift') # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_1.i_shift.full_inst_name, 'msk_top_regs.LPF_Config_1.i_shift')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Data_Width.data_width'):
            self.assertEqual(self.dut.Tx_Data_Width.data_width.inst_name, 'data_width') # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Data_Width.data_width.full_inst_name, 'msk_top_regs.Tx_Data_Width.data_width')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Data_Width.data_width'):
            self.assertEqual(self.dut.Rx_Data_Width.data_width.inst_name, 'data_width') # type: ignore[union-attr]
            self.assertEqual(self.dut.Rx_Data_Width.data_width.full_inst_name, 'msk_top_regs.Rx_Data_Width.data_width')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_sel'):
            self.assertEqual(self.dut.PRBS_Control.prbs_sel.inst_name, 'prbs_sel') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Control.prbs_sel.full_inst_name, 'msk_top_regs.PRBS_Control.prbs_sel')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_error_insert'):
            self.assertEqual(self.dut.PRBS_Control.prbs_error_insert.inst_name, 'prbs_error_insert') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Control.prbs_error_insert.full_inst_name, 'msk_top_regs.PRBS_Control.prbs_error_insert')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_clear'):
            self.assertEqual(self.dut.PRBS_Control.prbs_clear.inst_name, 'prbs_clear') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Control.prbs_clear.full_inst_name, 'msk_top_regs.PRBS_Control.prbs_clear')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_manual_sync'):
            self.assertEqual(self.dut.PRBS_Control.prbs_manual_sync.inst_name, 'prbs_manual_sync') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Control.prbs_manual_sync.full_inst_name, 'msk_top_regs.PRBS_Control.prbs_manual_sync')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_reserved'):
            self.assertEqual(self.dut.PRBS_Control.prbs_reserved.inst_name, 'prbs_reserved') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Control.prbs_reserved.full_inst_name, 'msk_top_regs.PRBS_Control.prbs_reserved')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_sync_threshold'):
            self.assertEqual(self.dut.PRBS_Control.prbs_sync_threshold.inst_name, 'prbs_sync_threshold') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Control.prbs_sync_threshold.full_inst_name, 'msk_top_regs.PRBS_Control.prbs_sync_threshold')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Initial_State.config_data'):
            self.assertEqual(self.dut.PRBS_Initial_State.config_data.inst_name, 'config_data') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Initial_State.config_data.full_inst_name, 'msk_top_regs.PRBS_Initial_State.config_data')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Polynomial.config_data'):
            self.assertEqual(self.dut.PRBS_Polynomial.config_data.inst_name, 'config_data') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Polynomial.config_data.full_inst_name, 'msk_top_regs.PRBS_Polynomial.config_data')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Error_Mask.config_data'):
            self.assertEqual(self.dut.PRBS_Error_Mask.config_data.inst_name, 'config_data') # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Error_Mask.config_data.full_inst_name, 'msk_top_regs.PRBS_Error_Mask.config_data')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard.rx_sample_discard'):
            self.assertEqual(self.dut.Rx_Sample_Discard.rx_sample_discard.inst_name, 'rx_sample_discard') # type: ignore[union-attr]
            self.assertEqual(self.dut.Rx_Sample_Discard.rx_sample_discard.full_inst_name, 'msk_top_regs.Rx_Sample_Discard.rx_sample_discard')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard.rx_nco_discard'):
            self.assertEqual(self.dut.Rx_Sample_Discard.rx_nco_discard.inst_name, 'rx_nco_discard') # type: ignore[union-attr]
            self.assertEqual(self.dut.Rx_Sample_Discard.rx_nco_discard.full_inst_name, 'msk_top_regs.Rx_Sample_Discard.rx_nco_discard')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_2.p_gain'):
            self.assertEqual(self.dut.LPF_Config_2.p_gain.inst_name, 'p_gain') # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_2.p_gain.full_inst_name, 'msk_top_regs.LPF_Config_2.p_gain')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_2.p_shift'):
            self.assertEqual(self.dut.LPF_Config_2.p_shift.inst_name, 'p_shift') # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_2.p_shift.full_inst_name, 'msk_top_regs.LPF_Config_2.p_shift')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena'):
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_ena.inst_name, 'tx_sync_ena') # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_ena.full_inst_name, 'msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_force'):
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_force.inst_name, 'tx_sync_force') # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_force.full_inst_name, 'msk_top_regs.Tx_Sync_Ctrl.tx_sync_force')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f1'):
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_f1.inst_name, 'tx_sync_f1') # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_f1.full_inst_name, 'msk_top_regs.Tx_Sync_Ctrl.tx_sync_f1')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f2'):
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_f2.inst_name, 'tx_sync_f2') # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_f2.full_inst_name, 'msk_top_regs.Tx_Sync_Ctrl.tx_sync_f2')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt'):
            self.assertEqual(self.dut.Tx_Sync_Cnt.tx_sync_cnt.inst_name, 'tx_sync_cnt') # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Cnt.tx_sync_cnt.full_inst_name, 'msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha1.alpha'):
            self.assertEqual(self.dut.lowpass_ema_alpha1.alpha.inst_name, 'alpha') # type: ignore[union-attr]
            self.assertEqual(self.dut.lowpass_ema_alpha1.alpha.full_inst_name, 'msk_top_regs.lowpass_ema_alpha1.alpha')  # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha2.alpha'):
            self.assertEqual(self.dut.lowpass_ema_alpha2.alpha.inst_name, 'alpha') # type: ignore[union-attr]
            self.assertEqual(self.dut.lowpass_ema_alpha2.alpha.full_inst_name, 'msk_top_regs.lowpass_ema_alpha2.alpha')  # type: ignore[union-attr]
        

    def test_name_property(self)  -> None:
        """
        Walk the address map and check the name property has been correctly populated
        """
        with self.subTest(msg='node: msk_top_regs.Hash_ID_Low'):
            
                
            self.assertEqual(self.dut.Hash_ID_Low.rdl_name, "Pluto MSK FPGA Hash ID - Lower 32-bits") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Hash_ID_High'):
            
                
            self.assertEqual(self.dut.Hash_ID_High.rdl_name, "Pluto MSK FPGA Hash ID - Upper 32-bits") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Init'):
            
                
            self.assertEqual(self.dut.MSK_Init.rdl_name, "MSK Modem Initialization Control") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control'):
            
                
            self.assertEqual(self.dut.MSK_Control.rdl_name, "MSK Modem Control") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Status'):
            
                
            self.assertEqual(self.dut.MSK_Status.rdl_name, "MSK Modem Status 0") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Fb_FreqWord'):
            
                
            self.assertEqual(self.dut.Fb_FreqWord.rdl_name, "Bitrate NCO Frequency Control Word") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.TX_F1_FreqWord'):
            
                
            self.assertEqual(self.dut.TX_F1_FreqWord.rdl_name, "Tx F1 NCO Frequency Control Word") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.TX_F2_FreqWord'):
            
                
            self.assertEqual(self.dut.TX_F2_FreqWord.rdl_name, "Tx F2 NCO Frequency Control Word") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.RX_F1_FreqWord'):
            
                
            self.assertEqual(self.dut.RX_F1_FreqWord.rdl_name, "Rx F1 NCO Frequency Control Word") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.RX_F2_FreqWord'):
            
                
            self.assertEqual(self.dut.RX_F2_FreqWord.rdl_name, "Rx F2 NCO Frequency Control Word") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_0'):
            
                
            self.assertEqual(self.dut.LPF_Config_0.rdl_name, "PI Controller Configuration and Low-pass Filter Configuration") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_1'):
            
                
            self.assertEqual(self.dut.LPF_Config_1.rdl_name, "PI Controller Configuration Configuration Register 1") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Data_Width'):
            
                
            self.assertEqual(self.dut.Tx_Data_Width.rdl_name, "Modem Tx Input Data Width") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Rx_Data_Width'):
            
                
            self.assertEqual(self.dut.Rx_Data_Width.rdl_name, "Modem Rx Output Data Width") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control'):
            
                
            self.assertEqual(self.dut.PRBS_Control.rdl_name, "PRBS Control 0") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Initial_State'):
            
                
            self.assertEqual(self.dut.PRBS_Initial_State.rdl_name, "PRBS Control 1") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Polynomial'):
            
                
            self.assertEqual(self.dut.PRBS_Polynomial.rdl_name, "PRBS Control 2") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Error_Mask'):
            
                
            self.assertEqual(self.dut.PRBS_Error_Mask.rdl_name, "PRBS Control 3") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard'):
            
                
            self.assertEqual(self.dut.Rx_Sample_Discard.rdl_name, "Rx Sample Discard") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_2'):
            
                
            self.assertEqual(self.dut.LPF_Config_2.rdl_name, "PI Controller Configuration Configuration Register 2") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Ctrl.rdl_name, "Transmitter Sync Control") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Cnt'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Cnt.rdl_name, "Transmitter Sync Duration") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha1'):
            
                
            self.assertEqual(self.dut.lowpass_ema_alpha1.rdl_name, "Exponential Moving Average Alpha") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha2'):
            
                
            self.assertEqual(self.dut.lowpass_ema_alpha2.rdl_name, "Exponential Moving Average Alpha") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Hash_ID_Low.hash_id_lo'):
            
                
            self.assertEqual(self.dut.Hash_ID_Low.hash_id_lo.rdl_name, "Hash ID Lower 32-bits") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Hash_ID_High.hash_id_hi'):
            
                
            self.assertEqual(self.dut.Hash_ID_High.hash_id_hi.rdl_name, "Hash ID Upper 32-bits") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Init.txrxinit'):
            
                
            self.assertEqual(self.dut.MSK_Init.txrxinit.rdl_name, "Tx/Rx Init Enable") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Init.txinit'):
            
                
            self.assertEqual(self.dut.MSK_Init.txinit.rdl_name, "Tx Init Enable") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Init.rxinit'):
            
                
            self.assertEqual(self.dut.MSK_Init.rxinit.rdl_name, "Rx Init Enable") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control.ptt'):
            
                
            self.assertEqual(self.dut.MSK_Control.ptt.rdl_name, "Push-to-Talk Enable") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control.loopback_ena'):
            
                
            self.assertEqual(self.dut.MSK_Control.loopback_ena.rdl_name, "Modem Digital Tx -\u003e Rx Loopback Enable") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control.rx_invert'):
            
                
            self.assertEqual(self.dut.MSK_Control.rx_invert.rdl_name, "Rx Data Invert Enable") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control.clear_counts'):
            
                
            self.assertEqual(self.dut.MSK_Control.clear_counts.rdl_name, "Clear Status Counters") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control.diff_encoder_loopback'):
            
                
            self.assertEqual(self.dut.MSK_Control.diff_encoder_loopback.rdl_name, "Differential Encoder -\u003e Decoder Loopback Enable") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Status.demod_sync_lock'):
            
                
            self.assertEqual(self.dut.MSK_Status.demod_sync_lock.rdl_name, "Demodulator Sync Status") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Status.tx_enable'):
            
                
            self.assertEqual(self.dut.MSK_Status.tx_enable.rdl_name, "AD9363 DAC Interface Tx Enable Input Active") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Status.rx_enable'):
            
                
            self.assertEqual(self.dut.MSK_Status.rx_enable.rdl_name, "AD9363 ADC Interface Rx Enable Input Active") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Status.tx_axis_valid'):
            
                
            self.assertEqual(self.dut.MSK_Status.tx_axis_valid.rdl_name, "Tx S_AXIS_VALID") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Fb_FreqWord.config_data'):
            
                
            self.assertEqual(self.dut.Fb_FreqWord.config_data.rdl_name, "Frequency Control Word") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.TX_F1_FreqWord.config_data'):
            
                
            self.assertEqual(self.dut.TX_F1_FreqWord.config_data.rdl_name, "Frequency Control Word") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.TX_F2_FreqWord.config_data'):
            
                
            self.assertEqual(self.dut.TX_F2_FreqWord.config_data.rdl_name, "Frequency Control Word") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.RX_F1_FreqWord.config_data'):
            
                
            self.assertEqual(self.dut.RX_F1_FreqWord.config_data.rdl_name, "Frequency Control Word") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.RX_F2_FreqWord.config_data'):
            
                
            self.assertEqual(self.dut.RX_F2_FreqWord.config_data.rdl_name, "Frequency Control Word") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_freeze'):
            
                
            self.assertEqual(self.dut.LPF_Config_0.lpf_freeze.rdl_name, "Freeze the accumulator\u0027s current value") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_zero'):
            
                
            self.assertEqual(self.dut.LPF_Config_0.lpf_zero.rdl_name, "Hold the PI Accumulator at zero") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.prbs_reserved'):
            
                
            self.assertEqual(self.dut.LPF_Config_0.prbs_reserved.rdl_name, "Reserved") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_alpha'):
            
                
            self.assertEqual(self.dut.LPF_Config_0.lpf_alpha.rdl_name, "Lowpass IIR filter alpha") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_1.i_gain'):
            
                
            self.assertEqual(self.dut.LPF_Config_1.i_gain.rdl_name, "Integral Gain Value") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_1.i_shift'):
            
                
            self.assertEqual(self.dut.LPF_Config_1.i_shift.rdl_name, "Integral Gain Bit Shift") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Data_Width.data_width'):
            
                
            self.assertEqual(self.dut.Tx_Data_Width.data_width.rdl_name, "Modem input/output data width") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Rx_Data_Width.data_width'):
            
                
            self.assertEqual(self.dut.Rx_Data_Width.data_width.rdl_name, "Modem input/output data width") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_sel'):
            
                
            self.assertEqual(self.dut.PRBS_Control.prbs_sel.rdl_name, "PRBS Data Select") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_error_insert'):
            
                
            self.assertEqual(self.dut.PRBS_Control.prbs_error_insert.rdl_name, "PRBS Error Insert") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_clear'):
            
                
            self.assertEqual(self.dut.PRBS_Control.prbs_clear.rdl_name, "PRBS Clear Counters") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_manual_sync'):
            
                
            self.assertEqual(self.dut.PRBS_Control.prbs_manual_sync.rdl_name, "PRBS Manual Sync") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_reserved'):
            
                
            self.assertEqual(self.dut.PRBS_Control.prbs_reserved.rdl_name, "Reserved") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_sync_threshold'):
            
                
            self.assertEqual(self.dut.PRBS_Control.prbs_sync_threshold.rdl_name, "PRBS Auto Sync Threshold") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Initial_State.config_data'):
            
                
            self.assertEqual(self.dut.PRBS_Initial_State.config_data.rdl_name, "PRBS Seed") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Polynomial.config_data'):
            
                
            self.assertEqual(self.dut.PRBS_Polynomial.config_data.rdl_name, "PRBS Polynomial") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Error_Mask.config_data'):
            
                
            self.assertEqual(self.dut.PRBS_Error_Mask.config_data.rdl_name, "PRBS Error Mask") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard.rx_sample_discard'):
            
                
            self.assertEqual(self.dut.Rx_Sample_Discard.rx_sample_discard.rdl_name, "Rx Sample Discard Value") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard.rx_nco_discard'):
            
                
            self.assertEqual(self.dut.Rx_Sample_Discard.rx_nco_discard.rdl_name, "Rx NCO Sample Discard Value") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_2.p_gain'):
            
                
            self.assertEqual(self.dut.LPF_Config_2.p_gain.rdl_name, "Proportional Gain Value") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_2.p_shift'):
            
                
            self.assertEqual(self.dut.LPF_Config_2.p_shift.rdl_name, "Proportional Gain Bit Shift") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_ena.rdl_name, "Tx Sync Enable") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_force'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_force.rdl_name, "Tx Sync Force") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f1'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_f1.rdl_name, "Tx F1 Sync Enable") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f2'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_f2.rdl_name, "Tx F2 Sync Enable") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Cnt.tx_sync_cnt.rdl_name, "Tx sync duration") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha1.alpha'):
            
                
            self.assertEqual(self.dut.lowpass_ema_alpha1.alpha.rdl_name, "EMA alpha") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha2.alpha'):
            
                
            self.assertEqual(self.dut.lowpass_ema_alpha2.alpha.rdl_name, "EMA alpha") # type: ignore[union-attr]
                
            

        

    def test_desc(self)  -> None:
        """
        Walk the address map and check the desc property has been correctly populated
        """
        with self.subTest(msg='node: msk_top_regs.Hash_ID_Low'):
            
                
            self.assertIsNone(self.dut.Hash_ID_Low.rdl_desc)  # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Hash_ID_High'):
            
                
            self.assertIsNone(self.dut.Hash_ID_High.rdl_desc)  # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Init'):
            
                
            self.assertEqual(self.dut.MSK_Init.rdl_desc, "Synchronous initialization of MSK Modem functions, does not affect configuration registers.") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control'):
            
                
            self.assertEqual(self.dut.MSK_Control.rdl_desc, "MSK Modem Configuration and Control") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Status'):
            
                
            self.assertEqual(self.dut.MSK_Status.rdl_desc, "Modem status bits") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Fb_FreqWord'):
            
                
            self.assertEqual(self.dut.Fb_FreqWord.rdl_desc, "Set Modem Data Rate") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.TX_F1_FreqWord'):
            
                
            self.assertEqual(self.dut.TX_F1_FreqWord.rdl_desc, "Set Modulator F1 Frequency") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.TX_F2_FreqWord'):
            
                
            self.assertEqual(self.dut.TX_F2_FreqWord.rdl_desc, "Set Modulator F2 Frequency") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.RX_F1_FreqWord'):
            
                
            self.assertEqual(self.dut.RX_F1_FreqWord.rdl_desc, "Set Demodulator F1 Frequency") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.RX_F2_FreqWord'):
            
                
            self.assertEqual(self.dut.RX_F2_FreqWord.rdl_desc, "Set Demodulator F2 Frequency") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_0'):
            
                
            self.assertEqual(self.dut.LPF_Config_0.rdl_desc, "Configure PI controller and low-pass filter") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_1'):
            
                
            self.assertEqual(self.dut.LPF_Config_1.rdl_desc, "Configures PI Controller I-gain and divisor") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Data_Width'):
            
                
            self.assertEqual(self.dut.Tx_Data_Width.rdl_desc, "Set the parallel data width of the parallel-to-serial converter") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Rx_Data_Width'):
            
                
            self.assertEqual(self.dut.Rx_Data_Width.rdl_desc, "Set the parallel data width of the serial-to-parallel converter") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control'):
            
                
            self.assertEqual(self.dut.PRBS_Control.rdl_desc, "Configures operation of the PRBS Generator and Monitor") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Initial_State'):
            
                
            self.assertEqual(self.dut.PRBS_Initial_State.rdl_desc, "PRBS Initial State") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Polynomial'):
            
                
            self.assertEqual(self.dut.PRBS_Polynomial.rdl_desc, "PRBS Polynomial") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Error_Mask'):
            
                
            self.assertEqual(self.dut.PRBS_Error_Mask.rdl_desc, "PRBS Error Mask") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard'):
            
                
            self.assertEqual(self.dut.Rx_Sample_Discard.rdl_desc, "Configure samples discard operation for demodulator") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_2'):
            
                
            self.assertEqual(self.dut.LPF_Config_2.rdl_desc, "Configures PI Controller I-gain and divisor") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Ctrl.rdl_desc, "Provides control bits for generation of transmitter synchronization patterns") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Cnt'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Cnt.rdl_desc, "Sets the duration of the synchronization tones when enabled") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha1'):
            
                
            self.assertEqual(self.dut.lowpass_ema_alpha1.rdl_desc, "Sets the alpha for the EMA") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha2'):
            
                
            self.assertEqual(self.dut.lowpass_ema_alpha2.rdl_desc, "Sets the alpha for the EMA") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Hash_ID_Low.hash_id_lo'):
            
                
            self.assertEqual(self.dut.Hash_ID_Low.hash_id_lo.rdl_desc, "Lower 32-bits of Pluto MSK FPGA Hash ID") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Hash_ID_High.hash_id_hi'):
            
                
            self.assertEqual(self.dut.Hash_ID_High.hash_id_hi.rdl_desc, "Upper 32-bits of Pluto MSK FPGA Hash ID") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Init.txrxinit'):
            
                
            self.assertEqual(self.dut.MSK_Init.txrxinit.rdl_desc, "0 -\u003e Normal modem operation \n1 -\u003e Initialize Tx and Rx") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Init.txinit'):
            
                
            self.assertEqual(self.dut.MSK_Init.txinit.rdl_desc, "0 -\u003e Normal Tx operation \n1 -\u003e Initialize Tx") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Init.rxinit'):
            
                
            self.assertEqual(self.dut.MSK_Init.rxinit.rdl_desc, "0 -\u003e Normal Rx operation \n1 -\u003e Initialize Rx") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control.ptt'):
            
                
            self.assertEqual(self.dut.MSK_Control.ptt.rdl_desc, "0 -\u003e PTT Disabled\n1 -\u003e PTT Enabled") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control.loopback_ena'):
            
                
            self.assertEqual(self.dut.MSK_Control.loopback_ena.rdl_desc, "0 -\u003e Modem loopback disabled\n1 -\u003e Modem loopback enabled") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control.rx_invert'):
            
                
            self.assertEqual(self.dut.MSK_Control.rx_invert.rdl_desc, "0 -\u003e Rx data normal\n1 -\u003e Rx data inverted") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control.clear_counts'):
            
                
            self.assertEqual(self.dut.MSK_Control.clear_counts.rdl_desc, "Clear Tx Bit Counter and Tx Enable Counter") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Control.diff_encoder_loopback'):
            
                
            self.assertEqual(self.dut.MSK_Control.diff_encoder_loopback.rdl_desc, "0 -\u003e Differential Encoder -\u003e Decoder loopback disabled\n1 -\u003e Differential Encoder -\u003e Decoder loopback enabled") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Status.demod_sync_lock'):
            
                
            self.assertEqual(self.dut.MSK_Status.demod_sync_lock.rdl_desc, "Demodulator Sync Status - not currently implemented") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Status.tx_enable'):
            
                
            self.assertEqual(self.dut.MSK_Status.tx_enable.rdl_desc, "1 -\u003e Data to DAC Enabled\n0 -\u003e Data to DAC Disabled") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Status.rx_enable'):
            
                
            self.assertEqual(self.dut.MSK_Status.rx_enable.rdl_desc, "1 -\u003e Data from ADC Enabled\n0 -\u003e Data from ADC Disabled") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.MSK_Status.tx_axis_valid'):
            
                
            self.assertEqual(self.dut.MSK_Status.tx_axis_valid.rdl_desc, "1 -\u003e S_AXIS_VALID Enabled\n0 -\u003e S_AXIS_VALID Disabled") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Fb_FreqWord.config_data'):
            
                
            self.assertEqual(self.dut.Fb_FreqWord.config_data.rdl_desc, "Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, \nwhere Fn is the desired NCO frequency, and Fs is the NCO sample rate") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.TX_F1_FreqWord.config_data'):
            
                
            self.assertEqual(self.dut.TX_F1_FreqWord.config_data.rdl_desc, "Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, \nwhere Fn is the desired NCO frequency, and Fs is the NCO sample rate") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.TX_F2_FreqWord.config_data'):
            
                
            self.assertEqual(self.dut.TX_F2_FreqWord.config_data.rdl_desc, "Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, \nwhere Fn is the desired NCO frequency, and Fs is the NCO sample rate") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.RX_F1_FreqWord.config_data'):
            
                
            self.assertEqual(self.dut.RX_F1_FreqWord.config_data.rdl_desc, "Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, \nwhere Fn is the desired NCO frequency, and Fs is the NCO sample rate") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.RX_F2_FreqWord.config_data'):
            
                
            self.assertEqual(self.dut.RX_F2_FreqWord.config_data.rdl_desc, "Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, \nwhere Fn is the desired NCO frequency, and Fs is the NCO sample rate") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_freeze'):
            
                
            self.assertEqual(self.dut.LPF_Config_0.lpf_freeze.rdl_desc, "0 -\u003e Normal operation\n1 -\u003e Freeze current value") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_zero'):
            
                
            self.assertEqual(self.dut.LPF_Config_0.lpf_zero.rdl_desc, "0 -\u003e Normal operation\n1 -\u003e Zero and hold accumulator") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.prbs_reserved'):
            
                
            self.assertIsNone(self.dut.LPF_Config_0.prbs_reserved.rdl_desc)  # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_alpha'):
            
                
            self.assertEqual(self.dut.LPF_Config_0.lpf_alpha.rdl_desc, "Value controls the filter rolloff") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_1.i_gain'):
            
                
            self.assertEqual(self.dut.LPF_Config_1.i_gain.rdl_desc, "Value m of 0-16,777,215 sets the integral multiplier") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_1.i_shift'):
            
                
            self.assertEqual(self.dut.LPF_Config_1.i_shift.rdl_desc, "Value n of 0-32 sets the integral divisor as 2^-n") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Data_Width.data_width'):
            
                
            self.assertEqual(self.dut.Tx_Data_Width.data_width.rdl_desc, "Set the data width of the modem input/output") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Rx_Data_Width.data_width'):
            
                
            self.assertEqual(self.dut.Rx_Data_Width.data_width.rdl_desc, "Set the data width of the modem input/output") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_sel'):
            
                
            self.assertEqual(self.dut.PRBS_Control.prbs_sel.rdl_desc, "0 -\u003e Select Normal Tx Data\n1 -\u003e Select PRBS Tx Data") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_error_insert'):
            
                
            self.assertEqual(self.dut.PRBS_Control.prbs_error_insert.rdl_desc, "0 -\u003e 1 :  Insert bit error in Tx data (both Normal and PRBS)\n1 -\u003e 0 : Insert bit error in Tx data (both Normal and PRBS)") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_clear'):
            
                
            self.assertEqual(self.dut.PRBS_Control.prbs_clear.rdl_desc, "0 -\u003e 1 : Clear PRBS Counters\n1 -\u003e 0 : Clear PRBS Counters") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_manual_sync'):
            
                
            self.assertEqual(self.dut.PRBS_Control.prbs_manual_sync.rdl_desc, "0 -\u003e 1 : Synchronize PRBS monitor\n1 -\u003e 0 : Synchronize PRBS monitor") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_reserved'):
            
                
            self.assertIsNone(self.dut.PRBS_Control.prbs_reserved.rdl_desc)  # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_sync_threshold'):
            
                
            self.assertEqual(self.dut.PRBS_Control.prbs_sync_threshold.rdl_desc, "0 : Auto Sync Disabled\nN \u003e 0 : Auto sync after N errors") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Initial_State.config_data'):
            
                
            self.assertEqual(self.dut.PRBS_Initial_State.config_data.rdl_desc, "Sets the starting value of the PRBS generator") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Polynomial.config_data'):
            
                
            self.assertEqual(self.dut.PRBS_Polynomial.config_data.rdl_desc, "Bit positions set to \u00271\u0027 indicate polynomial feedback positions") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.PRBS_Error_Mask.config_data'):
            
                
            self.assertEqual(self.dut.PRBS_Error_Mask.config_data.rdl_desc, "Bit positions set to \u00271\u0027 indicate bits that are inverted when a bit error is inserted") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard.rx_sample_discard'):
            
                
            self.assertEqual(self.dut.Rx_Sample_Discard.rx_sample_discard.rdl_desc, "Number of Rx samples to discard") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard.rx_nco_discard'):
            
                
            self.assertEqual(self.dut.Rx_Sample_Discard.rx_nco_discard.rdl_desc, "Number of NCO samples to discard") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_2.p_gain'):
            
                
            self.assertEqual(self.dut.LPF_Config_2.p_gain.rdl_desc, "Value m of 0-16,777,215 sets the proportional multiplier") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.LPF_Config_2.p_shift'):
            
                
            self.assertEqual(self.dut.LPF_Config_2.p_shift.rdl_desc, "Value n of 0-32 sets the proportional divisor as 2^-n") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_ena.rdl_desc, "0 -\u003e Disable sync transmission\n1 -\u003e Enable sync transmission when PTT is asserted") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_force'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_force.rdl_desc, "0 : Normal operation)\n1 : Transmit synchronization pattern)") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f1'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_f1.rdl_desc, "Enables/Disables transmission of F1 tone for receiver synchronization\n0 : F1 tone transmission disabled\n1 : F1 tone transmission enabled\nBoth F1 and F2 can be enabled at the same time") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f2'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Ctrl.tx_sync_f2.rdl_desc, "Enables/Disables transmission of F2 tone for receiver synchronization\n0 : F2 tone transmission disabled\n1 : F2 tone transmission enabled\nBoth F1 and F2 can be enabled at the same time") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt'):
            
                
            self.assertEqual(self.dut.Tx_Sync_Cnt.tx_sync_cnt.rdl_desc, "Value from 0x00_0000 to 0xFF_FFFF. \nThis value represents the number bit-times the synchronization \nsignal should be sent after PTT is asserted.") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha1.alpha'):
            
                
            self.assertEqual(self.dut.lowpass_ema_alpha1.alpha.rdl_desc, "Value from 0x0_0000 to 0x3_FFFF represent the EMA alpha") # type: ignore[union-attr]
                
            

        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha2.alpha'):
            
                
            self.assertEqual(self.dut.lowpass_ema_alpha2.alpha.rdl_desc, "Value from 0x0_0000 to 0x3_FFFF represent the EMA alpha") # type: ignore[union-attr]
                
            

        

    def test_sizes(self) -> None:
        """
        Check that the sizes all match
        """
        with self.subTest(msg='node: msk_top_regs.Hash_ID_Low'):
            self.assertEqual(self.dut.Hash_ID_Low.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Hash_ID_High'):
            self.assertEqual(self.dut.Hash_ID_High.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Init'):
            self.assertEqual(self.dut.MSK_Init.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control'):
            self.assertEqual(self.dut.MSK_Control.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Status'):
            self.assertEqual(self.dut.MSK_Status.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Fb_FreqWord'):
            self.assertEqual(self.dut.Fb_FreqWord.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.TX_F1_FreqWord'):
            self.assertEqual(self.dut.TX_F1_FreqWord.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.TX_F2_FreqWord'):
            self.assertEqual(self.dut.TX_F2_FreqWord.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.RX_F1_FreqWord'):
            self.assertEqual(self.dut.RX_F1_FreqWord.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.RX_F2_FreqWord'):
            self.assertEqual(self.dut.RX_F2_FreqWord.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_0'):
            self.assertEqual(self.dut.LPF_Config_0.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_1'):
            self.assertEqual(self.dut.LPF_Config_1.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Data_Width'):
            self.assertEqual(self.dut.Tx_Data_Width.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Data_Width'):
            self.assertEqual(self.dut.Rx_Data_Width.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control'):
            self.assertEqual(self.dut.PRBS_Control.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Initial_State'):
            self.assertEqual(self.dut.PRBS_Initial_State.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Polynomial'):
            self.assertEqual(self.dut.PRBS_Polynomial.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Error_Mask'):
            self.assertEqual(self.dut.PRBS_Error_Mask.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard'):
            self.assertEqual(self.dut.Rx_Sample_Discard.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_2'):
            self.assertEqual(self.dut.LPF_Config_2.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl'):
            self.assertEqual(self.dut.Tx_Sync_Ctrl.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Cnt'):
            self.assertEqual(self.dut.Tx_Sync_Cnt.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha1'):
            self.assertEqual(self.dut.lowpass_ema_alpha1.size, 4) # type: ignore[union-attr]
        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha2'):
            self.assertEqual(self.dut.lowpass_ema_alpha2.size, 4) # type: ignore[union-attr]
        

        # check the size of the address map itself
        
        with self.subTest(msg='node: msk_top_regs'):
            self.assertEqual(self.dut.size, 96) # type: ignore[union-attr]
        


    def test_register_properties(self)  -> None:
        """
        Walk the address map and check the address, size and accesswidth of every register is
        correct
        """
        with self.subTest(msg='register: msk_top_regs.Hash_ID_Low'):
            self.assertEqual(self.dut.Hash_ID_Low.address, 0) # type: ignore[union-attr]
            self.assertEqual(self.dut.Hash_ID_Low.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.Hash_ID_Low.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.Hash_ID_Low.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.Hash_ID_High'):
            self.assertEqual(self.dut.Hash_ID_High.address, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.Hash_ID_High.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.Hash_ID_High.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.Hash_ID_High.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.MSK_Init'):
            self.assertEqual(self.dut.MSK_Init.address, 8) # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Init.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Init.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Init.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.MSK_Control'):
            self.assertEqual(self.dut.MSK_Control.address, 12) # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Control.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Control.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Control.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.MSK_Status'):
            self.assertEqual(self.dut.MSK_Status.address, 16) # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Status.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Status.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.MSK_Status.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.Fb_FreqWord'):
            self.assertEqual(self.dut.Fb_FreqWord.address, 20) # type: ignore[union-attr]
            self.assertEqual(self.dut.Fb_FreqWord.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.Fb_FreqWord.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.Fb_FreqWord.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.TX_F1_FreqWord'):
            self.assertEqual(self.dut.TX_F1_FreqWord.address, 24) # type: ignore[union-attr]
            self.assertEqual(self.dut.TX_F1_FreqWord.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.TX_F1_FreqWord.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.TX_F1_FreqWord.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.TX_F2_FreqWord'):
            self.assertEqual(self.dut.TX_F2_FreqWord.address, 28) # type: ignore[union-attr]
            self.assertEqual(self.dut.TX_F2_FreqWord.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.TX_F2_FreqWord.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.TX_F2_FreqWord.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.RX_F1_FreqWord'):
            self.assertEqual(self.dut.RX_F1_FreqWord.address, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.RX_F1_FreqWord.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.RX_F1_FreqWord.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.RX_F1_FreqWord.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.RX_F2_FreqWord'):
            self.assertEqual(self.dut.RX_F2_FreqWord.address, 36) # type: ignore[union-attr]
            self.assertEqual(self.dut.RX_F2_FreqWord.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.RX_F2_FreqWord.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.RX_F2_FreqWord.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0'):
            self.assertEqual(self.dut.LPF_Config_0.address, 40) # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_0.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_0.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_0.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.LPF_Config_1'):
            self.assertEqual(self.dut.LPF_Config_1.address, 44) # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_1.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_1.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_1.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.Tx_Data_Width'):
            self.assertEqual(self.dut.Tx_Data_Width.address, 48) # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Data_Width.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Data_Width.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Data_Width.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.Rx_Data_Width'):
            self.assertEqual(self.dut.Rx_Data_Width.address, 52) # type: ignore[union-attr]
            self.assertEqual(self.dut.Rx_Data_Width.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.Rx_Data_Width.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.Rx_Data_Width.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.PRBS_Control'):
            self.assertEqual(self.dut.PRBS_Control.address, 56) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Control.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Control.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Control.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.PRBS_Initial_State'):
            self.assertEqual(self.dut.PRBS_Initial_State.address, 60) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Initial_State.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Initial_State.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Initial_State.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.PRBS_Polynomial'):
            self.assertEqual(self.dut.PRBS_Polynomial.address, 64) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Polynomial.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Polynomial.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Polynomial.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.PRBS_Error_Mask'):
            self.assertEqual(self.dut.PRBS_Error_Mask.address, 68) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Error_Mask.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Error_Mask.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.PRBS_Error_Mask.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.Rx_Sample_Discard'):
            self.assertEqual(self.dut.Rx_Sample_Discard.address, 72) # type: ignore[union-attr]
            self.assertEqual(self.dut.Rx_Sample_Discard.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.Rx_Sample_Discard.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.Rx_Sample_Discard.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.LPF_Config_2'):
            self.assertEqual(self.dut.LPF_Config_2.address, 76) # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_2.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_2.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.LPF_Config_2.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl'):
            self.assertEqual(self.dut.Tx_Sync_Ctrl.address, 80) # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Ctrl.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Ctrl.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Ctrl.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Cnt'):
            self.assertEqual(self.dut.Tx_Sync_Cnt.address, 84) # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Cnt.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Cnt.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.Tx_Sync_Cnt.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha1'):
            self.assertEqual(self.dut.lowpass_ema_alpha1.address, 88) # type: ignore[union-attr]
            self.assertEqual(self.dut.lowpass_ema_alpha1.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.lowpass_ema_alpha1.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.lowpass_ema_alpha1.accesswidth, 32) # type: ignore[union-attr]
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha2'):
            self.assertEqual(self.dut.lowpass_ema_alpha2.address, 92) # type: ignore[union-attr]
            self.assertEqual(self.dut.lowpass_ema_alpha2.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.lowpass_ema_alpha2.size, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.lowpass_ema_alpha2.accesswidth, 32) # type: ignore[union-attr]
        

    def test_memory_properties(self)  -> None:
        """
        Walk the address map and check the address, size and accesswidth of every memory is
        correct
        """
        mut: AsyncMemory
        

    def test_field_properties(self)  -> None:
        """
        walk the address map and check:
        - that the lsb and msb of every field is correct
        - that where default values are provided they are applied correctly
        """
        fut:Field
        with self.subTest(msg='field: msk_top_regs.Hash_ID_Low.hash_id_lo'):
            # test properties of field: msk_top_regs.Hash_ID_Low.hash_id_lo
            fut = self.dut.Hash_ID_Low.hash_id_lo # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0x0)
            self.assertEqual(fut.max_value,0xFFFFFFFF)
                
            self.assertEqual(fut.default,2863289685)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.Hash_ID_High.hash_id_hi'):
            # test properties of field: msk_top_regs.Hash_ID_High.hash_id_hi
            fut = self.dut.Hash_ID_High.hash_id_hi # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0x0)
            self.assertEqual(fut.max_value,0xFFFFFFFF)
                
            self.assertEqual(fut.default,1431677610)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.MSK_Init.txrxinit'):
            # test properties of field: msk_top_regs.MSK_Init.txrxinit
            fut = self.dut.MSK_Init.txrxinit # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,0)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,0)
            self.assertEqual(fut.bitmask,0x1)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFE)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,1)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.MSK_Init.txinit'):
            # test properties of field: msk_top_regs.MSK_Init.txinit
            fut = self.dut.MSK_Init.txinit # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,1)
            self.assertEqual(fut.msb,1)
            self.assertEqual(fut.low,1)
            self.assertEqual(fut.high,1)
            self.assertEqual(fut.bitmask,0x2)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFD)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,1)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.MSK_Init.rxinit'):
            # test properties of field: msk_top_regs.MSK_Init.rxinit
            fut = self.dut.MSK_Init.rxinit # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,2)
            self.assertEqual(fut.msb,2)
            self.assertEqual(fut.low,2)
            self.assertEqual(fut.high,2)
            self.assertEqual(fut.bitmask,0x4)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFB)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,1)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.MSK_Control.ptt'):
            # test properties of field: msk_top_regs.MSK_Control.ptt
            fut = self.dut.MSK_Control.ptt # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,0)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,0)
            self.assertEqual(fut.bitmask,0x1)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFE)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.MSK_Control.loopback_ena'):
            # test properties of field: msk_top_regs.MSK_Control.loopback_ena
            fut = self.dut.MSK_Control.loopback_ena # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,1)
            self.assertEqual(fut.msb,1)
            self.assertEqual(fut.low,1)
            self.assertEqual(fut.high,1)
            self.assertEqual(fut.bitmask,0x2)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFD)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.MSK_Control.rx_invert'):
            # test properties of field: msk_top_regs.MSK_Control.rx_invert
            fut = self.dut.MSK_Control.rx_invert # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,2)
            self.assertEqual(fut.msb,2)
            self.assertEqual(fut.low,2)
            self.assertEqual(fut.high,2)
            self.assertEqual(fut.bitmask,0x4)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFB)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.MSK_Control.clear_counts'):
            # test properties of field: msk_top_regs.MSK_Control.clear_counts
            fut = self.dut.MSK_Control.clear_counts # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,3)
            self.assertEqual(fut.msb,3)
            self.assertEqual(fut.low,3)
            self.assertEqual(fut.high,3)
            self.assertEqual(fut.bitmask,0x8)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFF7)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.MSK_Control.diff_encoder_loopback'):
            # test properties of field: msk_top_regs.MSK_Control.diff_encoder_loopback
            fut = self.dut.MSK_Control.diff_encoder_loopback # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,4)
            self.assertEqual(fut.msb,4)
            self.assertEqual(fut.low,4)
            self.assertEqual(fut.high,4)
            self.assertEqual(fut.bitmask,0x10)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFEF)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.MSK_Status.demod_sync_lock'):
            # test properties of field: msk_top_regs.MSK_Status.demod_sync_lock
            fut = self.dut.MSK_Status.demod_sync_lock # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,0)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,0)
            self.assertEqual(fut.bitmask,0x1)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFE)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,True)
        with self.subTest(msg='field: msk_top_regs.MSK_Status.tx_enable'):
            # test properties of field: msk_top_regs.MSK_Status.tx_enable
            fut = self.dut.MSK_Status.tx_enable # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,1)
            self.assertEqual(fut.msb,1)
            self.assertEqual(fut.low,1)
            self.assertEqual(fut.high,1)
            self.assertEqual(fut.bitmask,0x2)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFD)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,True)
        with self.subTest(msg='field: msk_top_regs.MSK_Status.rx_enable'):
            # test properties of field: msk_top_regs.MSK_Status.rx_enable
            fut = self.dut.MSK_Status.rx_enable # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,2)
            self.assertEqual(fut.msb,2)
            self.assertEqual(fut.low,2)
            self.assertEqual(fut.high,2)
            self.assertEqual(fut.bitmask,0x4)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFB)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,True)
        with self.subTest(msg='field: msk_top_regs.MSK_Status.tx_axis_valid'):
            # test properties of field: msk_top_regs.MSK_Status.tx_axis_valid
            fut = self.dut.MSK_Status.tx_axis_valid # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,3)
            self.assertEqual(fut.msb,3)
            self.assertEqual(fut.low,3)
            self.assertEqual(fut.high,3)
            self.assertEqual(fut.bitmask,0x8)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFF7)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,True)
        with self.subTest(msg='field: msk_top_regs.Fb_FreqWord.config_data'):
            # test properties of field: msk_top_regs.Fb_FreqWord.config_data
            fut = self.dut.Fb_FreqWord.config_data # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0x0)
            self.assertEqual(fut.max_value,0xFFFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.TX_F1_FreqWord.config_data'):
            # test properties of field: msk_top_regs.TX_F1_FreqWord.config_data
            fut = self.dut.TX_F1_FreqWord.config_data # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0x0)
            self.assertEqual(fut.max_value,0xFFFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.TX_F2_FreqWord.config_data'):
            # test properties of field: msk_top_regs.TX_F2_FreqWord.config_data
            fut = self.dut.TX_F2_FreqWord.config_data # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0x0)
            self.assertEqual(fut.max_value,0xFFFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.RX_F1_FreqWord.config_data'):
            # test properties of field: msk_top_regs.RX_F1_FreqWord.config_data
            fut = self.dut.RX_F1_FreqWord.config_data # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0x0)
            self.assertEqual(fut.max_value,0xFFFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.RX_F2_FreqWord.config_data'):
            # test properties of field: msk_top_regs.RX_F2_FreqWord.config_data
            fut = self.dut.RX_F2_FreqWord.config_data # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0x0)
            self.assertEqual(fut.max_value,0xFFFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.lpf_freeze'):
            # test properties of field: msk_top_regs.LPF_Config_0.lpf_freeze
            fut = self.dut.LPF_Config_0.lpf_freeze # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,0)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,0)
            self.assertEqual(fut.bitmask,0x1)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFE)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.lpf_zero'):
            # test properties of field: msk_top_regs.LPF_Config_0.lpf_zero
            fut = self.dut.LPF_Config_0.lpf_zero # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,1)
            self.assertEqual(fut.msb,1)
            self.assertEqual(fut.low,1)
            self.assertEqual(fut.high,1)
            self.assertEqual(fut.bitmask,0x2)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFD)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.prbs_reserved'):
            # test properties of field: msk_top_regs.LPF_Config_0.prbs_reserved
            fut = self.dut.LPF_Config_0.prbs_reserved # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,2)
            self.assertEqual(fut.msb,7)
            self.assertEqual(fut.low,2)
            self.assertEqual(fut.high,7)
            self.assertEqual(fut.bitmask,0xFC)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFF03)
            self.assertEqual(fut.max_value,0x3F)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.lpf_alpha'):
            # test properties of field: msk_top_regs.LPF_Config_0.lpf_alpha
            fut = self.dut.LPF_Config_0.lpf_alpha # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,8)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,8)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFF00)
            self.assertEqual(fut.inverse_bitmask,0xFF)
            self.assertEqual(fut.max_value,0xFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.LPF_Config_1.i_gain'):
            # test properties of field: msk_top_regs.LPF_Config_1.i_gain
            fut = self.dut.LPF_Config_1.i_gain # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,23)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,23)
            self.assertEqual(fut.bitmask,0xFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0xFF000000)
            self.assertEqual(fut.max_value,0xFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.LPF_Config_1.i_shift'):
            # test properties of field: msk_top_regs.LPF_Config_1.i_shift
            fut = self.dut.LPF_Config_1.i_shift # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,24)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,24)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFF000000)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFF)
            self.assertEqual(fut.max_value,0xFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.Tx_Data_Width.data_width'):
            # test properties of field: msk_top_regs.Tx_Data_Width.data_width
            fut = self.dut.Tx_Data_Width.data_width # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,7)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,7)
            self.assertEqual(fut.bitmask,0xFF)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFF00)
            self.assertEqual(fut.max_value,0xFF)
                
            self.assertEqual(fut.default,8)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.Rx_Data_Width.data_width'):
            # test properties of field: msk_top_regs.Rx_Data_Width.data_width
            fut = self.dut.Rx_Data_Width.data_width # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,7)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,7)
            self.assertEqual(fut.bitmask,0xFF)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFF00)
            self.assertEqual(fut.max_value,0xFF)
                
            self.assertEqual(fut.default,8)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_sel'):
            # test properties of field: msk_top_regs.PRBS_Control.prbs_sel
            fut = self.dut.PRBS_Control.prbs_sel # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,0)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,0)
            self.assertEqual(fut.bitmask,0x1)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFE)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_error_insert'):
            # test properties of field: msk_top_regs.PRBS_Control.prbs_error_insert
            fut = self.dut.PRBS_Control.prbs_error_insert # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,1)
            self.assertEqual(fut.msb,1)
            self.assertEqual(fut.low,1)
            self.assertEqual(fut.high,1)
            self.assertEqual(fut.bitmask,0x2)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFD)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_clear'):
            # test properties of field: msk_top_regs.PRBS_Control.prbs_clear
            fut = self.dut.PRBS_Control.prbs_clear # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,2)
            self.assertEqual(fut.msb,2)
            self.assertEqual(fut.low,2)
            self.assertEqual(fut.high,2)
            self.assertEqual(fut.bitmask,0x4)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFB)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_manual_sync'):
            # test properties of field: msk_top_regs.PRBS_Control.prbs_manual_sync
            fut = self.dut.PRBS_Control.prbs_manual_sync # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,3)
            self.assertEqual(fut.msb,3)
            self.assertEqual(fut.low,3)
            self.assertEqual(fut.high,3)
            self.assertEqual(fut.bitmask,0x8)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFF7)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_reserved'):
            # test properties of field: msk_top_regs.PRBS_Control.prbs_reserved
            fut = self.dut.PRBS_Control.prbs_reserved # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,4)
            self.assertEqual(fut.msb,15)
            self.assertEqual(fut.low,4)
            self.assertEqual(fut.high,15)
            self.assertEqual(fut.bitmask,0xFFF0)
            self.assertEqual(fut.inverse_bitmask,0xFFFF000F)
            self.assertEqual(fut.max_value,0xFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_sync_threshold'):
            # test properties of field: msk_top_regs.PRBS_Control.prbs_sync_threshold
            fut = self.dut.PRBS_Control.prbs_sync_threshold # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,16)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,16)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFF0000)
            self.assertEqual(fut.inverse_bitmask,0xFFFF)
            self.assertEqual(fut.max_value,0xFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.PRBS_Initial_State.config_data'):
            # test properties of field: msk_top_regs.PRBS_Initial_State.config_data
            fut = self.dut.PRBS_Initial_State.config_data # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0x0)
            self.assertEqual(fut.max_value,0xFFFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.PRBS_Polynomial.config_data'):
            # test properties of field: msk_top_regs.PRBS_Polynomial.config_data
            fut = self.dut.PRBS_Polynomial.config_data # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0x0)
            self.assertEqual(fut.max_value,0xFFFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.PRBS_Error_Mask.config_data'):
            # test properties of field: msk_top_regs.PRBS_Error_Mask.config_data
            fut = self.dut.PRBS_Error_Mask.config_data # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0x0)
            self.assertEqual(fut.max_value,0xFFFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.Rx_Sample_Discard.rx_sample_discard'):
            # test properties of field: msk_top_regs.Rx_Sample_Discard.rx_sample_discard
            fut = self.dut.Rx_Sample_Discard.rx_sample_discard # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,7)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,7)
            self.assertEqual(fut.bitmask,0xFF)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFF00)
            self.assertEqual(fut.max_value,0xFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.Rx_Sample_Discard.rx_nco_discard'):
            # test properties of field: msk_top_regs.Rx_Sample_Discard.rx_nco_discard
            fut = self.dut.Rx_Sample_Discard.rx_nco_discard # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,8)
            self.assertEqual(fut.msb,15)
            self.assertEqual(fut.low,8)
            self.assertEqual(fut.high,15)
            self.assertEqual(fut.bitmask,0xFF00)
            self.assertEqual(fut.inverse_bitmask,0xFFFF00FF)
            self.assertEqual(fut.max_value,0xFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.LPF_Config_2.p_gain'):
            # test properties of field: msk_top_regs.LPF_Config_2.p_gain
            fut = self.dut.LPF_Config_2.p_gain # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,23)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,23)
            self.assertEqual(fut.bitmask,0xFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0xFF000000)
            self.assertEqual(fut.max_value,0xFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.LPF_Config_2.p_shift'):
            # test properties of field: msk_top_regs.LPF_Config_2.p_shift
            fut = self.dut.LPF_Config_2.p_shift # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,24)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,24)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFF000000)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFF)
            self.assertEqual(fut.max_value,0xFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena'):
            # test properties of field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena
            fut = self.dut.Tx_Sync_Ctrl.tx_sync_ena # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,0)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,0)
            self.assertEqual(fut.bitmask,0x1)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFE)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_force'):
            # test properties of field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_force
            fut = self.dut.Tx_Sync_Ctrl.tx_sync_force # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,1)
            self.assertEqual(fut.msb,1)
            self.assertEqual(fut.low,1)
            self.assertEqual(fut.high,1)
            self.assertEqual(fut.bitmask,0x2)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFD)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f1'):
            # test properties of field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f1
            fut = self.dut.Tx_Sync_Ctrl.tx_sync_f1 # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,2)
            self.assertEqual(fut.msb,2)
            self.assertEqual(fut.low,2)
            self.assertEqual(fut.high,2)
            self.assertEqual(fut.bitmask,0x4)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFB)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f2'):
            # test properties of field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f2
            fut = self.dut.Tx_Sync_Ctrl.tx_sync_f2 # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,3)
            self.assertEqual(fut.msb,3)
            self.assertEqual(fut.low,3)
            self.assertEqual(fut.high,3)
            self.assertEqual(fut.bitmask,0x8)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFF7)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt'):
            # test properties of field: msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt
            fut = self.dut.Tx_Sync_Cnt.tx_sync_cnt # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,23)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,23)
            self.assertEqual(fut.bitmask,0xFFFFFF)
            self.assertEqual(fut.inverse_bitmask,0xFF000000)
            self.assertEqual(fut.max_value,0xFFFFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.lowpass_ema_alpha1.alpha'):
            # test properties of field: msk_top_regs.lowpass_ema_alpha1.alpha
            fut = self.dut.lowpass_ema_alpha1.alpha # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,17)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,17)
            self.assertEqual(fut.bitmask,0x3FFFF)
            self.assertEqual(fut.inverse_bitmask,0xFFFC0000)
            self.assertEqual(fut.max_value,0x3FFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: msk_top_regs.lowpass_ema_alpha2.alpha'):
            # test properties of field: msk_top_regs.lowpass_ema_alpha2.alpha
            fut = self.dut.lowpass_ema_alpha2.alpha # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,17)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,17)
            self.assertEqual(fut.bitmask,0x3FFFF)
            self.assertEqual(fut.inverse_bitmask,0xFFFC0000)
            self.assertEqual(fut.max_value,0x3FFFF)
                
            self.assertEqual(fut.default,0)
                
            self.assertEqual(fut.is_volatile,False)
        

    def test_field_encoding_properties(self)  -> None:
        """
        Check that enumeration has the name and desc meta data from the systemRDL
        """
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    def test_user_defined_properties(self)  -> None:
        """
        Walk the address map and check user defined properties are correctly pulled up
        """
        with self.subTest(msg='register: msk_top_regs.Hash_ID_Low'):
            
            self.assertDictEqual(self.dut.Hash_ID_Low.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Hash_ID_High'):
            
            self.assertDictEqual(self.dut.Hash_ID_High.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Init'):
            
            self.assertDictEqual(self.dut.MSK_Init.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Control'):
            
            self.assertDictEqual(self.dut.MSK_Control.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Status'):
            
            self.assertDictEqual(self.dut.MSK_Status.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Fb_FreqWord'):
            
            self.assertDictEqual(self.dut.Fb_FreqWord.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.TX_F1_FreqWord'):
            
            self.assertDictEqual(self.dut.TX_F1_FreqWord.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.TX_F2_FreqWord'):
            
            self.assertDictEqual(self.dut.TX_F2_FreqWord.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.RX_F1_FreqWord'):
            
            self.assertDictEqual(self.dut.RX_F1_FreqWord.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.RX_F2_FreqWord'):
            
            self.assertDictEqual(self.dut.RX_F2_FreqWord.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0'):
            
            self.assertDictEqual(self.dut.LPF_Config_0.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_1'):
            
            self.assertDictEqual(self.dut.LPF_Config_1.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Tx_Data_Width'):
            
            self.assertDictEqual(self.dut.Tx_Data_Width.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Rx_Data_Width'):
            
            self.assertDictEqual(self.dut.Rx_Data_Width.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Control'):
            
            self.assertDictEqual(self.dut.PRBS_Control.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Initial_State'):
            
            self.assertDictEqual(self.dut.PRBS_Initial_State.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Polynomial'):
            
            self.assertDictEqual(self.dut.PRBS_Polynomial.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Error_Mask'):
            
            self.assertDictEqual(self.dut.PRBS_Error_Mask.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Rx_Sample_Discard'):
            
            self.assertDictEqual(self.dut.Rx_Sample_Discard.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_2'):
            
            self.assertDictEqual(self.dut.LPF_Config_2.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl'):
            
            self.assertDictEqual(self.dut.Tx_Sync_Ctrl.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Cnt'):
            
            self.assertDictEqual(self.dut.Tx_Sync_Cnt.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha1'):
            
            self.assertDictEqual(self.dut.lowpass_ema_alpha1.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha2'):
            
            self.assertDictEqual(self.dut.lowpass_ema_alpha2.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Hash_ID_Low.hash_id_lo'):
            
            self.assertDictEqual(self.dut.Hash_ID_Low.hash_id_lo.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Hash_ID_High.hash_id_hi'):
            
            self.assertDictEqual(self.dut.Hash_ID_High.hash_id_hi.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Init.txrxinit'):
            
            self.assertDictEqual(self.dut.MSK_Init.txrxinit.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Init.txinit'):
            
            self.assertDictEqual(self.dut.MSK_Init.txinit.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Init.rxinit'):
            
            self.assertDictEqual(self.dut.MSK_Init.rxinit.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Control.ptt'):
            
            self.assertDictEqual(self.dut.MSK_Control.ptt.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Control.loopback_ena'):
            
            self.assertDictEqual(self.dut.MSK_Control.loopback_ena.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Control.rx_invert'):
            
            self.assertDictEqual(self.dut.MSK_Control.rx_invert.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Control.clear_counts'):
            
            self.assertDictEqual(self.dut.MSK_Control.clear_counts.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Control.diff_encoder_loopback'):
            
            self.assertDictEqual(self.dut.MSK_Control.diff_encoder_loopback.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Status.demod_sync_lock'):
            
            self.assertDictEqual(self.dut.MSK_Status.demod_sync_lock.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Status.tx_enable'):
            
            self.assertDictEqual(self.dut.MSK_Status.tx_enable.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Status.rx_enable'):
            
            self.assertDictEqual(self.dut.MSK_Status.rx_enable.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.MSK_Status.tx_axis_valid'):
            
            self.assertDictEqual(self.dut.MSK_Status.tx_axis_valid.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Fb_FreqWord.config_data'):
            
            self.assertDictEqual(self.dut.Fb_FreqWord.config_data.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.TX_F1_FreqWord.config_data'):
            
            self.assertDictEqual(self.dut.TX_F1_FreqWord.config_data.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.TX_F2_FreqWord.config_data'):
            
            self.assertDictEqual(self.dut.TX_F2_FreqWord.config_data.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.RX_F1_FreqWord.config_data'):
            
            self.assertDictEqual(self.dut.RX_F1_FreqWord.config_data.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.RX_F2_FreqWord.config_data'):
            
            self.assertDictEqual(self.dut.RX_F2_FreqWord.config_data.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0.lpf_freeze'):
            
            self.assertDictEqual(self.dut.LPF_Config_0.lpf_freeze.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0.lpf_zero'):
            
            self.assertDictEqual(self.dut.LPF_Config_0.lpf_zero.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0.prbs_reserved'):
            
            self.assertDictEqual(self.dut.LPF_Config_0.prbs_reserved.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0.lpf_alpha'):
            
            self.assertDictEqual(self.dut.LPF_Config_0.lpf_alpha.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_1.i_gain'):
            
            self.assertDictEqual(self.dut.LPF_Config_1.i_gain.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_1.i_shift'):
            
            self.assertDictEqual(self.dut.LPF_Config_1.i_shift.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Tx_Data_Width.data_width'):
            
            self.assertDictEqual(self.dut.Tx_Data_Width.data_width.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Rx_Data_Width.data_width'):
            
            self.assertDictEqual(self.dut.Rx_Data_Width.data_width.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Control.prbs_sel'):
            
            self.assertDictEqual(self.dut.PRBS_Control.prbs_sel.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Control.prbs_error_insert'):
            
            self.assertDictEqual(self.dut.PRBS_Control.prbs_error_insert.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Control.prbs_clear'):
            
            self.assertDictEqual(self.dut.PRBS_Control.prbs_clear.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Control.prbs_manual_sync'):
            
            self.assertDictEqual(self.dut.PRBS_Control.prbs_manual_sync.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Control.prbs_reserved'):
            
            self.assertDictEqual(self.dut.PRBS_Control.prbs_reserved.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Control.prbs_sync_threshold'):
            
            self.assertDictEqual(self.dut.PRBS_Control.prbs_sync_threshold.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Initial_State.config_data'):
            
            self.assertDictEqual(self.dut.PRBS_Initial_State.config_data.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Polynomial.config_data'):
            
            self.assertDictEqual(self.dut.PRBS_Polynomial.config_data.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Error_Mask.config_data'):
            
            self.assertDictEqual(self.dut.PRBS_Error_Mask.config_data.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Rx_Sample_Discard.rx_sample_discard'):
            
            self.assertDictEqual(self.dut.Rx_Sample_Discard.rx_sample_discard.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Rx_Sample_Discard.rx_nco_discard'):
            
            self.assertDictEqual(self.dut.Rx_Sample_Discard.rx_nco_discard.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_2.p_gain'):
            
            self.assertDictEqual(self.dut.LPF_Config_2.p_gain.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_2.p_shift'):
            
            self.assertDictEqual(self.dut.LPF_Config_2.p_shift.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena'):
            
            self.assertDictEqual(self.dut.Tx_Sync_Ctrl.tx_sync_ena.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl.tx_sync_force'):
            
            self.assertDictEqual(self.dut.Tx_Sync_Ctrl.tx_sync_force.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f1'):
            
            self.assertDictEqual(self.dut.Tx_Sync_Ctrl.tx_sync_f1.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f2'):
            
            self.assertDictEqual(self.dut.Tx_Sync_Ctrl.tx_sync_f2.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt'):
            
            self.assertDictEqual(self.dut.Tx_Sync_Cnt.tx_sync_cnt.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha1.alpha'):
            
            self.assertDictEqual(self.dut.lowpass_ema_alpha1.alpha.udp,{})
            
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha2.alpha'):
            
            self.assertDictEqual(self.dut.lowpass_ema_alpha2.alpha.udp,{})
            
        

    async def test_register_read_and_write(self) -> None:
        """
        Walk the register map and check every register can be read and written to correctly
        """
        rut: Reg
        # test access operations (read and/or write) to register:
        # msk_top_regs.Hash_ID_Low
        with self.subTest(msg='register: msk_top_regs.Hash_ID_Low'):
            rut=self.dut.Hash_ID_Low # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                # test that a non-writable register has no write method and attempting one generates and error
                with self.assertRaises(AttributeError):
                    await rut.write(0) # type: ignore[attr-defined]

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.Hash_ID_High
        with self.subTest(msg='register: msk_top_regs.Hash_ID_High'):
            rut=self.dut.Hash_ID_High # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                # test that a non-writable register has no write method and attempting one generates and error
                with self.assertRaises(AttributeError):
                    await rut.write(0) # type: ignore[attr-defined]

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Init
        with self.subTest(msg='register: msk_top_regs.MSK_Init'):
            rut=self.dut.MSK_Init # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Control
        with self.subTest(msg='register: msk_top_regs.MSK_Control'):
            rut=self.dut.MSK_Control # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.MSK_Status
        with self.subTest(msg='register: msk_top_regs.MSK_Status'):
            rut=self.dut.MSK_Status # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                # test that a non-writable register has no write method and attempting one generates and error
                with self.assertRaises(AttributeError):
                    await rut.write(0) # type: ignore[attr-defined]

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.Fb_FreqWord
        with self.subTest(msg='register: msk_top_regs.Fb_FreqWord'):
            rut=self.dut.Fb_FreqWord # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=20,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=20,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=20,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=20,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=20,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=20,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=20,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.TX_F1_FreqWord
        with self.subTest(msg='register: msk_top_regs.TX_F1_FreqWord'):
            rut=self.dut.TX_F1_FreqWord # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=24,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=24,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=24,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=24,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=24,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=24,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=24,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.TX_F2_FreqWord
        with self.subTest(msg='register: msk_top_regs.TX_F2_FreqWord'):
            rut=self.dut.TX_F2_FreqWord # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=28,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=28,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=28,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=28,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=28,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=28,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=28,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.RX_F1_FreqWord
        with self.subTest(msg='register: msk_top_regs.RX_F1_FreqWord'):
            rut=self.dut.RX_F1_FreqWord # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=32,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=32,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=32,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=32,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=32,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=32,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=32,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.RX_F2_FreqWord
        with self.subTest(msg='register: msk_top_regs.RX_F2_FreqWord'):
            rut=self.dut.RX_F2_FreqWord # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=36,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=36,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=36,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=36,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=36,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=36,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=36,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_0
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0'):
            rut=self.dut.LPF_Config_0 # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_1
        with self.subTest(msg='register: msk_top_regs.LPF_Config_1'):
            rut=self.dut.LPF_Config_1 # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Data_Width
        with self.subTest(msg='register: msk_top_regs.Tx_Data_Width'):
            rut=self.dut.Tx_Data_Width # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.Rx_Data_Width
        with self.subTest(msg='register: msk_top_regs.Rx_Data_Width'):
            rut=self.dut.Rx_Data_Width # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Control
        with self.subTest(msg='register: msk_top_regs.PRBS_Control'):
            rut=self.dut.PRBS_Control # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Initial_State
        with self.subTest(msg='register: msk_top_regs.PRBS_Initial_State'):
            rut=self.dut.PRBS_Initial_State # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=60,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=60,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=60,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=60,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=60,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=60,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=60,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Polynomial
        with self.subTest(msg='register: msk_top_regs.PRBS_Polynomial'):
            rut=self.dut.PRBS_Polynomial # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=64,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=64,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=64,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=64,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=64,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=64,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=64,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.PRBS_Error_Mask
        with self.subTest(msg='register: msk_top_regs.PRBS_Error_Mask'):
            rut=self.dut.PRBS_Error_Mask # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=68,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=68,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=68,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=68,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=68,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=68,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=68,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.Rx_Sample_Discard
        with self.subTest(msg='register: msk_top_regs.Rx_Sample_Discard'):
            rut=self.dut.Rx_Sample_Discard # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.LPF_Config_2
        with self.subTest(msg='register: msk_top_regs.LPF_Config_2'):
            rut=self.dut.LPF_Config_2 # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Sync_Ctrl
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl'):
            rut=self.dut.Tx_Sync_Ctrl # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.Tx_Sync_Cnt
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Cnt'):
            rut=self.dut.Tx_Sync_Cnt # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.lowpass_ema_alpha1
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha1'):
            rut=self.dut.lowpass_ema_alpha1 # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # msk_top_regs.lowpass_ema_alpha2
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha2'):
            rut=self.dut.lowpass_ema_alpha2 # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegAsyncReadOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Readable Async Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(await rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(await rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(await rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                if not isinstance(rut, (RegAsyncWriteOnly, RegAsyncReadWrite)):
                    raise TypeError('Register is not a Writeable Async Type')
                
                # test the write with high value
                await rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                await rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                await rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writing a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    await rut.write(-1)

                with self.assertRaises(ValueError):
                    await rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        

    async def test_int_field_read_and_write(self) -> None:
        """
        Check the ability to read and write to integer (non-eumn) fields
        """
        fut:Field
        

        # test access operations (read and/or write) to field:
        # msk_top_regs.Hash_ID_Low.hash_id_lo
        with self.subTest(msg='field: msk_top_regs.Hash_ID_Low.hash_id_lo'):
            fut = self.dut.Hash_ID_Low.hash_id_lo # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0x0
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()

        # test access operations (read and/or write) to field:
        # msk_top_regs.Hash_ID_High.hash_id_hi
        with self.subTest(msg='field: msk_top_regs.Hash_ID_High.hash_id_hi'):
            fut = self.dut.Hash_ID_High.hash_id_hi # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0x0
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Init.txrxinit
        with self.subTest(msg='field: msk_top_regs.MSK_Init.txrxinit'):
            fut = self.dut.MSK_Init.txrxinit # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFE
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x1
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x1) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.MSK_Init.txrxinit.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=self.dut.MSK_Init.txrxinit.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFE) | \
                                         (0x1 & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Init.txinit
        with self.subTest(msg='field: msk_top_regs.MSK_Init.txinit'):
            fut = self.dut.MSK_Init.txinit # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFD
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x2
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x2) >> 1
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.MSK_Init.txinit.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=self.dut.MSK_Init.txinit.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFD) | \
                                         (0x2 & (field_value << 1)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Init.rxinit
        with self.subTest(msg='field: msk_top_regs.MSK_Init.rxinit'):
            fut = self.dut.MSK_Init.rxinit # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFB
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x4
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x4) >> 2
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.MSK_Init.rxinit.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=8,
                                    width=32,
                                    accesswidth=self.dut.MSK_Init.rxinit.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFB) | \
                                         (0x4 & (field_value << 2)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Control.ptt
        with self.subTest(msg='field: msk_top_regs.MSK_Control.ptt'):
            fut = self.dut.MSK_Control.ptt # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFE
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x1
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x1) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.MSK_Control.ptt.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=self.dut.MSK_Control.ptt.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFE) | \
                                         (0x1 & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Control.loopback_ena
        with self.subTest(msg='field: msk_top_regs.MSK_Control.loopback_ena'):
            fut = self.dut.MSK_Control.loopback_ena # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFD
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x2
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x2) >> 1
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.MSK_Control.loopback_ena.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=self.dut.MSK_Control.loopback_ena.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFD) | \
                                         (0x2 & (field_value << 1)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Control.rx_invert
        with self.subTest(msg='field: msk_top_regs.MSK_Control.rx_invert'):
            fut = self.dut.MSK_Control.rx_invert # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFB
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x4
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x4) >> 2
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.MSK_Control.rx_invert.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=self.dut.MSK_Control.rx_invert.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFB) | \
                                         (0x4 & (field_value << 2)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Control.clear_counts
        with self.subTest(msg='field: msk_top_regs.MSK_Control.clear_counts'):
            fut = self.dut.MSK_Control.clear_counts # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFF7
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x8
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x8) >> 3
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.MSK_Control.clear_counts.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=self.dut.MSK_Control.clear_counts.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFF7) | \
                                         (0x8 & (field_value << 3)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Control.diff_encoder_loopback
        with self.subTest(msg='field: msk_top_regs.MSK_Control.diff_encoder_loopback'):
            fut = self.dut.MSK_Control.diff_encoder_loopback # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFEF
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x10
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x10) >> 4
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.MSK_Control.diff_encoder_loopback.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=12,
                                    width=32,
                                    accesswidth=self.dut.MSK_Control.diff_encoder_loopback.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFEF) | \
                                         (0x10 & (field_value << 4)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Status.demod_sync_lock
        with self.subTest(msg='field: msk_top_regs.MSK_Status.demod_sync_lock'):
            fut = self.dut.MSK_Status.demod_sync_lock # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFE
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x1
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x1) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Status.tx_enable
        with self.subTest(msg='field: msk_top_regs.MSK_Status.tx_enable'):
            fut = self.dut.MSK_Status.tx_enable # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFD
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x2
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x2) >> 1
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Status.rx_enable
        with self.subTest(msg='field: msk_top_regs.MSK_Status.rx_enable'):
            fut = self.dut.MSK_Status.rx_enable # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFB
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x4
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x4) >> 2
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()

        # test access operations (read and/or write) to field:
        # msk_top_regs.MSK_Status.tx_axis_valid
        with self.subTest(msg='field: msk_top_regs.MSK_Status.tx_axis_valid'):
            fut = self.dut.MSK_Status.tx_axis_valid # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFF7
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x8
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x8) >> 3
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=16,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()

        # test access operations (read and/or write) to field:
        # msk_top_regs.Fb_FreqWord.config_data
        with self.subTest(msg='field: msk_top_regs.Fb_FreqWord.config_data'):
            fut = self.dut.Fb_FreqWord.config_data # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0x0
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=20,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=20,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=20,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.Fb_FreqWord.config_data.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_not_called()
                        write_callback_mock.assert_called_once_with(
                                    addr=20,
                                    width=32,
                                    accesswidth=self.dut.Fb_FreqWord.config_data.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0x0) | \
                                         (0xFFFFFFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.TX_F1_FreqWord.config_data
        with self.subTest(msg='field: msk_top_regs.TX_F1_FreqWord.config_data'):
            fut = self.dut.TX_F1_FreqWord.config_data # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0x0
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=24,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=24,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=24,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.TX_F1_FreqWord.config_data.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_not_called()
                        write_callback_mock.assert_called_once_with(
                                    addr=24,
                                    width=32,
                                    accesswidth=self.dut.TX_F1_FreqWord.config_data.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0x0) | \
                                         (0xFFFFFFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.TX_F2_FreqWord.config_data
        with self.subTest(msg='field: msk_top_regs.TX_F2_FreqWord.config_data'):
            fut = self.dut.TX_F2_FreqWord.config_data # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0x0
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=28,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=28,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=28,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.TX_F2_FreqWord.config_data.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_not_called()
                        write_callback_mock.assert_called_once_with(
                                    addr=28,
                                    width=32,
                                    accesswidth=self.dut.TX_F2_FreqWord.config_data.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0x0) | \
                                         (0xFFFFFFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.RX_F1_FreqWord.config_data
        with self.subTest(msg='field: msk_top_regs.RX_F1_FreqWord.config_data'):
            fut = self.dut.RX_F1_FreqWord.config_data # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0x0
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=32,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=32,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=32,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.RX_F1_FreqWord.config_data.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_not_called()
                        write_callback_mock.assert_called_once_with(
                                    addr=32,
                                    width=32,
                                    accesswidth=self.dut.RX_F1_FreqWord.config_data.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0x0) | \
                                         (0xFFFFFFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.RX_F2_FreqWord.config_data
        with self.subTest(msg='field: msk_top_regs.RX_F2_FreqWord.config_data'):
            fut = self.dut.RX_F2_FreqWord.config_data # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0x0
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=36,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=36,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=36,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.RX_F2_FreqWord.config_data.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_not_called()
                        write_callback_mock.assert_called_once_with(
                                    addr=36,
                                    width=32,
                                    accesswidth=self.dut.RX_F2_FreqWord.config_data.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0x0) | \
                                         (0xFFFFFFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.LPF_Config_0.lpf_freeze
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.lpf_freeze'):
            fut = self.dut.LPF_Config_0.lpf_freeze # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFE
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x1
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x1) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.LPF_Config_0.lpf_freeze.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=self.dut.LPF_Config_0.lpf_freeze.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFE) | \
                                         (0x1 & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.LPF_Config_0.lpf_zero
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.lpf_zero'):
            fut = self.dut.LPF_Config_0.lpf_zero # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFD
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x2
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x2) >> 1
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.LPF_Config_0.lpf_zero.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=self.dut.LPF_Config_0.lpf_zero.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFD) | \
                                         (0x2 & (field_value << 1)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.LPF_Config_0.prbs_reserved
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.prbs_reserved'):
            fut = self.dut.LPF_Config_0.prbs_reserved # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFF03
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFC
                self.assertEqual(await fut.read(),
                                 0x3F)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFC) >> 2
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x3F + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x3F, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.LPF_Config_0.prbs_reserved.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=self.dut.LPF_Config_0.prbs_reserved.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFF03) | \
                                         (0xFC & (field_value << 2)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x3F + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.LPF_Config_0.lpf_alpha
        with self.subTest(msg='field: msk_top_regs.LPF_Config_0.lpf_alpha'):
            fut = self.dut.LPF_Config_0.lpf_alpha # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFF
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFF00
                self.assertEqual(await fut.read(),
                                 0xFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFF00) >> 8
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.LPF_Config_0.lpf_alpha.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=40,
                                    width=32,
                                    accesswidth=self.dut.LPF_Config_0.lpf_alpha.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFF) | \
                                         (0xFFFFFF00 & (field_value << 8)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.LPF_Config_1.i_gain
        with self.subTest(msg='field: msk_top_regs.LPF_Config_1.i_gain'):
            fut = self.dut.LPF_Config_1.i_gain # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFF000000
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.LPF_Config_1.i_gain.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=self.dut.LPF_Config_1.i_gain.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFF000000) | \
                                         (0xFFFFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.LPF_Config_1.i_shift
        with self.subTest(msg='field: msk_top_regs.LPF_Config_1.i_shift'):
            fut = self.dut.LPF_Config_1.i_shift # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFF
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFF000000
                self.assertEqual(await fut.read(),
                                 0xFF)
                read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFF000000) >> 24
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.LPF_Config_1.i_shift.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=44,
                                    width=32,
                                    accesswidth=self.dut.LPF_Config_1.i_shift.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFF) | \
                                         (0xFF000000 & (field_value << 24)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.Tx_Data_Width.data_width
        with self.subTest(msg='field: msk_top_regs.Tx_Data_Width.data_width'):
            fut = self.dut.Tx_Data_Width.data_width # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFF00
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFF
                self.assertEqual(await fut.read(),
                                 0xFF)
                read_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.Tx_Data_Width.data_width.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=48,
                                    width=32,
                                    accesswidth=self.dut.Tx_Data_Width.data_width.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFF00) | \
                                         (0xFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.Rx_Data_Width.data_width
        with self.subTest(msg='field: msk_top_regs.Rx_Data_Width.data_width'):
            fut = self.dut.Rx_Data_Width.data_width # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFF00
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFF
                self.assertEqual(await fut.read(),
                                 0xFF)
                read_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.Rx_Data_Width.data_width.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=52,
                                    width=32,
                                    accesswidth=self.dut.Rx_Data_Width.data_width.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFF00) | \
                                         (0xFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.PRBS_Control.prbs_sel
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_sel'):
            fut = self.dut.PRBS_Control.prbs_sel # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFE
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x1
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x1) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.PRBS_Control.prbs_sel.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=self.dut.PRBS_Control.prbs_sel.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFE) | \
                                         (0x1 & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.PRBS_Control.prbs_error_insert
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_error_insert'):
            fut = self.dut.PRBS_Control.prbs_error_insert # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.PRBS_Control.prbs_error_insert.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=self.dut.PRBS_Control.prbs_error_insert.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFD) | \
                                         (0x2 & (field_value << 1)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.PRBS_Control.prbs_clear
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_clear'):
            fut = self.dut.PRBS_Control.prbs_clear # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.PRBS_Control.prbs_clear.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=self.dut.PRBS_Control.prbs_clear.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFB) | \
                                         (0x4 & (field_value << 2)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.PRBS_Control.prbs_manual_sync
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_manual_sync'):
            fut = self.dut.PRBS_Control.prbs_manual_sync # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.PRBS_Control.prbs_manual_sync.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=self.dut.PRBS_Control.prbs_manual_sync.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFF7) | \
                                         (0x8 & (field_value << 3)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.PRBS_Control.prbs_reserved
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_reserved'):
            fut = self.dut.PRBS_Control.prbs_reserved # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFF000F
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFF0
                self.assertEqual(await fut.read(),
                                 0xFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFF0) >> 4
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.PRBS_Control.prbs_reserved.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=self.dut.PRBS_Control.prbs_reserved.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFF000F) | \
                                         (0xFFF0 & (field_value << 4)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.PRBS_Control.prbs_sync_threshold
        with self.subTest(msg='field: msk_top_regs.PRBS_Control.prbs_sync_threshold'):
            fut = self.dut.PRBS_Control.prbs_sync_threshold # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFF
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFF0000
                self.assertEqual(await fut.read(),
                                 0xFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFF0000) >> 16
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.PRBS_Control.prbs_sync_threshold.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=56,
                                    width=32,
                                    accesswidth=self.dut.PRBS_Control.prbs_sync_threshold.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFF) | \
                                         (0xFFFF0000 & (field_value << 16)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.PRBS_Initial_State.config_data
        with self.subTest(msg='field: msk_top_regs.PRBS_Initial_State.config_data'):
            fut = self.dut.PRBS_Initial_State.config_data # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0x0
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=60,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=60,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=60,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.PRBS_Initial_State.config_data.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_not_called()
                        write_callback_mock.assert_called_once_with(
                                    addr=60,
                                    width=32,
                                    accesswidth=self.dut.PRBS_Initial_State.config_data.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0x0) | \
                                         (0xFFFFFFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.PRBS_Polynomial.config_data
        with self.subTest(msg='field: msk_top_regs.PRBS_Polynomial.config_data'):
            fut = self.dut.PRBS_Polynomial.config_data # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0x0
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=64,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=64,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=64,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.PRBS_Polynomial.config_data.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_not_called()
                        write_callback_mock.assert_called_once_with(
                                    addr=64,
                                    width=32,
                                    accesswidth=self.dut.PRBS_Polynomial.config_data.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0x0) | \
                                         (0xFFFFFFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.PRBS_Error_Mask.config_data
        with self.subTest(msg='field: msk_top_regs.PRBS_Error_Mask.config_data'):
            fut = self.dut.PRBS_Error_Mask.config_data # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0x0
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=68,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=68,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=68,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.PRBS_Error_Mask.config_data.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_not_called()
                        write_callback_mock.assert_called_once_with(
                                    addr=68,
                                    width=32,
                                    accesswidth=self.dut.PRBS_Error_Mask.config_data.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0x0) | \
                                         (0xFFFFFFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.Rx_Sample_Discard.rx_sample_discard
        with self.subTest(msg='field: msk_top_regs.Rx_Sample_Discard.rx_sample_discard'):
            fut = self.dut.Rx_Sample_Discard.rx_sample_discard # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFF00
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFF
                self.assertEqual(await fut.read(),
                                 0xFF)
                read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.Rx_Sample_Discard.rx_sample_discard.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=self.dut.Rx_Sample_Discard.rx_sample_discard.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFF00) | \
                                         (0xFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.Rx_Sample_Discard.rx_nco_discard
        with self.subTest(msg='field: msk_top_regs.Rx_Sample_Discard.rx_nco_discard'):
            fut = self.dut.Rx_Sample_Discard.rx_nco_discard # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFF00FF
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFF00
                self.assertEqual(await fut.read(),
                                 0xFF)
                read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFF00) >> 8
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.Rx_Sample_Discard.rx_nco_discard.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=72,
                                    width=32,
                                    accesswidth=self.dut.Rx_Sample_Discard.rx_nco_discard.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFF00FF) | \
                                         (0xFF00 & (field_value << 8)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.LPF_Config_2.p_gain
        with self.subTest(msg='field: msk_top_regs.LPF_Config_2.p_gain'):
            fut = self.dut.LPF_Config_2.p_gain # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFF000000
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.LPF_Config_2.p_gain.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=self.dut.LPF_Config_2.p_gain.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFF000000) | \
                                         (0xFFFFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.LPF_Config_2.p_shift
        with self.subTest(msg='field: msk_top_regs.LPF_Config_2.p_shift'):
            fut = self.dut.LPF_Config_2.p_shift # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFF
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFF000000
                self.assertEqual(await fut.read(),
                                 0xFF)
                read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFF000000) >> 24
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.LPF_Config_2.p_shift.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=76,
                                    width=32,
                                    accesswidth=self.dut.LPF_Config_2.p_shift.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFF) | \
                                         (0xFF000000 & (field_value << 24)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena'):
            fut = self.dut.Tx_Sync_Ctrl.tx_sync_ena # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFE
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x1
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x1) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.Tx_Sync_Ctrl.tx_sync_ena.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=self.dut.Tx_Sync_Ctrl.tx_sync_ena.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFE) | \
                                         (0x1 & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.Tx_Sync_Ctrl.tx_sync_force
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_force'):
            fut = self.dut.Tx_Sync_Ctrl.tx_sync_force # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFD
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x2
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x2) >> 1
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.Tx_Sync_Ctrl.tx_sync_force.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=self.dut.Tx_Sync_Ctrl.tx_sync_force.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFD) | \
                                         (0x2 & (field_value << 1)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.Tx_Sync_Ctrl.tx_sync_f1
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f1'):
            fut = self.dut.Tx_Sync_Ctrl.tx_sync_f1 # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFFB
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x4
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x4) >> 2
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.Tx_Sync_Ctrl.tx_sync_f1.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=self.dut.Tx_Sync_Ctrl.tx_sync_f1.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFFB) | \
                                         (0x4 & (field_value << 2)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.Tx_Sync_Ctrl.tx_sync_f2
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f2'):
            fut = self.dut.Tx_Sync_Ctrl.tx_sync_f2 # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFF7
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x8
                self.assertEqual(await fut.read(),
                                 0x1)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x8) >> 3
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.Tx_Sync_Ctrl.tx_sync_f2.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=80,
                                    width=32,
                                    accesswidth=self.dut.Tx_Sync_Ctrl.tx_sync_f2.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFFFFF7) | \
                                         (0x8 & (field_value << 3)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt
        with self.subTest(msg='field: msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt'):
            fut = self.dut.Tx_Sync_Cnt.tx_sync_cnt # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFF000000
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFF
                self.assertEqual(await fut.read(),
                                 0xFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0xFFFFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0xFFFFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.Tx_Sync_Cnt.tx_sync_cnt.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=84,
                                    width=32,
                                    accesswidth=self.dut.Tx_Sync_Cnt.tx_sync_cnt.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFF000000) | \
                                         (0xFFFFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0xFFFFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.lowpass_ema_alpha1.alpha
        with self.subTest(msg='field: msk_top_regs.lowpass_ema_alpha1.alpha'):
            fut = self.dut.lowpass_ema_alpha1.alpha # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFC0000
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x3FFFF
                self.assertEqual(await fut.read(),
                                 0x3FFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x3FFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x3FFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x3FFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.lowpass_ema_alpha1.alpha.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=88,
                                    width=32,
                                    accesswidth=self.dut.lowpass_ema_alpha1.alpha.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFC0000) | \
                                         (0x3FFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x3FFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

        # test access operations (read and/or write) to field:
        # msk_top_regs.lowpass_ema_alpha2.alpha
        with self.subTest(msg='field: msk_top_regs.lowpass_ema_alpha2.alpha'):
            fut = self.dut.lowpass_ema_alpha2.alpha # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldAsyncReadOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable async field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFC0000
                self.assertEqual(await fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0x3FFFF
                self.assertEqual(await fut.read(),
                                 0x3FFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0x3FFFF) >> 0
                self.assertEqual(await fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                # check the write
                
                if not isinstance(fut, (FieldAsyncWriteOnly, FieldAsyncReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable async field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x3FFFF + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x3FFFF, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        await self.dut.lowpass_ema_alpha2.alpha.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)
                        
                        write_callback_mock.assert_called_once_with(
                                    addr=92,
                                    width=32,
                                    accesswidth=self.dut.lowpass_ema_alpha2.alpha.parent_register.accesswidth, # type: ignore[union-attr]
                                    data=(reg_base_value & 0xFFFC0000) | \
                                         (0x3FFFF & (field_value << 0)))
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    await fut.write(0x3FFFF + 1)

                with self.assertRaises(ValueError):
                    await fut.write(-1)

    

    async def test_register_read_fields(self) -> None:
        """
        Walk the register map and check every register read_fields method
        """
        reference_read_fields: dict[str, Union[bool, SystemRDLEnum, int]]
        
        with self.subTest(msg='register: msk_top_regs.Hash_ID_Low'):
            # test read_fields to register:
            # msk_top_regs.Hash_ID_Low
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'hash_id_lo' : await self.dut.Hash_ID_Low.hash_id_lo.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.Hash_ID_Low.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.Hash_ID_High'):
            # test read_fields to register:
            # msk_top_regs.Hash_ID_High
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'hash_id_hi' : await self.dut.Hash_ID_High.hash_id_hi.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.Hash_ID_High.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.MSK_Init'):
            # test read_fields to register:
            # msk_top_regs.MSK_Init
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFD) | (rand_field_value << 1)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFB) | (rand_field_value << 2)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'txrxinit' : await self.dut.MSK_Init.txrxinit.read(),
                                          'txinit' : await self.dut.MSK_Init.txinit.read(),
                                          'rxinit' : await self.dut.MSK_Init.rxinit.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.MSK_Init.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.MSK_Control'):
            # test read_fields to register:
            # msk_top_regs.MSK_Control
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFD) | (rand_field_value << 1)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFB) | (rand_field_value << 2)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFF7) | (rand_field_value << 3)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFEF) | (rand_field_value << 4)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'ptt' : await self.dut.MSK_Control.ptt.read(),
                                          'loopback_ena' : await self.dut.MSK_Control.loopback_ena.read(),
                                          'rx_invert' : await self.dut.MSK_Control.rx_invert.read(),
                                          'clear_counts' : await self.dut.MSK_Control.clear_counts.read(),
                                          'diff_encoder_loopback' : await self.dut.MSK_Control.diff_encoder_loopback.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.MSK_Control.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.MSK_Status'):
            # test read_fields to register:
            # msk_top_regs.MSK_Status
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFD) | (rand_field_value << 1)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFB) | (rand_field_value << 2)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFF7) | (rand_field_value << 3)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'demod_sync_lock' : await self.dut.MSK_Status.demod_sync_lock.read(),
                                          'tx_enable' : await self.dut.MSK_Status.tx_enable.read(),
                                          'rx_enable' : await self.dut.MSK_Status.rx_enable.read(),
                                          'tx_axis_valid' : await self.dut.MSK_Status.tx_axis_valid.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.MSK_Status.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.Fb_FreqWord'):
            # test read_fields to register:
            # msk_top_regs.Fb_FreqWord
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'config_data' : await self.dut.Fb_FreqWord.config_data.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.Fb_FreqWord.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.TX_F1_FreqWord'):
            # test read_fields to register:
            # msk_top_regs.TX_F1_FreqWord
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'config_data' : await self.dut.TX_F1_FreqWord.config_data.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.TX_F1_FreqWord.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.TX_F2_FreqWord'):
            # test read_fields to register:
            # msk_top_regs.TX_F2_FreqWord
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'config_data' : await self.dut.TX_F2_FreqWord.config_data.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.TX_F2_FreqWord.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.RX_F1_FreqWord'):
            # test read_fields to register:
            # msk_top_regs.RX_F1_FreqWord
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'config_data' : await self.dut.RX_F1_FreqWord.config_data.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.RX_F1_FreqWord.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.RX_F2_FreqWord'):
            # test read_fields to register:
            # msk_top_regs.RX_F2_FreqWord
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'config_data' : await self.dut.RX_F2_FreqWord.config_data.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.RX_F2_FreqWord.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0'):
            # test read_fields to register:
            # msk_top_regs.LPF_Config_0
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFD) | (rand_field_value << 1)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x3F + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF03) | (rand_field_value << 2)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFF) | (rand_field_value << 8)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'lpf_freeze' : await self.dut.LPF_Config_0.lpf_freeze.read(),
                                          'lpf_zero' : await self.dut.LPF_Config_0.lpf_zero.read(),
                                          'prbs_reserved' : await self.dut.LPF_Config_0.prbs_reserved.read(),
                                          'lpf_alpha' : await self.dut.LPF_Config_0.lpf_alpha.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.LPF_Config_0.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.LPF_Config_1'):
            # test read_fields to register:
            # msk_top_regs.LPF_Config_1
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFF000000) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF) | (rand_field_value << 24)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'i_gain' : await self.dut.LPF_Config_1.i_gain.read(),
                                          'i_shift' : await self.dut.LPF_Config_1.i_shift.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.LPF_Config_1.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.Tx_Data_Width'):
            # test read_fields to register:
            # msk_top_regs.Tx_Data_Width
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF00) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'data_width' : await self.dut.Tx_Data_Width.data_width.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.Tx_Data_Width.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.Rx_Data_Width'):
            # test read_fields to register:
            # msk_top_regs.Rx_Data_Width
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF00) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'data_width' : await self.dut.Rx_Data_Width.data_width.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.Rx_Data_Width.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.PRBS_Control'):
            # test read_fields to register:
            # msk_top_regs.PRBS_Control
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                
            
                
                    
                
            
                
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFF000F) | (rand_field_value << 4)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFF) | (rand_field_value << 16)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'prbs_sel' : await self.dut.PRBS_Control.prbs_sel.read(),
                                          'prbs_reserved' : await self.dut.PRBS_Control.prbs_reserved.read(),
                                          'prbs_sync_threshold' : await self.dut.PRBS_Control.prbs_sync_threshold.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.PRBS_Control.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.PRBS_Initial_State'):
            # test read_fields to register:
            # msk_top_regs.PRBS_Initial_State
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'config_data' : await self.dut.PRBS_Initial_State.config_data.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.PRBS_Initial_State.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.PRBS_Polynomial'):
            # test read_fields to register:
            # msk_top_regs.PRBS_Polynomial
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'config_data' : await self.dut.PRBS_Polynomial.config_data.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.PRBS_Polynomial.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.PRBS_Error_Mask'):
            # test read_fields to register:
            # msk_top_regs.PRBS_Error_Mask
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'config_data' : await self.dut.PRBS_Error_Mask.config_data.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.PRBS_Error_Mask.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.Rx_Sample_Discard'):
            # test read_fields to register:
            # msk_top_regs.Rx_Sample_Discard
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF00) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFF00FF) | (rand_field_value << 8)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'rx_sample_discard' : await self.dut.Rx_Sample_Discard.rx_sample_discard.read(),
                                          'rx_nco_discard' : await self.dut.Rx_Sample_Discard.rx_nco_discard.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.Rx_Sample_Discard.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.LPF_Config_2'):
            # test read_fields to register:
            # msk_top_regs.LPF_Config_2
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFF000000) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF) | (rand_field_value << 24)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'p_gain' : await self.dut.LPF_Config_2.p_gain.read(),
                                          'p_shift' : await self.dut.LPF_Config_2.p_shift.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.LPF_Config_2.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl'):
            # test read_fields to register:
            # msk_top_regs.Tx_Sync_Ctrl
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFD) | (rand_field_value << 1)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFB) | (rand_field_value << 2)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFF7) | (rand_field_value << 3)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'tx_sync_ena' : await self.dut.Tx_Sync_Ctrl.tx_sync_ena.read(),
                                          'tx_sync_force' : await self.dut.Tx_Sync_Ctrl.tx_sync_force.read(),
                                          'tx_sync_f1' : await self.dut.Tx_Sync_Ctrl.tx_sync_f1.read(),
                                          'tx_sync_f2' : await self.dut.Tx_Sync_Ctrl.tx_sync_f2.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.Tx_Sync_Ctrl.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Cnt'):
            # test read_fields to register:
            # msk_top_regs.Tx_Sync_Cnt
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFF000000) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'tx_sync_cnt' : await self.dut.Tx_Sync_Cnt.tx_sync_cnt.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.Tx_Sync_Cnt.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha1'):
            # test read_fields to register:
            # msk_top_regs.lowpass_ema_alpha1
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x3FFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFC0000) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'alpha' : await self.dut.lowpass_ema_alpha1.alpha.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.lowpass_ema_alpha1.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha2'):
            # test read_fields to register:
            # msk_top_regs.lowpass_ema_alpha2
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x3FFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFC0000) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'alpha' : await self.dut.lowpass_ema_alpha2.alpha.read()
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(await self.dut.lowpass_ema_alpha2.read_fields(),
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()

    async def test_register_read_context_manager(self) -> None:
        """
        Walk the register map and check every register read_fields method
        """
        reference_read_fields: dict[str, Union[bool, SystemRDLEnum, int]]
        
        # test context manager to register:
        # msk_top_regs.Hash_ID_Low
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.Hash_ID_Low'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'hash_id_lo' : await self.dut.Hash_ID_Low.hash_id_lo.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.Hash_ID_Low.single_read() as reg_context: # type: ignore[union-attr]
                    self.assertEqual(reference_read_fields['hash_id_lo'],
                                      await reg_context.get_child_by_system_rdl_name('hash_id_lo').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.Hash_ID_High
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.Hash_ID_High'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'hash_id_hi' : await self.dut.Hash_ID_High.hash_id_hi.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.Hash_ID_High.single_read() as reg_context: # type: ignore[union-attr]
                    self.assertEqual(reference_read_fields['hash_id_hi'],
                                      await reg_context.get_child_by_system_rdl_name('hash_id_hi').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.MSK_Init
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.MSK_Init'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFD) | (rand_field_value << 1)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFB) | (rand_field_value << 2)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'txrxinit' : await self.dut.MSK_Init.txrxinit.read(),  # type: ignore[union-attr]
                                          'txinit' : await self.dut.MSK_Init.txinit.read(),  # type: ignore[union-attr]
                                          'rxinit' : await self.dut.MSK_Init.rxinit.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.MSK_Init.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['txrxinit'],
                                      await reg_context.get_child_by_system_rdl_name('txrxinit').read()
                                     )
                    self.assertEqual(reference_read_fields['txinit'],
                                      await reg_context.get_child_by_system_rdl_name('txinit').read()
                                     )
                    self.assertEqual(reference_read_fields['rxinit'],
                                      await reg_context.get_child_by_system_rdl_name('rxinit').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.MSK_Control
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.MSK_Control'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFD) | (rand_field_value << 1)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFB) | (rand_field_value << 2)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFF7) | (rand_field_value << 3)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFEF) | (rand_field_value << 4)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'ptt' : await self.dut.MSK_Control.ptt.read(),  # type: ignore[union-attr]
                                          'loopback_ena' : await self.dut.MSK_Control.loopback_ena.read(),  # type: ignore[union-attr]
                                          'rx_invert' : await self.dut.MSK_Control.rx_invert.read(),  # type: ignore[union-attr]
                                          'clear_counts' : await self.dut.MSK_Control.clear_counts.read(),  # type: ignore[union-attr]
                                          'diff_encoder_loopback' : await self.dut.MSK_Control.diff_encoder_loopback.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.MSK_Control.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['ptt'],
                                      await reg_context.get_child_by_system_rdl_name('ptt').read()
                                     )
                    self.assertEqual(reference_read_fields['loopback_ena'],
                                      await reg_context.get_child_by_system_rdl_name('loopback_ena').read()
                                     )
                    self.assertEqual(reference_read_fields['rx_invert'],
                                      await reg_context.get_child_by_system_rdl_name('rx_invert').read()
                                     )
                    self.assertEqual(reference_read_fields['clear_counts'],
                                      await reg_context.get_child_by_system_rdl_name('clear_counts').read()
                                     )
                    self.assertEqual(reference_read_fields['diff_encoder_loopback'],
                                      await reg_context.get_child_by_system_rdl_name('diff_encoder_loopback').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.MSK_Status
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.MSK_Status'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFD) | (rand_field_value << 1)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFB) | (rand_field_value << 2)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFF7) | (rand_field_value << 3)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'demod_sync_lock' : await self.dut.MSK_Status.demod_sync_lock.read(),  # type: ignore[union-attr]
                                          'tx_enable' : await self.dut.MSK_Status.tx_enable.read(),  # type: ignore[union-attr]
                                          'rx_enable' : await self.dut.MSK_Status.rx_enable.read(),  # type: ignore[union-attr]
                                          'tx_axis_valid' : await self.dut.MSK_Status.tx_axis_valid.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.MSK_Status.single_read() as reg_context: # type: ignore[union-attr]
                    self.assertEqual(reference_read_fields['demod_sync_lock'],
                                      await reg_context.get_child_by_system_rdl_name('demod_sync_lock').read()
                                     )
                    self.assertEqual(reference_read_fields['tx_enable'],
                                      await reg_context.get_child_by_system_rdl_name('tx_enable').read()
                                     )
                    self.assertEqual(reference_read_fields['rx_enable'],
                                      await reg_context.get_child_by_system_rdl_name('rx_enable').read()
                                     )
                    self.assertEqual(reference_read_fields['tx_axis_valid'],
                                      await reg_context.get_child_by_system_rdl_name('tx_axis_valid').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.Fb_FreqWord
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.Fb_FreqWord'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'config_data' : await self.dut.Fb_FreqWord.config_data.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.Fb_FreqWord.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['config_data'],
                                      await reg_context.get_child_by_system_rdl_name('config_data').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.TX_F1_FreqWord
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.TX_F1_FreqWord'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'config_data' : await self.dut.TX_F1_FreqWord.config_data.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.TX_F1_FreqWord.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['config_data'],
                                      await reg_context.get_child_by_system_rdl_name('config_data').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.TX_F2_FreqWord
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.TX_F2_FreqWord'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'config_data' : await self.dut.TX_F2_FreqWord.config_data.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.TX_F2_FreqWord.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['config_data'],
                                      await reg_context.get_child_by_system_rdl_name('config_data').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.RX_F1_FreqWord
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.RX_F1_FreqWord'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'config_data' : await self.dut.RX_F1_FreqWord.config_data.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.RX_F1_FreqWord.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['config_data'],
                                      await reg_context.get_child_by_system_rdl_name('config_data').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.RX_F2_FreqWord
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.RX_F2_FreqWord'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'config_data' : await self.dut.RX_F2_FreqWord.config_data.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.RX_F2_FreqWord.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['config_data'],
                                      await reg_context.get_child_by_system_rdl_name('config_data').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.LPF_Config_0
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFD) | (rand_field_value << 1)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x3F + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF03) | (rand_field_value << 2)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFF) | (rand_field_value << 8)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'lpf_freeze' : await self.dut.LPF_Config_0.lpf_freeze.read(),  # type: ignore[union-attr]
                                          'lpf_zero' : await self.dut.LPF_Config_0.lpf_zero.read(),  # type: ignore[union-attr]
                                          'prbs_reserved' : await self.dut.LPF_Config_0.prbs_reserved.read(),  # type: ignore[union-attr]
                                          'lpf_alpha' : await self.dut.LPF_Config_0.lpf_alpha.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.LPF_Config_0.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['lpf_freeze'],
                                      await reg_context.get_child_by_system_rdl_name('lpf_freeze').read()
                                     )
                    self.assertEqual(reference_read_fields['lpf_zero'],
                                      await reg_context.get_child_by_system_rdl_name('lpf_zero').read()
                                     )
                    self.assertEqual(reference_read_fields['prbs_reserved'],
                                      await reg_context.get_child_by_system_rdl_name('prbs_reserved').read()
                                     )
                    self.assertEqual(reference_read_fields['lpf_alpha'],
                                      await reg_context.get_child_by_system_rdl_name('lpf_alpha').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.LPF_Config_1
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.LPF_Config_1'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFF000000) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF) | (rand_field_value << 24)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'i_gain' : await self.dut.LPF_Config_1.i_gain.read(),  # type: ignore[union-attr]
                                          'i_shift' : await self.dut.LPF_Config_1.i_shift.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.LPF_Config_1.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['i_gain'],
                                      await reg_context.get_child_by_system_rdl_name('i_gain').read()
                                     )
                    self.assertEqual(reference_read_fields['i_shift'],
                                      await reg_context.get_child_by_system_rdl_name('i_shift').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.Tx_Data_Width
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.Tx_Data_Width'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF00) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'data_width' : await self.dut.Tx_Data_Width.data_width.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.Tx_Data_Width.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['data_width'],
                                      await reg_context.get_child_by_system_rdl_name('data_width').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.Rx_Data_Width
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.Rx_Data_Width'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF00) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'data_width' : await self.dut.Rx_Data_Width.data_width.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.Rx_Data_Width.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['data_width'],
                                      await reg_context.get_child_by_system_rdl_name('data_width').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.PRBS_Control
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.PRBS_Control'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                
            
                
                    
                
            
                
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFF000F) | (rand_field_value << 4)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFF) | (rand_field_value << 16)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'prbs_sel' : await self.dut.PRBS_Control.prbs_sel.read(),  # type: ignore[union-attr]
                                          'prbs_reserved' : await self.dut.PRBS_Control.prbs_reserved.read(),  # type: ignore[union-attr]
                                          'prbs_sync_threshold' : await self.dut.PRBS_Control.prbs_sync_threshold.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.PRBS_Control.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['prbs_sel'],
                                      await reg_context.get_child_by_system_rdl_name('prbs_sel').read()
                                     )
                    self.assertEqual(reference_read_fields['prbs_reserved'],
                                      await reg_context.get_child_by_system_rdl_name('prbs_reserved').read()
                                     )
                    self.assertEqual(reference_read_fields['prbs_sync_threshold'],
                                      await reg_context.get_child_by_system_rdl_name('prbs_sync_threshold').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.PRBS_Initial_State
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.PRBS_Initial_State'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'config_data' : await self.dut.PRBS_Initial_State.config_data.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.PRBS_Initial_State.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['config_data'],
                                      await reg_context.get_child_by_system_rdl_name('config_data').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.PRBS_Polynomial
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.PRBS_Polynomial'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'config_data' : await self.dut.PRBS_Polynomial.config_data.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.PRBS_Polynomial.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['config_data'],
                                      await reg_context.get_child_by_system_rdl_name('config_data').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.PRBS_Error_Mask
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.PRBS_Error_Mask'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0x0) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'config_data' : await self.dut.PRBS_Error_Mask.config_data.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.PRBS_Error_Mask.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['config_data'],
                                      await reg_context.get_child_by_system_rdl_name('config_data').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.Rx_Sample_Discard
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.Rx_Sample_Discard'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF00) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFF00FF) | (rand_field_value << 8)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'rx_sample_discard' : await self.dut.Rx_Sample_Discard.rx_sample_discard.read(),  # type: ignore[union-attr]
                                          'rx_nco_discard' : await self.dut.Rx_Sample_Discard.rx_nco_discard.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.Rx_Sample_Discard.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['rx_sample_discard'],
                                      await reg_context.get_child_by_system_rdl_name('rx_sample_discard').read()
                                     )
                    self.assertEqual(reference_read_fields['rx_nco_discard'],
                                      await reg_context.get_child_by_system_rdl_name('rx_nco_discard').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.LPF_Config_2
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.LPF_Config_2'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFF000000) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFF) | (rand_field_value << 24)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'p_gain' : await self.dut.LPF_Config_2.p_gain.read(),  # type: ignore[union-attr]
                                          'p_shift' : await self.dut.LPF_Config_2.p_shift.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.LPF_Config_2.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['p_gain'],
                                      await reg_context.get_child_by_system_rdl_name('p_gain').read()
                                     )
                    self.assertEqual(reference_read_fields['p_shift'],
                                      await reg_context.get_child_by_system_rdl_name('p_shift').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.Tx_Sync_Ctrl
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFE) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFD) | (rand_field_value << 1)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFFB) | (rand_field_value << 2)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0x1 + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFF7) | (rand_field_value << 3)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'tx_sync_ena' : await self.dut.Tx_Sync_Ctrl.tx_sync_ena.read(),  # type: ignore[union-attr]
                                          'tx_sync_force' : await self.dut.Tx_Sync_Ctrl.tx_sync_force.read(),  # type: ignore[union-attr]
                                          'tx_sync_f1' : await self.dut.Tx_Sync_Ctrl.tx_sync_f1.read(),  # type: ignore[union-attr]
                                          'tx_sync_f2' : await self.dut.Tx_Sync_Ctrl.tx_sync_f2.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.Tx_Sync_Ctrl.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['tx_sync_ena'],
                                      await reg_context.get_child_by_system_rdl_name('tx_sync_ena').read()
                                     )
                    self.assertEqual(reference_read_fields['tx_sync_force'],
                                      await reg_context.get_child_by_system_rdl_name('tx_sync_force').read()
                                     )
                    self.assertEqual(reference_read_fields['tx_sync_f1'],
                                      await reg_context.get_child_by_system_rdl_name('tx_sync_f1').read()
                                     )
                    self.assertEqual(reference_read_fields['tx_sync_f2'],
                                      await reg_context.get_child_by_system_rdl_name('tx_sync_f2').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.Tx_Sync_Cnt
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Cnt'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFF000000) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'tx_sync_cnt' : await self.dut.Tx_Sync_Cnt.tx_sync_cnt.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.Tx_Sync_Cnt.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['tx_sync_cnt'],
                                      await reg_context.get_child_by_system_rdl_name('tx_sync_cnt').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.lowpass_ema_alpha1
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha1'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x3FFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFC0000) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'alpha' : await self.dut.lowpass_ema_alpha1.alpha.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.lowpass_ema_alpha1.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['alpha'],
                                      await reg_context.get_child_by_system_rdl_name('alpha').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()
        # test context manager to register:
        # msk_top_regs.lowpass_ema_alpha2
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha2'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0x3FFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFC0000) | (rand_field_value << 0)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'alpha' : await self.dut.lowpass_ema_alpha2.alpha.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                async with self.dut.lowpass_ema_alpha2.single_read_modify_write(skip_write=True) as reg_context: # type: ignore[union-attr]
                
                    self.assertEqual(reference_read_fields['alpha'],
                                      await reg_context.get_child_by_system_rdl_name('alpha').read()
                                     )
                    pass

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()

    async def test_register_write_context_manager(self) -> None:
        """
        Test the read modify write context manager
        """
        async def write_field_combinations(reg: RegAsyncReadWrite, writable_fields:list[str]) -> None:
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:
                # fix for #196 (excessive test time) if the number of fields is greater than 4
                # the combinations are reduced to only tests combinations of three plus the full
                # set
                if len(writable_fields) > 4:
                    perms_iterator: Iterable[int] = chain(range(1,4), [len(writable_fields)])
                else:
                    perms_iterator = range(1, len(writable_fields) + 1)
                for fields_to_write in chain.from_iterable((combinations(writable_fields, perms) for perms in perms_iterator)):
                    field_values: dict[str, Union[bool, SystemRDLEnum, int]] = {}
                    expected_value = 0
                    for field_str in fields_to_write:
                        field = getattr(reg, field_str)
                        if hasattr(field, 'enum_cls'):
                            rand_enum_value = random_enum_reg_value(field.enum_cls)
                            rand_field_value = rand_enum_value.value
                            field_values[field_str] = rand_enum_value
                        else:
                            rand_field_value = random.randrange(0, field.max_value + 1)
                            field_values[field_str] = rand_field_value

                        if field.msb == field.high:
                            expected_value = ( expected_value & field.inverse_bitmask ) | (rand_field_value << field.low)
                        elif field.msb == field.low:
                            expected_value = ( expected_value & field.inverse_bitmask ) | (self._reverse_bits(value=rand_field_value, number_bits=field.width) << field.low)
                        else:
                            raise RuntimeError('invalid msb/lsb high/low combination')

                    # read/write without verify
                    read_callback_mock.return_value = 0
                    async with reg.single_read_modify_write(verify=False) as reg_session:
                        for field_name, field_value in field_values.items():
                            field = getattr(reg_session, field_name)
                            await field.write(field_value)

                    write_callback_mock.assert_called_once_with(
                            addr=reg.address,
                            width=reg.width,
                            accesswidth=reg.accesswidth,
                            data=expected_value)
                    read_callback_mock.assert_called_once()
                    write_callback_mock.reset_mock()
                    read_callback_mock.reset_mock()

                    # read/write/verify pass
                    async with reg.single_read_modify_write(verify=True) as reg_session:
                        for field_name, field_value in field_values.items():
                            field = getattr(reg_session, field_name)
                            await field.write(field_value)
                        read_callback_mock.return_value = expected_value

                    write_callback_mock.assert_called_once_with(
                            addr=reg.address,
                            width=reg.width,
                            accesswidth=reg.accesswidth,
                            data=expected_value)
                    self.assertEqual(read_callback_mock.call_count, 2)
                    write_callback_mock.reset_mock()
                    read_callback_mock.reset_mock()

                    # read/write/verify pass
                    with self.assertRaises(RegisterWriteVerifyError) as context:
                        async with reg.single_read_modify_write(verify=True) as reg_session:
                            for field_name, field_value in field_values.items():
                                field = getattr(reg_session, field_name)
                                await field.write(field_value)
                            read_callback_mock.return_value = expected_value ^ reg_session.max_value

                    write_callback_mock.reset_mock()
                    read_callback_mock.reset_mock()

        
        with self.subTest(msg='register: msk_top_regs.MSK_Init'):
            await write_field_combinations(reg=self.dut.MSK_Init,
                               writable_fields = [ 'txrxinit',
                                                   'txinit',
                                                   'rxinit'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.MSK_Control'):
            await write_field_combinations(reg=self.dut.MSK_Control,
                               writable_fields = [ 'ptt',
                                                   'loopback_ena',
                                                   'rx_invert',
                                                   'clear_counts',
                                                   'diff_encoder_loopback'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.Fb_FreqWord'):
            await write_field_combinations(reg=self.dut.Fb_FreqWord,
                               writable_fields = [ 'config_data'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.TX_F1_FreqWord'):
            await write_field_combinations(reg=self.dut.TX_F1_FreqWord,
                               writable_fields = [ 'config_data'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.TX_F2_FreqWord'):
            await write_field_combinations(reg=self.dut.TX_F2_FreqWord,
                               writable_fields = [ 'config_data'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.RX_F1_FreqWord'):
            await write_field_combinations(reg=self.dut.RX_F1_FreqWord,
                               writable_fields = [ 'config_data'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.RX_F2_FreqWord'):
            await write_field_combinations(reg=self.dut.RX_F2_FreqWord,
                               writable_fields = [ 'config_data'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0'):
            await write_field_combinations(reg=self.dut.LPF_Config_0,
                               writable_fields = [ 'lpf_freeze',
                                                   'lpf_zero',
                                                   'prbs_reserved',
                                                   'lpf_alpha'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.LPF_Config_1'):
            await write_field_combinations(reg=self.dut.LPF_Config_1,
                               writable_fields = [ 'i_gain',
                                                   'i_shift'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.Tx_Data_Width'):
            await write_field_combinations(reg=self.dut.Tx_Data_Width,
                               writable_fields = [ 'data_width'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.Rx_Data_Width'):
            await write_field_combinations(reg=self.dut.Rx_Data_Width,
                               writable_fields = [ 'data_width'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.PRBS_Control'):
            await write_field_combinations(reg=self.dut.PRBS_Control,
                               writable_fields = [ 'prbs_sel',
                                                   'prbs_error_insert',
                                                   'prbs_clear',
                                                   'prbs_manual_sync',
                                                   'prbs_reserved',
                                                   'prbs_sync_threshold'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.PRBS_Initial_State'):
            await write_field_combinations(reg=self.dut.PRBS_Initial_State,
                               writable_fields = [ 'config_data'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.PRBS_Polynomial'):
            await write_field_combinations(reg=self.dut.PRBS_Polynomial,
                               writable_fields = [ 'config_data'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.PRBS_Error_Mask'):
            await write_field_combinations(reg=self.dut.PRBS_Error_Mask,
                               writable_fields = [ 'config_data'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.Rx_Sample_Discard'):
            await write_field_combinations(reg=self.dut.Rx_Sample_Discard,
                               writable_fields = [ 'rx_sample_discard',
                                                   'rx_nco_discard'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.LPF_Config_2'):
            await write_field_combinations(reg=self.dut.LPF_Config_2,
                               writable_fields = [ 'p_gain',
                                                   'p_shift'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl'):
            await write_field_combinations(reg=self.dut.Tx_Sync_Ctrl,
                               writable_fields = [ 'tx_sync_ena',
                                                   'tx_sync_force',
                                                   'tx_sync_f1',
                                                   'tx_sync_f2'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Cnt'):
            await write_field_combinations(reg=self.dut.Tx_Sync_Cnt,
                               writable_fields = [ 'tx_sync_cnt'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha1'):
            await write_field_combinations(reg=self.dut.lowpass_ema_alpha1,
                               writable_fields = [ 'alpha'
                                                   ])
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha2'):
            await write_field_combinations(reg=self.dut.lowpass_ema_alpha2,
                               writable_fields = [ 'alpha'
                                                   ])

    async def test_register_write_fields(self) -> None:
        """
        Walk the register map and check every register write_fields method
        """
        rand_enum_value:SystemRDLEnum
        async def write_field_combinations(reg: RegAsyncReadWrite, writable_fields:list[str]) -> None:
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:
                # fix for #196 (excessive test time) if the number of fields is greater than 4
                # the combinations are reduced to only tests combinations of three plus the full
                # set
                if len(writable_fields) > 4:
                    perms_iterator: Iterable[int] = chain(range(1,4), [len(writable_fields)])
                else:
                    perms_iterator = range(1, len(writable_fields) + 1)
                for fields_to_write in chain.from_iterable((combinations(writable_fields, perms) for perms in perms_iterator)):
                    kwargs: dict[str, Union[bool, SystemRDLEnum, int]] = {}
                    expected_value = 0
                    for field_str in fields_to_write:
                        field = getattr(reg, field_str)
                        if hasattr(field, 'enum_cls'):
                            rand_enum_value = random_enum_reg_value(field.enum_cls)
                            rand_field_value = rand_enum_value.value
                            kwargs[field_str] = rand_enum_value
                        else:
                            rand_field_value = random.randrange(0, field.max_value + 1)
                            kwargs[field_str] = rand_field_value

                        if field.msb == field.high:
                            expected_value = ( expected_value & field.inverse_bitmask ) | (rand_field_value << field.low)
                        elif field.msb == field.low:
                            expected_value = ( expected_value & field.inverse_bitmask ) | (self._reverse_bits(value=rand_field_value, number_bits=field.width) << field.low)
                        else:
                            raise RuntimeError('invalid msb/lsb high/low combination')

                    await reg.write_fields(**kwargs)
                    write_callback_mock.assert_called_once_with(
                            addr=reg.address,
                            width=reg.width,
                            accesswidth=reg.accesswidth,
                            data=expected_value)
                    read_callback_mock.assert_called_once()
                    write_callback_mock.reset_mock()
                    read_callback_mock.reset_mock()

        kwargs : dict[str, Union[bool, SystemRDLEnum, int]]

        
        with self.subTest(msg='register: msk_top_regs.MSK_Init'):
            # test read_fields to register:
            # msk_top_regs.MSK_Init
            await write_field_combinations(reg=self.dut.MSK_Init,
                                       writable_fields = [ 'txrxinit',
                                                           'txinit',
                                                           'rxinit'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.MSK_Control'):
            # test read_fields to register:
            # msk_top_regs.MSK_Control
            await write_field_combinations(reg=self.dut.MSK_Control,
                                       writable_fields = [ 'ptt',
                                                           'loopback_ena',
                                                           'rx_invert',
                                                           'clear_counts',
                                                           'diff_encoder_loopback'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.Fb_FreqWord'):
            # test read_fields to register:
            # msk_top_regs.Fb_FreqWord
            await write_field_combinations(reg=self.dut.Fb_FreqWord,
                                       writable_fields = [ 'config_data'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.TX_F1_FreqWord'):
            # test read_fields to register:
            # msk_top_regs.TX_F1_FreqWord
            await write_field_combinations(reg=self.dut.TX_F1_FreqWord,
                                       writable_fields = [ 'config_data'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.TX_F2_FreqWord'):
            # test read_fields to register:
            # msk_top_regs.TX_F2_FreqWord
            await write_field_combinations(reg=self.dut.TX_F2_FreqWord,
                                       writable_fields = [ 'config_data'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.RX_F1_FreqWord'):
            # test read_fields to register:
            # msk_top_regs.RX_F1_FreqWord
            await write_field_combinations(reg=self.dut.RX_F1_FreqWord,
                                       writable_fields = [ 'config_data'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.RX_F2_FreqWord'):
            # test read_fields to register:
            # msk_top_regs.RX_F2_FreqWord
            await write_field_combinations(reg=self.dut.RX_F2_FreqWord,
                                       writable_fields = [ 'config_data'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0'):
            # test read_fields to register:
            # msk_top_regs.LPF_Config_0
            await write_field_combinations(reg=self.dut.LPF_Config_0,
                                       writable_fields = [ 'lpf_freeze',
                                                           'lpf_zero',
                                                           'prbs_reserved',
                                                           'lpf_alpha'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_1'):
            # test read_fields to register:
            # msk_top_regs.LPF_Config_1
            await write_field_combinations(reg=self.dut.LPF_Config_1,
                                       writable_fields = [ 'i_gain',
                                                           'i_shift'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.Tx_Data_Width'):
            # test read_fields to register:
            # msk_top_regs.Tx_Data_Width
            await write_field_combinations(reg=self.dut.Tx_Data_Width,
                                       writable_fields = [ 'data_width'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.Rx_Data_Width'):
            # test read_fields to register:
            # msk_top_regs.Rx_Data_Width
            await write_field_combinations(reg=self.dut.Rx_Data_Width,
                                       writable_fields = [ 'data_width'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Control'):
            # test read_fields to register:
            # msk_top_regs.PRBS_Control
            await write_field_combinations(reg=self.dut.PRBS_Control,
                                       writable_fields = [ 'prbs_sel',
                                                           'prbs_error_insert',
                                                           'prbs_clear',
                                                           'prbs_manual_sync',
                                                           'prbs_reserved',
                                                           'prbs_sync_threshold'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Initial_State'):
            # test read_fields to register:
            # msk_top_regs.PRBS_Initial_State
            await write_field_combinations(reg=self.dut.PRBS_Initial_State,
                                       writable_fields = [ 'config_data'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Polynomial'):
            # test read_fields to register:
            # msk_top_regs.PRBS_Polynomial
            await write_field_combinations(reg=self.dut.PRBS_Polynomial,
                                       writable_fields = [ 'config_data'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.PRBS_Error_Mask'):
            # test read_fields to register:
            # msk_top_regs.PRBS_Error_Mask
            await write_field_combinations(reg=self.dut.PRBS_Error_Mask,
                                       writable_fields = [ 'config_data'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.Rx_Sample_Discard'):
            # test read_fields to register:
            # msk_top_regs.Rx_Sample_Discard
            await write_field_combinations(reg=self.dut.Rx_Sample_Discard,
                                       writable_fields = [ 'rx_sample_discard',
                                                           'rx_nco_discard'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.LPF_Config_2'):
            # test read_fields to register:
            # msk_top_regs.LPF_Config_2
            await write_field_combinations(reg=self.dut.LPF_Config_2,
                                       writable_fields = [ 'p_gain',
                                                           'p_shift'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl'):
            # test read_fields to register:
            # msk_top_regs.Tx_Sync_Ctrl
            await write_field_combinations(reg=self.dut.Tx_Sync_Ctrl,
                                       writable_fields = [ 'tx_sync_ena',
                                                           'tx_sync_force',
                                                           'tx_sync_f1',
                                                           'tx_sync_f2'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Cnt'):
            # test read_fields to register:
            # msk_top_regs.Tx_Sync_Cnt
            await write_field_combinations(reg=self.dut.Tx_Sync_Cnt,
                                       writable_fields = [ 'tx_sync_cnt'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha1'):
            # test read_fields to register:
            # msk_top_regs.lowpass_ema_alpha1
            await write_field_combinations(reg=self.dut.lowpass_ema_alpha1,
                                       writable_fields = [ 'alpha'
                                                           ])
            
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha2'):
            # test read_fields to register:
            # msk_top_regs.lowpass_ema_alpha2
            await write_field_combinations(reg=self.dut.lowpass_ema_alpha2,
                                       writable_fields = [ 'alpha'
                                                           ])
            

    

    def test_adding_attributes(self) -> None:
        """
        Walk the address map and attempt to set a new value on each node

        The attribute name: cppkbrgmgeloagvfgjjeiiushygirh was randomly generated to be unlikely to
        every be a attribute name

        """
        with self.subTest(msg='node: msk_top_regs.Hash_ID_Low'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Hash_ID_Low.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Hash_ID_High'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Hash_ID_High.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Init'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Init.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Control.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Status'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Status.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Fb_FreqWord'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Fb_FreqWord.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.TX_F1_FreqWord'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.TX_F1_FreqWord.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.TX_F2_FreqWord'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.TX_F2_FreqWord.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.RX_F1_FreqWord'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.RX_F1_FreqWord.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.RX_F2_FreqWord'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.RX_F2_FreqWord.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_0'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.LPF_Config_0.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_1'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.LPF_Config_1.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Data_Width'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Tx_Data_Width.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Data_Width'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Rx_Data_Width.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Control.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Initial_State'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Initial_State.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Polynomial'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Polynomial.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Error_Mask'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Error_Mask.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Rx_Sample_Discard.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_2'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.LPF_Config_2.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Tx_Sync_Ctrl.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Cnt'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Tx_Sync_Cnt.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha1'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.lowpass_ema_alpha1.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha2'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.lowpass_ema_alpha2.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Hash_ID_Low.hash_id_lo'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Hash_ID_Low.hash_id_lo.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Hash_ID_High.hash_id_hi'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Hash_ID_High.hash_id_hi.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Init.txrxinit'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Init.txrxinit.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Init.txinit'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Init.txinit.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Init.rxinit'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Init.rxinit.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control.ptt'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Control.ptt.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control.loopback_ena'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Control.loopback_ena.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control.rx_invert'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Control.rx_invert.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control.clear_counts'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Control.clear_counts.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Control.diff_encoder_loopback'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Control.diff_encoder_loopback.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Status.demod_sync_lock'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Status.demod_sync_lock.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Status.tx_enable'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Status.tx_enable.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Status.rx_enable'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Status.rx_enable.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.MSK_Status.tx_axis_valid'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.MSK_Status.tx_axis_valid.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Fb_FreqWord.config_data'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Fb_FreqWord.config_data.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.TX_F1_FreqWord.config_data'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.TX_F1_FreqWord.config_data.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.TX_F2_FreqWord.config_data'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.TX_F2_FreqWord.config_data.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.RX_F1_FreqWord.config_data'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.RX_F1_FreqWord.config_data.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.RX_F2_FreqWord.config_data'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.RX_F2_FreqWord.config_data.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_freeze'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.LPF_Config_0.lpf_freeze.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_zero'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.LPF_Config_0.lpf_zero.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.prbs_reserved'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.LPF_Config_0.prbs_reserved.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_0.lpf_alpha'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.LPF_Config_0.lpf_alpha.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_1.i_gain'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.LPF_Config_1.i_gain.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_1.i_shift'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.LPF_Config_1.i_shift.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Data_Width.data_width'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Tx_Data_Width.data_width.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Data_Width.data_width'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Rx_Data_Width.data_width.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_sel'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Control.prbs_sel.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_error_insert'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Control.prbs_error_insert.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_clear'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Control.prbs_clear.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_manual_sync'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Control.prbs_manual_sync.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_reserved'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Control.prbs_reserved.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Control.prbs_sync_threshold'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Control.prbs_sync_threshold.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Initial_State.config_data'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Initial_State.config_data.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Polynomial.config_data'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Polynomial.config_data.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.PRBS_Error_Mask.config_data'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.PRBS_Error_Mask.config_data.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard.rx_sample_discard'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Rx_Sample_Discard.rx_sample_discard.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Rx_Sample_Discard.rx_nco_discard'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Rx_Sample_Discard.rx_nco_discard.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_2.p_gain'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.LPF_Config_2.p_gain.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.LPF_Config_2.p_shift'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.LPF_Config_2.p_shift.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_ena'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Tx_Sync_Ctrl.tx_sync_ena.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_force'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Tx_Sync_Ctrl.tx_sync_force.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f1'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Tx_Sync_Ctrl.tx_sync_f1.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Ctrl.tx_sync_f2'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Tx_Sync_Ctrl.tx_sync_f2.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.Tx_Sync_Cnt.tx_sync_cnt'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.Tx_Sync_Cnt.tx_sync_cnt.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha1.alpha'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.lowpass_ema_alpha1.alpha.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: msk_top_regs.lowpass_ema_alpha2.alpha'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.lowpass_ema_alpha2.alpha.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        

    
    def test_top_traversal_iterators(self) -> None:
        
        expected_writable_regs: list[WritableAsyncRegister]
        expected_readable_regs: list[ReadableAsyncRegister]
        expected_memories:list[Union[MemoryAsyncReadOnly, MemoryAsyncWriteOnly, MemoryAsyncReadWrite]]

        
        expected_sections : list[Union[AsyncAddressMap, AsyncRegFile]]

        # check the readable registers
        expected_readable_regs = [self.dut.Hash_ID_Low, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.Hash_ID_High, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.MSK_Init, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.MSK_Control, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.MSK_Status, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.Fb_FreqWord, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.TX_F1_FreqWord, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.TX_F2_FreqWord, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.RX_F1_FreqWord, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.RX_F2_FreqWord, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.LPF_Config_0, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.LPF_Config_1, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.Tx_Data_Width, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.Rx_Data_Width, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.PRBS_Control, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.PRBS_Initial_State, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.PRBS_Polynomial, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.PRBS_Error_Mask, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.Rx_Sample_Discard, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.LPF_Config_2, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.Tx_Sync_Ctrl, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.Tx_Sync_Cnt, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.lowpass_ema_alpha1, # type: ignore[union-attr,list-item] 
                                        
                                    self.dut.lowpass_ema_alpha2, # type: ignore[union-attr,list-item] 
                                        
                                     ]
        readable_regs = []
        for readable_reg in self.dut.get_readable_registers(unroll=True):  # type: ignore[union-attr]
            self.assertIsInstance(readable_reg, (RegAsyncReadWrite, RegAsyncReadOnly))
            readable_regs.append(readable_reg)
        self.assertCountEqual(expected_readable_regs, readable_regs)
        
        expected_readable_regs = [self.dut.Hash_ID_Low, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Hash_ID_High, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.MSK_Init, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.MSK_Control, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.MSK_Status, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Fb_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.TX_F1_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.TX_F2_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.RX_F1_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.RX_F2_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.LPF_Config_0, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.LPF_Config_1, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Tx_Data_Width, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Rx_Data_Width, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Control, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Initial_State, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Polynomial, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Error_Mask, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Rx_Sample_Discard, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.LPF_Config_2, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Tx_Sync_Ctrl, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Tx_Sync_Cnt, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.lowpass_ema_alpha1, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.lowpass_ema_alpha2, # type: ignore[union-attr,list-item] 
                                       
                                    ]
        readable_regs = []
        for readable_reg in self.dut.get_readable_registers(unroll=False):  # type: ignore[union-attr]
            readable_regs.append(readable_reg)
        self.assertCountEqual(expected_readable_regs, readable_regs)

        # check the writable registers
        expected_writable_regs = [
                                       
                                   
                                       
                                   self.dut.MSK_Init, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.MSK_Control, # type: ignore[union-attr,list-item] 
                                       
                                   
                                       
                                   self.dut.Fb_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.TX_F1_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.TX_F2_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.RX_F1_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.RX_F2_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.LPF_Config_0, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.LPF_Config_1, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Tx_Data_Width, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Rx_Data_Width, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Control, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Initial_State, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Polynomial, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Error_Mask, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Rx_Sample_Discard, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.LPF_Config_2, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Tx_Sync_Ctrl, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Tx_Sync_Cnt, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.lowpass_ema_alpha1, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.lowpass_ema_alpha2, # type: ignore[union-attr,list-item] 
                                       
                                    ]
        writable_regs = []
        for writable_reg in self.dut.get_writable_registers(unroll=True):  # type: ignore[union-attr]
            self.assertIsInstance(writable_reg, (RegAsyncReadWrite, RegAsyncWriteOnly))
            writable_regs.append(writable_reg)
        self.assertCountEqual(expected_writable_regs, writable_regs)
        
        expected_writable_regs = [
                                       
                                   
                                       
                                   self.dut.MSK_Init, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.MSK_Control, # type: ignore[union-attr,list-item] 
                                       
                                   
                                       
                                   self.dut.Fb_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.TX_F1_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.TX_F2_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.RX_F1_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.RX_F2_FreqWord, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.LPF_Config_0, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.LPF_Config_1, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Tx_Data_Width, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Rx_Data_Width, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Control, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Initial_State, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Polynomial, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.PRBS_Error_Mask, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Rx_Sample_Discard, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.LPF_Config_2, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Tx_Sync_Ctrl, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.Tx_Sync_Cnt, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.lowpass_ema_alpha1, # type: ignore[union-attr,list-item] 
                                       
                                   self.dut.lowpass_ema_alpha2, # type: ignore[union-attr,list-item] 
                                       
                                    ]
        writable_regs = []
        for writable_reg in self.dut.get_writable_registers(unroll=False):  # type: ignore[union-attr]
            writable_regs.append(writable_reg)
        self.assertCountEqual(expected_writable_regs, writable_regs)

        # check the sections
        expected_sections = [
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                               ]
        sections = []
        for section in self.dut.get_sections(unroll=True):  # type: ignore[union-attr]
            self.assertIsInstance(section, (AsyncAddressMap, AsyncRegFile))
            sections.append(section)
        self.assertCountEqual(expected_sections, sections)
        
        expected_sections = [
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                               ]
        sections = []
        for section in self.dut.get_sections(unroll=False):  # type: ignore[union-attr]
            sections.append(section)
        self.assertCountEqual(expected_sections, sections)

        # check the memories
        expected_memories = [
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                               ]
        memories = []
        for memory in self.dut.get_memories(unroll=True):  # type: ignore[union-attr]
            self.assertIsInstance(memory, (MemoryAsyncReadOnly, MemoryAsyncWriteOnly, MemoryAsyncReadWrite))
            memories.append(memory)
        self.assertCountEqual(expected_memories, memories)
        
        expected_memories = [
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                              
                                  
                               ]
        memories = []
        for memory in self.dut.get_memories(unroll=False):  # type: ignore[union-attr]
            self.assertIsInstance(memory, (MemoryAsyncReadOnly, MemoryAsyncWriteOnly, MemoryAsyncReadWrite, MemoryAsyncReadOnlyArray, MemoryAsyncWriteOnlyArray, MemoryAsyncReadWriteArray))
            memories.append(memory)
        self.assertCountEqual(expected_memories, memories)

    

    

    

    

    

    def test_traversal_iterators(self) -> None:
        """
        Walk the address map and check that the iterators for each node as as expected
        """
        
        expected_writable_fields: list[Union[FieldAsyncWriteOnly, FieldAsyncReadWrite]]
        expected_readable_fields: list[Union[FieldAsyncReadOnly, FieldAsyncReadWrite]]
        expected_fields: list[Union[FieldAsyncWriteOnly, FieldAsyncReadOnly, FieldAsyncReadWrite]]
        expected_writable_regs: list[WritableAsyncRegister]
        expected_readable_regs: list[ReadableAsyncRegister]
        expected_memories:list[Union[MemoryAsyncReadOnly, MemoryAsyncWriteOnly, MemoryAsyncReadWrite]]

        
        expected_sections : list[Union[AsyncAddressMap, AsyncRegFile]]

        # test all the registers
        with self.subTest(msg='register: msk_top_regs.Hash_ID_Low'):
                
            expected_fields = [self.dut.Hash_ID_Low.hash_id_lo, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.Hash_ID_Low.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            # register should not have writable_fields attribute
            self.assertFalse(hasattr(self.dut.Hash_ID_Low, 'writable_fields')) # type: ignore[union-attr]
                    
                    
            expected_readable_fields = [self.dut.Hash_ID_Low.hash_id_lo, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.Hash_ID_Low.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.Hash_ID_High'):
                
            expected_fields = [self.dut.Hash_ID_High.hash_id_hi, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.Hash_ID_High.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            # register should not have writable_fields attribute
            self.assertFalse(hasattr(self.dut.Hash_ID_High, 'writable_fields')) # type: ignore[union-attr]
                    
                    
            expected_readable_fields = [self.dut.Hash_ID_High.hash_id_hi, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.Hash_ID_High.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.MSK_Init'):
                
            expected_fields = [self.dut.MSK_Init.txrxinit, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.MSK_Init.txinit, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.MSK_Init.rxinit, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.MSK_Init.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.MSK_Init.txrxinit, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Init.txinit, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Init.rxinit, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.MSK_Init.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.MSK_Init.txrxinit, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Init.txinit, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Init.rxinit, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.MSK_Init.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.MSK_Control'):
                
            expected_fields = [self.dut.MSK_Control.ptt, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.MSK_Control.loopback_ena, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.MSK_Control.rx_invert, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.MSK_Control.clear_counts, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.MSK_Control.diff_encoder_loopback, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.MSK_Control.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.MSK_Control.ptt, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Control.loopback_ena, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Control.rx_invert, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Control.clear_counts, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Control.diff_encoder_loopback, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.MSK_Control.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.MSK_Control.ptt, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Control.loopback_ena, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Control.rx_invert, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Control.clear_counts, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Control.diff_encoder_loopback, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.MSK_Control.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.MSK_Status'):
                
            expected_fields = [self.dut.MSK_Status.demod_sync_lock, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.MSK_Status.tx_enable, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.MSK_Status.rx_enable, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.MSK_Status.tx_axis_valid, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.MSK_Status.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            # register should not have writable_fields attribute
            self.assertFalse(hasattr(self.dut.MSK_Status, 'writable_fields')) # type: ignore[union-attr]
                    
                    
            expected_readable_fields = [self.dut.MSK_Status.demod_sync_lock, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Status.tx_enable, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Status.rx_enable, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.MSK_Status.tx_axis_valid, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.MSK_Status.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.Fb_FreqWord'):
                
            expected_fields = [self.dut.Fb_FreqWord.config_data, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.Fb_FreqWord.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.Fb_FreqWord.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.Fb_FreqWord.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.Fb_FreqWord.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.Fb_FreqWord.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.TX_F1_FreqWord'):
                
            expected_fields = [self.dut.TX_F1_FreqWord.config_data, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.TX_F1_FreqWord.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.TX_F1_FreqWord.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.TX_F1_FreqWord.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.TX_F1_FreqWord.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.TX_F1_FreqWord.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.TX_F2_FreqWord'):
                
            expected_fields = [self.dut.TX_F2_FreqWord.config_data, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.TX_F2_FreqWord.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.TX_F2_FreqWord.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.TX_F2_FreqWord.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.TX_F2_FreqWord.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.TX_F2_FreqWord.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.RX_F1_FreqWord'):
                
            expected_fields = [self.dut.RX_F1_FreqWord.config_data, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.RX_F1_FreqWord.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.RX_F1_FreqWord.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.RX_F1_FreqWord.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.RX_F1_FreqWord.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.RX_F1_FreqWord.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.RX_F2_FreqWord'):
                
            expected_fields = [self.dut.RX_F2_FreqWord.config_data, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.RX_F2_FreqWord.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.RX_F2_FreqWord.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.RX_F2_FreqWord.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.RX_F2_FreqWord.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.RX_F2_FreqWord.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.LPF_Config_0'):
                
            expected_fields = [self.dut.LPF_Config_0.lpf_freeze, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.LPF_Config_0.lpf_zero, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.LPF_Config_0.prbs_reserved, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.LPF_Config_0.lpf_alpha, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.LPF_Config_0.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.LPF_Config_0.lpf_freeze, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.LPF_Config_0.lpf_zero, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.LPF_Config_0.prbs_reserved, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.LPF_Config_0.lpf_alpha, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.LPF_Config_0.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.LPF_Config_0.lpf_freeze, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.LPF_Config_0.lpf_zero, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.LPF_Config_0.prbs_reserved, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.LPF_Config_0.lpf_alpha, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.LPF_Config_0.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.LPF_Config_1'):
                
            expected_fields = [self.dut.LPF_Config_1.i_gain, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.LPF_Config_1.i_shift, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.LPF_Config_1.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.LPF_Config_1.i_gain, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.LPF_Config_1.i_shift, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.LPF_Config_1.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.LPF_Config_1.i_gain, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.LPF_Config_1.i_shift, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.LPF_Config_1.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.Tx_Data_Width'):
                
            expected_fields = [self.dut.Tx_Data_Width.data_width, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.Tx_Data_Width.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.Tx_Data_Width.data_width, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.Tx_Data_Width.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.Tx_Data_Width.data_width, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.Tx_Data_Width.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.Rx_Data_Width'):
                
            expected_fields = [self.dut.Rx_Data_Width.data_width, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.Rx_Data_Width.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.Rx_Data_Width.data_width, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.Rx_Data_Width.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.Rx_Data_Width.data_width, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.Rx_Data_Width.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.PRBS_Control'):
                
            expected_fields = [self.dut.PRBS_Control.prbs_sel, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.PRBS_Control.prbs_error_insert, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.PRBS_Control.prbs_clear, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.PRBS_Control.prbs_manual_sync, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.PRBS_Control.prbs_reserved, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.PRBS_Control.prbs_sync_threshold, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.PRBS_Control.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.PRBS_Control.prbs_sel, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.PRBS_Control.prbs_error_insert, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.PRBS_Control.prbs_clear, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.PRBS_Control.prbs_manual_sync, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.PRBS_Control.prbs_reserved, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.PRBS_Control.prbs_sync_threshold, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.PRBS_Control.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.PRBS_Control.prbs_sel, # type: ignore[union-attr,list-item] 
                                            
                                         
                                            
                                         
                                            
                                         
                                            
                                         self.dut.PRBS_Control.prbs_reserved, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.PRBS_Control.prbs_sync_threshold, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.PRBS_Control.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.PRBS_Initial_State'):
                
            expected_fields = [self.dut.PRBS_Initial_State.config_data, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.PRBS_Initial_State.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.PRBS_Initial_State.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.PRBS_Initial_State.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.PRBS_Initial_State.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.PRBS_Initial_State.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.PRBS_Polynomial'):
                
            expected_fields = [self.dut.PRBS_Polynomial.config_data, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.PRBS_Polynomial.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.PRBS_Polynomial.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.PRBS_Polynomial.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.PRBS_Polynomial.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.PRBS_Polynomial.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.PRBS_Error_Mask'):
                
            expected_fields = [self.dut.PRBS_Error_Mask.config_data, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.PRBS_Error_Mask.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.PRBS_Error_Mask.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.PRBS_Error_Mask.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.PRBS_Error_Mask.config_data, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.PRBS_Error_Mask.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.Rx_Sample_Discard'):
                
            expected_fields = [self.dut.Rx_Sample_Discard.rx_sample_discard, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.Rx_Sample_Discard.rx_nco_discard, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.Rx_Sample_Discard.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.Rx_Sample_Discard.rx_sample_discard, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.Rx_Sample_Discard.rx_nco_discard, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.Rx_Sample_Discard.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.Rx_Sample_Discard.rx_sample_discard, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.Rx_Sample_Discard.rx_nco_discard, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.Rx_Sample_Discard.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.LPF_Config_2'):
                
            expected_fields = [self.dut.LPF_Config_2.p_gain, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.LPF_Config_2.p_shift, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.LPF_Config_2.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.LPF_Config_2.p_gain, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.LPF_Config_2.p_shift, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.LPF_Config_2.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.LPF_Config_2.p_gain, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.LPF_Config_2.p_shift, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.LPF_Config_2.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Ctrl'):
                
            expected_fields = [self.dut.Tx_Sync_Ctrl.tx_sync_ena, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.Tx_Sync_Ctrl.tx_sync_force, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.Tx_Sync_Ctrl.tx_sync_f1, # type: ignore[union-attr,list-item]
                                        
                                    
                                 self.dut.Tx_Sync_Ctrl.tx_sync_f2, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.Tx_Sync_Ctrl.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.Tx_Sync_Ctrl.tx_sync_ena, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.Tx_Sync_Ctrl.tx_sync_force, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.Tx_Sync_Ctrl.tx_sync_f1, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.Tx_Sync_Ctrl.tx_sync_f2, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.Tx_Sync_Ctrl.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.Tx_Sync_Ctrl.tx_sync_ena, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.Tx_Sync_Ctrl.tx_sync_force, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.Tx_Sync_Ctrl.tx_sync_f1, # type: ignore[union-attr,list-item] 
                                            
                                         self.dut.Tx_Sync_Ctrl.tx_sync_f2, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.Tx_Sync_Ctrl.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.Tx_Sync_Cnt'):
                
            expected_fields = [self.dut.Tx_Sync_Cnt.tx_sync_cnt, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.Tx_Sync_Cnt.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.Tx_Sync_Cnt.tx_sync_cnt, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.Tx_Sync_Cnt.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.Tx_Sync_Cnt.tx_sync_cnt, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.Tx_Sync_Cnt.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha1'):
                
            expected_fields = [self.dut.lowpass_ema_alpha1.alpha, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.lowpass_ema_alpha1.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.lowpass_ema_alpha1.alpha, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.lowpass_ema_alpha1.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.lowpass_ema_alpha1.alpha, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.lowpass_ema_alpha1.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: msk_top_regs.lowpass_ema_alpha2'):
                
            expected_fields = [self.dut.lowpass_ema_alpha2.alpha, # type: ignore[union-attr,list-item]
                                        
                                    
                                 
                                         ]
            fields = []
            for field in self.dut.lowpass_ema_alpha2.fields:  # type: ignore[union-attr]
                fields.append(field)
            self.assertCountEqual(expected_fields, fields)
                
            expected_writable_fields = [self.dut.lowpass_ema_alpha2.alpha, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.lowpass_ema_alpha2.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            expected_readable_fields = [self.dut.lowpass_ema_alpha2.alpha, # type: ignore[union-attr,list-item] 
                                            
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.lowpass_ema_alpha2.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        
        # test all the memories
        
        # test all the address maps
        
        # test all the register files
        

    def test_name_map(self) -> None:
        """
        Check that the function for getting a node by its original systemRDL name works
        """
        
        
        self.assertEqual(self.dut.Hash_ID_Low.get_child_by_system_rdl_name('hash_id_lo').inst_name, 'hash_id_lo')
        
        
        
        
        
        self.assertEqual(self.dut.Hash_ID_High.get_child_by_system_rdl_name('hash_id_hi').inst_name, 'hash_id_hi')
        
        
        
        
        
        self.assertEqual(self.dut.MSK_Init.get_child_by_system_rdl_name('txrxinit').inst_name, 'txrxinit')
        
        
        
        
        self.assertEqual(self.dut.MSK_Init.get_child_by_system_rdl_name('txinit').inst_name, 'txinit')
        
        
        
        
        self.assertEqual(self.dut.MSK_Init.get_child_by_system_rdl_name('rxinit').inst_name, 'rxinit')
        
        
        
        
        
        self.assertEqual(self.dut.MSK_Control.get_child_by_system_rdl_name('ptt').inst_name, 'ptt')
        
        
        
        
        self.assertEqual(self.dut.MSK_Control.get_child_by_system_rdl_name('loopback_ena').inst_name, 'loopback_ena')
        
        
        
        
        self.assertEqual(self.dut.MSK_Control.get_child_by_system_rdl_name('rx_invert').inst_name, 'rx_invert')
        
        
        
        
        self.assertEqual(self.dut.MSK_Control.get_child_by_system_rdl_name('clear_counts').inst_name, 'clear_counts')
        
        
        
        
        self.assertEqual(self.dut.MSK_Control.get_child_by_system_rdl_name('diff_encoder_loopback').inst_name, 'diff_encoder_loopback')
        
        
        
        
        
        self.assertEqual(self.dut.MSK_Status.get_child_by_system_rdl_name('demod_sync_lock').inst_name, 'demod_sync_lock')
        
        
        
        
        self.assertEqual(self.dut.MSK_Status.get_child_by_system_rdl_name('tx_enable').inst_name, 'tx_enable')
        
        
        
        
        self.assertEqual(self.dut.MSK_Status.get_child_by_system_rdl_name('rx_enable').inst_name, 'rx_enable')
        
        
        
        
        self.assertEqual(self.dut.MSK_Status.get_child_by_system_rdl_name('tx_axis_valid').inst_name, 'tx_axis_valid')
        
        
        
        
        
        self.assertEqual(self.dut.Fb_FreqWord.get_child_by_system_rdl_name('config_data').inst_name, 'config_data')
        
        
        
        
        
        self.assertEqual(self.dut.TX_F1_FreqWord.get_child_by_system_rdl_name('config_data').inst_name, 'config_data')
        
        
        
        
        
        self.assertEqual(self.dut.TX_F2_FreqWord.get_child_by_system_rdl_name('config_data').inst_name, 'config_data')
        
        
        
        
        
        self.assertEqual(self.dut.RX_F1_FreqWord.get_child_by_system_rdl_name('config_data').inst_name, 'config_data')
        
        
        
        
        
        self.assertEqual(self.dut.RX_F2_FreqWord.get_child_by_system_rdl_name('config_data').inst_name, 'config_data')
        
        
        
        
        
        self.assertEqual(self.dut.LPF_Config_0.get_child_by_system_rdl_name('lpf_freeze').inst_name, 'lpf_freeze')
        
        
        
        
        self.assertEqual(self.dut.LPF_Config_0.get_child_by_system_rdl_name('lpf_zero').inst_name, 'lpf_zero')
        
        
        
        
        self.assertEqual(self.dut.LPF_Config_0.get_child_by_system_rdl_name('prbs_reserved').inst_name, 'prbs_reserved')
        
        
        
        
        self.assertEqual(self.dut.LPF_Config_0.get_child_by_system_rdl_name('lpf_alpha').inst_name, 'lpf_alpha')
        
        
        
        
        
        self.assertEqual(self.dut.LPF_Config_1.get_child_by_system_rdl_name('i_gain').inst_name, 'i_gain')
        
        
        
        
        self.assertEqual(self.dut.LPF_Config_1.get_child_by_system_rdl_name('i_shift').inst_name, 'i_shift')
        
        
        
        
        
        self.assertEqual(self.dut.Tx_Data_Width.get_child_by_system_rdl_name('data_width').inst_name, 'data_width')
        
        
        
        
        
        self.assertEqual(self.dut.Rx_Data_Width.get_child_by_system_rdl_name('data_width').inst_name, 'data_width')
        
        
        
        
        
        self.assertEqual(self.dut.PRBS_Control.get_child_by_system_rdl_name('prbs_sel').inst_name, 'prbs_sel')
        
        
        
        
        self.assertEqual(self.dut.PRBS_Control.get_child_by_system_rdl_name('prbs_error_insert').inst_name, 'prbs_error_insert')
        
        
        
        
        self.assertEqual(self.dut.PRBS_Control.get_child_by_system_rdl_name('prbs_clear').inst_name, 'prbs_clear')
        
        
        
        
        self.assertEqual(self.dut.PRBS_Control.get_child_by_system_rdl_name('prbs_manual_sync').inst_name, 'prbs_manual_sync')
        
        
        
        
        self.assertEqual(self.dut.PRBS_Control.get_child_by_system_rdl_name('prbs_reserved').inst_name, 'prbs_reserved')
        
        
        
        
        self.assertEqual(self.dut.PRBS_Control.get_child_by_system_rdl_name('prbs_sync_threshold').inst_name, 'prbs_sync_threshold')
        
        
        
        
        
        self.assertEqual(self.dut.PRBS_Initial_State.get_child_by_system_rdl_name('config_data').inst_name, 'config_data')
        
        
        
        
        
        self.assertEqual(self.dut.PRBS_Polynomial.get_child_by_system_rdl_name('config_data').inst_name, 'config_data')
        
        
        
        
        
        self.assertEqual(self.dut.PRBS_Error_Mask.get_child_by_system_rdl_name('config_data').inst_name, 'config_data')
        
        
        
        
        
        self.assertEqual(self.dut.Rx_Sample_Discard.get_child_by_system_rdl_name('rx_sample_discard').inst_name, 'rx_sample_discard')
        
        
        
        
        self.assertEqual(self.dut.Rx_Sample_Discard.get_child_by_system_rdl_name('rx_nco_discard').inst_name, 'rx_nco_discard')
        
        
        
        
        
        self.assertEqual(self.dut.LPF_Config_2.get_child_by_system_rdl_name('p_gain').inst_name, 'p_gain')
        
        
        
        
        self.assertEqual(self.dut.LPF_Config_2.get_child_by_system_rdl_name('p_shift').inst_name, 'p_shift')
        
        
        
        
        
        self.assertEqual(self.dut.Tx_Sync_Ctrl.get_child_by_system_rdl_name('tx_sync_ena').inst_name, 'tx_sync_ena')
        
        
        
        
        self.assertEqual(self.dut.Tx_Sync_Ctrl.get_child_by_system_rdl_name('tx_sync_force').inst_name, 'tx_sync_force')
        
        
        
        
        self.assertEqual(self.dut.Tx_Sync_Ctrl.get_child_by_system_rdl_name('tx_sync_f1').inst_name, 'tx_sync_f1')
        
        
        
        
        self.assertEqual(self.dut.Tx_Sync_Ctrl.get_child_by_system_rdl_name('tx_sync_f2').inst_name, 'tx_sync_f2')
        
        
        
        
        
        self.assertEqual(self.dut.Tx_Sync_Cnt.get_child_by_system_rdl_name('tx_sync_cnt').inst_name, 'tx_sync_cnt')
        
        
        
        
        
        self.assertEqual(self.dut.lowpass_ema_alpha1.get_child_by_system_rdl_name('alpha').inst_name, 'alpha')
        
        
        
        
        
        self.assertEqual(self.dut.lowpass_ema_alpha2.get_child_by_system_rdl_name('alpha').inst_name, 'alpha')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    



class msk_top_regs_block_access(msk_top_regs_TestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    

    async def test_register_array_context_manager(self) -> None:
        """
        Walk the register map and check that register map context managers work correctly
        """
        

class msk_top_regs_alt_block_access(msk_top_regs_TestCase_AltBlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods with the alternative callbacks, this is a simpler
    version of the tests above
    """
    

    async def test_register_array_context_manager(self) -> None:
        """
        Walk the register map and check that register map context managers work correctly
        """
        


if __name__ == '__main__':

    if sys.version_info < (3, 8):
        asynctest.main()
    else:
        unittest.main()




