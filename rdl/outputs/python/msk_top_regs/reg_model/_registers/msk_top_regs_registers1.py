

"""
Python Wrapper for the msk_top_regs register model

This code was generated from the PeakRDL-python package version 2.3.0

"""










from typing import Iterator
from typing import Union
from typing import overload
from typing import Literal
from typing import Any
from typing import NoReturn
from typing import Type

from ...lib import Node, NodeArray, Base
from ...lib import UDPStruct

from ...lib import AsyncMemory
from ...lib import AsyncAddressMap
from ...lib import AsyncRegFile
from ...lib import MemoryAsyncReadOnly, MemoryAsyncWriteOnly, MemoryAsyncReadWrite
from ...lib import AsyncReg
from ...lib import RegAsyncReadOnly, RegAsyncWriteOnly, RegAsyncReadWrite
from ...lib import RegAsyncReadOnlyArray, RegAsyncWriteOnlyArray, RegAsyncReadWriteArray
from ...lib import ReadableAsyncMemory, WritableAsyncMemory
from ...lib import FieldAsyncReadOnly, FieldAsyncWriteOnly, FieldAsyncReadWrite, Field

from ...lib import FieldSizeProps, FieldMiscProps






from .fields import msk_top_regs_rx_sample_discard_rx_sample_discard_neg_0x38eb4151bea7286c_cls
from .fields import msk_top_regs_rx_sample_discard_rx_nco_discard_neg_0x2b9c27e13c5cf83b_cls
from .fields import msk_top_regs_lpf_config_2_p_gain_neg_0x564ffd3b5c9ee5a_cls
from .fields import msk_top_regs_lpf_config_2_p_shift_0x4bc9a5c1aa9bb185_cls
from .fields import msk_top_regs_status_reg_data_0x4aca4cd89620a2eb_cls
from .fields import msk_top_regs_status_reg_data_neg_0x6c861e11e512bee8_cls
from .fields import msk_top_regs_status_reg_data_0x6606ce01300ede9e_cls
from .fields import msk_top_regs_status_reg_data_neg_0x4bf1ae36b78b0b04_cls
from .fields import msk_top_regs_tx_sync_ctrl_tx_sync_ena_neg_0x6fd8f3a2460f4f63_cls
from .fields import msk_top_regs_tx_sync_ctrl_tx_sync_force_0x9cde1909b978b15_cls
from .fields import msk_top_regs_tx_sync_cnt_tx_sync_cnt_neg_0x523b45dbe13fc09a_cls
from .fields import msk_top_regs_lowpass_ema_alpha_alpha_neg_0x23adfbbd4f5ca699_cls
from .fields import msk_top_regs_rx_power_data_neg_0x7d59af4abd6cddc0_cls
from .fields import msk_top_regs_status_reg_data_neg_0x105bc235a0a31370_cls
from .fields import msk_top_regs_frame_sync_status_frame_sync_locked_0x3f4fc2458f4f0cd2_cls
from .fields import msk_top_regs_frame_sync_status_frame_buffer_overflow_0x2a4a1a70827edd3d_cls
from .fields import msk_top_regs_frame_sync_status_frames_received_neg_0x7dbb6db13933fcd3_cls
from .fields import msk_top_regs_frame_sync_status_frame_sync_errors_neg_0x5b451d83cc348092_cls
from .fields import msk_top_regs_symbol_lock_control_symbol_lock_count_0x19781f0b431fdeca_cls
from .fields import msk_top_regs_symbol_lock_control_symbol_lock_threshold_0x4839317bf846465b_cls
from .fields import msk_top_regs_symbol_lock_status_f1f2_neg_0x39a76b7538e7e440_cls
from .fields import msk_top_regs_symbol_lock_status_f1_0x7a9ecba509a49e91_cls
from .fields import msk_top_regs_symbol_lock_status_f2_neg_0x4fb0b06c30787656_cls
from .fields import msk_top_regs_symbol_lock_status_unlock_f1_0x300f85594684937f_cls
from .fields import msk_top_regs_symbol_lock_status_unlock_f2_neg_0x4dd96876769cb4aa_cls
from .fields import msk_top_regs_symbol_lock_time_f1_0x2a2d395dea4e58d0_cls
from .fields import msk_top_regs_symbol_lock_time_f2_0x2bd399539720f3f_cls

