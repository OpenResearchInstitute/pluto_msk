


"""
Python Wrapper for the msk_top_regs register model

This code was generated from the PeakRDL-python package version 2.3.0

"""












from typing import Iterator
from typing import Optional
from typing import Union
from typing import Type
from typing import overload
from typing import Literal
from typing import Any
from typing import NoReturn
import warnings



from ..lib import Node, NodeArray, Base
from ..lib import UDPStruct

from ..lib  import AddressMapArray, RegFileArray
from ..lib import AsyncMemory, AsyncMemoryArray
from ..lib import AsyncAddressMap
from ..lib import AsyncRegFile
from ..lib  import AsyncAddressMapArray
from ..lib  import AsyncRegFileArray
from ..lib import MemoryAsyncReadOnly, MemoryAsyncWriteOnly, MemoryAsyncReadWrite
from ..lib import MemoryAsyncReadOnlyArray, MemoryAsyncWriteOnlyArray, MemoryAsyncReadWriteArray
from ..lib import AsyncReg, AsyncRegArray
from ..lib import RegAsyncReadOnly, RegAsyncWriteOnly, RegAsyncReadWrite
from ..lib import RegAsyncReadOnlyArray, RegAsyncWriteOnlyArray, RegAsyncReadWriteArray
from ..lib import FieldAsyncReadOnly, FieldAsyncWriteOnly, FieldAsyncReadWrite, Field

from ..lib import ReadableAsyncRegister, WritableAsyncRegister
from ..lib import ReadableAsyncMemory, WritableAsyncMemory
from ..lib import ReadableAsyncRegisterArray, WriteableAsyncRegisterArray



from ..lib import AsyncCallbackSet, AsyncCallbackSetLegacy





from ._registers import msk_top_regs_msk_hash_lo_0x743ecd7f54200b33_cls
from ._registers import msk_top_regs_msk_hash_hi_0x2fdfea8796573801_cls
from ._registers import msk_top_regs_msk_init_0x5784a15eda1d51f6_cls
from ._registers import msk_top_regs_msk_ctrl_0x6338546fd42c56c3_cls
from ._registers import msk_top_regs_msk_stat_0_0x11225f92044176be_cls
from ._registers import msk_top_regs_msk_stat_1_0x485040a78b4facc5_cls
from ._registers import msk_top_regs_msk_stat_2_0x79ca52b735200588_cls
from ._registers import msk_top_regs_config_nco_fw_0x444933e78de34535_cls
from ._registers import msk_top_regs_config_nco_fw_0x44f085218acb5a0b_cls
from ._registers import msk_top_regs_config_nco_fw_0x553395d594c88659_cls
from ._registers import msk_top_regs_config_nco_fw_0x33a361db4d08e83f_cls
from ._registers import msk_top_regs_config_nco_fw_neg_0x36fc9ff50bd27297_cls
from ._registers import msk_top_regs_lpf_config_0_neg_0x63d56b11f2a8b2a5_cls
from ._registers import msk_top_regs_lpf_config_1_0x6269262ac0819864_cls
from ._registers import msk_top_regs_data_width_0x30221bea82717e1e_cls
from ._registers import msk_top_regs_data_width_neg_0x361b7b87da257944_cls
from ._registers import msk_top_regs_prbs_ctrl_0x72ace307ca7cc42_cls
from ._registers import msk_top_regs_config_prbs_seed_neg_0x19de76e0a2449a75_cls
from ._registers import msk_top_regs_config_prbs_poly_0x59367282cbe7a1c8_cls
from ._registers import msk_top_regs_config_prbs_errmask_neg_0xcddb11619d27b12_cls
from ._registers import msk_top_regs_stat_32_bits_0x74f460ee43ed88ef_cls
from ._registers import msk_top_regs_stat_32_errs_neg_0x410fa9bc87190658_cls
from ._registers import msk_top_regs_stat_32_lpf_acc_0x1be0f0bf59c971f9_cls
from ._registers import msk_top_regs_stat_32_lpf_acc_neg_0x71a284902b1741d_cls
from ._registers import msk_top_regs_msk_stat_3_neg_0x724989d9d7fa96aa_cls
from ._registers import msk_top_regs_rx_sample_discard_0x57460af07270e6fd_cls
from ._registers import msk_top_regs_lpf_config_2_neg_0x65b9ddf457a2004f_cls
from ._registers import msk_top_regs_status_reg_neg_0x561e6a8e0b780b6c_cls
from ._registers import msk_top_regs_status_reg_neg_0x4d2d9eda85ed7f85_cls
from ._registers import msk_top_regs_status_reg_0xc76f462239d17e2_cls
from ._registers import msk_top_regs_status_reg_neg_0x3bb1d84b87620443_cls
from ._registers import msk_top_regs_tx_sync_ctrl_0x6860c618c7262d61_cls
from ._registers import msk_top_regs_tx_sync_cnt_neg_0x1511021194f49355_cls
from ._registers import msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls
from ._registers import msk_top_regs_rx_power_neg_0x2149d23df4ec0d38_cls
from ._registers import msk_top_regs_status_reg_neg_0x612bf1b594ba3a1d_cls
from ._registers import msk_top_regs_status_reg_neg_0x7fad4991d4c753dd_cls
from ._registers import msk_top_regs_frame_sync_status_0x1c3505bac15a3964_cls
from ._registers import msk_top_regs_symbol_lock_control_0x7a327095be616a18_cls
from ._registers import msk_top_regs_symbol_lock_status_0x1d147971e0fe260c_cls
from ._registers import msk_top_regs_symbol_lock_time_neg_0x2caa632680878580_cls


