<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: msk_top_regs
  - src/regblock_udps.rdl
  - src/msk_top_regs.rdl
-->

## msk_top_regs address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x98

<p>MSK Modem Configuration and Status Registers</p>

|Offset|       Identifier      |                             Name                            |
|------|-----------------------|-------------------------------------------------------------|
| 0x00 |      Hash_ID_Low      |            Pluto MSK FPGA Hash ID - Lower 32-bits           |
| 0x04 |      Hash_ID_High     |            Pluto MSK FPGA Hash ID - Upper 32-bits           |
| 0x08 |        MSK_Init       |               MSK Modem Initialization Control              |
| 0x0C |      MSK_Control      |                      MSK Modem Control                      |
| 0x10 |       MSK_Status      |                      MSK Modem Status 0                     |
| 0x14 |      Tx_Bit_Count     |                      MSK Modem Status 1                     |
| 0x18 |    Tx_Enable_Count    |                      MSK Modem Status 2                     |
| 0x1C |      Fb_FreqWord      |              Bitrate NCO Frequency Control Word             |
| 0x20 |     TX_F1_FreqWord    |               Tx F1 NCO Frequency Control Word              |
| 0x24 |     TX_F2_FreqWord    |               Tx F2 NCO Frequency Control Word              |
| 0x28 |     RX_F1_FreqWord    |               Rx F1 NCO Frequency Control Word              |
| 0x2C |     RX_F2_FreqWord    |               Rx F2 NCO Frequency Control Word              |
| 0x30 |      LPF_Config_0     |PI Controller Configuration and Low-pass Filter Configuration|
| 0x34 |      LPF_Config_1     |     PI Controller Configuration Configuration Register 1    |
| 0x38 |     Tx_Data_Width     |                  Modem Tx Input Data Width                  |
| 0x3C |     Rx_Data_Width     |                  Modem Rx Output Data Width                 |
| 0x40 |      PRBS_Control     |                        PRBS Control 0                       |
| 0x44 |   PRBS_Initial_State  |                        PRBS Control 1                       |
| 0x48 |    PRBS_Polynomial    |                        PRBS Control 2                       |
| 0x4C |    PRBS_Error_Mask    |                        PRBS Control 3                       |
| 0x50 |     PRBS_Bit_Count    |                        PRBS Status 0                        |
| 0x54 |    PRBS_Error_Count   |                        PRBS Status 1                        |
| 0x58 |      LPF_Accum_F1     |                 F1 PI Controller Accumulator                |
| 0x5C |      LPF_Accum_F2     |                 F2 PI Controller Accumulator                |
| 0x60 |    axis_xfer_count    |                      MSK Modem Status 3                     |
| 0x64 |   Rx_Sample_Discard   |                      Rx Sample Discard                      |
| 0x68 |      LPF_Config_2     |     PI Controller Configuration Configuration Register 2    |
| 0x6C |     f1_nco_adjust     |                   F1 NCO Frequency Adjust                   |
| 0x70 |     f2_nco_adjust     |                   F2 NCO Frequency Adjust                   |
| 0x74 |        f1_error       |                        F1 Error Value                       |
| 0x78 |        f2_error       |                        F2 Error Value                       |
| 0x7C |      Tx_Sync_Ctrl     |                   Transmitter Sync Control                  |
| 0x80 |      Tx_Sync_Cnt      |                  Transmitter Sync Duration                  |
| 0x84 |   lowpass_ema_alpha1  |               Exponential Moving Average Alpha              |
| 0x88 |   lowpass_ema_alpha2  |               Exponential Moving Average Alpha              |
| 0x8C |        rx_power       |                        Receive Power                        |
| 0x90 |tx_async_fifo_rd_wr_ptr|            Tx async FIFO read and write pointers            |
| 0x94 |rx_async_fifo_rd_wr_ptr|            Rx async FIFO read and write pointers            |

### Hash_ID_Low register

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x4