# register definitions
    
    
class msk_top_regs_rx_sample_discard_0x57460af07270e6fd_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__rx_sample_discard', '__rx_nco_discard']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__rx_sample_discard:msk_top_regs_rx_sample_discard_rx_sample_discard_neg_0x38eb4151bea7286c_cls = msk_top_regs_rx_sample_discard_rx_sample_discard_neg_0x38eb4151bea7286c_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=0, msb=7,
                low=0, high=7),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.rx_sample_discard',
            inst_name='rx_sample_discard',
            field_type=int)
        self.__rx_nco_discard:msk_top_regs_rx_sample_discard_rx_nco_discard_neg_0x2b9c27e13c5cf83b_cls = msk_top_regs_rx_sample_discard_rx_nco_discard_neg_0x2b9c27e13c5cf83b_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=8, msb=15,
                low=8, high=15),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.rx_nco_discard',
            inst_name='rx_nco_discard',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def rx_sample_discard(self) -> msk_top_regs_rx_sample_discard_rx_sample_discard_neg_0x38eb4151bea7286c_cls:
        """
        Property to access rx_sample_discard field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Rx Sample Discard Value                                            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of Rx samples to discard</p>                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rx_sample_discard
    @property
    def rx_nco_discard(self) -> msk_top_regs_rx_sample_discard_rx_nco_discard_neg_0x2b9c27e13c5cf83b_cls:
        """
        Property to access rx_nco_discard field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Rx NCO Sample Discard Value                                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of NCO samples to discard</p>                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rx_nco_discard

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'rx_sample_discard':'rx_sample_discard','rx_nco_discard':'rx_nco_discard',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_sample_discard"]) -> 'msk_top_regs_rx_sample_discard_rx_sample_discard_neg_0x38eb4151bea7286c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_nco_discard"]) -> 'msk_top_regs_rx_sample_discard_rx_nco_discard_neg_0x2b9c27e13c5cf83b_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_rx_sample_discard_rx_sample_discard_neg_0x38eb4151bea7286c_cls', 'msk_top_regs_rx_sample_discard_rx_nco_discard_neg_0x2b9c27e13c5cf83b_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx Sample Discard"
    @property
    def rdl_desc(self) -> str:
        return "Configure samples discard operation for demodulator"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.rx_sample_discard
        yield self.rx_nco_discard
        
        
    

    
    
class msk_top_regs_lpf_config_2_neg_0x65b9ddf457a2004f_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__p_gain', '__p_shift']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__p_gain:msk_top_regs_lpf_config_2_p_gain_neg_0x564ffd3b5c9ee5a_cls = msk_top_regs_lpf_config_2_p_gain_neg_0x564ffd3b5c9ee5a_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=24,
                lsb=0, msb=23,
                low=0, high=23),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.p_gain',
            inst_name='p_gain',
            field_type=int)
        self.__p_shift:msk_top_regs_lpf_config_2_p_shift_0x4bc9a5c1aa9bb185_cls = msk_top_regs_lpf_config_2_p_shift_0x4bc9a5c1aa9bb185_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=24, msb=31,
                low=24, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.p_shift',
            inst_name='p_shift',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def p_gain(self) -> msk_top_regs_lpf_config_2_p_gain_neg_0x564ffd3b5c9ee5a_cls:
        """
        Property to access p_gain field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Proportional Gain Value                                            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Value m of 0-16,777,215 sets the proportional multiplier</p>    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__p_gain
    @property
    def p_shift(self) -> msk_top_regs_lpf_config_2_p_shift_0x4bc9a5c1aa9bb185_cls:
        """
        Property to access p_shift field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Proportional Gain Bit Shift                                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Value n of 0-32 sets the proportional divisor as 2^-n</p>       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__p_shift

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'p_gain':'p_gain','p_shift':'p_shift',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["p_gain"]) -> 'msk_top_regs_lpf_config_2_p_gain_neg_0x564ffd3b5c9ee5a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["p_shift"]) -> 'msk_top_regs_lpf_config_2_p_shift_0x4bc9a5c1aa9bb185_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_lpf_config_2_p_gain_neg_0x564ffd3b5c9ee5a_cls', 'msk_top_regs_lpf_config_2_p_shift_0x4bc9a5c1aa9bb185_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PI Controller Configuration Configuration Register 2"
    @property
    def rdl_desc(self) -> str:
        return "Configures PI Controller I-gain and divisor"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.p_gain
        yield self.p_shift
        
        
    

    
    
