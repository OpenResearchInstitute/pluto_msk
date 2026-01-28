

"""
Python Wrapper for the msk_top_regs register model

This code was generated from the PeakRDL-python package version 2.3.0

"""









from ....lib import UDPStruct
from ....lib import FieldAsyncReadOnly, FieldAsyncWriteOnly, FieldAsyncReadWrite, Field


# field definitions
    
    
class msk_top_regs_frame_sync_status_frame_sync_locked_0x3f4fc2458f4f0cd2_cls(FieldAsyncReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Frame Sync Lock"
    @property
    def rdl_desc(self) -> str:
        return "0 - Frame sync not locked\n1 - Frame sync locked"
    
    
    

    
    
class msk_top_regs_frame_sync_status_frame_buffer_overflow_0x2a4a1a70827edd3d_cls(FieldAsyncReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Frame Buffer Overflow"
    @property
    def rdl_desc(self) -> str:
        return "0 - Normal operation\n1 - Buffer overflow"
    
    
    

    
    
class msk_top_regs_frame_sync_status_frames_received_neg_0x7dbb6db13933fcd3_cls(FieldAsyncReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Frames Received"
    @property
    def rdl_desc(self) -> str:
        return "Count of frames received. Value is 0x00_0000 to 0xFF_FFFF. Counter rolls over when max count is reached."
    
    
    

    
    
class msk_top_regs_frame_sync_status_frame_sync_errors_neg_0x5b451d83cc348092_cls(FieldAsyncReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Frames Sync Errors"
    @property
    def rdl_desc(self) -> str:
        return "Count of frame sync errors. Value is 0 to 63. Counter rolls over when max count is reached."
    
    
    

    
    
class msk_top_regs_symbol_lock_control_symbol_lock_count_0x19781f0b431fdeca_cls(FieldAsyncReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Symbol Lock Integration Count"
    @property
    def rdl_desc(self) -> str:
        return "Sets the integration period in symbols. Value is from 0 to 1023."
    
    
    

    
    
class msk_top_regs_symbol_lock_control_symbol_lock_threshold_0x4839317bf846465b_cls(FieldAsyncReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Symbol Lock Threshold"
    @property
    def rdl_desc(self) -> str:
        return "Sets the threshold value on which to declare symbol sync"
    
    
    

    
    
class msk_top_regs_symbol_lock_status_f1f2_neg_0x39a76b7538e7e440_cls(FieldAsyncReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Symbol Lock F1 and F2"
    @property
    def rdl_desc(self) -> str:
        return "0 - Unlocked\n1 - F1 and F2 locked"
    
    
    

    
    
class msk_top_regs_symbol_lock_status_f1_0x7a9ecba509a49e91_cls(FieldAsyncReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Symbol Lock F1"
    @property
    def rdl_desc(self) -> str:
        return "0 - Unlocked\n1 - F1 locked"
    
    
    

    
    
class msk_top_regs_symbol_lock_status_f2_neg_0x4fb0b06c30787656_cls(FieldAsyncReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Symbol Lock F2"
    @property
    def rdl_desc(self) -> str:
        return "0 - Unlocked\n1 - F2 locked"
    
    
    

    
    
class msk_top_regs_symbol_lock_status_unlock_f1_0x300f85594684937f_cls(FieldAsyncReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "F1 unlocked since last read"
    @property
    def rdl_desc(self) -> str:
        return "0 - No unlock since last read\n1 - One or mode unlocks since last read"
    
    
    

    
    
class msk_top_regs_symbol_lock_status_unlock_f2_neg_0x4dd96876769cb4aa_cls(FieldAsyncReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "F2 unlocked since last read"
    @property
    def rdl_desc(self) -> str:
        return "0 - No unlock since last read\n1 - One or mode unlocks since last read"
    
    
    

    
    
class msk_top_regs_symbol_lock_time_f1_0x2a2d395dea4e58d0_cls(FieldAsyncReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "F1 Symbol Lock Time"
    @property
    def rdl_desc(self) -> str:
        return "Number of symbols for F1 lock since init released"
    
    
    

    
    
class msk_top_regs_symbol_lock_time_f2_0x2bd399539720f3f_cls(FieldAsyncReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "F2 Symbol Lock Time"
    @property
    def rdl_desc(self) -> str:
        return "Number of symbols for F2 lock since init released"
    
    
    


if __name__ == '__main__':
    pass