|Bits|Identifier|Access|   Reset  |         Name        |
|----|----------|------|----------|---------------------|
|31:0|hash_id_lo|   r  |0xAAAA5555|Hash ID Lower 32-bits|

#### hash_id_lo field

<p>Lower 32-bits of Pluto MSK FPGA Hash ID</p>

### Hash_ID_High register

- Absolute Address: 0x4
- Base Offset: 0x4
- Size: 0x4

|Bits|Identifier|Access|   Reset  |         Name        |
|----|----------|------|----------|---------------------|
|31:0|hash_id_hi|   r  |0x5555AAAA|Hash ID Upper 32-bits|

#### hash_id_hi field

<p>Upper 32-bits of Pluto MSK FPGA Hash ID</p>

### MSK_Init register

- Absolute Address: 0x8
- Base Offset: 0x8
- Size: 0x4

<p>Synchronous initialization of MSK Modem functions, does not affect configuration registers.</p>

|Bits|Identifier|Access|Reset|       Name      |
|----|----------|------|-----|-----------------|
|  0 | txrxinit |  rw  | 0x1 |Tx/Rx Init Enable|
|  1 |  txinit  |  rw  | 0x1 |  Tx Init Enable |
|  2 |  rxinit  |  rw  | 0x1 |  Rx Init Enable |

#### txrxinit field

<p>0 -&gt; Normal modem operation </p>
<p>1 -&gt; Initialize Tx and Rx</p>

#### txinit field

<p>0 -&gt; Normal Tx operation</p>
<p>1 -&gt; Initialize Tx</p>

#### rxinit field

<p>0 -&gt; Normal Rx operation   </p>
<p>1 -&gt; Initialize Rx</p>

### MSK_Control register

- Absolute Address: 0xC
- Base Offset: 0xC
- Size: 0x4

<p>MSK Modem Configuration and Control</p>

|Bits|      Identifier     |Access|Reset|                      Name                     |
|----|---------------------|------|-----|-----------------------------------------------|
|  0 |         ptt         |  rw  | 0x0 |              Push-to-Talk Enable              |
|  1 |     loopback_ena    |  rw  | 0x0 |     Modem Digital Tx -> Rx Loopback Enable    |
|  2 |      rx_invert      |  rw  | 0x0 |             Rx Data Invert Enable             |
|  3 |     clear_counts    |  rw  | 0x0 |             Clear Status Counters             |
|  4 |diff_encoder_loopback|  rw  | 0x0 |Differential Encoder -> Decoder Loopback Enable|

#### ptt field

<p>0 -&gt; PTT Disabled
1 -&gt; PTT Enabled</p>

#### loopback_ena field

<p>0 -&gt; Modem loopback disabled</p>
<p>1 -&gt; Modem loopback enabled</p>

#### rx_invert field

<p>0 -&gt; Rx data normal
1 -&gt; Rx data inverted</p>

#### clear_counts field

<p>Clear Tx Bit Counter and Tx Enable Counter</p>

#### diff_encoder_loopback field

<p>0 -&gt; Differential Encoder -&gt; Decoder loopback disabled</p>
<p>1 -&gt; Differential Encoder -&gt; Decoder loopback enabled</p>

### MSK_Status register

- Absolute Address: 0x10
- Base Offset: 0x10
- Size: 0x4

<p>Modem status bits</p>

|Bits|   Identifier  |Access|Reset|                    Name                   |
|----|---------------|------|-----|-------------------------------------------|
|  0 |demod_sync_lock|   r  | 0x0 |          Demodulator Sync Status          |
|  1 |   tx_enable   |   r  | 0x0 |AD9363 DAC Interface Tx Enable Input Active|
|  2 |   rx_enable   |   r  | 0x0 |AD9363 ADC Interface Rx Enable Input Active|
|  3 | tx_axis_valid |   r  | 0x0 |              Tx S_AXIS_VALID              |

#### demod_sync_lock field

