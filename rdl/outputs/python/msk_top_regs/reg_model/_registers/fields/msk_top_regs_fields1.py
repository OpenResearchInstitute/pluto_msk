

"""
Python Wrapper for the msk_top_regs register model

This code was generated from the PeakRDL-python package version 2.3.0

"""









from ....lib import UDPStruct
from ....lib import FieldAsyncReadOnly, FieldAsyncWriteOnly, FieldAsyncReadWrite, Field


# field definitions
    
    
class msk_top_regs_prbs_ctrl_prbs_error_insert_neg_0x34b21fe1f6161153_cls(FieldAsyncWriteOnly):
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
    |              |      <p>0 -&gt; 1 :  Insert bit error in Tx data (both Normal and       |
    |              |      PRBS)</p> <p>1 -&gt; 0 : Insert bit error in Tx data (both Normal  |
    |              |      and PRBS)</p>                                                      |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Error Insert"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e 1 :  Insert bit error in Tx data (both Normal and PRBS)\n\n1 -\u003e 0 : Insert bit error in Tx data (both Normal and PRBS)"
    
    
    

    
    
class msk_top_regs_prbs_ctrl_prbs_clear_neg_0x2672d40dbb0c1154_cls(FieldAsyncWriteOnly):
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
    |              |      <p>0 -&gt; 1 : Clear PRBS Counters</p> <p>1 -&gt; 0 : Clear PRBS   |
    |              |      Counters</p>                                                       |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Clear Counters"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e 1 : Clear PRBS Counters\n\n1 -\u003e 0 : Clear PRBS Counters"
    
    
    

    
    
class msk_top_regs_prbs_ctrl_prbs_manual_sync_neg_0x2862b6e9670d772f_cls(FieldAsyncWriteOnly):
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
    |              |      <p>0 -&gt; 1 : Synchronize PRBS monitor</p> <p>1 -&gt; 0 :         |
    |              |      Synchronize PRBS monitor</p>                                       |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Manual Sync"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e 1 : Synchronize PRBS monitor\n\n1 -\u003e 0 : Synchronize PRBS monitor"
    
    
    

    
    
class msk_top_regs_prbs_ctrl_prbs_sync_threshold_0x6fb8cbe5e8cd57c9_cls(FieldAsyncReadWrite):
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
    |              |      <p>0 : Auto Sync Disabled</p> <p>N &gt; 0 : Auto sync after N      |
    |              |      errors</p>                                                         |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Auto Sync Threshold"
    @property
    def rdl_desc(self) -> str:
        return "0 : Auto Sync Disabled\n\nN \u003e 0 : Auto sync after N errors"
    
    
    

    
    
class msk_top_regs_config_prbs_seed_config_data_0x73a9fcd47073237e_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_config_prbs_poly_config_data_neg_0x5fc157fe7df0f535_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_config_prbs_errmask_config_data_neg_0x172894e16caf1f6a_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_stat_32_bits_data_neg_0x544fe2aae1d2774_cls(FieldAsyncReadWrite):
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
    |              |      <p>This register is write-to-capture.</p> <p>To read data the      |
    |              |      following steps are required:</p> <p>1 - Write any value to this   |
    |              |      register to capture read data</p> <p>2 - Read the register</p>     |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Bits Received"
    @property
    def rdl_desc(self) -> str:
        return "Number of bits received by the PRBS monitor since last\nBER can be calculated as the ratio of received bits to errored-bits\n\nThis register is write-to-capture.\n\nTo read data the following steps are required:\n\n1 - Write any value to this register to capture read data\n\n2 - Read the register"
    
    
    

    
    
class msk_top_regs_stat_32_errs_data_0x7af54aff70ab45c5_cls(FieldAsyncReadWrite):
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
    |              |      errored-bits</p> <p>This register is write-to-capture.</p> <p>To   |
    |              |      read data the following steps are required:</p> <p>1 - Write any   |
    |              |      value to this register to capture read data</p> <p>2 - Read the    |
    |              |      register</p>                                                       |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PRBS Bit Errors"
    @property
    def rdl_desc(self) -> str:
        return "Number of errored-bits received by the PRBS monitor since last sync\nBER can be calculated as the ratio of received bits to errored-bits\n\nThis register is write-to-capture.\n\nTo read data the following steps are required:\n\n1 - Write any value to this register to capture read data\n\n2 - Read the register"
    
    
    

    
    
class msk_top_regs_stat_32_lpf_acc_data_neg_0x5ba1df96a18c1ea7_cls(FieldAsyncReadWrite):
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
    |              |      <p>PI Controller Accumulator Value</p> <p>This register is write-  |
    |              |      to-capture.</p> <p>To read data the following steps are            |
    |              |      required:</p> <p>1 - Write any value to this register to capture   |
    |              |      read data</p> <p>2 - Read the register</p>                         |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "PI Controller Accumulator Value"
    @property
    def rdl_desc(self) -> str:
        return "PI Controller Accumulator Value\n\nThis register is write-to-capture.\n\nTo read data the following steps are required:\n\n1 - Write any value to this register to capture read data\n\n2 - Read the register"
    
    
    

    
    