class msk_top_regs_status_reg_neg_0x561e6a8e0b780b6c_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_status_reg_data_0x4aca4cd89620a2eb_cls = msk_top_regs_status_reg_data_0x4aca4cd89620a2eb_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_status_reg_data_0x4aca4cd89620a2eb_cls:
        """
        Property to access data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Frequency offet applied to the F1 NCO</p> <p>This register is   |
        |              |      write-to-capture.</p> <p>To read data the following steps are      |
        |              |      required:</p> <p>1 - Write any value to this register to capture   |
        |              |      read data</p> <p>2 - Read the register</p>                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_status_reg_data_0x4aca4cd89620a2eb_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F1 NCO Frequency Adjust"
    @property
    def rdl_desc(self) -> str:
        return "Status Register"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_status_reg_neg_0x4d2d9eda85ed7f85_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_status_reg_data_neg_0x6c861e11e512bee8_cls = msk_top_regs_status_reg_data_neg_0x6c861e11e512bee8_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_status_reg_data_neg_0x6c861e11e512bee8_cls:
        """
        Property to access data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Frequency offet applied to the F2 NCO</p> <p>This register is   |
        |              |      write-to-capture.</p> <p>To read data the following steps are      |
        |              |      required:</p> <p>1 - Write any value to this register to capture   |
        |              |      read data</p> <p>2 - Read the register</p>                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_status_reg_data_neg_0x6c861e11e512bee8_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F2 NCO Frequency Adjust"
    @property
    def rdl_desc(self) -> str:
        return "Status Register"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_status_reg_0xc76f462239d17e2_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_status_reg_data_0x6606ce01300ede9e_cls = msk_top_regs_status_reg_data_0x6606ce01300ede9e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_status_reg_data_0x6606ce01300ede9e_cls:
        """
        Property to access data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Error value of the F1 Costas loop after each active bit         |
        |              |      period</p> <p>This register is write-to-capture.</p> <p>To read    |
        |              |      data the following steps are required:</p> <p>1 - Write any value  |
        |              |      to this register to capture read data</p> <p>2 - Read the          |
        |              |      register</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_status_reg_data_0x6606ce01300ede9e_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F1 Error Value"
    @property
    def rdl_desc(self) -> str:
        return "Status Register"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_status_reg_neg_0x3bb1d84b87620443_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_status_reg_data_neg_0x4bf1ae36b78b0b04_cls = msk_top_regs_status_reg_data_neg_0x4bf1ae36b78b0b04_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_status_reg_data_neg_0x4bf1ae36b78b0b04_cls:
        """
        Property to access data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Error value of the F2 Costas loop after each active bit         |
        |              |      period</p> <p>This register is write-to-capture.</p> <p>To read    |
        |              |      data the following steps are required:</p> <p>1 - Write any value  |
        |              |      to this register to capture read data</p> <p>2 - Read the          |
        |              |      register</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_status_reg_data_neg_0x4bf1ae36b78b0b04_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F2 Error Value"
    @property
    def rdl_desc(self) -> str:
        return "Status Register"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_tx_sync_ctrl_0x6860c618c7262d61_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__tx_sync_ena', '__tx_sync_force']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__tx_sync_ena:msk_top_regs_tx_sync_ctrl_tx_sync_ena_neg_0x6fd8f3a2460f4f63_cls = msk_top_regs_tx_sync_ctrl_tx_sync_ena_neg_0x6fd8f3a2460f4f63_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tx_sync_ena',
            inst_name='tx_sync_ena',
            field_type=int)
        self.__tx_sync_force:msk_top_regs_tx_sync_ctrl_tx_sync_force_0x9cde1909b978b15_cls = msk_top_regs_tx_sync_ctrl_tx_sync_force_0x9cde1909b978b15_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1, msb=1,
                low=1, high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tx_sync_force',
            inst_name='tx_sync_force',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tx_sync_ena(self) -> msk_top_regs_tx_sync_ctrl_tx_sync_ena_neg_0x6fd8f3a2460f4f63_cls:
        """
        Property to access tx_sync_ena field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx Sync Enable                                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 : Disable sync transmission</p> <p>1 : Enable sync            |
        |              |      transmission when PTT is asserted</p>                              |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_sync_ena
    @property
    def tx_sync_force(self) -> msk_top_regs_tx_sync_ctrl_tx_sync_force_0x9cde1909b978b15_cls:
        """
        Property to access tx_sync_force field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx Sync Force                                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 : Normal operation</p> <p>1 : Continuously transmit           |
        |              |      synchronization pattern</p>                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_sync_force

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tx_sync_ena':'tx_sync_ena','tx_sync_force':'tx_sync_force',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_sync_ena"]) -> 'msk_top_regs_tx_sync_ctrl_tx_sync_ena_neg_0x6fd8f3a2460f4f63_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_sync_force"]) -> 'msk_top_regs_tx_sync_ctrl_tx_sync_force_0x9cde1909b978b15_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_tx_sync_ctrl_tx_sync_ena_neg_0x6fd8f3a2460f4f63_cls', 'msk_top_regs_tx_sync_ctrl_tx_sync_force_0x9cde1909b978b15_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Transmitter Sync Control"
    @property
    def rdl_desc(self) -> str:
        return "Provides control bits for generation of transmitter synchronization patterns"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.tx_sync_ena
        yield self.tx_sync_force
        
        
    

    
    
