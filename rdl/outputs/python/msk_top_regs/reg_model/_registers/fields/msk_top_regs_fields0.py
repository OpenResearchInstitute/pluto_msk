

"""
Python Wrapper for the msk_top_regs register model

This code was generated from the PeakRDL-python package version 2.3.0

"""









from ....lib import UDPStruct
from ....lib import FieldAsyncReadOnly, FieldAsyncWriteOnly, FieldAsyncReadWrite, Field


# field definitions
    
    
class msk_top_regs_msk_hash_lo_hash_id_lo_neg_0x105bacf44f0ca709_cls(FieldAsyncReadOnly):
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
    
    
    

    
    
class msk_top_regs_msk_hash_hi_hash_id_hi_0x4570a64f2713e448_cls(FieldAsyncReadOnly):
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
    
    
    

    
    
class msk_top_regs_msk_init_txrxinit_neg_0x2f4bea5a67f66424_cls(FieldAsyncReadWrite):
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
    |              |      <p>0 -&gt; Normal modem operation </p> <p>1 -&gt; Initialize Tx    |
    |              |      and Rx</p>                                                         |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx/Rx Init Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Normal modem operation \n\n1 -\u003e Initialize Tx and Rx"
    
    
    

    
    
class msk_top_regs_msk_init_txinit_neg_0x15f317dcac1ceee_cls(FieldAsyncReadWrite):
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
    |              |      <p>0 -&gt; Normal Tx operation</p> <p>1 -&gt; Initialize Tx</p>    |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx Init Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Normal Tx operation\n\n1 -\u003e Initialize Tx"
    
    
    

    
    
class msk_top_regs_msk_init_rxinit_neg_0x16300a51d9e0ebc6_cls(FieldAsyncReadWrite):
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
    |              |      <p>0 -&gt; Normal Rx operation   </p> <p>1 -&gt; Initialize Rx</p> |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Rx Init Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Normal Rx operation   \n\n1 -\u003e Initialize Rx"
    
    
    

    
    
class msk_top_regs_msk_ctrl_ptt_neg_0x3ef0035cee99a68d_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_msk_ctrl_loopback_ena_0x99b143f50703af0_cls(FieldAsyncReadWrite):
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
    |              |      <p>0 -&gt; Modem loopback disabled</p> <p>1 -&gt; Modem loopback   |
    |              |      enabled</p>                                                        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Modem Digital Tx -\u003e Rx Loopback Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Modem loopback disabled\n\n1 -\u003e Modem loopback enabled"
    
    
    

    
    
class msk_top_regs_msk_ctrl_rx_invert_neg_0x7a9e4517851e9732_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_msk_ctrl_clear_counts_neg_0x55e2450e4ad31070_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_msk_ctrl_diff_encoder_loopback_neg_0x6ea17fae4f290ad0_cls(FieldAsyncReadWrite):
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
    |              |      <p>0 -&gt; Differential Encoder -&gt; Decoder loopback             |
    |              |      disabled</p> <p>1 -&gt; Differential Encoder -&gt; Decoder         |
    |              |      loopback enabled</p>                                               |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Differential Encoder -\u003e Decoder Loopback Enable"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Differential Encoder -\u003e Decoder loopback disabled\n\n1 -\u003e Differential Encoder -\u003e Decoder loopback enabled"
    
    
    

    
    
class msk_top_regs_msk_stat_0_demod_sync_lock_neg_0x2950cdf9067a0d19_cls(FieldAsyncReadOnly):
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
    
    
    

    
    
class msk_top_regs_msk_stat_0_tx_enable_0x7a56cd6d195d2e65_cls(FieldAsyncReadOnly):
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
    |              |      <p>1 -&gt; Data to DAC Enabled</p> <p>0 -&gt; Data to DAC          |
    |              |      Disabled</p>                                                       |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "AD9363 DAC Interface Tx Enable Input Active"
    @property
    def rdl_desc(self) -> str:
        return "1 -\u003e Data to DAC Enabled\n\n0 -\u003e Data to DAC Disabled"
    
    
    

    
    
