<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: msk_top_regs
  - msk_top_regs.rdl
-->

## msk_top_regs address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x50

<p>MSK Modem Configuration and Status Registers</p>

|Offset|    Identifier    |Name|
|------|------------------|----|
| 0x00 |    Hash_ID_Low   |  — |
| 0x04 |   Hash_ID_High   |  — |
| 0x08 |     MSK_Init     |  — |
| 0x0C |    MSK_Control   |  — |
| 0x10 |    MSK_Status    |  — |
| 0x14 |   Tx_Bit_Count   |  — |
| 0x18 |  Tx_Enable_Count |  — |
| 0x1C |    Fb_FreqWord   |  — |
| 0x20 |    F1_FreqWord   |  — |
| 0x24 |    F2_FreqWord   |  — |
| 0x28 |   LPF_Config_0   |  — |
| 0x2C |   LPF_Config_1   |  — |
| 0x30 |   Tx_Data_Width  |  — |
| 0x34 |   Rx_Data_Width  |  — |
| 0x38 |   PRBS_Control   |  — |
| 0x3C |PRBS_Initial_State|  — |
| 0x40 |  PRBS_Polynomial |  — |
| 0x44 |  PRBS_Error_Mask |  — |
| 0x48 |  PRBS_Bit_Count  |  — |
| 0x4C | PRBS_Error_Count |  — |

### Hash_ID_Low register

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x4

<p>A hash generated at build time to uniquely identify FPGA builds.</p>

|Bits|Identifier|Access|   Reset  |Name|
|----|----------|------|----------|----|
|31:0|hash_id_lo|   r  |0xAAAA5555|  — |

#### hash_id_lo field

<p>Lower 32-bits of Hash ID</p>

### Hash_ID_High register

- Absolute Address: 0x4
- Base Offset: 0x4
- Size: 0x4

<p>A hash generated at build time to uniquely identify FPGA builds.</p>

|Bits|Identifier|Access|   Reset  |Name|
|----|----------|------|----------|----|
|31:0|hash_id_hi|   r  |0x5555AAAA|  — |

#### hash_id_hi field

<p>Upper 32-bits of Hash ID</p>

### MSK_Init register

- Absolute Address: 0x8
- Base Offset: 0x8
- Size: 0x4

<p>0 -&gt; Normal modem operation; 1 -&gt; Puts modem in initialization state</p>

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|  0 |   init   |  rw  | 0x1 |  — |

### MSK_Control register

- Absolute Address: 0xC
- Base Offset: 0xC
- Size: 0x4

<p>MSK Controls</p>

|Bits| Identifier |Access|Reset|Name|
|----|------------|------|-----|----|
|  0 |     ptt    |  rw  | 0x0 |  — |
|  1 |loopback_ena|  rw  | 0x0 |  — |
|  2 |  rx_invert |  rw  | 0x0 |  — |
|  3 |clear_counts|  rw  | 0x0 |  — |

#### ptt field

<p>0 -&gt; PTT Disabled; 1 -&gt; PTT Enabled</p>

#### loopback_ena field

<p>0 -&gt; Modem loopback disabled; 1 -&gt; Modem loopback enabled</p>

#### rx_invert field

<p>0 -&gt; Rx data normal; 1 -&gt; Rx data inverted</p>

#### clear_counts field

<p>Clear Tx Bit Counter and Tx Enable Counter</p>

### MSK_Status register

- Absolute Address: 0x10
- Base Offset: 0x10
- Size: 0x4

|Bits|   Identifier  |Access|Reset|Name|
|----|---------------|------|-----|----|
|  0 |demod_sync_lock|   r  | 0x0 |  — |
|  1 |   tx_enable   |   r  | 0x0 |  — |
|  2 |   rx_enable   |   r  | 0x0 |  — |

### Tx_Bit_Count register

- Absolute Address: 0x14
- Base Offset: 0x14
- Size: 0x4

|Bits|  Identifier  |Access|Reset|Name|
|----|--------------|------|-----|----|
|31:0|data_req_count|   r  | 0x0 |  — |

