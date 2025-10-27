


"""
Python Wrapper for the msk_top_regs register model

This code was generated from the PeakRDL-python package version 1.4.0

"""


from enum import unique
from typing import Iterator
from typing import Optional
from typing import Union
from typing import Type
from typing import overload
from typing import Literal
from typing import Any
from typing import NoReturn
from typing import AsyncGenerator

import warnings



from contextlib import asynccontextmanager

from ..lib import Node, Base
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
from ..lib import FieldSizeProps, FieldMiscProps


from ..lib import SystemRDLEnum, SystemRDLEnumEntry



from ..lib import AsyncCallbackSet, AsyncCallbackSetLegacy



















# regfile, register and field definitions
    
    
    
class msk_top_regs_data32_desc_7b98a70e_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Bits 31:16 -&gt; write pointer (12-bits) Bits 15:00 -&gt; read  |
    |              |      pointer (12-bits)</p>                                              |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_desc(self) -> str:
        return "Bits 31:16 -\u003e write pointer (12-bits)\nBits 15:00 -\u003e read pointer (12-bits)"
    
    
    

    
    
class msk_top_regs_observation_data_data_cf6acbd7_name_8a90eed1_cls(RegAsyncReadOnly):
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
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_data32_desc_7b98a70e_cls = msk_top_regs_data32_desc_7b98a70e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_data32_desc_7b98a70e_cls:
        """
        Property to access data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Bits 31:16 -&gt; write pointer (12-bits) Bits 15:00 -&gt; read  |
        |              |      pointer (12-bits)</p>                                              |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_data32_desc_7b98a70e_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx async FIFO read and write pointers"
    
    
    

    
    
    
class msk_top_regs_data32_desc_7b98a70e_0x0x1075e913_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Bits 31:16 -&gt; write pointer (12-bits) Bits 15:00 -&gt; read  |
    |              |      pointer (12-bits)</p>                                              |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_desc(self) -> str:
        return "Bits 31:16 -\u003e write pointer (12-bits)\nBits 15:00 -\u003e read pointer (12-bits)"
    
    
    

    
    
class msk_top_regs_observation_data_data_cf6acbd7_name_aa4ec676_cls(RegAsyncReadOnly):
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
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_data32_desc_7b98a70e_0x0x1075e913_cls = msk_top_regs_data32_desc_7b98a70e_0x0x1075e913_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_data32_desc_7b98a70e_0x0x1075e913_cls:
        """
        Property to access data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Bits 31:16 -&gt; write pointer (12-bits) Bits 15:00 -&gt; read  |
        |              |      pointer (12-bits)</p>                                              |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_data32_desc_7b98a70e_0x0x1075e913_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx async FIFO read and write pointers"
    
    
    

    
    
    
class msk_top_regs_rx_power_rx_power_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

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
    |              |      <p>Value that represent the RMS power of the incoming I;</p>       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Receive Power"
    @property
    def rdl_desc(self) -> str:
        return "Value that represent the RMS power of the incoming I;"
    
    
    

    
    
class msk_top_regs_rx_power_cls(RegAsyncReadOnly):
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
    |              |      <p>Receive power computed from I/Q ssamples</p>                    |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__rx_power']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__rx_power:msk_top_regs_rx_power_rx_power_cls = msk_top_regs_rx_power_rx_power_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=23,
                lsb=0,
                msb=22,
                low=0,
                high=22),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.rx_power',
            inst_name='rx_power',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.rx_power
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def rx_power(self) -> msk_top_regs_rx_power_rx_power_cls:
        """
        Property to access rx_power field of the register

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
        |              |      <p>Value that represent the RMS power of the incoming I;</p>       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rx_power

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'rx_power':'rx_power',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_rx_power_rx_power_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Receive Power"
    @property
    def rdl_desc(self) -> str:
        return "Receive power computed from I/Q ssamples"
    
    
    

    
    
    
class msk_top_regs_lowpass_ema_alpha_alpha_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

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

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "EMA alpha"
    @property
    def rdl_desc(self) -> str:
        return "Value from 0x0_0000 to 0x3_FFFF represent the EMA alpha"
    
    
    

    
    
class msk_top_regs_lowpass_ema_alpha_cls(RegAsyncReadWrite):
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
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__alpha:msk_top_regs_lowpass_ema_alpha_alpha_cls = msk_top_regs_lowpass_ema_alpha_alpha_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=18,
                lsb=0,
                msb=17,
                low=0,
                high=17),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.alpha',
            inst_name='alpha',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.alpha
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def alpha(self) -> msk_top_regs_lowpass_ema_alpha_alpha_cls:
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
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'alpha':'alpha',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_lowpass_ema_alpha_alpha_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Exponential Moving Average Alpha"
    @property
    def rdl_desc(self) -> str:
        return "Sets the alpha for the EMA"
    
    
    

    
    
    
class msk_top_regs_lowpass_ema_alpha_alpha_0x0x1075e9a9_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

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

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "EMA alpha"
    @property
    def rdl_desc(self) -> str:
        return "Value from 0x0_0000 to 0x3_FFFF represent the EMA alpha"
    
    
    

    
    
class msk_top_regs_lowpass_ema_alpha_0x0x1075e9f4_cls(RegAsyncReadWrite):
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
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__alpha:msk_top_regs_lowpass_ema_alpha_alpha_0x0x1075e9a9_cls = msk_top_regs_lowpass_ema_alpha_alpha_0x0x1075e9a9_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=18,
                lsb=0,
                msb=17,
                low=0,
                high=17),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.alpha',
            inst_name='alpha',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.alpha
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def alpha(self) -> msk_top_regs_lowpass_ema_alpha_alpha_0x0x1075e9a9_cls:
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
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'alpha':'alpha',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_lowpass_ema_alpha_alpha_0x0x1075e9a9_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Exponential Moving Average Alpha"
    @property
    def rdl_desc(self) -> str:
        return "Sets the alpha for the EMA"
    
    
    

    
    
    
class msk_top_regs_tx_sync_cnt_tx_sync_cnt_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

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
    |              |      <p>Value from 0x00_0000 to 0xFF_FFFF.  This value represents the   |
    |              |      number bit-times the synchronization  signal should be sent after  |
    |              |      PTT is asserted.</p>                                               |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx sync duration"
    @property
    def rdl_desc(self) -> str:
        return "Value from 0x00_0000 to 0xFF_FFFF. \nThis value represents the number bit-times the synchronization \nsignal should be sent after PTT is asserted."
    
    
    

    
    
class msk_top_regs_tx_sync_cnt_cls(RegAsyncReadWrite):
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
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__tx_sync_cnt:msk_top_regs_tx_sync_cnt_tx_sync_cnt_cls = msk_top_regs_tx_sync_cnt_tx_sync_cnt_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=24,
                lsb=0,
                msb=23,
                low=0,
                high=23),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tx_sync_cnt',
            inst_name='tx_sync_cnt',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.tx_sync_cnt
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def tx_sync_cnt(self) -> msk_top_regs_tx_sync_cnt_tx_sync_cnt_cls:
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
        |              |      <p>Value from 0x00_0000 to 0xFF_FFFF.  This value represents the   |
        |              |      number bit-times the synchronization  signal should be sent after  |
        |              |      PTT is asserted.</p>                                               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_sync_cnt

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'tx_sync_cnt':'tx_sync_cnt',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_tx_sync_cnt_tx_sync_cnt_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Transmitter Sync Duration"
    @property
    def rdl_desc(self) -> str:
        return "Sets the duration of the synchronization tones when enabled"
    
    
    

    
    
    
class msk_top_regs_tx_sync_ctrl_tx_sync_f2_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Tx F2 Sync Enable                                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Enables/Disables transmission of F2 tone for receiver           |
    |              |      synchronization 0 : F2 tone transmission disabled 1 : F2 tone      |
    |              |      transmission enabled Both F1 and F2 can be enabled at the same     |
    |              |      time</p>                                                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx F2 Sync Enable"
    @property
    def rdl_desc(self) -> str:
        return "Enables/Disables transmission of F2 tone for receiver synchronization\n0 : F2 tone transmission disabled\n1 : F2 tone transmission enabled\nBoth F1 and F2 can be enabled at the same time"
    
    
    

    
    
    
class msk_top_regs_tx_sync_ctrl_tx_sync_f1_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Tx F1 Sync Enable                                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Enables/Disables transmission of F1 tone for receiver           |
    |              |      synchronization 0 : F1 tone transmission disabled 1 : F1 tone      |
    |              |      transmission enabled Both F1 and F2 can be enabled at the same     |
    |              |      time</p>                                                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx F1 Sync Enable"
    @property
    def rdl_desc(self) -> str:
        return "Enables/Disables transmission of F1 tone for receiver synchronization\n0 : F1 tone transmission disabled\n1 : F1 tone transmission enabled\nBoth F1 and F2 can be enabled at the same time"
    
    
    

    
    
    
class msk_top_regs_tx_sync_ctrl_tx_sync_force_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

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
    |              |      <p>0 : Normal operation) 1 : Transmit synchronization pattern)</p> |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx Sync Force"
    @property
    def rdl_desc(self) -> str:
        return "0 : Normal operation)\n1 : Transmit synchronization pattern)"
    
    
    

    
    
    
class msk_top_regs_tx_sync_ctrl_tx_sync_ena_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

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
    |              |      <p>0 -&gt; Disable sync transmission 1 -&gt; Enable sync           |
    |              |      transmission when PTT is asserted</p>                              |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx Sync Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Disable sync transmission\n1 -\u003e Enable sync transmission when PTT is asserted"
    
    
    

    
    
class msk_top_regs_tx_sync_ctrl_cls(RegAsyncReadWrite):
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

    __slots__ : list[str] = ['__tx_sync_ena', '__tx_sync_force', '__tx_sync_f1', '__tx_sync_f2']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__tx_sync_ena:msk_top_regs_tx_sync_ctrl_tx_sync_ena_cls = msk_top_regs_tx_sync_ctrl_tx_sync_ena_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0,
                msb=0,
                low=0,
                high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tx_sync_ena',
            inst_name='tx_sync_ena',
            field_type=int)
        self.__tx_sync_force:msk_top_regs_tx_sync_ctrl_tx_sync_force_cls = msk_top_regs_tx_sync_ctrl_tx_sync_force_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1,
                msb=1,
                low=1,
                high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tx_sync_force',
            inst_name='tx_sync_force',
            field_type=int)
        self.__tx_sync_f1:msk_top_regs_tx_sync_ctrl_tx_sync_f1_cls = msk_top_regs_tx_sync_ctrl_tx_sync_f1_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2,
                msb=2,
                low=2,
                high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tx_sync_f1',
            inst_name='tx_sync_f1',
            field_type=int)
        self.__tx_sync_f2:msk_top_regs_tx_sync_ctrl_tx_sync_f2_cls = msk_top_regs_tx_sync_ctrl_tx_sync_f2_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=3,
                msb=3,
                low=3,
                high=3),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tx_sync_f2',
            inst_name='tx_sync_f2',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.tx_sync_ena
        yield self.tx_sync_force
        yield self.tx_sync_f1
        yield self.tx_sync_f2
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def tx_sync_ena(self) -> msk_top_regs_tx_sync_ctrl_tx_sync_ena_cls:
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
        |              |      <p>0 -&gt; Disable sync transmission 1 -&gt; Enable sync           |
        |              |      transmission when PTT is asserted</p>                              |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_sync_ena
    @property
    def tx_sync_force(self) -> msk_top_regs_tx_sync_ctrl_tx_sync_force_cls:
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
        |              |      <p>0 : Normal operation) 1 : Transmit synchronization pattern)</p> |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_sync_force
    @property
    def tx_sync_f1(self) -> msk_top_regs_tx_sync_ctrl_tx_sync_f1_cls:
        """
        Property to access tx_sync_f1 field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx F1 Sync Enable                                                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables/Disables transmission of F1 tone for receiver           |
        |              |      synchronization 0 : F1 tone transmission disabled 1 : F1 tone      |
        |              |      transmission enabled Both F1 and F2 can be enabled at the same     |
        |              |      time</p>                                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_sync_f1
    @property
    def tx_sync_f2(self) -> msk_top_regs_tx_sync_ctrl_tx_sync_f2_cls:
        """
        Property to access tx_sync_f2 field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx F2 Sync Enable                                                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables/Disables transmission of F2 tone for receiver           |
        |              |      synchronization 0 : F2 tone transmission disabled 1 : F2 tone      |
        |              |      transmission enabled Both F1 and F2 can be enabled at the same     |
        |              |      time</p>                                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_sync_f2

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'tx_sync_ena':'tx_sync_ena','tx_sync_force':'tx_sync_force','tx_sync_f1':'tx_sync_f1','tx_sync_f2':'tx_sync_f2',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_sync_ena"]) -> msk_top_regs_tx_sync_ctrl_tx_sync_ena_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_sync_force"]) -> msk_top_regs_tx_sync_ctrl_tx_sync_force_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_sync_f1"]) -> msk_top_regs_tx_sync_ctrl_tx_sync_f1_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_sync_f2"]) -> msk_top_regs_tx_sync_ctrl_tx_sync_f2_cls: ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union[msk_top_regs_tx_sync_ctrl_tx_sync_ena_cls, msk_top_regs_tx_sync_ctrl_tx_sync_force_cls, msk_top_regs_tx_sync_ctrl_tx_sync_f1_cls, msk_top_regs_tx_sync_ctrl_tx_sync_f2_cls, ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Transmitter Sync Control"
    @property
    def rdl_desc(self) -> str:
        return "Provides control bits for generation of transmitter synchronization patterns"
    
    
    

    
    
    
class msk_top_regs_data32_desc_70869502_name_3de9a0d3_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

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
    |              |      <p>Error value of the F2 Costas loop after each active bit         |
    |              |      period</p>                                                         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "F2 Error Value"
    @property
    def rdl_desc(self) -> str:
        return "Error value of the F2 Costas loop after each active bit period"
    
    
    

    
    
class msk_top_regs_observation_data_data_272a00b6_desc_70869502_name_3de9a0d3_cls(RegAsyncReadOnly):
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
    |              |      <p>Error value of the F2 Costas loop after each active bit         |
    |              |      period</p>                                                         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_data32_desc_70869502_name_3de9a0d3_cls = msk_top_regs_data32_desc_70869502_name_3de9a0d3_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_data32_desc_70869502_name_3de9a0d3_cls:
        """
        Property to access data field of the register

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
        |              |      <p>Error value of the F2 Costas loop after each active bit         |
        |              |      period</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_data32_desc_70869502_name_3de9a0d3_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F2 Error Value"
    @property
    def rdl_desc(self) -> str:
        return "Error value of the F2 Costas loop after each active bit period"
    
    
    

    
    
    