class msk_top_regs_msk_stat_3_data_0x158d4610c7260e45_cls(FieldAsyncReadWrite):
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
    |              |      <p>Number completed S_AXIS transfers</p> <p>This register is       |
    |              |      write-to-capture.</p> <p>To read data the following steps are      |
    |              |      required:</p> <p>1 - Write any value to this register to capture   |
    |              |      read data</p> <p>2 - Read the register</p>                         |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "S_AXIS Transfers"
    @property
    def rdl_desc(self) -> str:
        return "Number completed S_AXIS transfers\n\nThis register is write-to-capture.\n\nTo read data the following steps are required:\n\n1 - Write any value to this register to capture read data\n\n2 - Read the register"
    
    
    

    
    
class msk_top_regs_rx_sample_discard_rx_sample_discard_neg_0x38eb4151bea7286c_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_rx_sample_discard_rx_nco_discard_neg_0x2b9c27e13c5cf83b_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_lpf_config_2_p_gain_neg_0x564ffd3b5c9ee5a_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_lpf_config_2_p_shift_0x4bc9a5c1aa9bb185_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_status_reg_data_0x4aca4cd89620a2eb_cls(FieldAsyncReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_desc(self) -> str:
        return "Frequency offet applied to the F1 NCO\n\nThis register is write-to-capture.\n\nTo read data the following steps are required:\n\n1 - Write any value to this register to capture read data\n\n2 - Read the register"
    
    
    

    
    
class msk_top_regs_status_reg_data_neg_0x6c861e11e512bee8_cls(FieldAsyncReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_desc(self) -> str:
        return "Frequency offet applied to the F2 NCO\n\nThis register is write-to-capture.\n\nTo read data the following steps are required:\n\n1 - Write any value to this register to capture read data\n\n2 - Read the register"
    
    
    

    
    
class msk_top_regs_status_reg_data_0x6606ce01300ede9e_cls(FieldAsyncReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_desc(self) -> str:
        return "Error value of the F1 Costas loop after each active bit period\n\nThis register is write-to-capture.\n\nTo read data the following steps are required:\n\n1 - Write any value to this register to capture read data\n\n2 - Read the register"
    
    
    

    
    
class msk_top_regs_status_reg_data_neg_0x4bf1ae36b78b0b04_cls(FieldAsyncReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_desc(self) -> str:
        return "Error value of the F2 Costas loop after each active bit period\n\nThis register is write-to-capture.\n\nTo read data the following steps are required:\n\n1 - Write any value to this register to capture read data\n\n2 - Read the register"
    
    
    

    
    
class msk_top_regs_tx_sync_ctrl_tx_sync_ena_neg_0x6fd8f3a2460f4f63_cls(FieldAsyncReadWrite):
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
    |              |      <p>0 : Disable sync transmission</p> <p>1 : Enable sync            |
    |              |      transmission when PTT is asserted</p>                              |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx Sync Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 : Disable sync transmission\n\n1 : Enable sync transmission when PTT is asserted"
    
    
    

    
    
class msk_top_regs_tx_sync_ctrl_tx_sync_force_0x9cde1909b978b15_cls(FieldAsyncReadWrite):
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
    |              |      <p>0 : Normal operation</p> <p>1 : Continuously transmit           |
    |              |      synchronization pattern</p>                                        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx Sync Force"
    @property
    def rdl_desc(self) -> str:
        return "0 : Normal operation\n\n1 : Continuously transmit synchronization pattern"
    
    
    

    
    
class msk_top_regs_tx_sync_cnt_tx_sync_cnt_neg_0x523b45dbe13fc09a_cls(FieldAsyncReadWrite):
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
    |              |      <p>Value from 0x00_0000 to 0xFF_FFFF. </p> <p>This value           |
    |              |      represents the number bit-times the synchronization signal should  |
    |              |      be sent after PTT is asserted.</p>                                 |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx sync duration"
    @property
    def rdl_desc(self) -> str:
        return "Value from 0x00_0000 to 0xFF_FFFF. \n\nThis value represents the number bit-times the synchronization signal should be sent after PTT is asserted."
    
    
    

    
    
class msk_top_regs_lowpass_ema_alpha_alpha_neg_0x23adfbbd4f5ca699_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_rx_power_data_neg_0x7d59af4abd6cddc0_cls(FieldAsyncReadWrite):
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
    |              |      <p>Value that represent the RMS power of the incoming signal       |
    |              |      (I-channel)</p> <p>This register is write-to-capture. To read data |
    |              |      the following steps are required:</p> <ol type="1"> <li> Write any |
    |              |      value to this register to capture read data </li><li> Read the     |
    |              |      register </li></ol>                                                |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Receive Power"
    @property
    def rdl_desc(self) -> str:
        return "Value that represent the RMS power of the incoming signal (I-channel)\n\nThis register is write-to-capture. To read data the following steps are required:\n[list=1]\n[*] Write any value to this register to capture read data\n[*] Read the register\n[/list]"
    
    
    

    
    
class msk_top_regs_status_reg_data_neg_0x105bc235a0a31370_cls(FieldAsyncReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_desc(self) -> str:
        return "Read and Write Pointers\n\n[code]\nBits 31:16 - write pointer (12-bits)\nBits 15:00 - read pointer (12-bits)\n[/code]\n\nThis register is write-to-capture. To read data the following steps are required:\n[list=1]\n[*] Write any value to this register to capture read data\n[*] Read the register\n[/list]"
    
    
    


if __name__ == '__main__':
    pass