### Tx_Enable_Count register

- Absolute Address: 0x18
- Base Offset: 0x18
- Size: 0x4

|Bits|  Identifier  |Access|Reset|Name|
|----|--------------|------|-----|----|
|31:0|data_req_count|   r  | 0x0 |  — |

### Fb_FreqWord register

- Absolute Address: 0x1C
- Base Offset: 0x1C
- Size: 0x4

|Bits| Identifier|Access|Reset|Name|
|----|-----------|------|-----|----|
|31:0|config_data|  rw  | 0x0 |  — |

### F1_FreqWord register

- Absolute Address: 0x20
- Base Offset: 0x20
- Size: 0x4

|Bits| Identifier|Access|Reset|Name|
|----|-----------|------|-----|----|
|31:0|config_data|  rw  | 0x0 |  — |

### F2_FreqWord register

- Absolute Address: 0x24
- Base Offset: 0x24
- Size: 0x4

|Bits| Identifier|Access|Reset|Name|
|----|-----------|------|-----|----|
|31:0|config_data|  rw  | 0x0 |  — |

### LPF_Config_0 register

- Absolute Address: 0x28
- Base Offset: 0x28
- Size: 0x4

| Bits|Identifier|Access|Reset|Name|
|-----|----------|------|-----|----|
|  0  |lpf_freeze|  rw  | 0x0 |  — |
|  1  | lpf_zero |  rw  | 0x0 |  — |
|31:16| lpf_alpha|  rw  | 0x0 |  — |

### LPF_Config_1 register

- Absolute Address: 0x2C
- Base Offset: 0x2C
- Size: 0x4

| Bits|Identifier|Access|Reset|Name|
|-----|----------|------|-----|----|
| 15:0|  i_gain  |  rw  | 0x0 |  — |
|31:16|  p_gain  |  rw  | 0x0 |  — |

### Tx_Data_Width register

- Absolute Address: 0x30
- Base Offset: 0x30
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
| 7:0|data_width|  rw  | 0x8 |  — |

### Rx_Data_Width register

- Absolute Address: 0x34
- Base Offset: 0x34
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
| 7:0|data_width|  rw  | 0x8 |  — |

### PRBS_Control register

- Absolute Address: 0x38
- Base Offset: 0x38
- Size: 0x4

|Bits|    Identifier   |Access|Reset|Name|
|----|-----------------|------|-----|----|
|  0 |     prbs_sel    |  rw  | 0x0 |  — |
|  1 |prbs_error_insert|   w  | 0x0 |  — |
|  2 |    prbs_clear   |   w  | 0x0 |  — |
|  3 |    prbs_sync    |   w  | 0x0 |  — |

### PRBS_Initial_State register

- Absolute Address: 0x3C
- Base Offset: 0x3C
- Size: 0x4

|Bits| Identifier|Access|Reset|Name|
|----|-----------|------|-----|----|
|31:0|config_data|  rw  | 0x0 |  — |

### PRBS_Polynomial register

- Absolute Address: 0x40
- Base Offset: 0x40
- Size: 0x4

|Bits| Identifier|Access|Reset|Name|
|----|-----------|------|-----|----|
|31:0|config_data|  rw  | 0x0 |  — |

### PRBS_Error_Mask register

- Absolute Address: 0x44
- Base Offset: 0x44
- Size: 0x4

|Bits| Identifier|Access|Reset|Name|
|----|-----------|------|-----|----|
|31:0|config_data|  rw  | 0x0 |  — |

### PRBS_Bit_Count register

- Absolute Address: 0x48
- Base Offset: 0x48
- Size: 0x4

|Bits| Identifier|Access|Reset|Name|
|----|-----------|------|-----|----|
|31:0|status_data|   r  |  —  |  — |

### PRBS_Error_Count register

- Absolute Address: 0x4C
- Base Offset: 0x4C
- Size: 0x4

|Bits| Identifier|Access|Reset|Name|
|----|-----------|------|-----|----|
|31:0|status_data|   r  |  —  |  — |