class msk_top_regs_tx_sync_cnt_neg_0x1511021194f49355_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__tx_sync_cnt']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__tx_sync_cnt:msk_top_regs_tx_sync_cnt_tx_sync_cnt_neg_0x523b45dbe13fc09a_cls = msk_top_regs_tx_sync_cnt_tx_sync_cnt_neg_0x523b45dbe13fc09a_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=24,
                lsb=0, msb=23,
                low=0, high=23),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tx_sync_cnt',
            inst_name='tx_sync_cnt',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tx_sync_cnt(self) -> msk_top_regs_tx_sync_cnt_tx_sync_cnt_neg_0x523b45dbe13fc09a_cls:
        """
        Property to access tx_sync_cnt field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx sync duration                                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Value from 0x00_0000 to 0xFF_FFFF. </p> <p>This value           |
        |              |      represents the number bit-times the synchronization signal should  |
        |              |      be sent after PTT is asserted.</p>                                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_sync_cnt

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tx_sync_cnt':'tx_sync_cnt',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_tx_sync_cnt_tx_sync_cnt_neg_0x523b45dbe13fc09a_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Transmitter Sync Duration"
    @property
    def rdl_desc(self) -> str:
        return "Sets the duration of the synchronization tones when enabled"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.tx_sync_cnt
        
        
    

    
    
class msk_top_regs_lowpass_ema_alpha_neg_0x1f19d8e3d96065c9_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__alpha']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__alpha:msk_top_regs_lowpass_ema_alpha_alpha_neg_0x23adfbbd4f5ca699_cls = msk_top_regs_lowpass_ema_alpha_alpha_neg_0x23adfbbd4f5ca699_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=18,
                lsb=0, msb=17,
                low=0, high=17),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.alpha',
            inst_name='alpha',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def alpha(self) -> msk_top_regs_lowpass_ema_alpha_alpha_neg_0x23adfbbd4f5ca699_cls:
        """
        Property to access alpha field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      EMA alpha                                                          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Value from 0x0_0000 to 0x3_FFFF represent the EMA alpha</p>     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__alpha

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'alpha':'alpha',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_lowpass_ema_alpha_alpha_neg_0x23adfbbd4f5ca699_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Exponential Moving Average Alpha"
    @property
    def rdl_desc(self) -> str:
        return "Sets the alpha for the EMA"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.alpha
        
        
    

    
    