# addrmap, regfile, memor and register definitions
    
    
class msk_top_regs_neg_0x6e59a13abed32d7c_cls(AsyncAddressMap):
    """
    Class to represent a address map in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Pluto MSK Registers                                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>MSK Modem Configuration and Status Registers</p>                |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__Hash_ID_Low', '__Hash_ID_High', '__MSK_Init', '__MSK_Control', '__MSK_Status', '__Tx_Bit_Count', '__Tx_Enable_Count', '__Fb_FreqWord', '__TX_F1_FreqWord', '__TX_F2_FreqWord', '__RX_F1_FreqWord', '__RX_F2_FreqWord', '__LPF_Config_0', '__LPF_Config_1', '__Tx_Data_Width', '__Rx_Data_Width', '__PRBS_Control', '__PRBS_Initial_State', '__PRBS_Polynomial', '__PRBS_Error_Mask', '__PRBS_Bit_Count', '__PRBS_Error_Count', '__LPF_Accum_F1', '__LPF_Accum_F2', '__axis_xfer_count', '__Rx_Sample_Discard', '__LPF_Config_2', '__f1_nco_adjust', '__f2_nco_adjust', '__f1_error', '__f2_error', '__Tx_Sync_Ctrl', '__Tx_Sync_Cnt', '__lowpass_ema_alpha1', '__lowpass_ema_alpha2', '__rx_power', '__tx_async_fifo_rd_wr_ptr', '__rx_async_fifo_rd_wr_ptr', '__rx_frame_sync_status', '__symbol_lock_control', '__symbol_lock_status', '__symbol_lock_time']

    def __init__(self, *,
                 address:int=0,
                 logger_handle:str='reg_model.msk_top_regs',
                 inst_name:str='msk_top_regs',
                 callbacks: Optional[Union[AsyncCallbackSet, AsyncCallbackSetLegacy]]=None,
                 parent:Optional[AsyncAddressMap]=None):

        if callbacks is not None:
            if not isinstance(callbacks, (AsyncCallbackSet, AsyncCallbackSetLegacy)):
                raise TypeError(f'callbacks should be AsyncCallbackSet, AsyncCallbackSetLegacy got {type(callbacks)}')

        super().__init__(callbacks=callbacks,
                         address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        
            
        self.__Hash_ID_Low:msk_top_regs_msk_hash_lo_0x743ecd7f54200b33_cls = msk_top_regs_msk_hash_lo_0x743ecd7f54200b33_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.Hash_ID_Low',
                                                                     inst_name='Hash_ID_Low', parent=self)
        
            
        self.__Hash_ID_High:msk_top_regs_msk_hash_hi_0x2fdfea8796573801_cls = msk_top_regs_msk_hash_hi_0x2fdfea8796573801_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.Hash_ID_High',
                                                                     inst_name='Hash_ID_High', parent=self)
        
            
        self.__MSK_Init:msk_top_regs_msk_init_0x5784a15eda1d51f6_cls = msk_top_regs_msk_init_0x5784a15eda1d51f6_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.MSK_Init',
                                                                     inst_name='MSK_Init', parent=self)
        
            
        self.__MSK_Control:msk_top_regs_msk_ctrl_0x6338546fd42c56c3_cls = msk_top_regs_msk_ctrl_0x6338546fd42c56c3_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.MSK_Control',
                                                                     inst_name='MSK_Control', parent=self)
        
            
        self.__MSK_Status:msk_top_regs_msk_stat_0_0x11225f92044176be_cls = msk_top_regs_msk_stat_0_0x11225f92044176be_cls(
                                                                     address=self.address+16,
                                                                     logger_handle=logger_handle+'.MSK_Status',
                                                                     inst_name='MSK_Status', parent=self)
        
            
        self.__Tx_Bit_Count:msk_top_regs_msk_stat_1_0x485040a78b4facc5_cls = msk_top_regs_msk_stat_1_0x485040a78b4facc5_cls(
                                                                     address=self.address+20,
                                                                     logger_handle=logger_handle+'.Tx_Bit_Count',
                                                                     inst_name='Tx_Bit_Count', parent=self)
        
            
        self.__Tx_Enable_Count:msk_top_regs_msk_stat_2_0x79ca52b735200588_cls = msk_top_regs_msk_stat_2_0x79ca52b735200588_cls(
                                                                     address=self.address+24,
                                                                     logger_handle=logger_handle+'.Tx_Enable_Count',
                                                                     inst_name='Tx_Enable_Count', parent=self)
        
            
        self.__Fb_FreqWord:msk_top_regs_config_nco_fw_0x444933e78de34535_cls = msk_top_regs_config_nco_fw_0x444933e78de34535_cls(
                                                                     address=self.address+28,
                                                                     logger_handle=logger_handle+'.Fb_FreqWord',
                                                                     inst_name='Fb_FreqWord', parent=self)
        
            
        self.__TX_F1_FreqWord:msk_top_regs_config_nco_fw_0x44f085218acb5a0b_cls = msk_top_regs_config_nco_fw_0x44f085218acb5a0b_cls(
                                                                     address=self.address+32,
                                                                     logger_handle=logger_handle+'.TX_F1_FreqWord',
                                                                     inst_name='TX_F1_FreqWord', parent=self)
        
            
        self.__TX_F2_FreqWord:msk_top_regs_config_nco_fw_0x553395d594c88659_cls = msk_top_regs_config_nco_fw_0x553395d594c88659_cls(
                                                                     address=self.address+36,
                                                                     logger_handle=logger_handle+'.TX_F2_FreqWord',
                                                                     inst_name='TX_F2_FreqWord', parent=self)
        
            
        self.__RX_F1_FreqWord:msk_top_regs_config_nco_fw_0x33a361db4d08e83f_cls = msk_top_regs_config_nco_fw_0x33a361db4d08e83f_cls(
                                                                     address=self.address+40,
                                                                     logger_handle=logger_handle+'.RX_F1_FreqWord',
                                                                     inst_name='RX_F1_FreqWord', parent=self)
        
            
        self.__RX_F2_FreqWord:msk_top_regs_config_nco_fw_neg_0x36fc9ff50bd27297_cls = msk_top_regs_config_nco_fw_neg_0x36fc9ff50bd27297_cls(
                                                                     address=self.address+44,
                                                                     logger_handle=logger_handle+'.RX_F2_FreqWord',
                                                                     inst_name='RX_F2_FreqWord', parent=self)
        
            
        self.__LPF_Config_0:msk_top_regs_lpf_config_0_neg_0x63d56b11f2a8b2a5_cls = msk_top_regs_lpf_config_0_neg_0x63d56b11f2a8b2a5_cls(
                                                                     address=self.address+48,
                                                                     logger_handle=logger_handle+'.LPF_Config_0',
                                                                     inst_name='LPF_Config_0', parent=self)
        
            
        self.__LPF_Config_1:msk_top_regs_lpf_config_1_0x6269262ac0819864_cls = msk_top_regs_lpf_config_1_0x6269262ac0819864_cls(
                                                                     address=self.address+52,
                                                                     logger_handle=logger_handle+'.LPF_Config_1',
                                                                     inst_name='LPF_Config_1', parent=self)
        
            
        self.__Tx_Data_Width:msk_top_regs_data_width_0x30221bea82717e1e_cls = msk_top_regs_data_width_0x30221bea82717e1e_cls(
                                                                     address=self.address+56,
                                                                     logger_handle=logger_handle+'.Tx_Data_Width',
                                                                     inst_name='Tx_Data_Width', parent=self)
        
            
        self.__Rx_Data_Width:msk_top_regs_data_width_neg_0x361b7b87da257944_cls = msk_top_regs_data_width_neg_0x361b7b87da257944_cls(
                                                                     address=self.address+60,
                                                                     logger_handle=logger_handle+'.Rx_Data_Width',
                                                                     inst_name='Rx_Data_Width', parent=self)
        
            
        self.__PRBS_Control:msk_top_regs_prbs_ctrl_0x72ace307ca7cc42_cls = msk_top_regs_prbs_ctrl_0x72ace307ca7cc42_cls(
                                                                     address=self.address+64,
                                                                     logger_handle=logger_handle+'.PRBS_Control',
                                                                     inst_name='PRBS_Control', parent=self)
        
            
        self.__PRBS_Initial_State:msk_top_regs_config_prbs_seed_neg_0x19de76e0a2449a75_cls = msk_top_regs_config_prbs_seed_neg_0x19de76e0a2449a75_cls(
                                                                     address=self.address+68,
                                                                     logger_handle=logger_handle+'.PRBS_Initial_State',
                                                                     inst_name='PRBS_Initial_State', parent=self)
        
            
        self.__PRBS_Polynomial:msk_top_regs_config_prbs_poly_0x59367282cbe7a1c8_cls = msk_top_regs_config_prbs_poly_0x59367282cbe7a1c8_cls(
                                                                     address=self.address+72,
                                                                     logger_handle=logger_handle+'.PRBS_Polynomial',
                                                                     inst_name='PRBS_Polynomial', parent=self)
        
            
        self.__PRBS_Error_Mask:msk_top_regs_config_prbs_errmask_neg_0xcddb11619d27b12_cls = msk_top_regs_config_prbs_errmask_neg_0xcddb11619d27b12_cls(
                                                                     address=self.address+76,
                                                                     logger_handle=logger_handle+'.PRBS_Error_Mask',
                                                                     inst_name='PRBS_Error_Mask', parent=self)
        
            
        self.__PRBS_Bit_Count:msk_top_regs_stat_32_bits_0x74f460ee43ed88ef_cls = msk_top_regs_stat_32_bits_0x74f460ee43ed88ef_cls(
                                                                     address=self.address+80,
                                                                     logger_handle=logger_handle+'.PRBS_Bit_Count',
                                                                     inst_name='PRBS_Bit_Count', parent=self)
        
            
        self.__PRBS_Error_Count:msk_top_regs_stat_32_errs_neg_0x410fa9bc87190658_cls = msk_top_regs_stat_32_errs_neg_0x410fa9bc87190658_cls(
                                                                     address=self.address+84,
                                                                     logger_handle=logger_handle+'.PRBS_Error_Count',
                                                                     inst_name='PRBS_Error_Count', parent=self)
        
            
        self.__LPF_Accum_F1:msk_top_regs_stat_32_lpf_acc_0x1be0f0bf59c971f9_cls = msk_top_regs_stat_32_lpf_acc_0x1be0f0bf59c971f9_cls(
                                                                     address=self.address+88,
                                                                     logger_handle=logger_handle+'.LPF_Accum_F1',
                                                                     inst_name='LPF_Accum_F1', parent=self)
        
            
        self.__LPF_Accum_F2:msk_top_regs_stat_32_lpf_acc_neg_0x71a284902b1741d_cls = msk_top_regs_stat_32_lpf_acc_neg_0x71a284902b1741d_cls(
                                                                     address=self.address+92,
                                                                     logger_handle=logger_handle+'.LPF_Accum_F2',
                                                                     inst_name='LPF_Accum_F2', parent=self)
        
            
        self.__axis_xfer_count:msk_top_regs_msk_stat_3_neg_0x724989d9d7fa96aa_cls = msk_top_regs_msk_stat_3_neg_0x724989d9d7fa96aa_cls(
                                                                     address=self.address+96,
                                                                     logger_handle=logger_handle+'.axis_xfer_count',
                                                                     inst_name='axis_xfer_count', parent=self)
        
            
        self.__Rx_Sample_Discard:msk_top_regs_rx_sample_discard_0x57460af07270e6fd_cls = msk_top_regs_rx_sample_discard_0x57460af07270e6fd_cls(
                                                                     address=self.address+100,
                                                                     logger_handle=logger_handle+'.Rx_Sample_Discard',
                                                                     inst_name='Rx_Sample_Discard', parent=self)
        
            
        self.__LPF_Config_2:msk_top_regs_lpf_config_2_neg_0x65b9ddf457a2004f_cls = msk_top_regs_lpf_config_2_neg_0x65b9ddf457a2004f_cls(
                                                                     address=self.address+104,
                                                                     logger_handle=logger_handle+'.LPF_Config_2',
                                                                     inst_name='LPF_Config_2', parent=self)
        
            
        self.__f1_nco_adjust:msk_top_regs_status_reg_neg_0x561e6a8e0b780b6c_cls = msk_top_regs_status_reg_neg_0x561e6a8e0b780b6c_cls(
                                                                     address=self.address+108,
                                                                     logger_handle=logger_handle+'.f1_nco_adjust',
                                                                     inst_name='f1_nco_adjust', parent=self)
        
            
        self.__f2_nco_adjust:msk_top_regs_status_reg_neg_0x4d2d9eda85ed7f85_cls = msk_top_regs_status_reg_neg_0x4d2d9eda85ed7f85_cls(
                                                                     address=self.address+112,
                                                                     logger_handle=logger_handle+'.f2_nco_adjust',
                                                                     inst_name='f2_nco_adjust', parent=self)
        
            
        self.__f1_error:msk_top_regs_status_reg_0xc76f462239d17e2_cls = msk_top_regs_status_reg_0xc76f462239d17e2_cls(
                                                                     address=self.address+116,
                                                                     logger_handle=logger_handle+'.f1_error',
                                                                     inst_name='f1_error', parent=self)
        
            
        self.__f2_error:msk_top_regs_status_reg_neg_0x3bb1d84b87620443_cls = msk_top_regs_status_reg_neg_0x3bb1d84b87620443_cls(
                                                                     address=self.address+120,
                                                                     logger_handle=logger_handle+'.f2_error',
                                                                     inst_name='f2_error', parent=self)
        
            
        self.__Tx_Sync_Ctrl:msk_top_regs_tx_sync_ctrl_0x6860c618c7262d61_cls = msk_top_regs_tx_sync_ctrl_0x6860c618c7262d61_cls(
                                                                     address=self.address+124,
                                                                     logger_handle=logger_handle+'.Tx_Sync_Ctrl',
                                                                     inst_name='Tx_Sync_Ctrl', parent=self)
        
            
        self.__Tx_Sync_Cnt:msk_top_regs_tx_sync_cnt_neg_0x1511021194f49355_cls = msk_top_regs_tx_sync_cnt_neg_0x1511021194f49355_cls(
                                                                     address=self.address+128,
                                                                     logger_handle=logger_handle+'.Tx_Sync_Cnt',
                                                                     inst_name='Tx_Sync_Cnt', parent=self)
        
            
        self.__lowpass_ema_alpha1:msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls = msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls(
                                                                     address=self.address+132,
                                                                     logger_handle=logger_handle+'.lowpass_ema_alpha1',
                                                                     inst_name='lowpass_ema_alpha1', parent=self)
        
            
        self.__lowpass_ema_alpha2:msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls = msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls(
                                                                     address=self.address+136,
                                                                     logger_handle=logger_handle+'.lowpass_ema_alpha2',
                                                                     inst_name='lowpass_ema_alpha2', parent=self)
        
            
        self.__rx_power:msk_top_regs_rx_power_neg_0x2149d23df4ec0d38_cls = msk_top_regs_rx_power_neg_0x2149d23df4ec0d38_cls(
                                                                     address=self.address+140,
                                                                     logger_handle=logger_handle+'.rx_power',
                                                                     inst_name='rx_power', parent=self)
        
            
        self.__tx_async_fifo_rd_wr_ptr:msk_top_regs_status_reg_neg_0x612bf1b594ba3a1d_cls = msk_top_regs_status_reg_neg_0x612bf1b594ba3a1d_cls(
                                                                     address=self.address+144,
                                                                     logger_handle=logger_handle+'.tx_async_fifo_rd_wr_ptr',
                                                                     inst_name='tx_async_fifo_rd_wr_ptr', parent=self)
        
            
        self.__rx_async_fifo_rd_wr_ptr:msk_top_regs_status_reg_neg_0x7fad4991d4c753dd_cls = msk_top_regs_status_reg_neg_0x7fad4991d4c753dd_cls(
                                                                     address=self.address+148,
                                                                     logger_handle=logger_handle+'.rx_async_fifo_rd_wr_ptr',
                                                                     inst_name='rx_async_fifo_rd_wr_ptr', parent=self)
        
            
        self.__rx_frame_sync_status:msk_top_regs_frame_sync_status_0x1c3505bac15a3964_cls = msk_top_regs_frame_sync_status_0x1c3505bac15a3964_cls(
                                                                     address=self.address+152,
                                                                     logger_handle=logger_handle+'.rx_frame_sync_status',
                                                                     inst_name='rx_frame_sync_status', parent=self)
        
            
        self.__symbol_lock_control:msk_top_regs_symbol_lock_control_0x7a327095be616a18_cls = msk_top_regs_symbol_lock_control_0x7a327095be616a18_cls(
                                                                     address=self.address+156,
                                                                     logger_handle=logger_handle+'.symbol_lock_control',
                                                                     inst_name='symbol_lock_control', parent=self)
        
            
        self.__symbol_lock_status:msk_top_regs_symbol_lock_status_0x1d147971e0fe260c_cls = msk_top_regs_symbol_lock_status_0x1d147971e0fe260c_cls(
                                                                     address=self.address+160,
                                                                     logger_handle=logger_handle+'.symbol_lock_status',
                                                                     inst_name='symbol_lock_status', parent=self)
        
            
        self.__symbol_lock_time:msk_top_regs_symbol_lock_time_neg_0x2caa632680878580_cls = msk_top_regs_symbol_lock_time_neg_0x2caa632680878580_cls(
                                                                     address=self.address+164,
                                                                     logger_handle=logger_handle+'.symbol_lock_time',
                                                                     inst_name='symbol_lock_time', parent=self)
        

    @property
    def size(self) -> int:
        return 168
    @property
    def Hash_ID_Low(self) -> 'msk_top_regs_msk_hash_lo_0x743ecd7f54200b33_cls':
        """
        Property to access Hash_ID_Low 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Pluto MSK FPGA Hash ID - Lower 32-bits                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__Hash_ID_Low
        
    @property
    def Hash_ID_High(self) -> 'msk_top_regs_msk_hash_hi_0x2fdfea8796573801_cls':
        """
        Property to access Hash_ID_High 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Pluto MSK FPGA Hash ID - Upper 32-bits                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__Hash_ID_High
        
    @property
    def MSK_Init(self) -> 'msk_top_regs_msk_init_0x5784a15eda1d51f6_cls':
        """
        Property to access MSK_Init 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      MSK Modem Initialization Control                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Synchronous initialization of MSK Modem functions, does not     |
        |              |      affect configuration registers.</p>                                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__MSK_Init
        
    @property
    def MSK_Control(self) -> 'msk_top_regs_msk_ctrl_0x6338546fd42c56c3_cls':
        """
        Property to access MSK_Control 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      MSK Modem Control                                                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>MSK Modem Configuration and Control</p>                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__MSK_Control
        
    @property
    def MSK_Status(self) -> 'msk_top_regs_msk_stat_0_0x11225f92044176be_cls':
        """
        Property to access MSK_Status 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      MSK Modem Status 0                                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Modem status bits</p>                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__MSK_Status
        
    @property
    def Tx_Bit_Count(self) -> 'msk_top_regs_msk_stat_1_0x485040a78b4facc5_cls':
        """
        Property to access Tx_Bit_Count 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      MSK Modem Status 1                                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Modem status data</p>                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__Tx_Bit_Count
        
    @property
    def Tx_Enable_Count(self) -> 'msk_top_regs_msk_stat_2_0x79ca52b735200588_cls':
        """
        Property to access Tx_Enable_Count 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      MSK Modem Status 2                                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Modem status data</p>                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__Tx_Enable_Count
        
    @property
    def Fb_FreqWord(self) -> 'msk_top_regs_config_nco_fw_0x444933e78de34535_cls':
        """
        Property to access Fb_FreqWord 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Bitrate NCO Frequency Control Word                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Set Modem Data Rate</p>                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__Fb_FreqWord
        
    @property
    def TX_F1_FreqWord(self) -> 'msk_top_regs_config_nco_fw_0x44f085218acb5a0b_cls':
        """
        Property to access TX_F1_FreqWord 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx F1 NCO Frequency Control Word                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Set Modulator F1 Frequency</p>                                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__TX_F1_FreqWord
        
    @property
    def TX_F2_FreqWord(self) -> 'msk_top_regs_config_nco_fw_0x553395d594c88659_cls':
        """
        Property to access TX_F2_FreqWord 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx F2 NCO Frequency Control Word                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Set Modulator F2 Frequency</p>                                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__TX_F2_FreqWord
        
    @property
    def RX_F1_FreqWord(self) -> 'msk_top_regs_config_nco_fw_0x33a361db4d08e83f_cls':
        """
        Property to access RX_F1_FreqWord 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Rx F1 NCO Frequency Control Word                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Set Demodulator F1 Frequency</p>                                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__RX_F1_FreqWord
        
    @property
    def RX_F2_FreqWord(self) -> 'msk_top_regs_config_nco_fw_neg_0x36fc9ff50bd27297_cls':
        """
        Property to access RX_F2_FreqWord 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Rx F2 NCO Frequency Control Word                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Set Demodulator F2 Frequency</p>                                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__RX_F2_FreqWord
        
    @property
    def LPF_Config_0(self) -> 'msk_top_regs_lpf_config_0_neg_0x63d56b11f2a8b2a5_cls':
        """
        Property to access LPF_Config_0 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PI Controller Configuration and Low-pass Filter Configuration      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Configure PI controller and low-pass filter</p>                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__LPF_Config_0
        
    @property
    def LPF_Config_1(self) -> 'msk_top_regs_lpf_config_1_0x6269262ac0819864_cls':
        """
        Property to access LPF_Config_1 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PI Controller Configuration Configuration Register 1               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Configures PI Controller I-gain and divisor</p>                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__LPF_Config_1
        
    @property
    def Tx_Data_Width(self) -> 'msk_top_regs_data_width_0x30221bea82717e1e_cls':
        """
        Property to access Tx_Data_Width 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Modem Tx Input Data Width                                          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Set the parallel data width of the parallel-to-serial           |
        |              |      converter</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__Tx_Data_Width
        
    @property
    def Rx_Data_Width(self) -> 'msk_top_regs_data_width_neg_0x361b7b87da257944_cls':
        """
        Property to access Rx_Data_Width 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Modem Rx Output Data Width                                         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Set the parallel data width of the serial-to-parallel           |
        |              |      converter</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__Rx_Data_Width
        
    @property
    def PRBS_Control(self) -> 'msk_top_regs_prbs_ctrl_0x72ace307ca7cc42_cls':
        """
        Property to access PRBS_Control 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Control 0                                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Configures operation of the PRBS Generator and Monitor</p>      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__PRBS_Control
        
    @property
    def PRBS_Initial_State(self) -> 'msk_top_regs_config_prbs_seed_neg_0x19de76e0a2449a75_cls':
        """
        Property to access PRBS_Initial_State 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Control 1                                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>PRBS Initial State</p>                                          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__PRBS_Initial_State
        
    @property
    def PRBS_Polynomial(self) -> 'msk_top_regs_config_prbs_poly_0x59367282cbe7a1c8_cls':
        """
        Property to access PRBS_Polynomial 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Control 2                                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>PRBS Polynomial</p>                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__PRBS_Polynomial
        
    @property
    def PRBS_Error_Mask(self) -> 'msk_top_regs_config_prbs_errmask_neg_0xcddb11619d27b12_cls':
        """
        Property to access PRBS_Error_Mask 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Control 3                                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>PRBS Error Mask</p>                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__PRBS_Error_Mask
        
    @property
    def PRBS_Bit_Count(self) -> 'msk_top_regs_stat_32_bits_0x74f460ee43ed88ef_cls':
        """
        Property to access PRBS_Bit_Count 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Status 0                                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>PRBS Bits Received</p>                                          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__PRBS_Bit_Count
        
    @property
    def PRBS_Error_Count(self) -> 'msk_top_regs_stat_32_errs_neg_0x410fa9bc87190658_cls':
        """
        Property to access PRBS_Error_Count 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Status 1                                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>PRBS Bit Errors</p>                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__PRBS_Error_Count
        
    @property
    def LPF_Accum_F1(self) -> 'msk_top_regs_stat_32_lpf_acc_0x1be0f0bf59c971f9_cls':
        """
        Property to access LPF_Accum_F1 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      F1 PI Controller Accumulator                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Value of the F1 PI Controller Accumulator</p>                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__LPF_Accum_F1
        
    @property
    def LPF_Accum_F2(self) -> 'msk_top_regs_stat_32_lpf_acc_neg_0x71a284902b1741d_cls':
        """
        Property to access LPF_Accum_F2 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      F2 PI Controller Accumulator                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Value of the F2 PI Controller Accumulator</p>                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__LPF_Accum_F2
        
    @property
    def axis_xfer_count(self) -> 'msk_top_regs_msk_stat_3_neg_0x724989d9d7fa96aa_cls':
        """
        Property to access axis_xfer_count 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      MSK Modem Status 3                                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Modem status data</p>                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__axis_xfer_count
        
    @property
    def Rx_Sample_Discard(self) -> 'msk_top_regs_rx_sample_discard_0x57460af07270e6fd_cls':
        """
        Property to access Rx_Sample_Discard 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Rx Sample Discard                                                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Configure samples discard operation for demodulator</p>         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__Rx_Sample_Discard
        
    @property
    def LPF_Config_2(self) -> 'msk_top_regs_lpf_config_2_neg_0x65b9ddf457a2004f_cls':
        """
        Property to access LPF_Config_2 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PI Controller Configuration Configuration Register 2               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Configures PI Controller I-gain and divisor</p>                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__LPF_Config_2
        
    @property
    def f1_nco_adjust(self) -> 'msk_top_regs_status_reg_neg_0x561e6a8e0b780b6c_cls':
        """
        Property to access f1_nco_adjust 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      F1 NCO Frequency Adjust                                            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Status Register</p>                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f1_nco_adjust
        
    @property
    def f2_nco_adjust(self) -> 'msk_top_regs_status_reg_neg_0x4d2d9eda85ed7f85_cls':
        """
        Property to access f2_nco_adjust 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      F2 NCO Frequency Adjust                                            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Status Register</p>                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f2_nco_adjust
        
    @property
    def f1_error(self) -> 'msk_top_regs_status_reg_0xc76f462239d17e2_cls':
        """
        Property to access f1_error 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      F1 Error Value                                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Status Register</p>                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f1_error
        
    @property
    def f2_error(self) -> 'msk_top_regs_status_reg_neg_0x3bb1d84b87620443_cls':
        """
        Property to access f2_error 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      F2 Error Value                                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Status Register</p>                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f2_error
        
    @property
    def Tx_Sync_Ctrl(self) -> 'msk_top_regs_tx_sync_ctrl_0x6860c618c7262d61_cls':
        """
        Property to access Tx_Sync_Ctrl 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Transmitter Sync Control                                           |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Provides control bits for generation of transmitter             |
        |              |      synchronization patterns</p>                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__Tx_Sync_Ctrl
        
    @property
    def Tx_Sync_Cnt(self) -> 'msk_top_regs_tx_sync_cnt_neg_0x1511021194f49355_cls':
        """
        Property to access Tx_Sync_Cnt 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Transmitter Sync Duration                                          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sets the duration of the synchronization tones when enabled</p> |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__Tx_Sync_Cnt
        
    @property
    def lowpass_ema_alpha1(self) -> 'msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls':
        """
        Property to access lowpass_ema_alpha1 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Exponential Moving Average Alpha                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sets the alpha for the EMA</p>                                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lowpass_ema_alpha1
        
    @property
    def lowpass_ema_alpha2(self) -> 'msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls':
        """
        Property to access lowpass_ema_alpha2 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Exponential Moving Average Alpha                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sets the alpha for the EMA</p>                                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lowpass_ema_alpha2
        
    @property
    def rx_power(self) -> 'msk_top_regs_rx_power_neg_0x2149d23df4ec0d38_cls':
        """
        Property to access rx_power 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Receive Power                                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Receive power computed from I/Q samples</p>                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rx_power
        
    @property
    def tx_async_fifo_rd_wr_ptr(self) -> 'msk_top_regs_status_reg_neg_0x612bf1b594ba3a1d_cls':
        """
        Property to access tx_async_fifo_rd_wr_ptr 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx async FIFO read and write pointers                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Tx async FIFO read and write pointers</p>                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_async_fifo_rd_wr_ptr
        
    @property
    def rx_async_fifo_rd_wr_ptr(self) -> 'msk_top_regs_status_reg_neg_0x7fad4991d4c753dd_cls':
        """
        Property to access rx_async_fifo_rd_wr_ptr 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Rx async FIFO read and write pointers                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Rx async FIFO read and write pointers</p>                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rx_async_fifo_rd_wr_ptr
        
    @property
    def rx_frame_sync_status(self) -> 'msk_top_regs_frame_sync_status_0x1c3505bac15a3964_cls':
        """
        Property to access rx_frame_sync_status 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Frame Sync Status                                                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rx_frame_sync_status
        
    @property
    def symbol_lock_control(self) -> 'msk_top_regs_symbol_lock_control_0x7a327095be616a18_cls':
        """
        Property to access symbol_lock_control 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Symbol Lock Control                                                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__symbol_lock_control
        
    @property
    def symbol_lock_status(self) -> 'msk_top_regs_symbol_lock_status_0x1d147971e0fe260c_cls':
        """
        Property to access symbol_lock_status 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Symbol Lock Status                                                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__symbol_lock_status
        
    @property
    def symbol_lock_time(self) -> 'msk_top_regs_symbol_lock_time_neg_0x2caa632680878580_cls':
        """
        Property to access symbol_lock_time 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Symbol Lock Time                                                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__symbol_lock_time
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'Hash_ID_Low':'Hash_ID_Low','Hash_ID_High':'Hash_ID_High','MSK_Init':'MSK_Init','MSK_Control':'MSK_Control','MSK_Status':'MSK_Status','Tx_Bit_Count':'Tx_Bit_Count','Tx_Enable_Count':'Tx_Enable_Count','Fb_FreqWord':'Fb_FreqWord','TX_F1_FreqWord':'TX_F1_FreqWord','TX_F2_FreqWord':'TX_F2_FreqWord','RX_F1_FreqWord':'RX_F1_FreqWord','RX_F2_FreqWord':'RX_F2_FreqWord','LPF_Config_0':'LPF_Config_0','LPF_Config_1':'LPF_Config_1','Tx_Data_Width':'Tx_Data_Width','Rx_Data_Width':'Rx_Data_Width','PRBS_Control':'PRBS_Control','PRBS_Initial_State':'PRBS_Initial_State','PRBS_Polynomial':'PRBS_Polynomial','PRBS_Error_Mask':'PRBS_Error_Mask','PRBS_Bit_Count':'PRBS_Bit_Count','PRBS_Error_Count':'PRBS_Error_Count','LPF_Accum_F1':'LPF_Accum_F1','LPF_Accum_F2':'LPF_Accum_F2','axis_xfer_count':'axis_xfer_count','Rx_Sample_Discard':'Rx_Sample_Discard','LPF_Config_2':'LPF_Config_2','f1_nco_adjust':'f1_nco_adjust','f2_nco_adjust':'f2_nco_adjust','f1_error':'f1_error','f2_error':'f2_error','Tx_Sync_Ctrl':'Tx_Sync_Ctrl','Tx_Sync_Cnt':'Tx_Sync_Cnt','lowpass_ema_alpha1':'lowpass_ema_alpha1','lowpass_ema_alpha2':'lowpass_ema_alpha2','rx_power':'rx_power','tx_async_fifo_rd_wr_ptr':'tx_async_fifo_rd_wr_ptr','rx_async_fifo_rd_wr_ptr':'rx_async_fifo_rd_wr_ptr','rx_frame_sync_status':'rx_frame_sync_status','symbol_lock_control':'symbol_lock_control','symbol_lock_status':'symbol_lock_status','symbol_lock_time':'symbol_lock_time',
            }

    
    
    
    
    
    
    # nodes:42
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Hash_ID_Low"]) -> 'msk_top_regs_msk_hash_lo_0x743ecd7f54200b33_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Hash_ID_High"]) -> 'msk_top_regs_msk_hash_hi_0x2fdfea8796573801_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["MSK_Init"]) -> 'msk_top_regs_msk_init_0x5784a15eda1d51f6_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["MSK_Control"]) -> 'msk_top_regs_msk_ctrl_0x6338546fd42c56c3_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["MSK_Status"]) -> 'msk_top_regs_msk_stat_0_0x11225f92044176be_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Tx_Bit_Count"]) -> 'msk_top_regs_msk_stat_1_0x485040a78b4facc5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Tx_Enable_Count"]) -> 'msk_top_regs_msk_stat_2_0x79ca52b735200588_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Fb_FreqWord"]) -> 'msk_top_regs_config_nco_fw_0x444933e78de34535_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["TX_F1_FreqWord"]) -> 'msk_top_regs_config_nco_fw_0x44f085218acb5a0b_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["TX_F2_FreqWord"]) -> 'msk_top_regs_config_nco_fw_0x553395d594c88659_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["RX_F1_FreqWord"]) -> 'msk_top_regs_config_nco_fw_0x33a361db4d08e83f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["RX_F2_FreqWord"]) -> 'msk_top_regs_config_nco_fw_neg_0x36fc9ff50bd27297_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["LPF_Config_0"]) -> 'msk_top_regs_lpf_config_0_neg_0x63d56b11f2a8b2a5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["LPF_Config_1"]) -> 'msk_top_regs_lpf_config_1_0x6269262ac0819864_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Tx_Data_Width"]) -> 'msk_top_regs_data_width_0x30221bea82717e1e_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Rx_Data_Width"]) -> 'msk_top_regs_data_width_neg_0x361b7b87da257944_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Control"]) -> 'msk_top_regs_prbs_ctrl_0x72ace307ca7cc42_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Initial_State"]) -> 'msk_top_regs_config_prbs_seed_neg_0x19de76e0a2449a75_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Polynomial"]) -> 'msk_top_regs_config_prbs_poly_0x59367282cbe7a1c8_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Error_Mask"]) -> 'msk_top_regs_config_prbs_errmask_neg_0xcddb11619d27b12_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Bit_Count"]) -> 'msk_top_regs_stat_32_bits_0x74f460ee43ed88ef_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Error_Count"]) -> 'msk_top_regs_stat_32_errs_neg_0x410fa9bc87190658_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["LPF_Accum_F1"]) -> 'msk_top_regs_stat_32_lpf_acc_0x1be0f0bf59c971f9_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["LPF_Accum_F2"]) -> 'msk_top_regs_stat_32_lpf_acc_neg_0x71a284902b1741d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["axis_xfer_count"]) -> 'msk_top_regs_msk_stat_3_neg_0x724989d9d7fa96aa_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Rx_Sample_Discard"]) -> 'msk_top_regs_rx_sample_discard_0x57460af07270e6fd_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["LPF_Config_2"]) -> 'msk_top_regs_lpf_config_2_neg_0x65b9ddf457a2004f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f1_nco_adjust"]) -> 'msk_top_regs_status_reg_neg_0x561e6a8e0b780b6c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f2_nco_adjust"]) -> 'msk_top_regs_status_reg_neg_0x4d2d9eda85ed7f85_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f1_error"]) -> 'msk_top_regs_status_reg_0xc76f462239d17e2_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f2_error"]) -> 'msk_top_regs_status_reg_neg_0x3bb1d84b87620443_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Tx_Sync_Ctrl"]) -> 'msk_top_regs_tx_sync_ctrl_0x6860c618c7262d61_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Tx_Sync_Cnt"]) -> 'msk_top_regs_tx_sync_cnt_neg_0x1511021194f49355_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lowpass_ema_alpha1"]) -> 'msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lowpass_ema_alpha2"]) -> 'msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_power"]) -> 'msk_top_regs_rx_power_neg_0x2149d23df4ec0d38_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_async_fifo_rd_wr_ptr"]) -> 'msk_top_regs_status_reg_neg_0x612bf1b594ba3a1d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_async_fifo_rd_wr_ptr"]) -> 'msk_top_regs_status_reg_neg_0x7fad4991d4c753dd_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_frame_sync_status"]) -> 'msk_top_regs_frame_sync_status_0x1c3505bac15a3964_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["symbol_lock_control"]) -> 'msk_top_regs_symbol_lock_control_0x7a327095be616a18_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["symbol_lock_status"]) -> 'msk_top_regs_symbol_lock_status_0x1d147971e0fe260c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["symbol_lock_time"]) -> 'msk_top_regs_symbol_lock_time_neg_0x2caa632680878580_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_msk_hash_lo_0x743ecd7f54200b33_cls', 'msk_top_regs_msk_hash_hi_0x2fdfea8796573801_cls', 'msk_top_regs_msk_init_0x5784a15eda1d51f6_cls', 'msk_top_regs_msk_ctrl_0x6338546fd42c56c3_cls', 'msk_top_regs_msk_stat_0_0x11225f92044176be_cls', 'msk_top_regs_msk_stat_1_0x485040a78b4facc5_cls', 'msk_top_regs_msk_stat_2_0x79ca52b735200588_cls', 'msk_top_regs_config_nco_fw_0x444933e78de34535_cls', 'msk_top_regs_config_nco_fw_0x44f085218acb5a0b_cls', 'msk_top_regs_config_nco_fw_0x553395d594c88659_cls', 'msk_top_regs_config_nco_fw_0x33a361db4d08e83f_cls', 'msk_top_regs_config_nco_fw_neg_0x36fc9ff50bd27297_cls', 'msk_top_regs_lpf_config_0_neg_0x63d56b11f2a8b2a5_cls', 'msk_top_regs_lpf_config_1_0x6269262ac0819864_cls', 'msk_top_regs_data_width_0x30221bea82717e1e_cls', 'msk_top_regs_data_width_neg_0x361b7b87da257944_cls', 'msk_top_regs_prbs_ctrl_0x72ace307ca7cc42_cls', 'msk_top_regs_config_prbs_seed_neg_0x19de76e0a2449a75_cls', 'msk_top_regs_config_prbs_poly_0x59367282cbe7a1c8_cls', 'msk_top_regs_config_prbs_errmask_neg_0xcddb11619d27b12_cls', 'msk_top_regs_stat_32_bits_0x74f460ee43ed88ef_cls', 'msk_top_regs_stat_32_errs_neg_0x410fa9bc87190658_cls', 'msk_top_regs_stat_32_lpf_acc_0x1be0f0bf59c971f9_cls', 'msk_top_regs_stat_32_lpf_acc_neg_0x71a284902b1741d_cls', 'msk_top_regs_msk_stat_3_neg_0x724989d9d7fa96aa_cls', 'msk_top_regs_rx_sample_discard_0x57460af07270e6fd_cls', 'msk_top_regs_lpf_config_2_neg_0x65b9ddf457a2004f_cls', 'msk_top_regs_status_reg_neg_0x561e6a8e0b780b6c_cls', 'msk_top_regs_status_reg_neg_0x4d2d9eda85ed7f85_cls', 'msk_top_regs_status_reg_0xc76f462239d17e2_cls', 'msk_top_regs_status_reg_neg_0x3bb1d84b87620443_cls', 'msk_top_regs_tx_sync_ctrl_0x6860c618c7262d61_cls', 'msk_top_regs_tx_sync_cnt_neg_0x1511021194f49355_cls', 'msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls', 'msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls', 'msk_top_regs_rx_power_neg_0x2149d23df4ec0d38_cls', 'msk_top_regs_status_reg_neg_0x612bf1b594ba3a1d_cls', 'msk_top_regs_status_reg_neg_0x7fad4991d4c753dd_cls', 'msk_top_regs_frame_sync_status_0x1c3505bac15a3964_cls', 'msk_top_regs_symbol_lock_control_0x7a327095be616a18_cls', 'msk_top_regs_symbol_lock_status_0x1d147971e0fe260c_cls', 'msk_top_regs_symbol_lock_time_neg_0x2caa632680878580_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Pluto MSK Registers"
    @property
    def rdl_desc(self) -> str:
        return "MSK Modem Configuration and Status Registers"
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.Hash_ID_Low
        yield self.Hash_ID_High
        yield self.MSK_Init
        yield self.MSK_Control
        yield self.MSK_Status
        yield self.Tx_Bit_Count
        yield self.Tx_Enable_Count
        yield self.Fb_FreqWord
        yield self.TX_F1_FreqWord
        yield self.TX_F2_FreqWord
        yield self.RX_F1_FreqWord
        yield self.RX_F2_FreqWord
        yield self.LPF_Config_0
        yield self.LPF_Config_1
        yield self.Tx_Data_Width
        yield self.Rx_Data_Width
        yield self.PRBS_Control
        yield self.PRBS_Initial_State
        yield self.PRBS_Polynomial
        yield self.PRBS_Error_Mask
        yield self.PRBS_Bit_Count
        yield self.PRBS_Error_Count
        yield self.LPF_Accum_F1
        yield self.LPF_Accum_F2
        yield self.axis_xfer_count
        yield self.Rx_Sample_Discard
        yield self.LPF_Config_2
        yield self.f1_nco_adjust
        yield self.f2_nco_adjust
        yield self.f1_error
        yield self.f2_error
        yield self.Tx_Sync_Ctrl
        yield self.Tx_Sync_Cnt
        yield self.lowpass_ema_alpha1
        yield self.lowpass_ema_alpha2
        yield self.rx_power
        yield self.tx_async_fifo_rd_wr_ptr
        yield self.rx_async_fifo_rd_wr_ptr
        yield self.rx_frame_sync_status
        yield self.symbol_lock_control
        yield self.symbol_lock_status
        yield self.symbol_lock_time
        
        
    


msk_top_regs_cls = msk_top_regs_neg_0x6e59a13abed32d7c_cls

if __name__ == '__main__':
    # dummy functions to demonstrate the class
    async def read_addr_space(addr: int, width: int, accesswidth: int) -> int:
        """
        Callback to simulate the operation of the package, everytime the read is called, it will
        request the user input the value to be read back.

        Args:
            addr: Address to write to
            width: Width of the register in bits
            accesswidth: Minimum access width of the register in bits

        Returns:
            value inputted by the used
        """
        assert isinstance(addr, int)
        assert isinstance(width, int)
        assert isinstance(accesswidth, int)
        return int(input('value to read from address:0x%X'%addr))

    async def write_addr_space(addr: int, width: int, accesswidth: int, data: int) -> None:
        """
        Callback to simulate the operation of the package, everytime the read is called, it will
        request the user input the value to be read back.

        Args:
            addr: Address to write to
            width: Width of the register in bits
            accesswidth: Minimum access width of the register in bits
            data: value to be written to the register

        Returns:
            None
        """
        assert isinstance(addr, int)
        assert isinstance(width, int)
        assert isinstance(accesswidth, int)
        assert isinstance(data, int)
        print('write data:0x%X to address:0x%X'%(data, addr))

    # create an instance of the class
    msk_top_regs = msk_top_regs_cls(callbacks = AsyncCallbackSet(read_callback=read_addr_space,
                                                                                                     write_callback=write_addr_space))