class msk_top_regs_data32_desc_417e1c96_name_3b640507_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

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
    |              |      <p>Error value of the F1 Costas loop after each active bit         |
    |              |      period</p>                                                         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "F1 Error Value"
    @property
    def rdl_desc(self) -> str:
        return "Error value of the F1 Costas loop after each active bit period"
    
    
    

    
    
class msk_top_regs_observation_data_data_25a21249_desc_417e1c96_name_3b640507_cls(RegAsyncReadOnly):
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
    |              |      <p>Error value of the F1 Costas loop after each active bit         |
    |              |      period</p>                                                         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_data32_desc_417e1c96_name_3b640507_cls = msk_top_regs_data32_desc_417e1c96_name_3b640507_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_data32_desc_417e1c96_name_3b640507_cls:
        """
        Property to access data field of the register

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
        |              |      <p>Error value of the F1 Costas loop after each active bit         |
        |              |      period</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_data32_desc_417e1c96_name_3b640507_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F1 Error Value"
    @property
    def rdl_desc(self) -> str:
        return "Error value of the F1 Costas loop after each active bit period"
    
    
    

    
    
    
class msk_top_regs_data32_desc_ebde6d39_name_2c154788_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

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
    |              |      <p>Frequency offet applied to the F2 NCO</p>                       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "F2 NCO Frequency Adjust"
    @property
    def rdl_desc(self) -> str:
        return "Frequency offet applied to the F2 NCO"
    
    
    

    
    
class msk_top_regs_observation_data_data_0515efaa_desc_ebde6d39_name_2c154788_cls(RegAsyncReadOnly):
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
    |              |      <p>Frequency offet applied to the F2 NCO</p>                       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_data32_desc_ebde6d39_name_2c154788_cls = msk_top_regs_data32_desc_ebde6d39_name_2c154788_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_data32_desc_ebde6d39_name_2c154788_cls:
        """
        Property to access data field of the register

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
        |              |      <p>Frequency offet applied to the F2 NCO</p>                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_data32_desc_ebde6d39_name_2c154788_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F2 NCO Frequency Adjust"
    @property
    def rdl_desc(self) -> str:
        return "Frequency offet applied to the F2 NCO"
    
    
    

    
    
    
class msk_top_regs_data32_desc_64ff3689_name_d8ad3b25_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

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
    |              |      <p>Frequency offet applied to the F1 NCO</p>                       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "F1 NCO Frequency Adjust"
    @property
    def rdl_desc(self) -> str:
        return "Frequency offet applied to the F1 NCO"
    
    
    

    
    
class msk_top_regs_observation_data_data_0c017ef4_desc_64ff3689_name_d8ad3b25_cls(RegAsyncReadOnly):
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
    |              |      <p>Frequency offet applied to the F1 NCO</p>                       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:msk_top_regs_data32_desc_64ff3689_name_d8ad3b25_cls = msk_top_regs_data32_desc_64ff3689_name_d8ad3b25_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data(self) -> msk_top_regs_data32_desc_64ff3689_name_d8ad3b25_cls:
        """
        Property to access data field of the register

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
        |              |      <p>Frequency offet applied to the F1 NCO</p>                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_data32_desc_64ff3689_name_d8ad3b25_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F1 NCO Frequency Adjust"
    @property
    def rdl_desc(self) -> str:
        return "Frequency offet applied to the F1 NCO"
    
    
    

    
    
    
class msk_top_regs_lpf_config_2_p_shift_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

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

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Proportional Gain Bit Shift"
    @property
    def rdl_desc(self) -> str:
        return "Value n of 0-32 sets the proportional divisor as 2^-n"
    
    
    

    
    
    
class msk_top_regs_lpf_config_2_p_gain_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

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

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Proportional Gain Value"
    @property
    def rdl_desc(self) -> str:
        return "Value m of 0-16,777,215 sets the proportional multiplier"
    
    
    

    
    
class msk_top_regs_lpf_config_2_cls(RegAsyncReadWrite):
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
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__p_gain:msk_top_regs_lpf_config_2_p_gain_cls = msk_top_regs_lpf_config_2_p_gain_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=24,
                lsb=0,
                msb=23,
                low=0,
                high=23),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.p_gain',
            inst_name='p_gain',
            field_type=int)
        self.__p_shift:msk_top_regs_lpf_config_2_p_shift_cls = msk_top_regs_lpf_config_2_p_shift_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=24,
                msb=31,
                low=24,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.p_shift',
            inst_name='p_shift',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.p_gain
        yield self.p_shift
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def p_gain(self) -> msk_top_regs_lpf_config_2_p_gain_cls:
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
    def p_shift(self) -> msk_top_regs_lpf_config_2_p_shift_cls:
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
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'p_gain':'p_gain','p_shift':'p_shift',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["p_gain"]) -> msk_top_regs_lpf_config_2_p_gain_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["p_shift"]) -> msk_top_regs_lpf_config_2_p_shift_cls: ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union[msk_top_regs_lpf_config_2_p_gain_cls, msk_top_regs_lpf_config_2_p_shift_cls, ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PI Controller Configuration Configuration Register 2"
    @property
    def rdl_desc(self) -> str:
        return "Configures PI Controller I-gain and divisor"
    
    
    

    
    
    
class msk_top_regs_rx_sample_discard_rx_nco_discard_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

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

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx NCO Sample Discard Value"
    @property
    def rdl_desc(self) -> str:
        return "Number of NCO samples to discard"
    
    
    

    
    
    
class msk_top_regs_rx_sample_discard_rx_sample_discard_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

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

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx Sample Discard Value"
    @property
    def rdl_desc(self) -> str:
        return "Number of Rx samples to discard"
    
    
    

    
    
class msk_top_regs_rx_sample_discard_cls(RegAsyncReadWrite):
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
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__rx_sample_discard:msk_top_regs_rx_sample_discard_rx_sample_discard_cls = msk_top_regs_rx_sample_discard_rx_sample_discard_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=0,
                msb=7,
                low=0,
                high=7),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.rx_sample_discard',
            inst_name='rx_sample_discard',
            field_type=int)
        self.__rx_nco_discard:msk_top_regs_rx_sample_discard_rx_nco_discard_cls = msk_top_regs_rx_sample_discard_rx_nco_discard_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=8,
                msb=15,
                low=8,
                high=15),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.rx_nco_discard',
            inst_name='rx_nco_discard',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.rx_sample_discard
        yield self.rx_nco_discard
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def rx_sample_discard(self) -> msk_top_regs_rx_sample_discard_rx_sample_discard_cls:
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
    def rx_nco_discard(self) -> msk_top_regs_rx_sample_discard_rx_nco_discard_cls:
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
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'rx_sample_discard':'rx_sample_discard','rx_nco_discard':'rx_nco_discard',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_sample_discard"]) -> msk_top_regs_rx_sample_discard_rx_sample_discard_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_nco_discard"]) -> msk_top_regs_rx_sample_discard_rx_nco_discard_cls: ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union[msk_top_regs_rx_sample_discard_rx_sample_discard_cls, msk_top_regs_rx_sample_discard_rx_nco_discard_cls, ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx Sample Discard"
    @property
    def rdl_desc(self) -> str:
        return "Configure samples discard operation for demodulator"
    
    
    

    
    
    
class msk_top_regs_msk_stat_3_xfer_count_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      S_AXIS Transfers                                                   |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Number completed S_AXIS transfers</p>                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "S_AXIS Transfers"
    @property
    def rdl_desc(self) -> str:
        return "Number completed S_AXIS transfers"
    
    
    

    
    
class msk_top_regs_msk_stat_3_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__xfer_count']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__xfer_count:msk_top_regs_msk_stat_3_xfer_count_cls = msk_top_regs_msk_stat_3_xfer_count_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.xfer_count',
            inst_name='xfer_count',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.xfer_count
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def xfer_count(self) -> msk_top_regs_msk_stat_3_xfer_count_cls:
        """
        Property to access xfer_count field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      S_AXIS Transfers                                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number completed S_AXIS transfers</p>                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__xfer_count

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'xfer_count':'xfer_count',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_msk_stat_3_xfer_count_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Status 3"
    @property
    def rdl_desc(self) -> str:
        return "Modem status data"
    
    
    

    
    
    
class msk_top_regs_stat_32_lpf_acc_status_data_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PI Controller Accumulator Value                                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>PI Controller Accumulator Value</p>                             |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PI Controller Accumulator Value"
    @property
    def rdl_desc(self) -> str:
        return "PI Controller Accumulator Value"
    
    
    

    
    
class msk_top_regs_stat_32_lpf_acc_desc_dea6bd99_name_758fd0ce_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__status_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__status_data:msk_top_regs_stat_32_lpf_acc_status_data_cls = msk_top_regs_stat_32_lpf_acc_status_data_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.status_data',
            inst_name='status_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.status_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def status_data(self) -> msk_top_regs_stat_32_lpf_acc_status_data_cls:
        """
        Property to access status_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PI Controller Accumulator Value                                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>PI Controller Accumulator Value</p>                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__status_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'status_data':'status_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_stat_32_lpf_acc_status_data_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F2 PI Controller Accumulator"
    @property
    def rdl_desc(self) -> str:
        return "Value of the F2 PI Controller Accumulator"
    
    
    

    
    
    
class msk_top_regs_stat_32_lpf_acc_status_data_0x0x1073cd31_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PI Controller Accumulator Value                                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>PI Controller Accumulator Value</p>                             |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PI Controller Accumulator Value"
    @property
    def rdl_desc(self) -> str:
        return "PI Controller Accumulator Value"
    
    
    

    
    
class msk_top_regs_stat_32_lpf_acc_desc_8cebc7dc_name_f20c6670_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__status_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__status_data:msk_top_regs_stat_32_lpf_acc_status_data_0x0x1073cd31_cls = msk_top_regs_stat_32_lpf_acc_status_data_0x0x1073cd31_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.status_data',
            inst_name='status_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.status_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def status_data(self) -> msk_top_regs_stat_32_lpf_acc_status_data_0x0x1073cd31_cls:
        """
        Property to access status_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PI Controller Accumulator Value                                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>PI Controller Accumulator Value</p>                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__status_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'status_data':'status_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_stat_32_lpf_acc_status_data_0x0x1073cd31_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F1 PI Controller Accumulator"
    @property
    def rdl_desc(self) -> str:
        return "Value of the F1 PI Controller Accumulator"
    
    
    

    
    
    