<p>Demodulator Sync Status - not currently implemented</p>

#### tx_enable field

<p>1 -&gt; Data to DAC Enabled</p>
<p>0 -&gt; Data to DAC Disabled</p>

#### rx_enable field

<p>1 -&gt; Data from ADC Enabled</p>
<p>0 -&gt; Data from ADC Disabled</p>

#### tx_axis_valid field

<p>1 -&gt; S_AXIS_VALID Enabled</p>
<p>0 -&gt; S_AXIS_VALID Disabled</p>

### Tx_Bit_Count register

- Absolute Address: 0x14
- Base Offset: 0x14
- Size: 0x4

<p>Modem status data</p>

|Bits|Identifier|Access|Reset|    Name    |
|----|----------|------|-----|------------|
|31:0|   data   |  rw  | 0x0 |Tx Bit Count|

#### data field

<p>Count of data requests made by modem</p>
<p>This register is write-to-capture.</p>
<p>To read data the following steps are required:</p>
<p>1 - Write any value to this register to capture read data</p>
<p>2 - Read the register</p>

### Tx_Enable_Count register

- Absolute Address: 0x18
- Base Offset: 0x18
- Size: 0x4

<p>Modem status data</p>

|Bits|Identifier|Access|Reset|      Name     |
|----|----------|------|-----|---------------|
|31:0|   data   |  rw  | 0x0 |Tx Enable Count|

#### data field

<p>Number of clocks on which Tx Enable is active</p>
<p>This register is write-to-capture.</p>
<p>To read data the following steps are required:</p>
<p>1 - Write any value to this register to capture read data</p>
<p>2 - Read the register</p>

### Fb_FreqWord register

- Absolute Address: 0x1C
- Base Offset: 0x1C
- Size: 0x4

<p>Set Modem Data Rate</p>

|Bits| Identifier|Access|Reset|         Name         |
|----|-----------|------|-----|----------------------|
|31:0|config_data|  rw  | 0x0 |Frequency Control Word|

#### config_data field

<p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, 
where Fn is the desired NCO frequency, and Fs is the NCO sample rate</p>

### TX_F1_FreqWord register

- Absolute Address: 0x20
- Base Offset: 0x20
- Size: 0x4

<p>Set Modulator F1 Frequency</p>

|Bits| Identifier|Access|Reset|         Name         |
|----|-----------|------|-----|----------------------|
|31:0|config_data|  rw  | 0x0 |Frequency Control Word|

#### config_data field

<p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, 
where Fn is the desired NCO frequency, and Fs is the NCO sample rate</p>

### TX_F2_FreqWord register

- Absolute Address: 0x24
- Base Offset: 0x24
- Size: 0x4

<p>Set Modulator F2 Frequency</p>

|Bits| Identifier|Access|Reset|         Name         |
|----|-----------|------|-----|----------------------|
|31:0|config_data|  rw  | 0x0 |Frequency Control Word|

#### config_data field

<p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, 
where Fn is the desired NCO frequency, and Fs is the NCO sample rate</p>

### RX_F1_FreqWord register

- Absolute Address: 0x28
- Base Offset: 0x28
- Size: 0x4

<p>Set Demodulator F1 Frequency</p>

|Bits| Identifier|Access|Reset|         Name         |
|----|-----------|------|-----|----------------------|
|31:0|config_data|  rw  | 0x0 |Frequency Control Word|

#### config_data field

<p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, 
where Fn is the desired NCO frequency, and Fs is the NCO sample rate</p>

### RX_F2_FreqWord register

- Absolute Address: 0x2C
- Base Offset: 0x2C
- Size: 0x4

<p>Set Demodulator F2 Frequency</p>

|Bits| Identifier|Access|Reset|         Name         |
|----|-----------|------|-----|----------------------|
|31:0|config_data|  rw  | 0x0 |Frequency Control Word|

#### config_data field

<p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, 
where Fn is the desired NCO frequency, and Fs is the NCO sample rate</p>

