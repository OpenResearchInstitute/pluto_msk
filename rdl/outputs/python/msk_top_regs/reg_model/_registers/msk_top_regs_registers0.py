

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






from .fields import msk_top_regs_msk_hash_lo_hash_id_lo_neg_0x105bacf44f0ca709_cls
from .fields import msk_top_regs_msk_hash_hi_hash_id_hi_0x4570a64f2713e448_cls
from .fields import msk_top_regs_msk_init_txrxinit_neg_0x2f4bea5a67f66424_cls
from .fields import msk_top_regs_msk_init_txinit_neg_0x15f317dcac1ceee_cls
from .fields import msk_top_regs_msk_init_rxinit_neg_0x16300a51d9e0ebc6_cls
from .fields import msk_top_regs_msk_ctrl_ptt_neg_0x3ef0035cee99a68d_cls
from .fields import msk_top_regs_msk_ctrl_loopback_ena_0x99b143f50703af0_cls
from .fields import msk_top_regs_msk_ctrl_rx_invert_neg_0x7a9e4517851e9732_cls
from .fields import msk_top_regs_msk_ctrl_clear_counts_neg_0x55e2450e4ad31070_cls
from .fields import msk_top_regs_msk_ctrl_diff_encoder_loopback_neg_0x6ea17fae4f290ad0_cls
from .fields import msk_top_regs_msk_stat_0_demod_sync_lock_neg_0x2950cdf9067a0d19_cls
from .fields import msk_top_regs_msk_stat_0_tx_enable_0x7a56cd6d195d2e65_cls
from .fields import msk_top_regs_msk_stat_0_rx_enable_neg_0x6dfa23c31cd45fbc_cls
from .fields import msk_top_regs_msk_stat_0_tx_axis_valid_neg_0x4af685b21106987d_cls
from .fields import msk_top_regs_msk_stat_1_data_neg_0x100875f913ba41b0_cls
from .fields import msk_top_regs_msk_stat_2_data_neg_0x1193896f2e20ab4d_cls
from .fields import msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls
from .fields import msk_top_regs_lpf_config_0_lpf_freeze_neg_0x52a4a2fbda7f6358_cls
from .fields import msk_top_regs_lpf_config_0_lpf_zero_neg_0x3e4e297867d24c30_cls
from .fields import msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls
from .fields import msk_top_regs_lpf_config_0_lpf_alpha_0x7718e3b25a61a530_cls
from .fields import msk_top_regs_lpf_config_1_i_gain_0x4e4f67093b462024_cls
from .fields import msk_top_regs_lpf_config_1_i_shift_neg_0x6c22d49419aff3cb_cls
from .fields import msk_top_regs_data_width_data_width_neg_0x302f654e739e31e1_cls
from .fields import msk_top_regs_prbs_ctrl_prbs_sel_neg_0x2b4072fcf0ec6645_cls
from .fields import msk_top_regs_prbs_ctrl_prbs_error_insert_neg_0x34b21fe1f6161153_cls
from .fields import msk_top_regs_prbs_ctrl_prbs_clear_neg_0x2672d40dbb0c1154_cls
from .fields import msk_top_regs_prbs_ctrl_prbs_manual_sync_neg_0x2862b6e9670d772f_cls
from .fields import msk_top_regs_prbs_ctrl_prbs_sync_threshold_0x6fb8cbe5e8cd57c9_cls
from .fields import msk_top_regs_config_prbs_seed_config_data_0x73a9fcd47073237e_cls
from .fields import msk_top_regs_config_prbs_poly_config_data_neg_0x5fc157fe7df0f535_cls
from .fields import msk_top_regs_config_prbs_errmask_config_data_neg_0x172894e16caf1f6a_cls
from .fields import msk_top_regs_stat_32_bits_data_neg_0x544fe2aae1d2774_cls
from .fields import msk_top_regs_stat_32_errs_data_0x7af54aff70ab45c5_cls
from .fields import msk_top_regs_stat_32_lpf_acc_data_neg_0x5ba1df96a18c1ea7_cls
from .fields import msk_top_regs_msk_stat_3_data_0x158d4610c7260e45_cls