class msk_top_regs_msk_stat_0_rx_enable_neg_0x6dfa23c31cd45fbc_cls(FieldAsyncReadOnly):
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
    |              |      <p>1 -&gt; Data from ADC Enabled</p> <p>0 -&gt; Data from ADC      |
    |              |      Disabled</p>                                                       |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "AD9363 ADC Interface Rx Enable Input Active"
    @property
    def rdl_desc(self) -> str:
        return "1 -\u003e Data from ADC Enabled\n\n0 -\u003e Data from ADC Disabled"
    
    
    

    
    
class msk_top_regs_msk_stat_0_tx_axis_valid_neg_0x4af685b21106987d_cls(FieldAsyncReadOnly):
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
    |              |      <p>1 -&gt; S_AXIS_VALID Enabled</p> <p>0 -&gt; S_AXIS_VALID        |
    |              |      Disabled</p>                                                       |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx S_AXIS_VALID"
    @property
    def rdl_desc(self) -> str:
        return "1 -\u003e S_AXIS_VALID Enabled\n\n0 -\u003e S_AXIS_VALID Disabled"
    
    
    

    
    
class msk_top_regs_msk_stat_1_data_neg_0x100875f913ba41b0_cls(FieldAsyncReadWrite):
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
    |              |      <p>Count of data requests made by modem</p> <p>This register is    |
    |              |      write-to-capture.</p> <p>To read data the following steps are      |
    |              |      required:</p> <p>1 - Write any value to this register to capture   |
    |              |      read data</p> <p>2 - Read the register</p>                         |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx Bit Count"
    @property
    def rdl_desc(self) -> str:
        return "Count of data requests made by modem\n\nThis register is write-to-capture.\n\nTo read data the following steps are required:\n\n1 - Write any value to this register to capture read data\n\n2 - Read the register"
    
    
    

    
    
class msk_top_regs_msk_stat_2_data_neg_0x1193896f2e20ab4d_cls(FieldAsyncReadWrite):
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
    |              |      <p>Number of clocks on which Tx Enable is active</p> <p>This       |
    |              |      register is write-to-capture.</p> <p>To read data the following    |
    |              |      steps are required:</p> <p>1 - Write any value to this register to |
    |              |      capture read data</p> <p>2 - Read the register</p>                 |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Tx Enable Count"
    @property
    def rdl_desc(self) -> str:
        return "Number of clocks on which Tx Enable is active\n\nThis register is write-to-capture.\n\nTo read data the following steps are required:\n\n1 - Write any value to this register to capture read data\n\n2 - Read the register"
    
    
    

    
    
class msk_top_regs_config_nco_fw_config_data_0x75b35e2cbdb56c01_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_lpf_config_0_lpf_freeze_neg_0x52a4a2fbda7f6358_cls(FieldAsyncReadWrite):
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
    |              |      <p>0 -&gt; Normal operation</p> <p>1 -&gt; Freeze current          |
    |              |      value</p>                                                          |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Freeze the accumulator\u0027s current value"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Normal operation\n\n1 -\u003e Freeze current value"
    
    
    

    
    
class msk_top_regs_lpf_config_0_lpf_zero_neg_0x3e4e297867d24c30_cls(FieldAsyncReadWrite):
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
    |              |      <p>0 -&gt; Normal operation</p> <p>1 -&gt; Zero and hold           |
    |              |      accumulator</p>                                                    |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "Hold the PI Accumulator at zero"
    @property
    def rdl_desc(self) -> str:
        return "0 -\u003e Normal operation\n\n1 -\u003e Zero and hold accumulator"
    
    
    

    
    
class msk_top_regs_lpf_config_0_prbs_reserved_neg_0x15b81a502eb28bf6_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_lpf_config_0_lpf_alpha_0x7718e3b25a61a530_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_lpf_config_1_i_gain_0x4e4f67093b462024_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_lpf_config_1_i_shift_neg_0x6c22d49419aff3cb_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_data_width_data_width_neg_0x302f654e739e31e1_cls(FieldAsyncReadWrite):
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
    
    
    

    
    
class msk_top_regs_prbs_ctrl_prbs_sel_neg_0x2b4072fcf0ec6645_cls(FieldAsyncReadWrite):
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
    
    
    


if __name__ == '__main__':
    pass