### LPF_Config_0 register

- Absolute Address: 0x30
- Base Offset: 0x30
- Size: 0x4

<p>Configure PI controller and low-pass filter</p>

|Bits|  Identifier |Access|Reset|                 Name                 |
|----|-------------|------|-----|--------------------------------------|
|  0 |  lpf_freeze |  rw  | 0x0 |Freeze the accumulator's current value|
|  1 |   lpf_zero  |  rw  | 0x0 |    Hold the PI Accumulator at zero   |
| 7:2|prbs_reserved|  rw  | 0x0 |               Reserved               |
|31:8|  lpf_alpha  |  rw  | 0x0 |       Lowpass IIR filter alpha       |

#### lpf_freeze field

<p>0 -&gt; Normal operation</p>
<p>1 -&gt; Freeze current value</p>

#### lpf_zero field

<p>0 -&gt; Normal operation</p>
<p>1 -&gt; Zero and hold accumulator</p>

#### lpf_alpha field

<p>Value controls the filter rolloff</p>

### LPF_Config_1 register

- Absolute Address: 0x34
- Base Offset: 0x34
- Size: 0x4

<p>Configures PI Controller I-gain and divisor</p>

| Bits|Identifier|Access|Reset|          Name         |
|-----|----------|------|-----|-----------------------|
| 23:0|  i_gain  |  rw  | 0x0 |  Integral Gain Value  |
|31:24|  i_shift |  rw  | 0x0 |Integral Gain Bit Shift|

#### i_gain field

<p>Value m of 0-16,777,215 sets the integral multiplier</p>

#### i_shift field

<p>Value n of 0-32 sets the integral divisor as 2^-n</p>

### Tx_Data_Width register

- Absolute Address: 0x38
- Base Offset: 0x38
- Size: 0x4

<p>Set the parallel data width of the parallel-to-serial converter</p>

|Bits|Identifier|Access|Reset|             Name            |
|----|----------|------|-----|-----------------------------|
| 7:0|data_width|  rw  | 0x8 |Modem input/output data width|

#### data_width field

<p>Set the data width of the modem input/output</p>

### Rx_Data_Width register

- Absolute Address: 0x3C
- Base Offset: 0x3C
- Size: 0x4

<p>Set the parallel data width of the serial-to-parallel converter</p>

|Bits|Identifier|Access|Reset|             Name            |
|----|----------|------|-----|-----------------------------|
| 7:0|data_width|  rw  | 0x8 |Modem input/output data width|

#### data_width field

<p>Set the data width of the modem input/output</p>

### PRBS_Control register

- Absolute Address: 0x40
- Base Offset: 0x40
- Size: 0x4

<p>Configures operation of the PRBS Generator and Monitor</p>

| Bits|     Identifier    |Access|Reset|          Name          |
|-----|-------------------|------|-----|------------------------|
|  0  |      prbs_sel     |  rw  | 0x0 |    PRBS Data Select    |
|  1  | prbs_error_insert |   w  | 0x0 |    PRBS Error Insert   |
|  2  |     prbs_clear    |   w  | 0x0 |   PRBS Clear Counters  |
|  3  |  prbs_manual_sync |   w  | 0x0 |    PRBS Manual Sync    |
| 15:4|   prbs_reserved   |  rw  | 0x0 |        Reserved        |
|31:16|prbs_sync_threshold|  rw  | 0x0 |PRBS Auto Sync Threshold|

#### prbs_sel field

<p>0 -&gt; Select Normal Tx Data
1 -&gt; Select PRBS Tx Data</p>

#### prbs_error_insert field

<p>0 -&gt; 1 :  Insert bit error in Tx data (both Normal and PRBS)</p>
<p>1 -&gt; 0 : Insert bit error in Tx data (both Normal and PRBS)</p>

#### prbs_clear field

<p>0 -&gt; 1 : Clear PRBS Counters</p>
<p>1 -&gt; 0 : Clear PRBS Counters</p>

