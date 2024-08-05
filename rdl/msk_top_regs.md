<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: Pluto_MSK_Modem
  - msk_top_regs.rdl
-->

## Pluto_MSK_Modem address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x43C00060

|  Offset  |  Identifier  |        Name       |
|----------|--------------|-------------------|
|0x43C00000|pluto_msk_regs|Pluto MSK Registers|

## pluto_msk_regs address map

- Absolute Address: 0x43C00000
- Base Offset: 0x43C00000
- Size: 0x60

<p>MSK Modem Configuration and Status Registers</p>

|Offset|    Identifier    |                             Name                            |
|------|------------------|-------------------------------------------------------------|
| 0x00 |    Hash_ID_Low   |            Pluto MSK FPGA Hash ID - Lower 32-bits           |
| 0x04 |   Hash_ID_High   |            Pluto MSK FPGA Hash ID - Upper 32-bits           |
| 0x08 |     MSK_Init     |                     MSK Modem Control 0                     |
| 0x0C |    MSK_Control   |                     MSK Modem Control 1                     |
| 0x10 |    MSK_Status    |                      MSK Modem Status 1                     |
| 0x14 |   Tx_Bit_Count   |                      MSK Modem Status 2                     |
| 0x18 |  Tx_Enable_Count |                      MSK Modem Status 3                     |
| 0x1C |    Fb_FreqWord   |              Bitrate NCO Frequency Control Word             |
| 0x20 |  TX_F1_FreqWord  |               Tx F1 NCO Frequency Control Word              |
| 0x24 |  TX_F2_FreqWord  |               Tx F2 NCO Frequency Control Word              |
| 0x28 |  RX_F1_FreqWord  |               Rx F1 NCO Frequency Control Word              |
| 0x2C |  RX_F2_FreqWord  |               Rx F2 NCO Frequency Control Word              |
| 0x30 |   LPF_Config_0   |PI Controller Configuration and Low-pass Filter Configuration|
| 0x34 |   LPF_Config_1   |PI Controller Configuration and Low-pass Filter Configuration|
| 0x38 |   Tx_Data_Width  |                  Modem Tx Input Data Width                  |
| 0x3C |   Rx_Data_Width  |                  Modem Rx Output Data Width                 |
| 0x40 |   PRBS_Control   |                        PRBS Control 0                       |
| 0x44 |PRBS_Initial_State|                        PRBS Control 1                       |
| 0x48 |  PRBS_Polynomial |                        PRBS Control 2                       |
| 0x4C |  PRBS_Error_Mask |                        PRBS Control 3                       |
| 0x50 |  PRBS_Bit_Count  |                        PRBS Status 0                        |
| 0x54 | PRBS_Error_Count |                        PRBS Status 1                        |
| 0x58 |   LPF_Accum_F1   |                 F1 PI Controller Accumulator                |
| 0x5C |   LPF_Accum_F2   |                 F2 PI Controller Accumulator                |

### Hash_ID_Low register

- Absolute Address: 0x43C00000
- Base Offset: 0x0
- Size: 0x4

|Bits|Identifier|Access|   Reset  |         Name        |
|----|----------|------|----------|---------------------|
|31:0|hash_id_lo|   r  |0xAAAA5555|Hash ID Lower 32-bits|

#### hash_id_lo field

<p>Lower 32-bits of Pluto MSK FPGA Hash ID</p>

### Hash_ID_High register

- Absolute Address: 0x43C00004
- Base Offset: 0x4
- Size: 0x4

|Bits|Identifier|Access|   Reset  |         Name        |
|----|----------|------|----------|---------------------|
|31:0|hash_id_hi|   r  |0x5555AAAA|Hash ID Upper 32-bits|

#### hash_id_hi field

<p>Upper 32-bits of Pluto MSK FPGA Hash ID</p>

### MSK_Init register

- Absolute Address: 0x43C00008
- Base Offset: 0x8
- Size: 0x4

<p>Synchronous initialization of MSK Modem functions, does not affect configuration registers.</p>