class msk_top_regs_rx_power_neg_0x2149d23df4ec0d38_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_rx_power_data_neg_0x7d59af4abd6cddc0_cls = msk_top_regs_rx_power_data_neg_0x7d59af4abd6cddc0_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=23,
                lsb=0, msb=22,
                low=0, high=22),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_rx_power_data_neg_0x7d59af4abd6cddc0_cls:
        """
        Property to access data field of the register

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
        |              |      <p>Value that represent the RMS power of the incoming signal       |
        |              |      (I-channel)</p> <p>This register is write-to-capture. To read data |
        |              |      the following steps are required:</p> <ol type="1"> <li> Write any |
        |              |      value to this register to capture read data </li><li> Read the     |
        |              |      register </li></ol>                                                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_rx_power_data_neg_0x7d59af4abd6cddc0_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Receive Power"
    @property
    def rdl_desc(self) -> str:
        return "Receive power computed from I/Q samples"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_status_reg_neg_0x612bf1b594ba3a1d_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_status_reg_data_neg_0x105bc235a0a31370_cls = msk_top_regs_status_reg_data_neg_0x105bc235a0a31370_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_status_reg_data_neg_0x105bc235a0a31370_cls:
        """
        Property to access data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Read and Write Pointers</p> <p><code> Bits 31:16 - write        |
        |              |      pointer (12-bits) Bits 15:00 - read pointer (12-bits)</code></p>   |
        |              |      <p>This register is write-to-capture. To read data the following   |
        |              |      steps are required:</p> <ol type="1"> <li> Write any value to this |
        |              |      register to capture read data </li><li> Read the register          |
        |              |      </li></ol>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_status_reg_data_neg_0x105bc235a0a31370_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx async FIFO read and write pointers"
    @property
    def rdl_desc(self) -> str:
        return "Tx async FIFO read and write pointers"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_status_reg_neg_0x7fad4991d4c753dd_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_status_reg_data_neg_0x105bc235a0a31370_cls = msk_top_regs_status_reg_data_neg_0x105bc235a0a31370_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_status_reg_data_neg_0x105bc235a0a31370_cls:
        """
        Property to access data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Read and Write Pointers</p> <p><code> Bits 31:16 - write        |
        |              |      pointer (12-bits) Bits 15:00 - read pointer (12-bits)</code></p>   |
        |              |      <p>This register is write-to-capture. To read data the following   |
        |              |      steps are required:</p> <ol type="1"> <li> Write any value to this |
        |              |      register to capture read data </li><li> Read the register          |
        |              |      </li></ol>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_status_reg_data_neg_0x105bc235a0a31370_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx async FIFO read and write pointers"
    @property
    def rdl_desc(self) -> str:
        return "Rx async FIFO read and write pointers"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_frame_sync_status_0x1c3505bac15a3964_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Frame Sync Status                                                  |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__frame_sync_locked', '__frame_buffer_overflow', '__frames_received', '__frame_sync_errors']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__frame_sync_locked:msk_top_regs_frame_sync_status_frame_sync_locked_0x3f4fc2458f4f0cd2_cls = msk_top_regs_frame_sync_status_frame_sync_locked_0x3f4fc2458f4f0cd2_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.frame_sync_locked',
            inst_name='frame_sync_locked',
            field_type=int)
        self.__frame_buffer_overflow:msk_top_regs_frame_sync_status_frame_buffer_overflow_0x2a4a1a70827edd3d_cls = msk_top_regs_frame_sync_status_frame_buffer_overflow_0x2a4a1a70827edd3d_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1, msb=1,
                low=1, high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.frame_buffer_overflow',
            inst_name='frame_buffer_overflow',
            field_type=int)
        self.__frames_received:msk_top_regs_frame_sync_status_frames_received_neg_0x7dbb6db13933fcd3_cls = msk_top_regs_frame_sync_status_frames_received_neg_0x7dbb6db13933fcd3_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=24,
                lsb=2, msb=25,
                low=2, high=25),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.frames_received',
            inst_name='frames_received',
            field_type=int)
        self.__frame_sync_errors:msk_top_regs_frame_sync_status_frame_sync_errors_neg_0x5b451d83cc348092_cls = msk_top_regs_frame_sync_status_frame_sync_errors_neg_0x5b451d83cc348092_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=6,
                lsb=26, msb=31,
                low=26, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.frame_sync_errors',
            inst_name='frame_sync_errors',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def frame_sync_locked(self) -> msk_top_regs_frame_sync_status_frame_sync_locked_0x3f4fc2458f4f0cd2_cls:
        """
        Property to access frame_sync_locked field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Frame Sync Lock                                                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 - Frame sync not locked 1 - Frame sync locked</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__frame_sync_locked
    @property
    def frame_buffer_overflow(self) -> msk_top_regs_frame_sync_status_frame_buffer_overflow_0x2a4a1a70827edd3d_cls:
        """
        Property to access frame_buffer_overflow field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Frame Buffer Overflow                                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 - Normal operation 1 - Buffer overflow</p>                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__frame_buffer_overflow
    @property
    def frames_received(self) -> msk_top_regs_frame_sync_status_frames_received_neg_0x7dbb6db13933fcd3_cls:
        """
        Property to access frames_received field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Frames Received                                                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Count of frames received. Value is 0x00_0000 to 0xFF_FFFF.      |
        |              |      Counter rolls over when max count is reached.</p>                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__frames_received
    @property
    def frame_sync_errors(self) -> msk_top_regs_frame_sync_status_frame_sync_errors_neg_0x5b451d83cc348092_cls:
        """
        Property to access frame_sync_errors field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Frames Sync Errors                                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Count of frame sync errors. Value is 0 to 63. Counter rolls     |
        |              |      over when max count is reached.</p>                                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__frame_sync_errors

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'frame_sync_locked':'frame_sync_locked','frame_buffer_overflow':'frame_buffer_overflow','frames_received':'frames_received','frame_sync_errors':'frame_sync_errors',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["frame_sync_locked"]) -> 'msk_top_regs_frame_sync_status_frame_sync_locked_0x3f4fc2458f4f0cd2_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["frame_buffer_overflow"]) -> 'msk_top_regs_frame_sync_status_frame_buffer_overflow_0x2a4a1a70827edd3d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["frames_received"]) -> 'msk_top_regs_frame_sync_status_frames_received_neg_0x7dbb6db13933fcd3_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["frame_sync_errors"]) -> 'msk_top_regs_frame_sync_status_frame_sync_errors_neg_0x5b451d83cc348092_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_frame_sync_status_frame_sync_locked_0x3f4fc2458f4f0cd2_cls', 'msk_top_regs_frame_sync_status_frame_buffer_overflow_0x2a4a1a70827edd3d_cls', 'msk_top_regs_frame_sync_status_frames_received_neg_0x7dbb6db13933fcd3_cls', 'msk_top_regs_frame_sync_status_frame_sync_errors_neg_0x5b451d83cc348092_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Frame Sync Status"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.frame_sync_locked
        yield self.frame_buffer_overflow
        yield self.frames_received
        yield self.frame_sync_errors
        
        
    

    
    
class msk_top_regs_symbol_lock_control_0x7a327095be616a18_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Symbol Lock Control                                                |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__symbol_lock_count', '__symbol_lock_threshold']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__symbol_lock_count:msk_top_regs_symbol_lock_control_symbol_lock_count_0x19781f0b431fdeca_cls = msk_top_regs_symbol_lock_control_symbol_lock_count_0x19781f0b431fdeca_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=10,
                lsb=0, msb=9,
                low=0, high=9),
            misc_props=FieldMiscProps(
                default=128,
                is_volatile=False),
            logger_handle=logger_handle+'.symbol_lock_count',
            inst_name='symbol_lock_count',
            field_type=int)
        self.__symbol_lock_threshold:msk_top_regs_symbol_lock_control_symbol_lock_threshold_0x4839317bf846465b_cls = msk_top_regs_symbol_lock_control_symbol_lock_threshold_0x4839317bf846465b_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=10, msb=25,
                low=10, high=25),
            misc_props=FieldMiscProps(
                default=10000,
                is_volatile=False),
            logger_handle=logger_handle+'.symbol_lock_threshold',
            inst_name='symbol_lock_threshold',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def symbol_lock_count(self) -> msk_top_regs_symbol_lock_control_symbol_lock_count_0x19781f0b431fdeca_cls:
        """
        Property to access symbol_lock_count field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Symbol Lock Integration Count                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sets the integration period in symbols. Value is from 0 to      |
        |              |      1023.</p>                                                          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__symbol_lock_count
    @property
    def symbol_lock_threshold(self) -> msk_top_regs_symbol_lock_control_symbol_lock_threshold_0x4839317bf846465b_cls:
        """
        Property to access symbol_lock_threshold field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Symbol Lock Threshold                                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sets the threshold value on which to declare symbol sync</p>    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__symbol_lock_threshold

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'symbol_lock_count':'symbol_lock_count','symbol_lock_threshold':'symbol_lock_threshold',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["symbol_lock_count"]) -> 'msk_top_regs_symbol_lock_control_symbol_lock_count_0x19781f0b431fdeca_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["symbol_lock_threshold"]) -> 'msk_top_regs_symbol_lock_control_symbol_lock_threshold_0x4839317bf846465b_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_symbol_lock_control_symbol_lock_count_0x19781f0b431fdeca_cls', 'msk_top_regs_symbol_lock_control_symbol_lock_threshold_0x4839317bf846465b_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Symbol Lock Control"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.symbol_lock_count
        yield self.symbol_lock_threshold
        
        
    

    
    
class msk_top_regs_symbol_lock_status_0x1d147971e0fe260c_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Symbol Lock Status                                                 |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__f1f2', '__f1', '__f2', '__unlock_f1', '__unlock_f2']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__f1f2:msk_top_regs_symbol_lock_status_f1f2_neg_0x39a76b7538e7e440_cls = msk_top_regs_symbol_lock_status_f1f2_neg_0x39a76b7538e7e440_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.f1f2',
            inst_name='f1f2',
            field_type=int)
        self.__f1:msk_top_regs_symbol_lock_status_f1_0x7a9ecba509a49e91_cls = msk_top_regs_symbol_lock_status_f1_0x7a9ecba509a49e91_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1, msb=1,
                low=1, high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.f1',
            inst_name='f1',
            field_type=int)
        self.__f2:msk_top_regs_symbol_lock_status_f2_neg_0x4fb0b06c30787656_cls = msk_top_regs_symbol_lock_status_f2_neg_0x4fb0b06c30787656_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2, msb=2,
                low=2, high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.f2',
            inst_name='f2',
            field_type=int)
        self.__unlock_f1:msk_top_regs_symbol_lock_status_unlock_f1_0x300f85594684937f_cls = msk_top_regs_symbol_lock_status_unlock_f1_0x300f85594684937f_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=3, msb=3,
                low=3, high=3),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.unlock_f1',
            inst_name='unlock_f1',
            field_type=int)
        self.__unlock_f2:msk_top_regs_symbol_lock_status_unlock_f2_neg_0x4dd96876769cb4aa_cls = msk_top_regs_symbol_lock_status_unlock_f2_neg_0x4dd96876769cb4aa_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=4, msb=4,
                low=4, high=4),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.unlock_f2',
            inst_name='unlock_f2',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def f1f2(self) -> msk_top_regs_symbol_lock_status_f1f2_neg_0x39a76b7538e7e440_cls:
        """
        Property to access f1f2 field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Symbol Lock F1 and F2                                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 - Unlocked 1 - F1 and F2 locked</p>                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f1f2
    @property
    def f1(self) -> msk_top_regs_symbol_lock_status_f1_0x7a9ecba509a49e91_cls:
        """
        Property to access f1 field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Symbol Lock F1                                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 - Unlocked 1 - F1 locked</p>                                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f1
    @property
    def f2(self) -> msk_top_regs_symbol_lock_status_f2_neg_0x4fb0b06c30787656_cls:
        """
        Property to access f2 field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Symbol Lock F2                                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 - Unlocked 1 - F2 locked</p>                                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f2
    @property
    def unlock_f1(self) -> msk_top_regs_symbol_lock_status_unlock_f1_0x300f85594684937f_cls:
        """
        Property to access unlock_f1 field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      F1 unlocked since last read                                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 - No unlock since last read 1 - One or mode unlocks since     |
        |              |      last read</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__unlock_f1
    @property
    def unlock_f2(self) -> msk_top_regs_symbol_lock_status_unlock_f2_neg_0x4dd96876769cb4aa_cls:
        """
        Property to access unlock_f2 field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      F2 unlocked since last read                                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 - No unlock since last read 1 - One or mode unlocks since     |
        |              |      last read</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__unlock_f2

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'f1f2':'f1f2','f1':'f1','f2':'f2','unlock_f1':'unlock_f1','unlock_f2':'unlock_f2',
            }

    
    
    
    
    
    
    # nodes:5
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f1f2"]) -> 'msk_top_regs_symbol_lock_status_f1f2_neg_0x39a76b7538e7e440_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f1"]) -> 'msk_top_regs_symbol_lock_status_f1_0x7a9ecba509a49e91_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f2"]) -> 'msk_top_regs_symbol_lock_status_f2_neg_0x4fb0b06c30787656_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["unlock_f1"]) -> 'msk_top_regs_symbol_lock_status_unlock_f1_0x300f85594684937f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["unlock_f2"]) -> 'msk_top_regs_symbol_lock_status_unlock_f2_neg_0x4dd96876769cb4aa_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_symbol_lock_status_f1f2_neg_0x39a76b7538e7e440_cls', 'msk_top_regs_symbol_lock_status_f1_0x7a9ecba509a49e91_cls', 'msk_top_regs_symbol_lock_status_f2_neg_0x4fb0b06c30787656_cls', 'msk_top_regs_symbol_lock_status_unlock_f1_0x300f85594684937f_cls', 'msk_top_regs_symbol_lock_status_unlock_f2_neg_0x4dd96876769cb4aa_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Symbol Lock Status"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.f1f2
        yield self.f1
        yield self.f2
        yield self.unlock_f1
        yield self.unlock_f2
        
        
    

    
    