# register definitions
    
    
class msk_top_regs_msk_hash_lo_0x743ecd7f54200b33_cls(RegAsyncReadOnly):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__hash_id_lo:msk_top_regs_msk_hash_lo_hash_id_lo_neg_0x105bacf44f0ca709_cls = msk_top_regs_msk_hash_lo_hash_id_lo_neg_0x105bacf44f0ca709_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=2863289685,
                is_volatile=False),
            logger_handle=logger_handle+'.hash_id_lo',
            inst_name='hash_id_lo',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def hash_id_lo(self) -> msk_top_regs_msk_hash_lo_hash_id_lo_neg_0x105bacf44f0ca709_cls:
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
        return {'hash_id_lo':'hash_id_lo',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_msk_hash_lo_hash_id_lo_neg_0x105bacf44f0ca709_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Pluto MSK FPGA Hash ID - Lower 32-bits"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.hash_id_lo
        
        
    

    
    
class msk_top_regs_msk_hash_hi_0x2fdfea8796573801_cls(RegAsyncReadOnly):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__hash_id_hi:msk_top_regs_msk_hash_hi_hash_id_hi_0x4570a64f2713e448_cls = msk_top_regs_msk_hash_hi_hash_id_hi_0x4570a64f2713e448_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=1431677610,
                is_volatile=False),
            logger_handle=logger_handle+'.hash_id_hi',
            inst_name='hash_id_hi',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def hash_id_hi(self) -> msk_top_regs_msk_hash_hi_hash_id_hi_0x4570a64f2713e448_cls:
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
        return {'hash_id_hi':'hash_id_hi',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_msk_hash_hi_hash_id_hi_0x4570a64f2713e448_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Pluto MSK FPGA Hash ID - Upper 32-bits"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.hash_id_hi
        
        
    

    
    
class msk_top_regs_msk_init_0x5784a15eda1d51f6_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__txrxinit:msk_top_regs_msk_init_txrxinit_neg_0x2f4bea5a67f66424_cls = msk_top_regs_msk_init_txrxinit_neg_0x2f4bea5a67f66424_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.txrxinit',
            inst_name='txrxinit',
            field_type=int)
        self.__txinit:msk_top_regs_msk_init_txinit_neg_0x15f317dcac1ceee_cls = msk_top_regs_msk_init_txinit_neg_0x15f317dcac1ceee_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1, msb=1,
                low=1, high=1),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.txinit',
            inst_name='txinit',
            field_type=int)
        self.__rxinit:msk_top_regs_msk_init_rxinit_neg_0x16300a51d9e0ebc6_cls = msk_top_regs_msk_init_rxinit_neg_0x16300a51d9e0ebc6_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2, msb=2,
                low=2, high=2),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.rxinit',
            inst_name='rxinit',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def txrxinit(self) -> msk_top_regs_msk_init_txrxinit_neg_0x2f4bea5a67f66424_cls:
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
        |              |      <p>0 -&gt; Normal modem operation </p> <p>1 -&gt; Initialize Tx    |
        |              |      and Rx</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__txrxinit
    @property
    def txinit(self) -> msk_top_regs_msk_init_txinit_neg_0x15f317dcac1ceee_cls:
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
        |              |      <p>0 -&gt; Normal Tx operation</p> <p>1 -&gt; Initialize Tx</p>    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__txinit
    @property
    def rxinit(self) -> msk_top_regs_msk_init_rxinit_neg_0x16300a51d9e0ebc6_cls:
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
        |              |      <p>0 -&gt; Normal Rx operation   </p> <p>1 -&gt; Initialize Rx</p> |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rxinit

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'txrxinit':'txrxinit','txinit':'txinit','rxinit':'rxinit',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["txrxinit"]) -> 'msk_top_regs_msk_init_txrxinit_neg_0x2f4bea5a67f66424_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["txinit"]) -> 'msk_top_regs_msk_init_txinit_neg_0x15f317dcac1ceee_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rxinit"]) -> 'msk_top_regs_msk_init_rxinit_neg_0x16300a51d9e0ebc6_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_msk_init_txrxinit_neg_0x2f4bea5a67f66424_cls', 'msk_top_regs_msk_init_txinit_neg_0x15f317dcac1ceee_cls', 'msk_top_regs_msk_init_rxinit_neg_0x16300a51d9e0ebc6_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Initialization Control"
    @property
    def rdl_desc(self) -> str:
        return "Synchronous initialization of MSK Modem functions, does not affect configuration registers."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.txrxinit
        yield self.txinit
        yield self.rxinit
        
        
    

    
    