|Bits|Identifier|Access|Reset|    Name   |
|----|----------|------|-----|-----------|
|  0 |   init   |  rw  | 0x1 |Init Enable|

#### init field

<p>0 -&gt; Normal modem operation 
1 -&gt; Initialize modem</p>

### MSK_Control register

- Absolute Address: 0x43C0000C
- Base Offset: 0xC
- Size: 0x4

<p>MSK Modem Configuration and Control</p>

|Bits|  Identifier  |Access|Reset|         Name        |
|----|--------------|------|-----|---------------------|
|  0 |      ptt     |  rw  | 0x0 | Push-to-Talk Enable |
|  1 | loopback_ena |  rw  | 0x0 |Modem Loopback Enable|
|  2 |   rx_invert  |  rw  | 0x0 |Rx Data Invert Enable|
|  3 | clear_counts |  rw  | 0x0 |Clear Status Counters|
|15:8|sample_discard|  rw  | 0x0 |    Sample Discard   |

#### ptt field

<p>0 -&gt; PTT Disabled
1 -&gt; PTT Enabled</p>

#### loopback_ena field

<p>0 -&gt; Modem loopback disabled
1 -&gt; Modem loopback enabled</p>

#### rx_invert field

<p>0 -&gt; Rx data normal
1 -&gt; Rx data inverted</p>

#### clear_counts field

<p>Clear Tx Bit Counter and Tx Enable Counter</p>

#### sample_discard field

<p>Number of samples to discard</p>

### MSK_Status register

- Absolute Address: 0x43C00010
- Base Offset: 0x10
- Size: 0x4

<p>Modem status bits</p>

|Bits|   Identifier  |Access|Reset|                    Name                   |
|----|---------------|------|-----|-------------------------------------------|
|  0 |demod_sync_lock|   r  | 0x0 |          Demodulator Sync Status          |
|  1 |   tx_enable   |   r  | 0x0 |AD9363 DAC Interface Tx Enable Input Active|
|  2 |   rx_enable   |   r  | 0x0 |AD9363 ADC Interface Rx Enable Input Active|

#### demod_sync_lock field

<p>Demodulator Sync Status - not currently implemented</p>

#### tx_enable field

<p>1 -&gt; Data to DAC Enabled
0 -&gt; Data to DAC Disabled</p>

#### rx_enable field

<p>1 -&gt; Data from ADC Enabled
0 -&gt; Data from ADC Disabled</p>

### Tx_Bit_Count register

- Absolute Address: 0x43C00014
- Base Offset: 0x14
- Size: 0x4

<p>Modem status data</p>

|Bits|  Identifier  |Access|Reset|    Name    |
|----|--------------|------|-----|------------|
|31:0|data_req_count|  rw  | 0x0 |Tx Bit Count|

#### data_req_count field

<p>Count of data requests made by modem</p>

### Tx_Enable_Count register

- Absolute Address: 0x43C00018
- Base Offset: 0x18
- Size: 0x4

<p>Modem status data</p>

|Bits|  Identifier  |Access|Reset|      Name     |
|----|--------------|------|-----|---------------|
|31:0|data_req_count|  rw  | 0x0 |Tx Enable Count|

#### data_req_count field

<p>Number of clocks on which Tx Enable is active</p>

### Fb_FreqWord register

- Absolute Address: 0x43C0001C
- Base Offset: 0x1C
- Size: 0x4

<p>Set Modem Data Rate</p>

|Bits| Identifier|Access|Reset|         Name         |
|----|-----------|------|-----|----------------------|
|31:0|config_data|  rw  | 0x0 |Frequency Control Word|

#### config_data field

<p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, where Fn is the desired NCO frequency, and Fs is the NCO sample rate</p>

### TX_F1_FreqWord register

- Absolute Address: 0x43C00020
- Base Offset: 0x20
- Size: 0x4

<p>Set Modulator F1 Frequency</p>

|Bits| Identifier|Access|Reset|         Name         |
|----|-----------|------|-----|----------------------|
|31:0|config_data|  rw  | 0x0 |Frequency Control Word|

#### config_data field

<p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, where Fn is the desired NCO frequency, and Fs is the NCO sample rate</p>