#### prbs_manual_sync field

<p>0 -&gt; 1 : Synchronize PRBS monitor</p>
<p>1 -&gt; 0 : Synchronize PRBS monitor</p>

#### prbs_sync_threshold field

<p>0 : Auto Sync Disabled</p>
<p>N &gt; 0 : Auto sync after N errors</p>

### PRBS_Initial_State register

- Absolute Address: 0x44
- Base Offset: 0x44
- Size: 0x4

<p>PRBS Initial State</p>

|Bits| Identifier|Access|Reset|   Name  |
|----|-----------|------|-----|---------|
|31:0|config_data|  rw  | 0x0 |PRBS Seed|

#### config_data field

<p>Sets the starting value of the PRBS generator</p>

### PRBS_Polynomial register

- Absolute Address: 0x48
- Base Offset: 0x48
- Size: 0x4

<p>PRBS Polynomial</p>

|Bits| Identifier|Access|Reset|      Name     |
|----|-----------|------|-----|---------------|
|31:0|config_data|  rw  | 0x0 |PRBS Polynomial|

#### config_data field

<p>Bit positions set to '1' indicate polynomial feedback positions</p>

### PRBS_Error_Mask register

- Absolute Address: 0x4C
- Base Offset: 0x4C
- Size: 0x4

<p>PRBS Error Mask</p>

|Bits| Identifier|Access|Reset|      Name     |
|----|-----------|------|-----|---------------|
|31:0|config_data|  rw  | 0x0 |PRBS Error Mask|

#### config_data field

<p>Bit positions set to '1' indicate bits that are inverted when a bit error is inserted</p>

### PRBS_Bit_Count register

- Absolute Address: 0x50
- Base Offset: 0x50
- Size: 0x4

<p>PRBS Bits Received</p>

|Bits|Identifier|Access|Reset|       Name       |
|----|----------|------|-----|------------------|
|31:0|   data   |  rw  | 0x0 |PRBS Bits Received|

#### data field

<p>Number of bits received by the PRBS monitor since last
BER can be calculated as the ratio of received bits to errored-bits</p>
<p>This register is write-to-capture.</p>
<p>To read data the following steps are required:</p>
<p>1 - Write any value to this register to capture read data</p>
<p>2 - Read the register</p>

### PRBS_Error_Count register

- Absolute Address: 0x54
- Base Offset: 0x54
- Size: 0x4

<p>PRBS Bit Errors</p>

|Bits|Identifier|Access|Reset|      Name     |
|----|----------|------|-----|---------------|
|31:0|   data   |  rw  | 0x0 |PRBS Bit Errors|

#### data field

<p>Number of errored-bits received by the PRBS monitor since last sync
BER can be calculated as the ratio of received bits to errored-bits</p>
<p>This register is write-to-capture.</p>
<p>To read data the following steps are required:</p>
<p>1 - Write any value to this register to capture read data</p>
<p>2 - Read the register</p>

### LPF_Accum_F1 register

- Absolute Address: 0x58
- Base Offset: 0x58
- Size: 0x4

<p>Value of the F1 PI Controller Accumulator</p>

|Bits|Identifier|Access|Reset|              Name             |
|----|----------|------|-----|-------------------------------|
|31:0|   data   |  rw  | 0x0 |PI Controller Accumulator Value|

#### data field

<p>PI Controller Accumulator Value</p>
<p>This register is write-to-capture.</p>
<p>To read data the following steps are required:</p>
<p>1 - Write any value to this register to capture read data</p>
<p>2 - Read the register</p>

### LPF_Accum_F2 register

- Absolute Address: 0x5C
- Base Offset: 0x5C
- Size: 0x4

<p>Value of the F2 PI Controller Accumulator</p>

|Bits|Identifier|Access|Reset|              Name             |
|----|----------|------|-----|-------------------------------|
|31:0|   data   |  rw  | 0x0 |PI Controller Accumulator Value|