class msk_top_regs_stat_32_errs_status_data_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PRBS Bit Errors                                                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Number of errored-bits received by the PRBS monitor since last  |
    |              |      sync BER can be calculated as the ratio of received bits to        |
    |              |      errored-bits</p>                                                   |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Bit Errors"
    @property
    def rdl_desc(self) -> str:
        return "Number of errored-bits received by the PRBS monitor since last sync\nBER can be calculated as the ratio of received bits to errored-bits"
    
    
    

    
    
class msk_top_regs_stat_32_errs_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__status_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__status_data:msk_top_regs_stat_32_errs_status_data_cls = msk_top_regs_stat_32_errs_status_data_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.status_data',
            inst_name='status_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.status_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def status_data(self) -> msk_top_regs_stat_32_errs_status_data_cls:
        """
        Property to access status_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Bit Errors                                                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of errored-bits received by the PRBS monitor since last  |
        |              |      sync BER can be calculated as the ratio of received bits to        |
        |              |      errored-bits</p>                                                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__status_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'status_data':'status_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_stat_32_errs_status_data_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Status 1"
    @property
    def rdl_desc(self) -> str:
        return "PRBS Bit Errors"
    
    
    

    
    
    
class msk_top_regs_stat_32_bits_status_data_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PRBS Bits Received                                                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Number of bits received by the PRBS monitor since last BER can  |
    |              |      be calculated as the ratio of received bits to errored-bits</p>    |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Bits Received"
    @property
    def rdl_desc(self) -> str:
        return "Number of bits received by the PRBS monitor since last\nBER can be calculated as the ratio of received bits to errored-bits"
    
    
    

    
    
class msk_top_regs_stat_32_bits_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__status_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__status_data:msk_top_regs_stat_32_bits_status_data_cls = msk_top_regs_stat_32_bits_status_data_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.status_data',
            inst_name='status_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.status_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def status_data(self) -> msk_top_regs_stat_32_bits_status_data_cls:
        """
        Property to access status_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Bits Received                                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of bits received by the PRBS monitor since last BER can  |
        |              |      be calculated as the ratio of received bits to errored-bits</p>    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__status_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'status_data':'status_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_stat_32_bits_status_data_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Status 0"
    @property
    def rdl_desc(self) -> str:
        return "PRBS Bits Received"
    
    
    

    
    
    
class msk_top_regs_config_prbs_errmask_config_data_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PRBS Error Mask                                                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Bit positions set to '1' indicate bits that are inverted when a |
    |              |      bit error is inserted</p>                                          |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Error Mask"
    @property
    def rdl_desc(self) -> str:
        return "Bit positions set to \u00271\u0027 indicate bits that are inverted when a bit error is inserted"
    
    
    

    
    
class msk_top_regs_config_prbs_errmask_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__config_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_prbs_errmask_config_data_cls = msk_top_regs_config_prbs_errmask_config_data_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.config_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_prbs_errmask_config_data_cls:
        """
        Property to access config_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Error Mask                                                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Bit positions set to '1' indicate bits that are inverted when a |
        |              |      bit error is inserted</p>                                          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__config_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_config_prbs_errmask_config_data_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Control 3"
    @property
    def rdl_desc(self) -> str:
        return "PRBS Error Mask"
    
    
    

    
    
    
class msk_top_regs_config_prbs_poly_config_data_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PRBS Polynomial                                                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Bit positions set to '1' indicate polynomial feedback           |
    |              |      positions</p>                                                      |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Polynomial"
    @property
    def rdl_desc(self) -> str:
        return "Bit positions set to \u00271\u0027 indicate polynomial feedback positions"
    
    
    

    
    
class msk_top_regs_config_prbs_poly_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__config_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_prbs_poly_config_data_cls = msk_top_regs_config_prbs_poly_config_data_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.config_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_prbs_poly_config_data_cls:
        """
        Property to access config_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Polynomial                                                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Bit positions set to '1' indicate polynomial feedback           |
        |              |      positions</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__config_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_config_prbs_poly_config_data_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Control 2"
    @property
    def rdl_desc(self) -> str:
        return "PRBS Polynomial"
    
    
    

    
    
    
class msk_top_regs_config_prbs_seed_config_data_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PRBS Seed                                                          |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Sets the starting value of the PRBS generator</p>               |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Seed"
    @property
    def rdl_desc(self) -> str:
        return "Sets the starting value of the PRBS generator"
    
    
    

    
    
class msk_top_regs_config_prbs_seed_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__config_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_prbs_seed_config_data_cls = msk_top_regs_config_prbs_seed_config_data_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.config_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_prbs_seed_config_data_cls:
        """
        Property to access config_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Seed                                                          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sets the starting value of the PRBS generator</p>               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__config_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_config_prbs_seed_config_data_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Control 1"
    @property
    def rdl_desc(self) -> str:
        return "PRBS Initial State"
    
    
    

    
    
    
class msk_top_regs_prbs_ctrl_prbs_sync_threshold_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PRBS Auto Sync Threshold                                           |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 : Auto Sync Disabled N &gt; 0 : Auto sync after N errors</p>  |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Auto Sync Threshold"
    @property
    def rdl_desc(self) -> str:
        return "0 : Auto Sync Disabled\nN \u003e 0 : Auto sync after N errors"
    
    
    

    
    
    
class msk_top_regs_prbs_ctrl_prbs_reserved_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Reserved                                                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Reserved"
    
    
    

    
    
    
class msk_top_regs_prbs_ctrl_prbs_manual_sync_cls(FieldAsyncWriteOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PRBS Manual Sync                                                   |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; 1 : Synchronize PRBS monitor 1 -&gt; 0 : Synchronize    |
    |              |      PRBS monitor</p>                                                   |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Manual Sync"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e 1 : Synchronize PRBS monitor\n1 -\u003e 0 : Synchronize PRBS monitor"
    
    
    

    
    
    
class msk_top_regs_prbs_ctrl_prbs_clear_cls(FieldAsyncWriteOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PRBS Clear Counters                                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; 1 : Clear PRBS Counters 1 -&gt; 0 : Clear PRBS          |
    |              |      Counters</p>                                                       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Clear Counters"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e 1 : Clear PRBS Counters\n1 -\u003e 0 : Clear PRBS Counters"
    
    
    

    
    
    
class msk_top_regs_prbs_ctrl_prbs_error_insert_cls(FieldAsyncWriteOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PRBS Error Insert                                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; 1 :  Insert bit error in Tx data (both Normal and PRBS) |
    |              |      1 -&gt; 0 : Insert bit error in Tx data (both Normal and PRBS)</p> |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Error Insert"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e 1 :  Insert bit error in Tx data (both Normal and PRBS)\n1 -\u003e 0 : Insert bit error in Tx data (both Normal and PRBS)"
    
    
    

    
    
    
class msk_top_regs_prbs_ctrl_prbs_sel_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      PRBS Data Select                                                   |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; Select Normal Tx Data 1 -&gt; Select PRBS Tx Data</p>   |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Data Select"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Select Normal Tx Data\n1 -\u003e Select PRBS Tx Data"
    
    
    

    
    
class msk_top_regs_prbs_ctrl_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__prbs_sel', '__prbs_error_insert', '__prbs_clear', '__prbs_manual_sync', '__prbs_reserved', '__prbs_sync_threshold']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__prbs_sel:msk_top_regs_prbs_ctrl_prbs_sel_cls = msk_top_regs_prbs_ctrl_prbs_sel_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0,
                msb=0,
                low=0,
                high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_sel',
            inst_name='prbs_sel',
            field_type=int)
        self.__prbs_error_insert:msk_top_regs_prbs_ctrl_prbs_error_insert_cls = msk_top_regs_prbs_ctrl_prbs_error_insert_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1,
                msb=1,
                low=1,
                high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_error_insert',
            inst_name='prbs_error_insert',
            field_type=int)
        self.__prbs_clear:msk_top_regs_prbs_ctrl_prbs_clear_cls = msk_top_regs_prbs_ctrl_prbs_clear_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2,
                msb=2,
                low=2,
                high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_clear',
            inst_name='prbs_clear',
            field_type=int)
        self.__prbs_manual_sync:msk_top_regs_prbs_ctrl_prbs_manual_sync_cls = msk_top_regs_prbs_ctrl_prbs_manual_sync_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=3,
                msb=3,
                low=3,
                high=3),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_manual_sync',
            inst_name='prbs_manual_sync',
            field_type=int)
        self.__prbs_reserved:msk_top_regs_prbs_ctrl_prbs_reserved_cls = msk_top_regs_prbs_ctrl_prbs_reserved_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=12,
                lsb=4,
                msb=15,
                low=4,
                high=15),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_reserved',
            inst_name='prbs_reserved',
            field_type=int)
        self.__prbs_sync_threshold:msk_top_regs_prbs_ctrl_prbs_sync_threshold_cls = msk_top_regs_prbs_ctrl_prbs_sync_threshold_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=16,
                msb=31,
                low=16,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_sync_threshold',
            inst_name='prbs_sync_threshold',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.prbs_sel
        yield self.prbs_error_insert
        yield self.prbs_clear
        yield self.prbs_manual_sync
        yield self.prbs_reserved
        yield self.prbs_sync_threshold
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def prbs_sel(self) -> msk_top_regs_prbs_ctrl_prbs_sel_cls:
        """
        Property to access prbs_sel field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Data Select                                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; Select Normal Tx Data 1 -&gt; Select PRBS Tx Data</p>   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__prbs_sel
    @property
    def prbs_error_insert(self) -> msk_top_regs_prbs_ctrl_prbs_error_insert_cls:
        """
        Property to access prbs_error_insert field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Error Insert                                                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; 1 :  Insert bit error in Tx data (both Normal and PRBS) |
        |              |      1 -&gt; 0 : Insert bit error in Tx data (both Normal and PRBS)</p> |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__prbs_error_insert
    @property
    def prbs_clear(self) -> msk_top_regs_prbs_ctrl_prbs_clear_cls:
        """
        Property to access prbs_clear field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Clear Counters                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; 1 : Clear PRBS Counters 1 -&gt; 0 : Clear PRBS          |
        |              |      Counters</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__prbs_clear
    @property
    def prbs_manual_sync(self) -> msk_top_regs_prbs_ctrl_prbs_manual_sync_cls:
        """
        Property to access prbs_manual_sync field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Manual Sync                                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; 1 : Synchronize PRBS monitor 1 -&gt; 0 : Synchronize    |
        |              |      PRBS monitor</p>                                                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__prbs_manual_sync
    @property
    def prbs_reserved(self) -> msk_top_regs_prbs_ctrl_prbs_reserved_cls:
        """
        Property to access prbs_reserved field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Reserved                                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__prbs_reserved
    @property
    def prbs_sync_threshold(self) -> msk_top_regs_prbs_ctrl_prbs_sync_threshold_cls:
        """
        Property to access prbs_sync_threshold field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      PRBS Auto Sync Threshold                                           |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 : Auto Sync Disabled N &gt; 0 : Auto sync after N errors</p>  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__prbs_sync_threshold

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'prbs_sel':'prbs_sel','prbs_error_insert':'prbs_error_insert','prbs_clear':'prbs_clear','prbs_manual_sync':'prbs_manual_sync','prbs_reserved':'prbs_reserved','prbs_sync_threshold':'prbs_sync_threshold',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_sel"]) -> msk_top_regs_prbs_ctrl_prbs_sel_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_error_insert"]) -> msk_top_regs_prbs_ctrl_prbs_error_insert_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_clear"]) -> msk_top_regs_prbs_ctrl_prbs_clear_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_manual_sync"]) -> msk_top_regs_prbs_ctrl_prbs_manual_sync_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_reserved"]) -> msk_top_regs_prbs_ctrl_prbs_reserved_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_sync_threshold"]) -> msk_top_regs_prbs_ctrl_prbs_sync_threshold_cls: ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union[msk_top_regs_prbs_ctrl_prbs_sel_cls, msk_top_regs_prbs_ctrl_prbs_error_insert_cls, msk_top_regs_prbs_ctrl_prbs_clear_cls, msk_top_regs_prbs_ctrl_prbs_manual_sync_cls, msk_top_regs_prbs_ctrl_prbs_reserved_cls, msk_top_regs_prbs_ctrl_prbs_sync_threshold_cls, ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Control 0"
    @property
    def rdl_desc(self) -> str:
        return "Configures operation of the PRBS Generator and Monitor"
    
    
    

    
    
    
class msk_top_regs_data_width_data_width_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Modem input/output data width                                      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Set the data width of the modem input/output</p>                |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Modem input/output data width"
    @property
    def rdl_desc(self) -> str:
        return "Set the data width of the modem input/output"
    
    
    

    
    
class msk_top_regs_data_width_desc_6097df38_name_4609588b_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__data_width']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data_width:msk_top_regs_data_width_data_width_cls = msk_top_regs_data_width_data_width_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=0,
                msb=7,
                low=0,
                high=7),
            misc_props=FieldMiscProps(
                default=8,
                is_volatile=False),
            logger_handle=logger_handle+'.data_width',
            inst_name='data_width',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data_width
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data_width(self) -> msk_top_regs_data_width_data_width_cls:
        """
        Property to access data_width field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Modem input/output data width                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Set the data width of the modem input/output</p>                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data_width

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'data_width':'data_width',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_data_width_data_width_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Modem Rx Output Data Width"
    @property
    def rdl_desc(self) -> str:
        return "Set the parallel data width of the serial-to-parallel converter"
    
    
    

    
    
    