### TX_F2_FreqWord register

- Absolute Address: 0x43C00024
- Base Offset: 0x24
- Size: 0x4

<p>Set Modulator F2 Frequency</p>

|Bits| Identifier|Access|Reset|         Name         |
|----|-----------|------|-----|----------------------|
|31:0|config_data|  rw  | 0x0 |Frequency Control Word|

#### config_data field

<p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, where Fn is the desired NCO frequency, and Fs is the NCO sample rate</p>

### RX_F1_FreqWord register

- Absolute Address: 0x43C00028
- Base Offset: 0x28
- Size: 0x4

<p>Set Demodulator F1 Frequency</p>

|Bits| Identifier|Access|Reset|         Name         |
|----|-----------|------|-----|----------------------|
|31:0|config_data|  rw  | 0x0 |Frequency Control Word|

#### config_data field

<p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, where Fn is the desired NCO frequency, and Fs is the NCO sample rate</p>

### RX_F2_FreqWord register

- Absolute Address: 0x43C0002C
- Base Offset: 0x2C
- Size: 0x4

<p>Set Demodulator F2 Frequency</p>

|Bits| Identifier|Access|Reset|         Name         |
|----|-----------|------|-----|----------------------|
|31:0|config_data|  rw  | 0x0 |Frequency Control Word|

#### config_data field

<p>Sets the center frequency of the NCO as FW = Fn * 2^32/Fs, where Fn is the desired NCO frequency, and Fs is the NCO sample rate</p>

### LPF_Config_0 register

- Absolute Address: 0x43C00030
- Base Offset: 0x30
- Size: 0x4

<p>Configure PI controller and low-pass filter</p>

| Bits|Identifier|Access|Reset|                 Name                 |
|-----|----------|------|-----|--------------------------------------|
|  0  |lpf_freeze|  rw  | 0x0 |Freeze the accumulator's current value|
|  1  | lpf_zero |  rw  | 0x0 |    Hold the PI Accumulator at zero   |
|31:16| lpf_alpha|  rw  | 0x0 |       Lowpass IIR filter alpha       |

#### lpf_freeze field

<p>0 -&gt; Normal operation
1 -&gt; Freeze current value</p>

#### lpf_zero field

<p>0 -&gt; Normal operation
1 -&gt; Zero and hold accumulator</p>

#### lpf_alpha field

<p>Value controls the filter rolloff</p>

### LPF_Config_1 register

- Absolute Address: 0x43C00034
- Base Offset: 0x34
- Size: 0x4

<p>Configure PI controller and low-pass filter</p>

| Bits|Identifier|Access|Reset|                           Name                           |
|-----|----------|------|-----|----------------------------------------------------------|
| 15:0|  i_gain  |  rw  | 0x0 |  Sets the integral gain of the PI controller integrator  |
|31:16|  p_gain  |  rw  | 0x0 |Sets the proportional gain of the PI controller integrator|

#### i_gain field

<p>Integral gain value</p>

#### p_gain field

<p>Proportional gain value</p>

### Tx_Data_Width register

- Absolute Address: 0x43C00038
- Base Offset: 0x38
- Size: 0x4

<p>Set the parallel data width of the parallel-to-serial converter</p>

|Bits|Identifier|Access|Reset|             Name            |
|----|----------|------|-----|-----------------------------|
| 7:0|data_width|  rw  | 0x8 |Modem input/output data width|

#### data_width field

<p>Set the data width of the modem input/output</p>

### Rx_Data_Width register

- Absolute Address: 0x43C0003C
- Base Offset: 0x3C
- Size: 0x4

<p>Set the parallel data width of the serial-to-parallel converter</p>

|Bits|Identifier|Access|Reset|             Name            |
|----|----------|------|-----|-----------------------------|
| 7:0|data_width|  rw  | 0x8 |Modem input/output data width|

#### data_width field

<p>Set the data width of the modem input/output</p>

### PRBS_Control register

- Absolute Address: 0x43C00040
- Base Offset: 0x40
- Size: 0x4

<p>Configures operation of the PRBS Generator and Monitor</p>