class msk_top_regs_msk_ctrl_0x6338546fd42c56c3_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__ptt:msk_top_regs_msk_ctrl_ptt_neg_0x3ef0035cee99a68d_cls = msk_top_regs_msk_ctrl_ptt_neg_0x3ef0035cee99a68d_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.ptt',
            inst_name='ptt',
            field_type=int)
        self.__loopback_ena:msk_top_regs_msk_ctrl_loopback_ena_0x99b143f50703af0_cls = msk_top_regs_msk_ctrl_loopback_ena_0x99b143f50703af0_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1, msb=1,
                low=1, high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.loopback_ena',
            inst_name='loopback_ena',
            field_type=int)
        self.__rx_invert:msk_top_regs_msk_ctrl_rx_invert_neg_0x7a9e4517851e9732_cls = msk_top_regs_msk_ctrl_rx_invert_neg_0x7a9e4517851e9732_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2, msb=2,
                low=2, high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.rx_invert',
            inst_name='rx_invert',
            field_type=int)
        self.__clear_counts:msk_top_regs_msk_ctrl_clear_counts_neg_0x55e2450e4ad31070_cls = msk_top_regs_msk_ctrl_clear_counts_neg_0x55e2450e4ad31070_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=3, msb=3,
                low=3, high=3),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.clear_counts',
            inst_name='clear_counts',
            field_type=int)
        self.__diff_encoder_loopback:msk_top_regs_msk_ctrl_diff_encoder_loopback_neg_0x6ea17fae4f290ad0_cls = msk_top_regs_msk_ctrl_diff_encoder_loopback_neg_0x6ea17fae4f290ad0_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=4, msb=4,
                low=4, high=4),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.diff_encoder_loopback',
            inst_name='diff_encoder_loopback',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def ptt(self) -> msk_top_regs_msk_ctrl_ptt_neg_0x3ef0035cee99a68d_cls:
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
    def loopback_ena(self) -> msk_top_regs_msk_ctrl_loopback_ena_0x99b143f50703af0_cls:
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
        |              |      <p>0 -&gt; Modem loopback disabled</p> <p>1 -&gt; Modem loopback   |
        |              |      enabled</p>                                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__loopback_ena
    @property
    def rx_invert(self) -> msk_top_regs_msk_ctrl_rx_invert_neg_0x7a9e4517851e9732_cls:
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
    def clear_counts(self) -> msk_top_regs_msk_ctrl_clear_counts_neg_0x55e2450e4ad31070_cls:
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
    def diff_encoder_loopback(self) -> msk_top_regs_msk_ctrl_diff_encoder_loopback_neg_0x6ea17fae4f290ad0_cls:
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
        |              |      <p>0 -&gt; Differential Encoder -&gt; Decoder loopback             |
        |              |      disabled</p> <p>1 -&gt; Differential Encoder -&gt; Decoder         |
        |              |      loopback enabled</p>                                               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__diff_encoder_loopback

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'ptt':'ptt','loopback_ena':'loopback_ena','rx_invert':'rx_invert','clear_counts':'clear_counts','diff_encoder_loopback':'diff_encoder_loopback',
            }

    
    
    
    
    
    
    # nodes:5
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["ptt"]) -> 'msk_top_regs_msk_ctrl_ptt_neg_0x3ef0035cee99a68d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["loopback_ena"]) -> 'msk_top_regs_msk_ctrl_loopback_ena_0x99b143f50703af0_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_invert"]) -> 'msk_top_regs_msk_ctrl_rx_invert_neg_0x7a9e4517851e9732_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["clear_counts"]) -> 'msk_top_regs_msk_ctrl_clear_counts_neg_0x55e2450e4ad31070_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["diff_encoder_loopback"]) -> 'msk_top_regs_msk_ctrl_diff_encoder_loopback_neg_0x6ea17fae4f290ad0_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_msk_ctrl_ptt_neg_0x3ef0035cee99a68d_cls', 'msk_top_regs_msk_ctrl_loopback_ena_0x99b143f50703af0_cls', 'msk_top_regs_msk_ctrl_rx_invert_neg_0x7a9e4517851e9732_cls', 'msk_top_regs_msk_ctrl_clear_counts_neg_0x55e2450e4ad31070_cls', 'msk_top_regs_msk_ctrl_diff_encoder_loopback_neg_0x6ea17fae4f290ad0_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Control"
    @property
    def rdl_desc(self) -> str:
        return "MSK Modem Configuration and Control"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.ptt
        yield self.loopback_ena
        yield self.rx_invert
        yield self.clear_counts
        yield self.diff_encoder_loopback
        
        
    

    
    