class msk_top_regs_data_width_data_width_0x0x107468c8_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Modem input/output data width                                      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Set the data width of the modem input/output</p>                |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Modem input/output data width"
    @property
    def rdl_desc(self) -> str:
        return "Set the data width of the modem input/output"
    
    
    

    
    
class msk_top_regs_data_width_desc_58c848dd_name_2fbd8eba_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__data_width']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data_width:msk_top_regs_data_width_data_width_0x0x107468c8_cls = msk_top_regs_data_width_data_width_0x0x107468c8_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=0,
                msb=7,
                low=0,
                high=7),
            misc_props=FieldMiscProps(
                default=8,
                is_volatile=False),
            logger_handle=logger_handle+'.data_width',
            inst_name='data_width',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.data_width
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def data_width(self) -> msk_top_regs_data_width_data_width_0x0x107468c8_cls:
        """
        Property to access data_width field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Modem input/output data width                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Set the data width of the modem input/output</p>                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data_width

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'data_width':'data_width',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_data_width_data_width_0x0x107468c8_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Modem Tx Input Data Width"
    @property
    def rdl_desc(self) -> str:
        return "Set the parallel data width of the parallel-to-serial converter"
    
    
    

    
    
    
class msk_top_regs_lpf_config_1_i_shift_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Integral Gain Bit Shift                                            |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Value n of 0-32 sets the integral divisor as 2^-n</p>           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Integral Gain Bit Shift"
    @property
    def rdl_desc(self) -> str:
        return "Value n of 0-32 sets the integral divisor as 2^-n"
    
    
    

    
    
    
class msk_top_regs_lpf_config_1_i_gain_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Integral Gain Value                                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Value m of 0-16,777,215 sets the integral multiplier</p>        |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Integral Gain Value"
    @property
    def rdl_desc(self) -> str:
        return "Value m of 0-16,777,215 sets the integral multiplier"
    
    
    

    
    
class msk_top_regs_lpf_config_1_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__i_gain', '__i_shift']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__i_gain:msk_top_regs_lpf_config_1_i_gain_cls = msk_top_regs_lpf_config_1_i_gain_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=24,
                lsb=0,
                msb=23,
                low=0,
                high=23),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.i_gain',
            inst_name='i_gain',
            field_type=int)
        self.__i_shift:msk_top_regs_lpf_config_1_i_shift_cls = msk_top_regs_lpf_config_1_i_shift_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=24,
                msb=31,
                low=24,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.i_shift',
            inst_name='i_shift',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.i_gain
        yield self.i_shift
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def i_gain(self) -> msk_top_regs_lpf_config_1_i_gain_cls:
        """
        Property to access i_gain field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Integral Gain Value                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Value m of 0-16,777,215 sets the integral multiplier</p>        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__i_gain
    @property
    def i_shift(self) -> msk_top_regs_lpf_config_1_i_shift_cls:
        """
        Property to access i_shift field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Integral Gain Bit Shift                                            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Value n of 0-32 sets the integral divisor as 2^-n</p>           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__i_shift

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'i_gain':'i_gain','i_shift':'i_shift',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["i_gain"]) -> msk_top_regs_lpf_config_1_i_gain_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["i_shift"]) -> msk_top_regs_lpf_config_1_i_shift_cls: ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union[msk_top_regs_lpf_config_1_i_gain_cls, msk_top_regs_lpf_config_1_i_shift_cls, ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PI Controller Configuration Configuration Register 1"
    @property
    def rdl_desc(self) -> str:
        return "Configures PI Controller I-gain and divisor"
    
    
    

    
    
    
class msk_top_regs_lpf_config_0_lpf_alpha_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Lowpass IIR filter alpha                                           |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Value controls the filter rolloff</p>                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Lowpass IIR filter alpha"
    @property
    def rdl_desc(self) -> str:
        return "Value controls the filter rolloff"
    
    
    

    
    
    
class msk_top_regs_lpf_config_0_prbs_reserved_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Reserved                                                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Reserved"
    
    
    

    
    
    
class msk_top_regs_lpf_config_0_lpf_zero_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Hold the PI Accumulator at zero                                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; Normal operation 1 -&gt; Zero and hold accumulator</p>  |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Hold the PI Accumulator at zero"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Normal operation\n1 -\u003e Zero and hold accumulator"
    
    
    

    
    
    
class msk_top_regs_lpf_config_0_lpf_freeze_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Freeze the accumulator's current value                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; Normal operation 1 -&gt; Freeze current value</p>       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Freeze the accumulator\u0027s current value"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Normal operation\n1 -\u003e Freeze current value"
    
    
    

    
    
class msk_top_regs_lpf_config_0_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__lpf_freeze', '__lpf_zero', '__prbs_reserved', '__lpf_alpha']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__lpf_freeze:msk_top_regs_lpf_config_0_lpf_freeze_cls = msk_top_regs_lpf_config_0_lpf_freeze_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0,
                msb=0,
                low=0,
                high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.lpf_freeze',
            inst_name='lpf_freeze',
            field_type=int)
        self.__lpf_zero:msk_top_regs_lpf_config_0_lpf_zero_cls = msk_top_regs_lpf_config_0_lpf_zero_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1,
                msb=1,
                low=1,
                high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.lpf_zero',
            inst_name='lpf_zero',
            field_type=int)
        self.__prbs_reserved:msk_top_regs_lpf_config_0_prbs_reserved_cls = msk_top_regs_lpf_config_0_prbs_reserved_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=6,
                lsb=2,
                msb=7,
                low=2,
                high=7),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_reserved',
            inst_name='prbs_reserved',
            field_type=int)
        self.__lpf_alpha:msk_top_regs_lpf_config_0_lpf_alpha_cls = msk_top_regs_lpf_config_0_lpf_alpha_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=24,
                lsb=8,
                msb=31,
                low=8,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.lpf_alpha',
            inst_name='lpf_alpha',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.lpf_freeze
        yield self.lpf_zero
        yield self.prbs_reserved
        yield self.lpf_alpha
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def lpf_freeze(self) -> msk_top_regs_lpf_config_0_lpf_freeze_cls:
        """
        Property to access lpf_freeze field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Freeze the accumulator's current value                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; Normal operation 1 -&gt; Freeze current value</p>       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lpf_freeze
    @property
    def lpf_zero(self) -> msk_top_regs_lpf_config_0_lpf_zero_cls:
        """
        Property to access lpf_zero field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Hold the PI Accumulator at zero                                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; Normal operation 1 -&gt; Zero and hold accumulator</p>  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lpf_zero
    @property
    def prbs_reserved(self) -> msk_top_regs_lpf_config_0_prbs_reserved_cls:
        """
        Property to access prbs_reserved field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Reserved                                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__prbs_reserved
    @property
    def lpf_alpha(self) -> msk_top_regs_lpf_config_0_lpf_alpha_cls:
        """
        Property to access lpf_alpha field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Lowpass IIR filter alpha                                           |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Value controls the filter rolloff</p>                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lpf_alpha

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'lpf_freeze':'lpf_freeze','lpf_zero':'lpf_zero','prbs_reserved':'prbs_reserved','lpf_alpha':'lpf_alpha',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lpf_freeze"]) -> msk_top_regs_lpf_config_0_lpf_freeze_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lpf_zero"]) -> msk_top_regs_lpf_config_0_lpf_zero_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_reserved"]) -> msk_top_regs_lpf_config_0_prbs_reserved_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lpf_alpha"]) -> msk_top_regs_lpf_config_0_lpf_alpha_cls: ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union[msk_top_regs_lpf_config_0_lpf_freeze_cls, msk_top_regs_lpf_config_0_lpf_zero_cls, msk_top_regs_lpf_config_0_prbs_reserved_cls, msk_top_regs_lpf_config_0_lpf_alpha_cls, ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PI Controller Configuration and Low-pass Filter Configuration"
    @property
    def rdl_desc(self) -> str:
        return "Configure PI controller and low-pass filter"
    
    
    

    
    
    
class msk_top_regs_config_nco_fw_config_data_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Frequency Control Word                                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs,      |
    |              |      where Fn is the desired NCO frequency, and Fs is the NCO sample    |
    |              |      rate</p>                                                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, \nwhere Fn is the desired NCO frequency, and Fs is the NCO sample rate"
    
    
    

    
    
class msk_top_regs_config_nco_fw_desc_43c0828f_name_bdc60ecf_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__config_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_nco_fw_config_data_cls = msk_top_regs_config_nco_fw_config_data_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.config_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_nco_fw_config_data_cls:
        """
        Property to access config_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Frequency Control Word                                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs,      |
        |              |      where Fn is the desired NCO frequency, and Fs is the NCO sample    |
        |              |      rate</p>                                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__config_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_config_nco_fw_config_data_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx F2 NCO Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Set Demodulator F2 Frequency"
    
    
    

    
    
    
class msk_top_regs_config_nco_fw_config_data_0x0x1074bb14_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Frequency Control Word                                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs,      |
    |              |      where Fn is the desired NCO frequency, and Fs is the NCO sample    |
    |              |      rate</p>                                                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, \nwhere Fn is the desired NCO frequency, and Fs is the NCO sample rate"
    
    
    

    
    
class msk_top_regs_config_nco_fw_desc_16fb48c8_name_8d01a20d_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__config_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_nco_fw_config_data_0x0x1074bb14_cls = msk_top_regs_config_nco_fw_config_data_0x0x1074bb14_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.config_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_nco_fw_config_data_0x0x1074bb14_cls:
        """
        Property to access config_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Frequency Control Word                                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs,      |
        |              |      where Fn is the desired NCO frequency, and Fs is the NCO sample    |
        |              |      rate</p>                                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__config_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_config_nco_fw_config_data_0x0x1074bb14_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx F1 NCO Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Set Demodulator F1 Frequency"
    
    
    

    
    
    
class msk_top_regs_config_nco_fw_config_data_0x0x107566c9_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Frequency Control Word                                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs,      |
    |              |      where Fn is the desired NCO frequency, and Fs is the NCO sample    |
    |              |      rate</p>                                                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, \nwhere Fn is the desired NCO frequency, and Fs is the NCO sample rate"
    
    
    

    
    
class msk_top_regs_config_nco_fw_desc_42134a4f_name_d97dbd51_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__config_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_nco_fw_config_data_0x0x107566c9_cls = msk_top_regs_config_nco_fw_config_data_0x0x107566c9_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.config_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_nco_fw_config_data_0x0x107566c9_cls:
        """
        Property to access config_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Frequency Control Word                                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs,      |
        |              |      where Fn is the desired NCO frequency, and Fs is the NCO sample    |
        |              |      rate</p>                                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__config_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_config_nco_fw_config_data_0x0x107566c9_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx F2 NCO Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Set Modulator F2 Frequency"
    
    
    

    
    
    