#### data field

<p>PI Controller Accumulator Value</p>
<p>This register is write-to-capture.</p>
<p>To read data the following steps are required:</p>
<p>1 - Write any value to this register to capture read data</p>
<p>2 - Read the register</p>

### axis_xfer_count register

- Absolute Address: 0x60
- Base Offset: 0x60
- Size: 0x4

<p>Modem status data</p>

|Bits|Identifier|Access|Reset|      Name      |
|----|----------|------|-----|----------------|
|31:0|   data   |  rw  | 0x0 |S_AXIS Transfers|

#### data field

<p>Number completed S_AXIS transfers</p>
<p>This register is write-to-capture.</p>
<p>To read data the following steps are required:</p>
<p>1 - Write any value to this register to capture read data</p>
<p>2 - Read the register</p>

### Rx_Sample_Discard register

- Absolute Address: 0x64
- Base Offset: 0x64
- Size: 0x4

<p>Configure samples discard operation for demodulator</p>

|Bits|    Identifier   |Access|Reset|            Name           |
|----|-----------------|------|-----|---------------------------|
| 7:0|rx_sample_discard|  rw  | 0x0 |  Rx Sample Discard Value  |
|15:8|  rx_nco_discard |  rw  | 0x0 |Rx NCO Sample Discard Value|

#### rx_sample_discard field

<p>Number of Rx samples to discard</p>

#### rx_nco_discard field

<p>Number of NCO samples to discard</p>

### LPF_Config_2 register

- Absolute Address: 0x68
- Base Offset: 0x68
- Size: 0x4

<p>Configures PI Controller I-gain and divisor</p>

| Bits|Identifier|Access|Reset|            Name           |
|-----|----------|------|-----|---------------------------|
| 23:0|  p_gain  |  rw  | 0x0 |  Proportional Gain Value  |
|31:24|  p_shift |  rw  | 0x0 |Proportional Gain Bit Shift|

#### p_gain field

<p>Value m of 0-16,777,215 sets the proportional multiplier</p>

#### p_shift field

<p>Value n of 0-32 sets the proportional divisor as 2^-n</p>

### f1_nco_adjust register

- Absolute Address: 0x6C
- Base Offset: 0x6C
- Size: 0x4

<p>Status Register</p>

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  | 0x0 |  — |

#### data field

<p>Frequency offet applied to the F1 NCO</p>
<p>This register is write-to-capture.</p>
<p>To read data the following steps are required:</p>
<p>1 - Write any value to this register to capture read data</p>
<p>2 - Read the register</p>

### f2_nco_adjust register

- Absolute Address: 0x70
- Base Offset: 0x70
- Size: 0x4

<p>Status Register</p>

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  | 0x0 |  — |

#### data field

<p>Frequency offet applied to the F2 NCO</p>
<p>This register is write-to-capture.</p>
<p>To read data the following steps are required:</p>
<p>1 - Write any value to this register to capture read data</p>
<p>2 - Read the register</p>

### f1_error register

- Absolute Address: 0x74
- Base Offset: 0x74
- Size: 0x4

<p>Status Register</p>

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  | 0x0 |  — |

#### data field

<p>Error value of the F1 Costas loop after each active bit period</p>
<p>This register is write-to-capture.</p>
<p>To read data the following steps are required:</p>
<p>1 - Write any value to this register to capture read data</p>
<p>2 - Read the register</p>

### f2_error register

- Absolute Address: 0x78
- Base Offset: 0x78
- Size: 0x4

<p>Status Register</p>

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  | 0x0 |  — |

#### data field

<p>Error value of the F2 Costas loop after each active bit period</p>
<p>This register is write-to-capture.</p>
<p>To read data the following steps are required:</p>
<p>1 - Write any value to this register to capture read data</p>
<p>2 - Read the register</p>

### Tx_Sync_Ctrl register