class msk_top_regs_symbol_lock_time_neg_0x2caa632680878580_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Symbol Lock Time                                                   |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__f1', '__f2']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__f1:msk_top_regs_symbol_lock_time_f1_0x2a2d395dea4e58d0_cls = msk_top_regs_symbol_lock_time_f1_0x2a2d395dea4e58d0_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=0, msb=15,
                low=0, high=15),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.f1',
            inst_name='f1',
            field_type=int)
        self.__f2:msk_top_regs_symbol_lock_time_f2_0x2bd399539720f3f_cls = msk_top_regs_symbol_lock_time_f2_0x2bd399539720f3f_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=16, msb=31,
                low=16, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.f2',
            inst_name='f2',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def f1(self) -> msk_top_regs_symbol_lock_time_f1_0x2a2d395dea4e58d0_cls:
        """
        Property to access f1 field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      F1 Symbol Lock Time                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of symbols for F1 lock since init released</p>           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f1
    @property
    def f2(self) -> msk_top_regs_symbol_lock_time_f2_0x2bd399539720f3f_cls:
        """
        Property to access f2 field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      F2 Symbol Lock Time                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of symbols for F2 lock since init released</p>           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f2

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'f1':'f1','f2':'f2',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f1"]) -> 'msk_top_regs_symbol_lock_time_f1_0x2a2d395dea4e58d0_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f2"]) -> 'msk_top_regs_symbol_lock_time_f2_0x2bd399539720f3f_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_symbol_lock_time_f1_0x2a2d395dea4e58d0_cls', 'msk_top_regs_symbol_lock_time_f2_0x2bd399539720f3f_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Symbol Lock Time"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.f1
        yield self.f2
        
        
    


if __name__ == '__main__':
    pass