class msk_top_regs_config_nco_fw_config_data_0x0x10756468_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Frequency Control Word                                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs,      |
    |              |      where Fn is the desired NCO frequency, and Fs is the NCO sample    |
    |              |      rate</p>                                                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, \nwhere Fn is the desired NCO frequency, and Fs is the NCO sample rate"
    
    
    

    
    
class msk_top_regs_config_nco_fw_desc_94d7aaf5_name_84dd0c1c_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__config_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_nco_fw_config_data_0x0x10756468_cls = msk_top_regs_config_nco_fw_config_data_0x0x10756468_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.config_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_nco_fw_config_data_0x0x10756468_cls:
        """
        Property to access config_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Frequency Control Word                                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs,      |
        |              |      where Fn is the desired NCO frequency, and Fs is the NCO sample    |
        |              |      rate</p>                                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__config_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_config_nco_fw_config_data_0x0x10756468_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx F1 NCO Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Set Modulator F1 Frequency"
    
    
    

    
    
    
class msk_top_regs_config_nco_fw_config_data_0x0x1075c880_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Frequency Control Word                                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs,      |
    |              |      where Fn is the desired NCO frequency, and Fs is the NCO sample    |
    |              |      rate</p>                                                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, \nwhere Fn is the desired NCO frequency, and Fs is the NCO sample rate"
    
    
    

    
    
class msk_top_regs_config_nco_fw_desc_c4924cc6_name_0c494469_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__config_data']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_nco_fw_config_data_0x0x1075c880_cls = msk_top_regs_config_nco_fw_config_data_0x0x1075c880_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.config_data
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_nco_fw_config_data_0x0x1075c880_cls:
        """
        Property to access config_data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Frequency Control Word                                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs,      |
        |              |      where Fn is the desired NCO frequency, and Fs is the NCO sample    |
        |              |      rate</p>                                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__config_data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_config_nco_fw_config_data_0x0x1075c880_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Bitrate NCO Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Set Modem Data Rate"
    
    
    

    
    
    
class msk_top_regs_msk_stat_2_tx_ena_counter_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Tx Enable Count                                                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Number of clocks on which Tx Enable is active</p>               |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx Enable Count"
    @property
    def rdl_desc(self) -> str:
        return "Number of clocks on which Tx Enable is active"
    
    
    

    
    
class msk_top_regs_msk_stat_2_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__tx_ena_counter']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__tx_ena_counter:msk_top_regs_msk_stat_2_tx_ena_counter_cls = msk_top_regs_msk_stat_2_tx_ena_counter_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.tx_ena_counter',
            inst_name='tx_ena_counter',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.tx_ena_counter
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def tx_ena_counter(self) -> msk_top_regs_msk_stat_2_tx_ena_counter_cls:
        """
        Property to access tx_ena_counter field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx Enable Count                                                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of clocks on which Tx Enable is active</p>               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_ena_counter

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'tx_ena_counter':'tx_ena_counter',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_msk_stat_2_tx_ena_counter_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Status 2"
    @property
    def rdl_desc(self) -> str:
        return "Modem status data"
    
    
    

    
    
    
class msk_top_regs_msk_stat_1_tx_bit_counter_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Tx Bit Count                                                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Count of data requests made by modem</p>                        |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx Bit Count"
    @property
    def rdl_desc(self) -> str:
        return "Count of data requests made by modem"
    
    
    

    
    
class msk_top_regs_msk_stat_1_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__tx_bit_counter']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__tx_bit_counter:msk_top_regs_msk_stat_1_tx_bit_counter_cls = msk_top_regs_msk_stat_1_tx_bit_counter_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.tx_bit_counter',
            inst_name='tx_bit_counter',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.tx_bit_counter
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def tx_bit_counter(self) -> msk_top_regs_msk_stat_1_tx_bit_counter_cls:
        """
        Property to access tx_bit_counter field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx Bit Count                                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Count of data requests made by modem</p>                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_bit_counter

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'tx_bit_counter':'tx_bit_counter',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_msk_stat_1_tx_bit_counter_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Status 1"
    @property
    def rdl_desc(self) -> str:
        return "Modem status data"
    
    
    

    
    
    
class msk_top_regs_msk_stat_0_tx_axis_valid_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Tx S_AXIS_VALID                                                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>1 -&gt; S_AXIS_VALID Enabled 0 -&gt; S_AXIS_VALID Disabled</p>  |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx S_AXIS_VALID"
    @property
    def rdl_desc(self) -> str:
        return "1 -\u003e S_AXIS_VALID Enabled\n0 -\u003e S_AXIS_VALID Disabled"
    
    
    

    
    
    
class msk_top_regs_msk_stat_0_rx_enable_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      AD9363 ADC Interface Rx Enable Input Active                        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>1 -&gt; Data from ADC Enabled 0 -&gt; Data from ADC             |
    |              |      Disabled</p>                                                       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "AD9363 ADC Interface Rx Enable Input Active"
    @property
    def rdl_desc(self) -> str:
        return "1 -\u003e Data from ADC Enabled\n0 -\u003e Data from ADC Disabled"
    
    
    

    
    
    
class msk_top_regs_msk_stat_0_tx_enable_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      AD9363 DAC Interface Tx Enable Input Active                        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>1 -&gt; Data to DAC Enabled 0 -&gt; Data to DAC Disabled</p>    |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "AD9363 DAC Interface Tx Enable Input Active"
    @property
    def rdl_desc(self) -> str:
        return "1 -\u003e Data to DAC Enabled\n0 -\u003e Data to DAC Disabled"
    
    
    

    
    
    
class msk_top_regs_msk_stat_0_demod_sync_lock_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Demodulator Sync Status                                            |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Demodulator Sync Status - not currently implemented</p>         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Demodulator Sync Status"
    @property
    def rdl_desc(self) -> str:
        return "Demodulator Sync Status - not currently implemented"
    
    
    

    
    
class msk_top_regs_msk_stat_0_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__demod_sync_lock', '__tx_enable', '__rx_enable', '__tx_axis_valid']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__demod_sync_lock:msk_top_regs_msk_stat_0_demod_sync_lock_cls = msk_top_regs_msk_stat_0_demod_sync_lock_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0,
                msb=0,
                low=0,
                high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.demod_sync_lock',
            inst_name='demod_sync_lock',
            field_type=int)
        self.__tx_enable:msk_top_regs_msk_stat_0_tx_enable_cls = msk_top_regs_msk_stat_0_tx_enable_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1,
                msb=1,
                low=1,
                high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.tx_enable',
            inst_name='tx_enable',
            field_type=int)
        self.__rx_enable:msk_top_regs_msk_stat_0_rx_enable_cls = msk_top_regs_msk_stat_0_rx_enable_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2,
                msb=2,
                low=2,
                high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.rx_enable',
            inst_name='rx_enable',
            field_type=int)
        self.__tx_axis_valid:msk_top_regs_msk_stat_0_tx_axis_valid_cls = msk_top_regs_msk_stat_0_tx_axis_valid_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=3,
                msb=3,
                low=3,
                high=3),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.tx_axis_valid',
            inst_name='tx_axis_valid',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.demod_sync_lock
        yield self.tx_enable
        yield self.rx_enable
        yield self.tx_axis_valid
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def demod_sync_lock(self) -> msk_top_regs_msk_stat_0_demod_sync_lock_cls:
        """
        Property to access demod_sync_lock field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Demodulator Sync Status                                            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Demodulator Sync Status - not currently implemented</p>         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__demod_sync_lock
    @property
    def tx_enable(self) -> msk_top_regs_msk_stat_0_tx_enable_cls:
        """
        Property to access tx_enable field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      AD9363 DAC Interface Tx Enable Input Active                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>1 -&gt; Data to DAC Enabled 0 -&gt; Data to DAC Disabled</p>    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_enable
    @property
    def rx_enable(self) -> msk_top_regs_msk_stat_0_rx_enable_cls:
        """
        Property to access rx_enable field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      AD9363 ADC Interface Rx Enable Input Active                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>1 -&gt; Data from ADC Enabled 0 -&gt; Data from ADC             |
        |              |      Disabled</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rx_enable
    @property
    def tx_axis_valid(self) -> msk_top_regs_msk_stat_0_tx_axis_valid_cls:
        """
        Property to access tx_axis_valid field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx S_AXIS_VALID                                                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>1 -&gt; S_AXIS_VALID Enabled 0 -&gt; S_AXIS_VALID Disabled</p>  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_axis_valid

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'demod_sync_lock':'demod_sync_lock','tx_enable':'tx_enable','rx_enable':'rx_enable','tx_axis_valid':'tx_axis_valid',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["demod_sync_lock"]) -> msk_top_regs_msk_stat_0_demod_sync_lock_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_enable"]) -> msk_top_regs_msk_stat_0_tx_enable_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_enable"]) -> msk_top_regs_msk_stat_0_rx_enable_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_axis_valid"]) -> msk_top_regs_msk_stat_0_tx_axis_valid_cls: ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union[msk_top_regs_msk_stat_0_demod_sync_lock_cls, msk_top_regs_msk_stat_0_tx_enable_cls, msk_top_regs_msk_stat_0_rx_enable_cls, msk_top_regs_msk_stat_0_tx_axis_valid_cls, ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Status 0"
    @property
    def rdl_desc(self) -> str:
        return "Modem status bits"
    
    
    

    
    
    
class msk_top_regs_msk_ctrl_diff_encoder_loopback_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Differential Encoder -> Decoder Loopback Enable                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; Differential Encoder -&gt; Decoder loopback disabled 1  |
    |              |      -&gt; Differential Encoder -&gt; Decoder loopback enabled</p>      |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Differential Encoder -\u003e Decoder Loopback Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Differential Encoder -\u003e Decoder loopback disabled\n1 -\u003e Differential Encoder -\u003e Decoder loopback enabled"
    
    
    

    
    
    
class msk_top_regs_msk_ctrl_clear_counts_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Clear Status Counters                                              |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Clear Tx Bit Counter and Tx Enable Counter</p>                  |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Clear Status Counters"
    @property
    def rdl_desc(self) -> str:
        return "Clear Tx Bit Counter and Tx Enable Counter"
    
    
    

    
    
    
class msk_top_regs_msk_ctrl_rx_invert_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Rx Data Invert Enable                                              |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; Rx data normal 1 -&gt; Rx data inverted</p>             |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx Data Invert Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Rx data normal\n1 -\u003e Rx data inverted"
    
    
    

    
    
    
class msk_top_regs_msk_ctrl_loopback_ena_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Modem Digital Tx -> Rx Loopback Enable                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; Modem loopback disabled 1 -&gt; Modem loopback          |
    |              |      enabled</p>                                                        |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Modem Digital Tx -\u003e Rx Loopback Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Modem loopback disabled\n1 -\u003e Modem loopback enabled"
    
    
    

    
    
    
class msk_top_regs_msk_ctrl_ptt_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Push-to-Talk Enable                                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; PTT Disabled 1 -&gt; PTT Enabled</p>                    |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Push-to-Talk Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e PTT Disabled\n1 -\u003e PTT Enabled"
    
    
    

    
    