class msk_top_regs_msk_stat_0_0x11225f92044176be_cls(RegAsyncReadOnly):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,ReadableAsyncMemory]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__demod_sync_lock:msk_top_regs_msk_stat_0_demod_sync_lock_neg_0x2950cdf9067a0d19_cls = msk_top_regs_msk_stat_0_demod_sync_lock_neg_0x2950cdf9067a0d19_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.demod_sync_lock',
            inst_name='demod_sync_lock',
            field_type=int)
        self.__tx_enable:msk_top_regs_msk_stat_0_tx_enable_0x7a56cd6d195d2e65_cls = msk_top_regs_msk_stat_0_tx_enable_0x7a56cd6d195d2e65_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1, msb=1,
                low=1, high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.tx_enable',
            inst_name='tx_enable',
            field_type=int)
        self.__rx_enable:msk_top_regs_msk_stat_0_rx_enable_neg_0x6dfa23c31cd45fbc_cls = msk_top_regs_msk_stat_0_rx_enable_neg_0x6dfa23c31cd45fbc_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2, msb=2,
                low=2, high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.rx_enable',
            inst_name='rx_enable',
            field_type=int)
        self.__tx_axis_valid:msk_top_regs_msk_stat_0_tx_axis_valid_neg_0x4af685b21106987d_cls = msk_top_regs_msk_stat_0_tx_axis_valid_neg_0x4af685b21106987d_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=3, msb=3,
                low=3, high=3),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.tx_axis_valid',
            inst_name='tx_axis_valid',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def demod_sync_lock(self) -> msk_top_regs_msk_stat_0_demod_sync_lock_neg_0x2950cdf9067a0d19_cls:
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
    def tx_enable(self) -> msk_top_regs_msk_stat_0_tx_enable_0x7a56cd6d195d2e65_cls:
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
        |              |      <p>1 -&gt; Data to DAC Enabled</p> <p>0 -&gt; Data to DAC          |
        |              |      Disabled</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_enable
    @property
    def rx_enable(self) -> msk_top_regs_msk_stat_0_rx_enable_neg_0x6dfa23c31cd45fbc_cls:
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
        |              |      <p>1 -&gt; Data from ADC Enabled</p> <p>0 -&gt; Data from ADC      |
        |              |      Disabled</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rx_enable
    @property
    def tx_axis_valid(self) -> msk_top_regs_msk_stat_0_tx_axis_valid_neg_0x4af685b21106987d_cls:
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
        |              |      <p>1 -&gt; S_AXIS_VALID Enabled</p> <p>0 -&gt; S_AXIS_VALID        |
        |              |      Disabled</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx_axis_valid

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'demod_sync_lock':'demod_sync_lock','tx_enable':'tx_enable','rx_enable':'rx_enable','tx_axis_valid':'tx_axis_valid',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["demod_sync_lock"]) -> 'msk_top_regs_msk_stat_0_demod_sync_lock_neg_0x2950cdf9067a0d19_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_enable"]) -> 'msk_top_regs_msk_stat_0_tx_enable_0x7a56cd6d195d2e65_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx_enable"]) -> 'msk_top_regs_msk_stat_0_rx_enable_neg_0x6dfa23c31cd45fbc_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx_axis_valid"]) -> 'msk_top_regs_msk_stat_0_tx_axis_valid_neg_0x4af685b21106987d_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_msk_stat_0_demod_sync_lock_neg_0x2950cdf9067a0d19_cls', 'msk_top_regs_msk_stat_0_tx_enable_0x7a56cd6d195d2e65_cls', 'msk_top_regs_msk_stat_0_rx_enable_neg_0x6dfa23c31cd45fbc_cls', 'msk_top_regs_msk_stat_0_tx_axis_valid_neg_0x4af685b21106987d_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Status 0"
    @property
    def rdl_desc(self) -> str:
        return "Modem status bits"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.demod_sync_lock
        yield self.tx_enable
        yield self.rx_enable
        yield self.tx_axis_valid
        
        
    

    
    