- Absolute Address: 0x7C
- Base Offset: 0x7C
- Size: 0x4

<p>Provides control bits for generation of transmitter synchronization patterns</p>

|Bits|  Identifier |Access|Reset|     Name     |
|----|-------------|------|-----|--------------|
|  0 | tx_sync_ena |  rw  | 0x0 |Tx Sync Enable|
|  1 |tx_sync_force|  rw  | 0x0 | Tx Sync Force|

#### tx_sync_ena field

<p>0 : Disable sync transmission</p>
<p>1 : Enable sync transmission when PTT is asserted</p>

#### tx_sync_force field

<p>0 : Normal operation</p>
<p>1 : Continuously transmit synchronization pattern</p>

### Tx_Sync_Cnt register

- Absolute Address: 0x80
- Base Offset: 0x80
- Size: 0x4

<p>Sets the duration of the synchronization tones when enabled</p>

|Bits| Identifier|Access|Reset|      Name      |
|----|-----------|------|-----|----------------|
|23:0|tx_sync_cnt|  rw  | 0x0 |Tx sync duration|

#### tx_sync_cnt field

<p>Value from 0x00_0000 to 0xFF_FFFF. </p>
<p>This value represents the number bit-times the synchronization signal should be sent after PTT is asserted.</p>

### lowpass_ema_alpha1 register

- Absolute Address: 0x84
- Base Offset: 0x84
- Size: 0x4

<p>Sets the alpha for the EMA</p>

|Bits|Identifier|Access|Reset|   Name  |
|----|----------|------|-----|---------|
|17:0|   alpha  |  rw  | 0x0 |EMA alpha|

#### alpha field

<p>Value from 0x0_0000 to 0x3_FFFF represent the EMA alpha</p>

### lowpass_ema_alpha2 register

- Absolute Address: 0x88
- Base Offset: 0x88
- Size: 0x4

<p>Sets the alpha for the EMA</p>

|Bits|Identifier|Access|Reset|   Name  |
|----|----------|------|-----|---------|
|17:0|   alpha  |  rw  | 0x0 |EMA alpha|

#### alpha field

<p>Value from 0x0_0000 to 0x3_FFFF represent the EMA alpha</p>

### rx_power register

- Absolute Address: 0x8C
- Base Offset: 0x8C
- Size: 0x4

<p>Receive power computed from I/Q samples</p>

|Bits|Identifier|Access|Reset|     Name    |
|----|----------|------|-----|-------------|
|22:0|   data   |  rw  | 0x0 |Receive Power|

#### data field

<p>Value that represent the RMS power of the incoming signal (I-channel)</p>
<p>This register is write-to-capture. To read data the following steps are required:</p>
<ol type="1">
<li> Write any value to this register to capture read data
</li><li> Read the register
</li></ol>

### tx_async_fifo_rd_wr_ptr register

- Absolute Address: 0x90
- Base Offset: 0x90
- Size: 0x4

<p>Tx async FIFO read and write pointers</p>

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  | 0x0 |  — |

#### data field

<p>Read and Write Pointers</p>
<p><code>
Bits 31:16 - write pointer (12-bits)
Bits 15:00 - read pointer (12-bits)</code></p>
<p>This register is write-to-capture. To read data the following steps are required:</p>
<ol type="1">
<li> Write any value to this register to capture read data
</li><li> Read the register
</li></ol>

### rx_async_fifo_rd_wr_ptr register

- Absolute Address: 0x94
- Base Offset: 0x94
- Size: 0x4

<p>Rx async FIFO read and write pointers</p>

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  | 0x0 |  — |

#### data field

<p>Read and Write Pointers</p>
<p><code>
Bits 31:16 - write pointer (12-bits)
Bits 15:00 - read pointer (12-bits)</code></p>
<p>This register is write-to-capture. To read data the following steps are required:</p>
<ol type="1">
<li> Write any value to this register to capture read data
</li><li> Read the register
</li></ol>