class msk_top_regs_msk_ctrl_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__ptt', '__loopback_ena', '__rx_invert', '__clear_counts', '__diff_encoder_loopback']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__ptt:msk_top_regs_msk_ctrl_ptt_cls = msk_top_regs_msk_ctrl_ptt_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0,
                msb=0,
                low=0,
                high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.ptt',
            inst_name='ptt',
            field_type=int)
        self.__loopback_ena:msk_top_regs_msk_ctrl_loopback_ena_cls = msk_top_regs_msk_ctrl_loopback_ena_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1,
                msb=1,
                low=1,
                high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.loopback_ena',
            inst_name='loopback_ena',
            field_type=int)
        self.__rx_invert:msk_top_regs_msk_ctrl_rx_invert_cls = msk_top_regs_msk_ctrl_rx_invert_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2,
                msb=2,
                low=2,
                high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.rx_invert',
            inst_name='rx_invert',
            field_type=int)
        self.__clear_counts:msk_top_regs_msk_ctrl_clear_counts_cls = msk_top_regs_msk_ctrl_clear_counts_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=3,
                msb=3,
                low=3,
                high=3),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.clear_counts',
            inst_name='clear_counts',
            field_type=int)
        self.__diff_encoder_loopback:msk_top_regs_msk_ctrl_diff_encoder_loopback_cls = msk_top_regs_msk_ctrl_diff_encoder_loopback_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=4,
                msb=4,
                low=4,
                high=4),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.diff_encoder_loopback',
            inst_name='diff_encoder_loopback',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.ptt
        yield self.loopback_ena
        yield self.rx_invert
        yield self.clear_counts
        yield self.diff_encoder_loopback
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def ptt(self) -> msk_top_regs_msk_ctrl_ptt_cls:
        """
        Property to access ptt field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Push-to-Talk Enable                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; PTT Disabled 1 -&gt; PTT Enabled</p>                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__ptt
    @property
    def loopback_ena(self) -> msk_top_regs_msk_ctrl_loopback_ena_cls:
        """
        Property to access loopback_ena field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Modem Digital Tx -> Rx Loopback Enable                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; Modem loopback disabled 1 -&gt; Modem loopback          |
        |              |      enabled</p>                                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__loopback_ena
    @property
    def rx_invert(self) -> msk_top_regs_msk_ctrl_rx_invert_cls:
        """
        Property to access rx_invert field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Rx Data Invert Enable                                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; Rx data normal 1 -&gt; Rx data inverted</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rx_invert
    @property
    def clear_counts(self) -> msk_top_regs_msk_ctrl_clear_counts_cls:
        """
        Property to access clear_counts field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Clear Status Counters                                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Clear Tx Bit Counter and Tx Enable Counter</p>                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__clear_counts
    @property
    def diff_encoder_loopback(self) -> msk_top_regs_msk_ctrl_diff_encoder_loopback_cls:
        """
        Property to access diff_encoder_loopback field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Differential Encoder -> Decoder Loopback Enable                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; Differential Encoder -&gt; Decoder loopback disabled 1  |
        |              |      -&gt; Differential Encoder -&gt; Decoder loopback enabled</p>      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__diff_encoder_loopback

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'ptt':'ptt','loopback_ena':'loopback_ena','rx_invert':'rx_invert','clear_counts':'clear_counts','diff_encoder_loopback':'diff_encoder_loopback',
            }

    
    
    
    
    
    
    # nodes:5
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["ptt"]) -> msk_top_regs_msk_ctrl_ptt_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["loopback_ena"]) -> msk_top_regs_msk_ctrl_loopback_ena_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_invert"]) -> msk_top_regs_msk_ctrl_rx_invert_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["clear_counts"]) -> msk_top_regs_msk_ctrl_clear_counts_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["diff_encoder_loopback"]) -> msk_top_regs_msk_ctrl_diff_encoder_loopback_cls: ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union[msk_top_regs_msk_ctrl_ptt_cls, msk_top_regs_msk_ctrl_loopback_ena_cls, msk_top_regs_msk_ctrl_rx_invert_cls, msk_top_regs_msk_ctrl_clear_counts_cls, msk_top_regs_msk_ctrl_diff_encoder_loopback_cls, ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Control"
    @property
    def rdl_desc(self) -> str:
        return "MSK Modem Configuration and Control"
    
    
    

    
    
    
class msk_top_regs_msk_init_rxinit_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Rx Init Enable                                                     |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; Normal Rx operation  1 -&gt; Initialize Rx</p>          |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx Init Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Normal Rx operation \n1 -\u003e Initialize Rx"
    
    
    

    
    
    
class msk_top_regs_msk_init_txinit_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Tx Init Enable                                                     |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; Normal Tx operation  1 -&gt; Initialize Tx</p>          |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx Init Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Normal Tx operation \n1 -\u003e Initialize Tx"
    
    
    

    
    
    
class msk_top_regs_msk_init_txrxinit_cls(FieldAsyncReadWrite):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Tx/Rx Init Enable                                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>0 -&gt; Normal modem operation  1 -&gt; Initialize Tx and       |
    |              |      Rx</p>                                                             |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx/Rx Init Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Normal modem operation \n1 -\u003e Initialize Tx and Rx"
    
    
    

    
    
class msk_top_regs_msk_init_cls(RegAsyncReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__txrxinit', '__txinit', '__rxinit']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__txrxinit:msk_top_regs_msk_init_txrxinit_cls = msk_top_regs_msk_init_txrxinit_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0,
                msb=0,
                low=0,
                high=0),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.txrxinit',
            inst_name='txrxinit',
            field_type=int)
        self.__txinit:msk_top_regs_msk_init_txinit_cls = msk_top_regs_msk_init_txinit_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1,
                msb=1,
                low=1,
                high=1),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.txinit',
            inst_name='txinit',
            field_type=int)
        self.__rxinit:msk_top_regs_msk_init_rxinit_cls = msk_top_regs_msk_init_rxinit_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2,
                msb=2,
                low=2,
                high=2),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.rxinit',
            inst_name='rxinit',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.txrxinit
        yield self.txinit
        yield self.rxinit
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def txrxinit(self) -> msk_top_regs_msk_init_txrxinit_cls:
        """
        Property to access txrxinit field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx/Rx Init Enable                                                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; Normal modem operation  1 -&gt; Initialize Tx and       |
        |              |      Rx</p>                                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__txrxinit
    @property
    def txinit(self) -> msk_top_regs_msk_init_txinit_cls:
        """
        Property to access txinit field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Tx Init Enable                                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; Normal Tx operation  1 -&gt; Initialize Tx</p>          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__txinit
    @property
    def rxinit(self) -> msk_top_regs_msk_init_rxinit_cls:
        """
        Property to access rxinit field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Rx Init Enable                                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>0 -&gt; Normal Rx operation  1 -&gt; Initialize Rx</p>          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rxinit

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'txrxinit':'txrxinit','txinit':'txinit','rxinit':'rxinit',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["txrxinit"]) -> msk_top_regs_msk_init_txrxinit_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["txinit"]) -> msk_top_regs_msk_init_txinit_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rxinit"]) -> msk_top_regs_msk_init_rxinit_cls: ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union[msk_top_regs_msk_init_txrxinit_cls, msk_top_regs_msk_init_txinit_cls, msk_top_regs_msk_init_rxinit_cls, ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Initialization Control"
    @property
    def rdl_desc(self) -> str:
        return "Synchronous initialization of MSK Modem functions, does not affect configuration registers."
    
    
    

    
    
    
class msk_top_regs_msk_hash_hi_hash_id_hi_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Hash ID Upper 32-bits                                              |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Upper 32-bits of Pluto MSK FPGA Hash ID</p>                     |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Hash ID Upper 32-bits"
    @property
    def rdl_desc(self) -> str:
        return "Upper 32-bits of Pluto MSK FPGA Hash ID"
    
    
    

    
    
class msk_top_regs_msk_hash_hi_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Pluto MSK FPGA Hash ID - Upper 32-bits                             |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__hash_id_hi']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__hash_id_hi:msk_top_regs_msk_hash_hi_hash_id_hi_cls = msk_top_regs_msk_hash_hi_hash_id_hi_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=1431677610,
                is_volatile=False),
            logger_handle=logger_handle+'.hash_id_hi',
            inst_name='hash_id_hi',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.hash_id_hi
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def hash_id_hi(self) -> msk_top_regs_msk_hash_hi_hash_id_hi_cls:
        """
        Property to access hash_id_hi field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Hash ID Upper 32-bits                                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Upper 32-bits of Pluto MSK FPGA Hash ID</p>                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__hash_id_hi

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'hash_id_hi':'hash_id_hi',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_msk_hash_hi_hash_id_hi_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Pluto MSK FPGA Hash ID - Upper 32-bits"
    
    
    

    
    
    
class msk_top_regs_msk_hash_lo_hash_id_lo_cls(FieldAsyncReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Hash ID Lower 32-bits                                              |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Lower 32-bits of Pluto MSK FPGA Hash ID</p>                     |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Hash ID Lower 32-bits"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32-bits of Pluto MSK FPGA Hash ID"
    
    
    

    
    
class msk_top_regs_msk_hash_lo_cls(RegAsyncReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Pluto MSK FPGA Hash ID - Lower 32-bits                             |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__hash_id_lo']

    def __init__(self,
                 address: int,
                 width: int,
                 accesswidth: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         width=width,
                         accesswidth=accesswidth,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__hash_id_lo:msk_top_regs_msk_hash_lo_hash_id_lo_cls = msk_top_regs_msk_hash_lo_hash_id_lo_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0,
                msb=31,
                low=0,
                high=31),
            misc_props=FieldMiscProps(
                default=2863289685,
                is_volatile=False),
            logger_handle=logger_handle+'.hash_id_lo',
            inst_name='hash_id_lo',
            field_type=int)

    @property
    def fields(self) -> Iterator[Union[FieldAsyncReadOnly, FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        """
        generator that produces has all the fields within the register
        """
        yield self.hash_id_lo
        
        # Empty generator in case there are no children of this type
        if False: yield


    

    # build the properties for the fields
    
    @property
    def hash_id_lo(self) -> msk_top_regs_msk_hash_lo_hash_id_lo_cls:
        """
        Property to access hash_id_lo field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Hash ID Lower 32-bits                                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Lower 32-bits of Pluto MSK FPGA Hash ID</p>                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__hash_id_lo

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'hash_id_lo':'hash_id_lo',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> msk_top_regs_msk_hash_lo_hash_id_lo_cls:
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Pluto MSK FPGA Hash ID - Lower 32-bits"
    
    
    

    
    