class msk_top_regs_msk_stat_1_0x485040a78b4facc5_cls(RegAsyncReadWrite):
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
        
        self.__data:msk_top_regs_msk_stat_1_data_neg_0x100875f913ba41b0_cls = msk_top_regs_msk_stat_1_data_neg_0x100875f913ba41b0_cls(
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
    def data(self) -> msk_top_regs_msk_stat_1_data_neg_0x100875f913ba41b0_cls:
        """
        Property to access data field of the register

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
        |              |      <p>Count of data requests made by modem</p> <p>This register is    |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_msk_stat_1_data_neg_0x100875f913ba41b0_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Status 1"
    @property
    def rdl_desc(self) -> str:
        return "Modem status data"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_msk_stat_2_0x79ca52b735200588_cls(RegAsyncReadWrite):
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
        
        self.__data:msk_top_regs_msk_stat_2_data_neg_0x1193896f2e20ab4d_cls = msk_top_regs_msk_stat_2_data_neg_0x1193896f2e20ab4d_cls(
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
    def data(self) -> msk_top_regs_msk_stat_2_data_neg_0x1193896f2e20ab4d_cls:
        """
        Property to access data field of the register

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
        |              |      <p>Number of clocks on which Tx Enable is active</p> <p>This       |
        |              |      register is write-to-capture.</p> <p>To read data the following    |
        |              |      steps are required:</p> <p>1 - Write any value to this register to |
        |              |      capture read data</p> <p>2 - Read the register</p>                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_msk_stat_2_data_neg_0x1193896f2e20ab4d_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Status 2"
    @property
    def rdl_desc(self) -> str:
        return "Modem status data"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_config_nco_fw_0x444933e78de34535_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls = msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls:
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
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Bitrate NCO Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Set Modem Data Rate"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.config_data
        
        
    

    
    
class msk_top_regs_config_nco_fw_0x44f085218acb5a0b_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls = msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls:
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
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx F1 NCO Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Set Modulator F1 Frequency"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.config_data
        
        
    

    
    
class msk_top_regs_config_nco_fw_0x553395d594c88659_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls = msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls:
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
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx F2 NCO Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Set Modulator F2 Frequency"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.config_data
        
        
    

    
    
class msk_top_regs_config_nco_fw_0x33a361db4d08e83f_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls = msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls:
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
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx F1 NCO Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Set Demodulator F1 Frequency"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.config_data
        
        
    

    
    
class msk_top_regs_config_nco_fw_neg_0x36fc9ff50bd27297_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls = msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls:
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
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx F2 NCO Frequency Control Word"
    @property
    def rdl_desc(self) -> str:
        return "Set Demodulator F2 Frequency"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.config_data
        
        
    

    
    
class msk_top_regs_lpf_config_0_neg_0x63d56b11f2a8b2a5_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__lpf_freeze:msk_top_regs_lpf_config_0_lpf_freeze_neg_0x52a4a2fbda7f6358_cls = msk_top_regs_lpf_config_0_lpf_freeze_neg_0x52a4a2fbda7f6358_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.lpf_freeze',
            inst_name='lpf_freeze',
            field_type=int)
        self.__lpf_zero:msk_top_regs_lpf_config_0_lpf_zero_neg_0x3e4e297867d24c30_cls = msk_top_regs_lpf_config_0_lpf_zero_neg_0x3e4e297867d24c30_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1, msb=1,
                low=1, high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.lpf_zero',
            inst_name='lpf_zero',
            field_type=int)
        self.__prbs_reserved:msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls = msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=6,
                lsb=2, msb=7,
                low=2, high=7),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_reserved',
            inst_name='prbs_reserved',
            field_type=int)
        self.__lpf_alpha:msk_top_regs_lpf_config_0_lpf_alpha_0x7718e3b25a61a530_cls = msk_top_regs_lpf_config_0_lpf_alpha_0x7718e3b25a61a530_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=24,
                lsb=8, msb=31,
                low=8, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.lpf_alpha',
            inst_name='lpf_alpha',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def lpf_freeze(self) -> msk_top_regs_lpf_config_0_lpf_freeze_neg_0x52a4a2fbda7f6358_cls:
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
        |              |      <p>0 -&gt; Normal operation</p> <p>1 -&gt; Freeze current          |
        |              |      value</p>                                                          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lpf_freeze
    @property
    def lpf_zero(self) -> msk_top_regs_lpf_config_0_lpf_zero_neg_0x3e4e297867d24c30_cls:
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
        |              |      <p>0 -&gt; Normal operation</p> <p>1 -&gt; Zero and hold           |
        |              |      accumulator</p>                                                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lpf_zero
    @property
    def prbs_reserved(self) -> msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls:
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
    def lpf_alpha(self) -> msk_top_regs_lpf_config_0_lpf_alpha_0x7718e3b25a61a530_cls:
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
        return {'lpf_freeze':'lpf_freeze','lpf_zero':'lpf_zero','prbs_reserved':'prbs_reserved','lpf_alpha':'lpf_alpha',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lpf_freeze"]) -> 'msk_top_regs_lpf_config_0_lpf_freeze_neg_0x52a4a2fbda7f6358_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lpf_zero"]) -> 'msk_top_regs_lpf_config_0_lpf_zero_neg_0x3e4e297867d24c30_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_reserved"]) -> 'msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lpf_alpha"]) -> 'msk_top_regs_lpf_config_0_lpf_alpha_0x7718e3b25a61a530_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_lpf_config_0_lpf_freeze_neg_0x52a4a2fbda7f6358_cls', 'msk_top_regs_lpf_config_0_lpf_zero_neg_0x3e4e297867d24c30_cls', 'msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls', 'msk_top_regs_lpf_config_0_lpf_alpha_0x7718e3b25a61a530_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PI Controller Configuration and Low-pass Filter Configuration"
    @property
    def rdl_desc(self) -> str:
        return "Configure PI controller and low-pass filter"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.lpf_freeze
        yield self.lpf_zero
        yield self.prbs_reserved
        yield self.lpf_alpha
        
        
    

    
    
class msk_top_regs_lpf_config_1_0x6269262ac0819864_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__i_gain:msk_top_regs_lpf_config_1_i_gain_0x4e4f67093b462024_cls = msk_top_regs_lpf_config_1_i_gain_0x4e4f67093b462024_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=24,
                lsb=0, msb=23,
                low=0, high=23),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.i_gain',
            inst_name='i_gain',
            field_type=int)
        self.__i_shift:msk_top_regs_lpf_config_1_i_shift_neg_0x6c22d49419aff3cb_cls = msk_top_regs_lpf_config_1_i_shift_neg_0x6c22d49419aff3cb_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=24, msb=31,
                low=24, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.i_shift',
            inst_name='i_shift',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def i_gain(self) -> msk_top_regs_lpf_config_1_i_gain_0x4e4f67093b462024_cls:
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
    def i_shift(self) -> msk_top_regs_lpf_config_1_i_shift_neg_0x6c22d49419aff3cb_cls:
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
        return {'i_gain':'i_gain','i_shift':'i_shift',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["i_gain"]) -> 'msk_top_regs_lpf_config_1_i_gain_0x4e4f67093b462024_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["i_shift"]) -> 'msk_top_regs_lpf_config_1_i_shift_neg_0x6c22d49419aff3cb_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_lpf_config_1_i_gain_0x4e4f67093b462024_cls', 'msk_top_regs_lpf_config_1_i_shift_neg_0x6c22d49419aff3cb_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PI Controller Configuration Configuration Register 1"
    @property
    def rdl_desc(self) -> str:
        return "Configures PI Controller I-gain and divisor"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.i_gain
        yield self.i_shift
        
        
    

    
    