|Bits|    Identifier   |Access|Reset|       Name      |
|----|-----------------|------|-----|-----------------|
|  0 |     prbs_sel    |  rw  | 0x0 | PRBS Data Select|
|  1 |prbs_error_insert|   w  | 0x0 |PRBS Error Insert|
|  2 |    prbs_clear   |   w  | 0x0 |     Reserved    |
|  3 |    prbs_sync    |   w  | 0x0 |    PRBS Sync    |

#### prbs_sel field

<p>0 -&gt; Select Normal Tx Data
1 -&gt; Select PRBS Tx Data</p>

#### prbs_error_insert field

<p>0 -&gt; No error insertion
1 -&gt; Insert bit error in Tx data (both Normal and PRBS)</p>

#### prbs_clear field

<p>Reserved</p>

#### prbs_sync field

<p>0 -&gt; Normal Operation
1 -&gt; Synchronize PRBS monitor</p>

### PRBS_Initial_State register

- Absolute Address: 0x43C00044
- Base Offset: 0x44
- Size: 0x4

<p>PRBS Initial State</p>

|Bits| Identifier|Access|Reset|   Name  |
|----|-----------|------|-----|---------|
|31:0|config_data|  rw  | 0x0 |PRBS Seed|

#### config_data field

<p>Sets the starting value of the PRBS generator</p>

### PRBS_Polynomial register

- Absolute Address: 0x43C00048
- Base Offset: 0x48
- Size: 0x4

<p>PRBS Polynomial</p>

|Bits| Identifier|Access|Reset|      Name     |
|----|-----------|------|-----|---------------|
|31:0|config_data|  rw  | 0x0 |PRBS Polynomial|

#### config_data field

<p>Bit positions set to '1' indicate polynomial feedback positions</p>

### PRBS_Error_Mask register

- Absolute Address: 0x43C0004C
- Base Offset: 0x4C
- Size: 0x4

<p>PRBS Error Mask</p>

|Bits| Identifier|Access|Reset|      Name     |
|----|-----------|------|-----|---------------|
|31:0|config_data|  rw  | 0x0 |PRBS Error Mask|

#### config_data field

<p>Bit positions set to '1' indicate bits that are inverted when a bit error is inserted</p>

### PRBS_Bit_Count register

- Absolute Address: 0x43C00050
- Base Offset: 0x50
- Size: 0x4

<p>PRBS Bits Received</p>

|Bits| Identifier|Access|Reset|       Name       |
|----|-----------|------|-----|------------------|
|31:0|status_data|   r  |  —  |PRBS Bits Received|

#### status_data field

<p>Number of bits received by the PRBS monitor since last
BER can be calculated as the ratio of received bits to errored-bits</p>

### PRBS_Error_Count register

- Absolute Address: 0x43C00054
- Base Offset: 0x54
- Size: 0x4

<p>PRBS Bit Errors</p>

|Bits| Identifier|Access|Reset|      Name     |
|----|-----------|------|-----|---------------|
|31:0|status_data|   r  |  —  |PRBS Bit Errors|

#### status_data field

<p>Number of errored-bits received by the PRBS monitor since last sync
BER can be calculated as the ratio of received bits to errored-bits</p>

### LPF_Accum_F1 register

- Absolute Address: 0x43C00058
- Base Offset: 0x58
- Size: 0x4

<p>Value of the F1 PI Controller Accumulator</p>

|Bits| Identifier|Access|Reset|              Name             |
|----|-----------|------|-----|-------------------------------|
|31:0|status_data|   r  |  —  |PI Controller Accumulator Value|

#### status_data field

<p>PI Controller Accumulator Value</p>

### LPF_Accum_F2 register

- Absolute Address: 0x43C0005C
- Base Offset: 0x5C
- Size: 0x4

<p>Value of the F2 PI Controller Accumulator</p>

|Bits| Identifier|Access|Reset|              Name             |
|----|-----------|------|-----|-------------------------------|
|31:0|status_data|   r  |  —  |PI Controller Accumulator Value|

#### status_data field

<p>PI Controller Accumulator Value</p>