class msk_top_regs_cls(AsyncAddressMap):
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

    __slots__ : list[str] = ['__Hash_ID_Low', '__Hash_ID_High', '__MSK_Init', '__MSK_Control', '__MSK_Status', '__Tx_Bit_Count', '__Tx_Enable_Count', '__Fb_FreqWord', '__TX_F1_FreqWord', '__TX_F2_FreqWord', '__RX_F1_FreqWord', '__RX_F2_FreqWord', '__LPF_Config_0', '__LPF_Config_1', '__Tx_Data_Width', '__Rx_Data_Width', '__PRBS_Control', '__PRBS_Initial_State', '__PRBS_Polynomial', '__PRBS_Error_Mask', '__PRBS_Bit_Count', '__PRBS_Error_Count', '__LPF_Accum_F1', '__LPF_Accum_F2', '__axis_xfer_count', '__Rx_Sample_Discard', '__LPF_Config_2', '__f1_nco_adjust', '__f2_nco_adjust', '__f1_error', '__f2_error', '__Tx_Sync_Ctrl', '__Tx_Sync_Cnt', '__lowpass_ema_alpha1', '__lowpass_ema_alpha2', '__rx_power', '__tx_async_fifo_rd_wr_ptr', '__rx_async_fifo_rd_wr_ptr']

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

        
            
        self.__Hash_ID_Low:msk_top_regs_msk_hash_lo_cls = msk_top_regs_msk_hash_lo_cls(
                                                                     address=self.address+0,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.Hash_ID_Low',
                                                                     inst_name='Hash_ID_Low', parent=self)
        
            
        self.__Hash_ID_High:msk_top_regs_msk_hash_hi_cls = msk_top_regs_msk_hash_hi_cls(
                                                                     address=self.address+4,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.Hash_ID_High',
                                                                     inst_name='Hash_ID_High', parent=self)
        
            
        self.__MSK_Init:msk_top_regs_msk_init_cls = msk_top_regs_msk_init_cls(
                                                                     address=self.address+8,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.MSK_Init',
                                                                     inst_name='MSK_Init', parent=self)
        
            
        self.__MSK_Control:msk_top_regs_msk_ctrl_cls = msk_top_regs_msk_ctrl_cls(
                                                                     address=self.address+12,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.MSK_Control',
                                                                     inst_name='MSK_Control', parent=self)
        
            
        self.__MSK_Status:msk_top_regs_msk_stat_0_cls = msk_top_regs_msk_stat_0_cls(
                                                                     address=self.address+16,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.MSK_Status',
                                                                     inst_name='MSK_Status', parent=self)
        
            
        self.__Tx_Bit_Count:msk_top_regs_msk_stat_1_cls = msk_top_regs_msk_stat_1_cls(
                                                                     address=self.address+20,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.Tx_Bit_Count',
                                                                     inst_name='Tx_Bit_Count', parent=self)
        
            
        self.__Tx_Enable_Count:msk_top_regs_msk_stat_2_cls = msk_top_regs_msk_stat_2_cls(
                                                                     address=self.address+24,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.Tx_Enable_Count',
                                                                     inst_name='Tx_Enable_Count', parent=self)
        
            
        self.__Fb_FreqWord:msk_top_regs_config_nco_fw_desc_c4924cc6_name_0c494469_cls = msk_top_regs_config_nco_fw_desc_c4924cc6_name_0c494469_cls(
                                                                     address=self.address+28,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.Fb_FreqWord',
                                                                     inst_name='Fb_FreqWord', parent=self)
        
            
        self.__TX_F1_FreqWord:msk_top_regs_config_nco_fw_desc_94d7aaf5_name_84dd0c1c_cls = msk_top_regs_config_nco_fw_desc_94d7aaf5_name_84dd0c1c_cls(
                                                                     address=self.address+32,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.TX_F1_FreqWord',
                                                                     inst_name='TX_F1_FreqWord', parent=self)
        
            
        self.__TX_F2_FreqWord:msk_top_regs_config_nco_fw_desc_42134a4f_name_d97dbd51_cls = msk_top_regs_config_nco_fw_desc_42134a4f_name_d97dbd51_cls(
                                                                     address=self.address+36,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.TX_F2_FreqWord',
                                                                     inst_name='TX_F2_FreqWord', parent=self)
        
            
        self.__RX_F1_FreqWord:msk_top_regs_config_nco_fw_desc_16fb48c8_name_8d01a20d_cls = msk_top_regs_config_nco_fw_desc_16fb48c8_name_8d01a20d_cls(
                                                                     address=self.address+40,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.RX_F1_FreqWord',
                                                                     inst_name='RX_F1_FreqWord', parent=self)
        
            
        self.__RX_F2_FreqWord:msk_top_regs_config_nco_fw_desc_43c0828f_name_bdc60ecf_cls = msk_top_regs_config_nco_fw_desc_43c0828f_name_bdc60ecf_cls(
                                                                     address=self.address+44,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.RX_F2_FreqWord',
                                                                     inst_name='RX_F2_FreqWord', parent=self)
        
            
        self.__LPF_Config_0:msk_top_regs_lpf_config_0_cls = msk_top_regs_lpf_config_0_cls(
                                                                     address=self.address+48,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.LPF_Config_0',
                                                                     inst_name='LPF_Config_0', parent=self)
        
            
        self.__LPF_Config_1:msk_top_regs_lpf_config_1_cls = msk_top_regs_lpf_config_1_cls(
                                                                     address=self.address+52,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.LPF_Config_1',
                                                                     inst_name='LPF_Config_1', parent=self)
        
            
        self.__Tx_Data_Width:msk_top_regs_data_width_desc_58c848dd_name_2fbd8eba_cls = msk_top_regs_data_width_desc_58c848dd_name_2fbd8eba_cls(
                                                                     address=self.address+56,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.Tx_Data_Width',
                                                                     inst_name='Tx_Data_Width', parent=self)
        
            
        self.__Rx_Data_Width:msk_top_regs_data_width_desc_6097df38_name_4609588b_cls = msk_top_regs_data_width_desc_6097df38_name_4609588b_cls(
                                                                     address=self.address+60,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.Rx_Data_Width',
                                                                     inst_name='Rx_Data_Width', parent=self)
        
            
        self.__PRBS_Control:msk_top_regs_prbs_ctrl_cls = msk_top_regs_prbs_ctrl_cls(
                                                                     address=self.address+64,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.PRBS_Control',
                                                                     inst_name='PRBS_Control', parent=self)
        
            
        self.__PRBS_Initial_State:msk_top_regs_config_prbs_seed_cls = msk_top_regs_config_prbs_seed_cls(
                                                                     address=self.address+68,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.PRBS_Initial_State',
                                                                     inst_name='PRBS_Initial_State', parent=self)
        
            
        self.__PRBS_Polynomial:msk_top_regs_config_prbs_poly_cls = msk_top_regs_config_prbs_poly_cls(
                                                                     address=self.address+72,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.PRBS_Polynomial',
                                                                     inst_name='PRBS_Polynomial', parent=self)
        
            
        self.__PRBS_Error_Mask:msk_top_regs_config_prbs_errmask_cls = msk_top_regs_config_prbs_errmask_cls(
                                                                     address=self.address+76,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.PRBS_Error_Mask',
                                                                     inst_name='PRBS_Error_Mask', parent=self)
        
            
        self.__PRBS_Bit_Count:msk_top_regs_stat_32_bits_cls = msk_top_regs_stat_32_bits_cls(
                                                                     address=self.address+80,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.PRBS_Bit_Count',
                                                                     inst_name='PRBS_Bit_Count', parent=self)
        
            
        self.__PRBS_Error_Count:msk_top_regs_stat_32_errs_cls = msk_top_regs_stat_32_errs_cls(
                                                                     address=self.address+84,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.PRBS_Error_Count',
                                                                     inst_name='PRBS_Error_Count', parent=self)
        
            
        self.__LPF_Accum_F1:msk_top_regs_stat_32_lpf_acc_desc_8cebc7dc_name_f20c6670_cls = msk_top_regs_stat_32_lpf_acc_desc_8cebc7dc_name_f20c6670_cls(
                                                                     address=self.address+88,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.LPF_Accum_F1',
                                                                     inst_name='LPF_Accum_F1', parent=self)
        
            
        self.__LPF_Accum_F2:msk_top_regs_stat_32_lpf_acc_desc_dea6bd99_name_758fd0ce_cls = msk_top_regs_stat_32_lpf_acc_desc_dea6bd99_name_758fd0ce_cls(
                                                                     address=self.address+92,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.LPF_Accum_F2',
                                                                     inst_name='LPF_Accum_F2', parent=self)
        
            
        self.__axis_xfer_count:msk_top_regs_msk_stat_3_cls = msk_top_regs_msk_stat_3_cls(
                                                                     address=self.address+96,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.axis_xfer_count',
                                                                     inst_name='axis_xfer_count', parent=self)
        
            
        self.__Rx_Sample_Discard:msk_top_regs_rx_sample_discard_cls = msk_top_regs_rx_sample_discard_cls(
                                                                     address=self.address+100,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.Rx_Sample_Discard',
                                                                     inst_name='Rx_Sample_Discard', parent=self)
        
            
        self.__LPF_Config_2:msk_top_regs_lpf_config_2_cls = msk_top_regs_lpf_config_2_cls(
                                                                     address=self.address+104,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.LPF_Config_2',
                                                                     inst_name='LPF_Config_2', parent=self)
        
            
        self.__f1_nco_adjust:msk_top_regs_observation_data_data_0c017ef4_desc_64ff3689_name_d8ad3b25_cls = msk_top_regs_observation_data_data_0c017ef4_desc_64ff3689_name_d8ad3b25_cls(
                                                                     address=self.address+108,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.f1_nco_adjust',
                                                                     inst_name='f1_nco_adjust', parent=self)
        
            
        self.__f2_nco_adjust:msk_top_regs_observation_data_data_0515efaa_desc_ebde6d39_name_2c154788_cls = msk_top_regs_observation_data_data_0515efaa_desc_ebde6d39_name_2c154788_cls(
                                                                     address=self.address+112,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.f2_nco_adjust',
                                                                     inst_name='f2_nco_adjust', parent=self)
        
            
        self.__f1_error:msk_top_regs_observation_data_data_25a21249_desc_417e1c96_name_3b640507_cls = msk_top_regs_observation_data_data_25a21249_desc_417e1c96_name_3b640507_cls(
                                                                     address=self.address+116,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.f1_error',
                                                                     inst_name='f1_error', parent=self)
        
            
        self.__f2_error:msk_top_regs_observation_data_data_272a00b6_desc_70869502_name_3de9a0d3_cls = msk_top_regs_observation_data_data_272a00b6_desc_70869502_name_3de9a0d3_cls(
                                                                     address=self.address+120,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.f2_error',
                                                                     inst_name='f2_error', parent=self)
        
            
        self.__Tx_Sync_Ctrl:msk_top_regs_tx_sync_ctrl_cls = msk_top_regs_tx_sync_ctrl_cls(
                                                                     address=self.address+124,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.Tx_Sync_Ctrl',
                                                                     inst_name='Tx_Sync_Ctrl', parent=self)
        
            
        self.__Tx_Sync_Cnt:msk_top_regs_tx_sync_cnt_cls = msk_top_regs_tx_sync_cnt_cls(
                                                                     address=self.address+128,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.Tx_Sync_Cnt',
                                                                     inst_name='Tx_Sync_Cnt', parent=self)
        
            
        self.__lowpass_ema_alpha1:msk_top_regs_lowpass_ema_alpha_0x0x1075e9f4_cls = msk_top_regs_lowpass_ema_alpha_0x0x1075e9f4_cls(
                                                                     address=self.address+132,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.lowpass_ema_alpha1',
                                                                     inst_name='lowpass_ema_alpha1', parent=self)
        
            
        self.__lowpass_ema_alpha2:msk_top_regs_lowpass_ema_alpha_cls = msk_top_regs_lowpass_ema_alpha_cls(
                                                                     address=self.address+136,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.lowpass_ema_alpha2',
                                                                     inst_name='lowpass_ema_alpha2', parent=self)
        
            
        self.__rx_power:msk_top_regs_rx_power_cls = msk_top_regs_rx_power_cls(
                                                                     address=self.address+140,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.rx_power',
                                                                     inst_name='rx_power', parent=self)
        
            
        self.__tx_async_fifo_rd_wr_ptr:msk_top_regs_observation_data_data_cf6acbd7_name_aa4ec676_cls = msk_top_regs_observation_data_data_cf6acbd7_name_aa4ec676_cls(
                                                                     address=self.address+144,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.tx_async_fifo_rd_wr_ptr',
                                                                     inst_name='tx_async_fifo_rd_wr_ptr', parent=self)
        
            
        self.__rx_async_fifo_rd_wr_ptr:msk_top_regs_observation_data_data_cf6acbd7_name_8a90eed1_cls = msk_top_regs_observation_data_data_cf6acbd7_name_8a90eed1_cls(
                                                                     address=self.address+148,
                                                                     accesswidth=32,
                                                                     width=32,
                                                                     logger_handle=logger_handle+'.rx_async_fifo_rd_wr_ptr',
                                                                     inst_name='rx_async_fifo_rd_wr_ptr', parent=self)
        

    @property
    def size(self) -> int:
        return 152
    @property
    def Hash_ID_Low(self) -> msk_top_regs_msk_hash_lo_cls:
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
    def Hash_ID_High(self) -> msk_top_regs_msk_hash_hi_cls:
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
    def MSK_Init(self) -> msk_top_regs_msk_init_cls:
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
    def MSK_Control(self) -> msk_top_regs_msk_ctrl_cls:
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
    def MSK_Status(self) -> msk_top_regs_msk_stat_0_cls:
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
    def Tx_Bit_Count(self) -> msk_top_regs_msk_stat_1_cls:
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
    def Tx_Enable_Count(self) -> msk_top_regs_msk_stat_2_cls:
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
    def Fb_FreqWord(self) -> msk_top_regs_config_nco_fw_desc_c4924cc6_name_0c494469_cls:
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
    def TX_F1_FreqWord(self) -> msk_top_regs_config_nco_fw_desc_94d7aaf5_name_84dd0c1c_cls:
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
    def TX_F2_FreqWord(self) -> msk_top_regs_config_nco_fw_desc_42134a4f_name_d97dbd51_cls:
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
    def RX_F1_FreqWord(self) -> msk_top_regs_config_nco_fw_desc_16fb48c8_name_8d01a20d_cls:
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
    def RX_F2_FreqWord(self) -> msk_top_regs_config_nco_fw_desc_43c0828f_name_bdc60ecf_cls:
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
    def LPF_Config_0(self) -> msk_top_regs_lpf_config_0_cls:
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
    def LPF_Config_1(self) -> msk_top_regs_lpf_config_1_cls:
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
    def Tx_Data_Width(self) -> msk_top_regs_data_width_desc_58c848dd_name_2fbd8eba_cls:
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
    def Rx_Data_Width(self) -> msk_top_regs_data_width_desc_6097df38_name_4609588b_cls:
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
    def PRBS_Control(self) -> msk_top_regs_prbs_ctrl_cls:
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
    def PRBS_Initial_State(self) -> msk_top_regs_config_prbs_seed_cls:
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
    def PRBS_Polynomial(self) -> msk_top_regs_config_prbs_poly_cls:
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
    def PRBS_Error_Mask(self) -> msk_top_regs_config_prbs_errmask_cls:
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
    def PRBS_Bit_Count(self) -> msk_top_regs_stat_32_bits_cls:
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
    def PRBS_Error_Count(self) -> msk_top_regs_stat_32_errs_cls:
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
    def LPF_Accum_F1(self) -> msk_top_regs_stat_32_lpf_acc_desc_8cebc7dc_name_f20c6670_cls:
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
    def LPF_Accum_F2(self) -> msk_top_regs_stat_32_lpf_acc_desc_dea6bd99_name_758fd0ce_cls:
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
    def axis_xfer_count(self) -> msk_top_regs_msk_stat_3_cls:
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
    def Rx_Sample_Discard(self) -> msk_top_regs_rx_sample_discard_cls:
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
    def LPF_Config_2(self) -> msk_top_regs_lpf_config_2_cls:
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
    def f1_nco_adjust(self) -> msk_top_regs_observation_data_data_0c017ef4_desc_64ff3689_name_d8ad3b25_cls:
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
        |              |      <p>Frequency offet applied to the F1 NCO</p>                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f1_nco_adjust
        
    @property
    def f2_nco_adjust(self) -> msk_top_regs_observation_data_data_0515efaa_desc_ebde6d39_name_2c154788_cls:
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
        |              |      <p>Frequency offet applied to the F2 NCO</p>                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f2_nco_adjust
        
    @property
    def f1_error(self) -> msk_top_regs_observation_data_data_25a21249_desc_417e1c96_name_3b640507_cls:
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
        |              |      <p>Error value of the F1 Costas loop after each active bit         |
        |              |      period</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f1_error
        
    @property
    def f2_error(self) -> msk_top_regs_observation_data_data_272a00b6_desc_70869502_name_3de9a0d3_cls:
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
        |              |      <p>Error value of the F2 Costas loop after each active bit         |
        |              |      period</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__f2_error
        
    @property
    def Tx_Sync_Ctrl(self) -> msk_top_regs_tx_sync_ctrl_cls:
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
    def Tx_Sync_Cnt(self) -> msk_top_regs_tx_sync_cnt_cls:
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
    def lowpass_ema_alpha1(self) -> msk_top_regs_lowpass_ema_alpha_0x0x1075e9f4_cls:
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
    def lowpass_ema_alpha2(self) -> msk_top_regs_lowpass_ema_alpha_cls:
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
    def rx_power(self) -> msk_top_regs_rx_power_cls:
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
        |              |      <p>Receive power computed from I/Q ssamples</p>                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rx_power
        
    @property
    def tx_async_fifo_rd_wr_ptr(self) -> msk_top_regs_observation_data_data_cf6acbd7_name_aa4ec676_cls:
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
        """
        return self.__tx_async_fifo_rd_wr_ptr
        
    @property
    def rx_async_fifo_rd_wr_ptr(self) -> msk_top_regs_observation_data_data_cf6acbd7_name_8a90eed1_cls:
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
        """
        return self.__rx_async_fifo_rd_wr_ptr
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'Hash_ID_Low':'Hash_ID_Low','Hash_ID_High':'Hash_ID_High','MSK_Init':'MSK_Init','MSK_Control':'MSK_Control','MSK_Status':'MSK_Status','Tx_Bit_Count':'Tx_Bit_Count','Tx_Enable_Count':'Tx_Enable_Count','Fb_FreqWord':'Fb_FreqWord','TX_F1_FreqWord':'TX_F1_FreqWord','TX_F2_FreqWord':'TX_F2_FreqWord','RX_F1_FreqWord':'RX_F1_FreqWord','RX_F2_FreqWord':'RX_F2_FreqWord','LPF_Config_0':'LPF_Config_0','LPF_Config_1':'LPF_Config_1','Tx_Data_Width':'Tx_Data_Width','Rx_Data_Width':'Rx_Data_Width','PRBS_Control':'PRBS_Control','PRBS_Initial_State':'PRBS_Initial_State','PRBS_Polynomial':'PRBS_Polynomial','PRBS_Error_Mask':'PRBS_Error_Mask','PRBS_Bit_Count':'PRBS_Bit_Count','PRBS_Error_Count':'PRBS_Error_Count','LPF_Accum_F1':'LPF_Accum_F1','LPF_Accum_F2':'LPF_Accum_F2','axis_xfer_count':'axis_xfer_count','Rx_Sample_Discard':'Rx_Sample_Discard','LPF_Config_2':'LPF_Config_2','f1_nco_adjust':'f1_nco_adjust','f2_nco_adjust':'f2_nco_adjust','f1_error':'f1_error','f2_error':'f2_error','Tx_Sync_Ctrl':'Tx_Sync_Ctrl','Tx_Sync_Cnt':'Tx_Sync_Cnt','lowpass_ema_alpha1':'lowpass_ema_alpha1','lowpass_ema_alpha2':'lowpass_ema_alpha2','rx_power':'rx_power','tx_async_fifo_rd_wr_ptr':'tx_async_fifo_rd_wr_ptr','rx_async_fifo_rd_wr_ptr':'rx_async_fifo_rd_wr_ptr',
            }

    
    
    
    
    
    
    # nodes:38
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Hash_ID_Low"]) -> msk_top_regs_msk_hash_lo_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Hash_ID_High"]) -> msk_top_regs_msk_hash_hi_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["MSK_Init"]) -> msk_top_regs_msk_init_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["MSK_Control"]) -> msk_top_regs_msk_ctrl_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["MSK_Status"]) -> msk_top_regs_msk_stat_0_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Tx_Bit_Count"]) -> msk_top_regs_msk_stat_1_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Tx_Enable_Count"]) -> msk_top_regs_msk_stat_2_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Fb_FreqWord"]) -> msk_top_regs_config_nco_fw_desc_c4924cc6_name_0c494469_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["TX_F1_FreqWord"]) -> msk_top_regs_config_nco_fw_desc_94d7aaf5_name_84dd0c1c_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["TX_F2_FreqWord"]) -> msk_top_regs_config_nco_fw_desc_42134a4f_name_d97dbd51_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["RX_F1_FreqWord"]) -> msk_top_regs_config_nco_fw_desc_16fb48c8_name_8d01a20d_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["RX_F2_FreqWord"]) -> msk_top_regs_config_nco_fw_desc_43c0828f_name_bdc60ecf_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["LPF_Config_0"]) -> msk_top_regs_lpf_config_0_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["LPF_Config_1"]) -> msk_top_regs_lpf_config_1_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Tx_Data_Width"]) -> msk_top_regs_data_width_desc_58c848dd_name_2fbd8eba_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Rx_Data_Width"]) -> msk_top_regs_data_width_desc_6097df38_name_4609588b_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Control"]) -> msk_top_regs_prbs_ctrl_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Initial_State"]) -> msk_top_regs_config_prbs_seed_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Polynomial"]) -> msk_top_regs_config_prbs_poly_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Error_Mask"]) -> msk_top_regs_config_prbs_errmask_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Bit_Count"]) -> msk_top_regs_stat_32_bits_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["PRBS_Error_Count"]) -> msk_top_regs_stat_32_errs_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["LPF_Accum_F1"]) -> msk_top_regs_stat_32_lpf_acc_desc_8cebc7dc_name_f20c6670_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["LPF_Accum_F2"]) -> msk_top_regs_stat_32_lpf_acc_desc_dea6bd99_name_758fd0ce_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["axis_xfer_count"]) -> msk_top_regs_msk_stat_3_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Rx_Sample_Discard"]) -> msk_top_regs_rx_sample_discard_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["LPF_Config_2"]) -> msk_top_regs_lpf_config_2_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f1_nco_adjust"]) -> msk_top_regs_observation_data_data_0c017ef4_desc_64ff3689_name_d8ad3b25_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f2_nco_adjust"]) -> msk_top_regs_observation_data_data_0515efaa_desc_ebde6d39_name_2c154788_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f1_error"]) -> msk_top_regs_observation_data_data_25a21249_desc_417e1c96_name_3b640507_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f2_error"]) -> msk_top_regs_observation_data_data_272a00b6_desc_70869502_name_3de9a0d3_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Tx_Sync_Ctrl"]) -> msk_top_regs_tx_sync_ctrl_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["Tx_Sync_Cnt"]) -> msk_top_regs_tx_sync_cnt_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lowpass_ema_alpha1"]) -> msk_top_regs_lowpass_ema_alpha_0x0x1075e9f4_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lowpass_ema_alpha2"]) -> msk_top_regs_lowpass_ema_alpha_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_power"]) -> msk_top_regs_rx_power_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_async_fifo_rd_wr_ptr"]) -> msk_top_regs_observation_data_data_cf6acbd7_name_aa4ec676_cls: ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_async_fifo_rd_wr_ptr"]) -> msk_top_regs_observation_data_data_cf6acbd7_name_8a90eed1_cls: ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union[msk_top_regs_msk_hash_lo_cls, msk_top_regs_msk_hash_hi_cls, msk_top_regs_msk_init_cls, msk_top_regs_msk_ctrl_cls, msk_top_regs_msk_stat_0_cls, msk_top_regs_msk_stat_1_cls, msk_top_regs_msk_stat_2_cls, msk_top_regs_config_nco_fw_desc_c4924cc6_name_0c494469_cls, msk_top_regs_config_nco_fw_desc_94d7aaf5_name_84dd0c1c_cls, msk_top_regs_config_nco_fw_desc_42134a4f_name_d97dbd51_cls, msk_top_regs_config_nco_fw_desc_16fb48c8_name_8d01a20d_cls, msk_top_regs_config_nco_fw_desc_43c0828f_name_bdc60ecf_cls, msk_top_regs_lpf_config_0_cls, msk_top_regs_lpf_config_1_cls, msk_top_regs_data_width_desc_58c848dd_name_2fbd8eba_cls, msk_top_regs_data_width_desc_6097df38_name_4609588b_cls, msk_top_regs_prbs_ctrl_cls, msk_top_regs_config_prbs_seed_cls, msk_top_regs_config_prbs_poly_cls, msk_top_regs_config_prbs_errmask_cls, msk_top_regs_stat_32_bits_cls, msk_top_regs_stat_32_errs_cls, msk_top_regs_stat_32_lpf_acc_desc_8cebc7dc_name_f20c6670_cls, msk_top_regs_stat_32_lpf_acc_desc_dea6bd99_name_758fd0ce_cls, msk_top_regs_msk_stat_3_cls, msk_top_regs_rx_sample_discard_cls, msk_top_regs_lpf_config_2_cls, msk_top_regs_observation_data_data_0c017ef4_desc_64ff3689_name_d8ad3b25_cls, msk_top_regs_observation_data_data_0515efaa_desc_ebde6d39_name_2c154788_cls, msk_top_regs_observation_data_data_25a21249_desc_417e1c96_name_3b640507_cls, msk_top_regs_observation_data_data_272a00b6_desc_70869502_name_3de9a0d3_cls, msk_top_regs_tx_sync_ctrl_cls, msk_top_regs_tx_sync_cnt_cls, msk_top_regs_lowpass_ema_alpha_0x0x1075e9f4_cls, msk_top_regs_lowpass_ema_alpha_cls, msk_top_regs_rx_power_cls, msk_top_regs_observation_data_data_cf6acbd7_name_aa4ec676_cls, msk_top_regs_observation_data_data_cf6acbd7_name_8a90eed1_cls, ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Pluto MSK Registers"
    @property
    def rdl_desc(self) -> str:
        return "MSK Modem Configuration and Status Registers"
    
    

    
    def get_registers(self, unroll:bool=False) -> Iterator[Union[AsyncReg, AsyncRegArray]]:
        """
        generator that produces all the registers of this node
        """
        
                    
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
        

        # Empty generator in case there are no children of this type
        if False: yield
    
    
    def get_sections(self, unroll:bool=False) -> Iterator[Union[AsyncAddressMap, AsyncRegFile, AsyncAddressMapArray, AsyncRegFileArray]]:
        """
        generator that produces all the AsyncAddressMap, AsyncRegFile, AsyncAddressMapArray, AsyncRegFileArray children of this node
        """
        

        # Empty generator in case there are no children of this type
        if False: yield
    
    def get_memories(self, unroll:bool=False) -> Iterator[Union[AsyncMemory, AsyncMemoryArray]]:
        """
        generator that produces all the AsyncMemory, AsyncMemoryArray children of this node
        """
        

        # Empty generator in case there are no children of this type
        if False: yield
    
    



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