class msk_top_regs_data_width_0x30221bea82717e1e_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data_width:msk_top_regs_data_width_data_width_neg_0x302f654e739e31e1_cls = msk_top_regs_data_width_data_width_neg_0x302f654e739e31e1_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=0, msb=7,
                low=0, high=7),
            misc_props=FieldMiscProps(
                default=8,
                is_volatile=False),
            logger_handle=logger_handle+'.data_width',
            inst_name='data_width',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def data_width(self) -> msk_top_regs_data_width_data_width_neg_0x302f654e739e31e1_cls:
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
        return {'data_width':'data_width',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_data_width_data_width_neg_0x302f654e739e31e1_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Modem Tx Input Data Width"
    @property
    def rdl_desc(self) -> str:
        return "Set the parallel data width of the parallel-to-serial converter"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data_width
        
        
    

    
    
class msk_top_regs_data_width_neg_0x361b7b87da257944_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data_width:msk_top_regs_data_width_data_width_neg_0x302f654e739e31e1_cls = msk_top_regs_data_width_data_width_neg_0x302f654e739e31e1_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=0, msb=7,
                low=0, high=7),
            misc_props=FieldMiscProps(
                default=8,
                is_volatile=False),
            logger_handle=logger_handle+'.data_width',
            inst_name='data_width',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def data_width(self) -> msk_top_regs_data_width_data_width_neg_0x302f654e739e31e1_cls:
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
        return {'data_width':'data_width',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_data_width_data_width_neg_0x302f654e739e31e1_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "Modem Rx Output Data Width"
    @property
    def rdl_desc(self) -> str:
        return "Set the parallel data width of the serial-to-parallel converter"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data_width
        
        
    

    
    
class msk_top_regs_prbs_ctrl_0x72ace307ca7cc42_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__prbs_sel:msk_top_regs_prbs_ctrl_prbs_sel_neg_0x2b4072fcf0ec6645_cls = msk_top_regs_prbs_ctrl_prbs_sel_neg_0x2b4072fcf0ec6645_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_sel',
            inst_name='prbs_sel',
            field_type=int)
        self.__prbs_error_insert:msk_top_regs_prbs_ctrl_prbs_error_insert_neg_0x34b21fe1f6161153_cls = msk_top_regs_prbs_ctrl_prbs_error_insert_neg_0x34b21fe1f6161153_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1, msb=1,
                low=1, high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_error_insert',
            inst_name='prbs_error_insert',
            field_type=int)
        self.__prbs_clear:msk_top_regs_prbs_ctrl_prbs_clear_neg_0x2672d40dbb0c1154_cls = msk_top_regs_prbs_ctrl_prbs_clear_neg_0x2672d40dbb0c1154_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2, msb=2,
                low=2, high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_clear',
            inst_name='prbs_clear',
            field_type=int)
        self.__prbs_manual_sync:msk_top_regs_prbs_ctrl_prbs_manual_sync_neg_0x2862b6e9670d772f_cls = msk_top_regs_prbs_ctrl_prbs_manual_sync_neg_0x2862b6e9670d772f_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=3, msb=3,
                low=3, high=3),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_manual_sync',
            inst_name='prbs_manual_sync',
            field_type=int)
        self.__prbs_reserved:msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls = msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=12,
                lsb=4, msb=15,
                low=4, high=15),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_reserved',
            inst_name='prbs_reserved',
            field_type=int)
        self.__prbs_sync_threshold:msk_top_regs_prbs_ctrl_prbs_sync_threshold_0x6fb8cbe5e8cd57c9_cls = msk_top_regs_prbs_ctrl_prbs_sync_threshold_0x6fb8cbe5e8cd57c9_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=16, msb=31,
                low=16, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.prbs_sync_threshold',
            inst_name='prbs_sync_threshold',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def prbs_sel(self) -> msk_top_regs_prbs_ctrl_prbs_sel_neg_0x2b4072fcf0ec6645_cls:
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
    def prbs_error_insert(self) -> msk_top_regs_prbs_ctrl_prbs_error_insert_neg_0x34b21fe1f6161153_cls:
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
        |              |      <p>0 -&gt; 1 :  Insert bit error in Tx data (both Normal and       |
        |              |      PRBS)</p> <p>1 -&gt; 0 : Insert bit error in Tx data (both Normal  |
        |              |      and PRBS)</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__prbs_error_insert
    @property
    def prbs_clear(self) -> msk_top_regs_prbs_ctrl_prbs_clear_neg_0x2672d40dbb0c1154_cls:
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
        |              |      <p>0 -&gt; 1 : Clear PRBS Counters</p> <p>1 -&gt; 0 : Clear PRBS   |
        |              |      Counters</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__prbs_clear
    @property
    def prbs_manual_sync(self) -> msk_top_regs_prbs_ctrl_prbs_manual_sync_neg_0x2862b6e9670d772f_cls:
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
        |              |      <p>0 -&gt; 1 : Synchronize PRBS monitor</p> <p>1 -&gt; 0 :         |
        |              |      Synchronize PRBS monitor</p>                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__prbs_manual_sync
    @property
    def prbs_reserved(self) -> msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls:
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
    def prbs_sync_threshold(self) -> msk_top_regs_prbs_ctrl_prbs_sync_threshold_0x6fb8cbe5e8cd57c9_cls:
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
        |              |      <p>0 : Auto Sync Disabled</p> <p>N &gt; 0 : Auto sync after N      |
        |              |      errors</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__prbs_sync_threshold

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'prbs_sel':'prbs_sel','prbs_error_insert':'prbs_error_insert','prbs_clear':'prbs_clear','prbs_manual_sync':'prbs_manual_sync','prbs_reserved':'prbs_reserved','prbs_sync_threshold':'prbs_sync_threshold',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_sel"]) -> 'msk_top_regs_prbs_ctrl_prbs_sel_neg_0x2b4072fcf0ec6645_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_error_insert"]) -> 'msk_top_regs_prbs_ctrl_prbs_error_insert_neg_0x34b21fe1f6161153_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_clear"]) -> 'msk_top_regs_prbs_ctrl_prbs_clear_neg_0x2672d40dbb0c1154_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_manual_sync"]) -> 'msk_top_regs_prbs_ctrl_prbs_manual_sync_neg_0x2862b6e9670d772f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_reserved"]) -> 'msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["prbs_sync_threshold"]) -> 'msk_top_regs_prbs_ctrl_prbs_sync_threshold_0x6fb8cbe5e8cd57c9_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['msk_top_regs_prbs_ctrl_prbs_sel_neg_0x2b4072fcf0ec6645_cls', 'msk_top_regs_prbs_ctrl_prbs_error_insert_neg_0x34b21fe1f6161153_cls', 'msk_top_regs_prbs_ctrl_prbs_clear_neg_0x2672d40dbb0c1154_cls', 'msk_top_regs_prbs_ctrl_prbs_manual_sync_neg_0x2862b6e9670d772f_cls', 'msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls', 'msk_top_regs_prbs_ctrl_prbs_sync_threshold_0x6fb8cbe5e8cd57c9_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Control 0"
    @property
    def rdl_desc(self) -> str:
        return "Configures operation of the PRBS Generator and Monitor"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.prbs_sel
        yield self.prbs_error_insert
        yield self.prbs_clear
        yield self.prbs_manual_sync
        yield self.prbs_reserved
        yield self.prbs_sync_threshold
        
        
    

    
    
class msk_top_regs_config_prbs_seed_neg_0x19de76e0a2449a75_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_prbs_seed_config_data_0x73a9fcd47073237e_cls = msk_top_regs_config_prbs_seed_config_data_0x73a9fcd47073237e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_prbs_seed_config_data_0x73a9fcd47073237e_cls:
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
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_config_prbs_seed_config_data_0x73a9fcd47073237e_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Control 1"
    @property
    def rdl_desc(self) -> str:
        return "PRBS Initial State"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.config_data
        
        
    

    
    
class msk_top_regs_config_prbs_poly_0x59367282cbe7a1c8_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_prbs_poly_config_data_neg_0x5fc157fe7df0f535_cls = msk_top_regs_config_prbs_poly_config_data_neg_0x5fc157fe7df0f535_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_prbs_poly_config_data_neg_0x5fc157fe7df0f535_cls:
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
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_config_prbs_poly_config_data_neg_0x5fc157fe7df0f535_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Control 2"
    @property
    def rdl_desc(self) -> str:
        return "PRBS Polynomial"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.config_data
        
        
    

    
    
class msk_top_regs_config_prbs_errmask_neg_0xcddb11619d27b12_cls(RegAsyncReadWrite):
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
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AsyncAddressMap,AsyncRegFile,MemoryAsyncReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__config_data:msk_top_regs_config_prbs_errmask_config_data_neg_0x172894e16caf1f6a_cls = msk_top_regs_config_prbs_errmask_config_data_neg_0x172894e16caf1f6a_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.config_data',
            inst_name='config_data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def config_data(self) -> msk_top_regs_config_prbs_errmask_config_data_neg_0x172894e16caf1f6a_cls:
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
        return {'config_data':'config_data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_config_prbs_errmask_config_data_neg_0x172894e16caf1f6a_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Control 3"
    @property
    def rdl_desc(self) -> str:
        return "PRBS Error Mask"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.config_data
        
        
    

    
    
class msk_top_regs_stat_32_bits_0x74f460ee43ed88ef_cls(RegAsyncReadWrite):
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
        
        self.__data:msk_top_regs_stat_32_bits_data_neg_0x544fe2aae1d2774_cls = msk_top_regs_stat_32_bits_data_neg_0x544fe2aae1d2774_cls(
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
    def data(self) -> msk_top_regs_stat_32_bits_data_neg_0x544fe2aae1d2774_cls:
        """
        Property to access data field of the register

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
        |              |      <p>This register is write-to-capture.</p> <p>To read data the      |
        |              |      following steps are required:</p> <p>1 - Write any value to this   |
        |              |      register to capture read data</p> <p>2 - Read the register</p>     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_stat_32_bits_data_neg_0x544fe2aae1d2774_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Status 0"
    @property
    def rdl_desc(self) -> str:
        return "PRBS Bits Received"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_stat_32_errs_neg_0x410fa9bc87190658_cls(RegAsyncReadWrite):
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
        
        self.__data:msk_top_regs_stat_32_errs_data_0x7af54aff70ab45c5_cls = msk_top_regs_stat_32_errs_data_0x7af54aff70ab45c5_cls(
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
    def data(self) -> msk_top_regs_stat_32_errs_data_0x7af54aff70ab45c5_cls:
        """
        Property to access data field of the register

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
        |              |      errored-bits</p> <p>This register is write-to-capture.</p> <p>To   |
        |              |      read data the following steps are required:</p> <p>1 - Write any   |
        |              |      value to this register to capture read data</p> <p>2 - Read the    |
        |              |      register</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_stat_32_errs_data_0x7af54aff70ab45c5_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Status 1"
    @property
    def rdl_desc(self) -> str:
        return "PRBS Bit Errors"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_stat_32_lpf_acc_0x1be0f0bf59c971f9_cls(RegAsyncReadWrite):
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
        
        self.__data:msk_top_regs_stat_32_lpf_acc_data_neg_0x5ba1df96a18c1ea7_cls = msk_top_regs_stat_32_lpf_acc_data_neg_0x5ba1df96a18c1ea7_cls(
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
    def data(self) -> msk_top_regs_stat_32_lpf_acc_data_neg_0x5ba1df96a18c1ea7_cls:
        """
        Property to access data field of the register

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
        |              |      <p>PI Controller Accumulator Value</p> <p>This register is write-  |
        |              |      to-capture.</p> <p>To read data the following steps are            |
        |              |      required:</p> <p>1 - Write any value to this register to capture   |
        |              |      read data</p> <p>2 - Read the register</p>                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_stat_32_lpf_acc_data_neg_0x5ba1df96a18c1ea7_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F1 PI Controller Accumulator"
    @property
    def rdl_desc(self) -> str:
        return "Value of the F1 PI Controller Accumulator"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_stat_32_lpf_acc_neg_0x71a284902b1741d_cls(RegAsyncReadWrite):
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
        
        self.__data:msk_top_regs_stat_32_lpf_acc_data_neg_0x5ba1df96a18c1ea7_cls = msk_top_regs_stat_32_lpf_acc_data_neg_0x5ba1df96a18c1ea7_cls(
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
    def data(self) -> msk_top_regs_stat_32_lpf_acc_data_neg_0x5ba1df96a18c1ea7_cls:
        """
        Property to access data field of the register

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
        |              |      <p>PI Controller Accumulator Value</p> <p>This register is write-  |
        |              |      to-capture.</p> <p>To read data the following steps are            |
        |              |      required:</p> <p>1 - Write any value to this register to capture   |
        |              |      read data</p> <p>2 - Read the register</p>                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_stat_32_lpf_acc_data_neg_0x5ba1df96a18c1ea7_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "F2 PI Controller Accumulator"
    @property
    def rdl_desc(self) -> str:
        return "Value of the F2 PI Controller Accumulator"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    

    
    
class msk_top_regs_msk_stat_3_neg_0x724989d9d7fa96aa_cls(RegAsyncReadWrite):
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
        
        self.__data:msk_top_regs_msk_stat_3_data_0x158d4610c7260e45_cls = msk_top_regs_msk_stat_3_data_0x158d4610c7260e45_cls(
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
    def data(self) -> msk_top_regs_msk_stat_3_data_0x158d4610c7260e45_cls:
        """
        Property to access data field of the register

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
        |              |      <p>Number completed S_AXIS transfers</p> <p>This register is       |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'msk_top_regs_msk_stat_3_data_0x158d4610c7260e45_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "MSK Modem Status 3"
    @property
    def rdl_desc(self) -> str:
        return "Modem status data"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldAsyncReadOnly,FieldAsyncWriteOnly,FieldAsyncReadWrite]]:
        
        
        yield self.data
        
        
    


if __name__ == '__main__':
    pass