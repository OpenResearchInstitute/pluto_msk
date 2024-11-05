// Generated by PeakRDL-cheader - A free and open-source header generator
//  https://github.com/SystemRDL/PeakRDL-cheader

#ifndef MSK_TOP_REGS_H
#define MSK_TOP_REGS_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <assert.h>

// Reg - msk_hash_lo
#define MSK_HASH_LO__HASH_ID_LO_bm 0xffffffff
#define MSK_HASH_LO__HASH_ID_LO_bp 0
#define MSK_HASH_LO__HASH_ID_LO_bw 32
#define MSK_HASH_LO__HASH_ID_LO_reset 0xaaaa5555

// Reg - msk_hash_hi
#define MSK_HASH_HI__HASH_ID_HI_bm 0xffffffff
#define MSK_HASH_HI__HASH_ID_HI_bp 0
#define MSK_HASH_HI__HASH_ID_HI_bw 32
#define MSK_HASH_HI__HASH_ID_HI_reset 0x5555aaaa

// Reg - msk_init
#define MSK_INIT__INIT_bm 0x1
#define MSK_INIT__INIT_bp 0
#define MSK_INIT__INIT_bw 1
#define MSK_INIT__INIT_reset 0x1

// Reg - msk_ctrl
#define MSK_CTRL__PTT_bm 0x1
#define MSK_CTRL__PTT_bp 0
#define MSK_CTRL__PTT_bw 1
#define MSK_CTRL__PTT_reset 0x0
#define MSK_CTRL__LOOPBACK_ENA_bm 0x2
#define MSK_CTRL__LOOPBACK_ENA_bp 1
#define MSK_CTRL__LOOPBACK_ENA_bw 1
#define MSK_CTRL__LOOPBACK_ENA_reset 0x0
#define MSK_CTRL__RX_INVERT_bm 0x4
#define MSK_CTRL__RX_INVERT_bp 2
#define MSK_CTRL__RX_INVERT_bw 1
#define MSK_CTRL__RX_INVERT_reset 0x0
#define MSK_CTRL__CLEAR_COUNTS_bm 0x8
#define MSK_CTRL__CLEAR_COUNTS_bp 3
#define MSK_CTRL__CLEAR_COUNTS_bw 1
#define MSK_CTRL__CLEAR_COUNTS_reset 0x0

// Reg - msk_stat_0
#define MSK_STAT_0__DEMOD_SYNC_LOCK_bm 0x1
#define MSK_STAT_0__DEMOD_SYNC_LOCK_bp 0
#define MSK_STAT_0__DEMOD_SYNC_LOCK_bw 1
#define MSK_STAT_0__DEMOD_SYNC_LOCK_reset 0x0
#define MSK_STAT_0__TX_ENABLE_bm 0x2
#define MSK_STAT_0__TX_ENABLE_bp 1
#define MSK_STAT_0__TX_ENABLE_bw 1
#define MSK_STAT_0__TX_ENABLE_reset 0x0
#define MSK_STAT_0__RX_ENABLE_bm 0x4
#define MSK_STAT_0__RX_ENABLE_bp 2
#define MSK_STAT_0__RX_ENABLE_bw 1
#define MSK_STAT_0__RX_ENABLE_reset 0x0
#define MSK_STAT_0__TX_AXIS_VALID_bm 0x8
#define MSK_STAT_0__TX_AXIS_VALID_bp 3
#define MSK_STAT_0__TX_AXIS_VALID_bw 1
#define MSK_STAT_0__TX_AXIS_VALID_reset 0x0

// Reg - msk_stat_1
#define MSK_STAT_1__TX_BIT_COUNTER_bm 0xffffffff
#define MSK_STAT_1__TX_BIT_COUNTER_bp 0
#define MSK_STAT_1__TX_BIT_COUNTER_bw 32
#define MSK_STAT_1__TX_BIT_COUNTER_reset 0x0

// Reg - msk_stat_2
#define MSK_STAT_2__TX_ENA_COUNTER_bm 0xffffffff
#define MSK_STAT_2__TX_ENA_COUNTER_bp 0
#define MSK_STAT_2__TX_ENA_COUNTER_bw 32
#define MSK_STAT_2__TX_ENA_COUNTER_reset 0x0

// Reg - config_nco_fw_desc_c4924cc6_name_0c494469
#define CONFIG_NCO_FW_DESC_C4924CC6_NAME_0C494469__CONFIG_DATA_bm 0xffffffff
#define CONFIG_NCO_FW_DESC_C4924CC6_NAME_0C494469__CONFIG_DATA_bp 0
#define CONFIG_NCO_FW_DESC_C4924CC6_NAME_0C494469__CONFIG_DATA_bw 32
#define CONFIG_NCO_FW_DESC_C4924CC6_NAME_0C494469__CONFIG_DATA_reset 0x0

// Reg - config_nco_fw_desc_94d7aaf5_name_84dd0c1c
#define CONFIG_NCO_FW_DESC_94D7AAF5_NAME_84DD0C1C__CONFIG_DATA_bm 0xffffffff
#define CONFIG_NCO_FW_DESC_94D7AAF5_NAME_84DD0C1C__CONFIG_DATA_bp 0
#define CONFIG_NCO_FW_DESC_94D7AAF5_NAME_84DD0C1C__CONFIG_DATA_bw 32
#define CONFIG_NCO_FW_DESC_94D7AAF5_NAME_84DD0C1C__CONFIG_DATA_reset 0x0

// Reg - config_nco_fw_desc_42134a4f_name_d97dbd51
#define CONFIG_NCO_FW_DESC_42134A4F_NAME_D97DBD51__CONFIG_DATA_bm 0xffffffff
#define CONFIG_NCO_FW_DESC_42134A4F_NAME_D97DBD51__CONFIG_DATA_bp 0
#define CONFIG_NCO_FW_DESC_42134A4F_NAME_D97DBD51__CONFIG_DATA_bw 32
#define CONFIG_NCO_FW_DESC_42134A4F_NAME_D97DBD51__CONFIG_DATA_reset 0x0

// Reg - config_nco_fw_desc_16fb48c8_name_8d01a20d
#define CONFIG_NCO_FW_DESC_16FB48C8_NAME_8D01A20D__CONFIG_DATA_bm 0xffffffff
#define CONFIG_NCO_FW_DESC_16FB48C8_NAME_8D01A20D__CONFIG_DATA_bp 0
#define CONFIG_NCO_FW_DESC_16FB48C8_NAME_8D01A20D__CONFIG_DATA_bw 32
#define CONFIG_NCO_FW_DESC_16FB48C8_NAME_8D01A20D__CONFIG_DATA_reset 0x0

// Reg - config_nco_fw_desc_43c0828f_name_bdc60ecf
#define CONFIG_NCO_FW_DESC_43C0828F_NAME_BDC60ECF__CONFIG_DATA_bm 0xffffffff
#define CONFIG_NCO_FW_DESC_43C0828F_NAME_BDC60ECF__CONFIG_DATA_bp 0
#define CONFIG_NCO_FW_DESC_43C0828F_NAME_BDC60ECF__CONFIG_DATA_bw 32
#define CONFIG_NCO_FW_DESC_43C0828F_NAME_BDC60ECF__CONFIG_DATA_reset 0x0

// Reg - lpf_config_0
#define LPF_CONFIG_0__LPF_FREEZE_bm 0x1
#define LPF_CONFIG_0__LPF_FREEZE_bp 0
#define LPF_CONFIG_0__LPF_FREEZE_bw 1
#define LPF_CONFIG_0__LPF_FREEZE_reset 0x0
#define LPF_CONFIG_0__LPF_ZERO_bm 0x2
#define LPF_CONFIG_0__LPF_ZERO_bp 1
#define LPF_CONFIG_0__LPF_ZERO_bw 1
#define LPF_CONFIG_0__LPF_ZERO_reset 0x0
#define LPF_CONFIG_0__PRBS_RESERVED_bm 0xfffc
#define LPF_CONFIG_0__PRBS_RESERVED_bp 2
#define LPF_CONFIG_0__PRBS_RESERVED_bw 14
#define LPF_CONFIG_0__PRBS_RESERVED_reset 0x0
#define LPF_CONFIG_0__LPF_ALPHA_bm 0xffff0000
#define LPF_CONFIG_0__LPF_ALPHA_bp 16
#define LPF_CONFIG_0__LPF_ALPHA_bw 16
#define LPF_CONFIG_0__LPF_ALPHA_reset 0x0

// Reg - lpf_config_1
#define LPF_CONFIG_1__I_GAIN_bm 0xffff
#define LPF_CONFIG_1__I_GAIN_bp 0
#define LPF_CONFIG_1__I_GAIN_bw 16
#define LPF_CONFIG_1__I_GAIN_reset 0x0
#define LPF_CONFIG_1__P_GAIN_bm 0xffff0000
#define LPF_CONFIG_1__P_GAIN_bp 16
#define LPF_CONFIG_1__P_GAIN_bw 16
#define LPF_CONFIG_1__P_GAIN_reset 0x0

// Reg - data_width_desc_58c848dd_name_2fbd8eba
#define DATA_WIDTH_DESC_58C848DD_NAME_2FBD8EBA__DATA_WIDTH_bm 0xff
#define DATA_WIDTH_DESC_58C848DD_NAME_2FBD8EBA__DATA_WIDTH_bp 0
#define DATA_WIDTH_DESC_58C848DD_NAME_2FBD8EBA__DATA_WIDTH_bw 8
#define DATA_WIDTH_DESC_58C848DD_NAME_2FBD8EBA__DATA_WIDTH_reset 0x8

// Reg - data_width_desc_6097df38_name_4609588b
#define DATA_WIDTH_DESC_6097DF38_NAME_4609588B__DATA_WIDTH_bm 0xff
#define DATA_WIDTH_DESC_6097DF38_NAME_4609588B__DATA_WIDTH_bp 0
#define DATA_WIDTH_DESC_6097DF38_NAME_4609588B__DATA_WIDTH_bw 8
#define DATA_WIDTH_DESC_6097DF38_NAME_4609588B__DATA_WIDTH_reset 0x8

// Reg - prbs_ctrl
#define PRBS_CTRL__PRBS_SEL_bm 0x1
#define PRBS_CTRL__PRBS_SEL_bp 0
#define PRBS_CTRL__PRBS_SEL_bw 1
#define PRBS_CTRL__PRBS_SEL_reset 0x0
#define PRBS_CTRL__PRBS_ERROR_INSERT_bm 0x2
#define PRBS_CTRL__PRBS_ERROR_INSERT_bp 1
#define PRBS_CTRL__PRBS_ERROR_INSERT_bw 1
#define PRBS_CTRL__PRBS_ERROR_INSERT_reset 0x0
#define PRBS_CTRL__PRBS_CLEAR_bm 0x4
#define PRBS_CTRL__PRBS_CLEAR_bp 2
#define PRBS_CTRL__PRBS_CLEAR_bw 1
#define PRBS_CTRL__PRBS_CLEAR_reset 0x0
#define PRBS_CTRL__PRBS_MANUAL_SYNC_bm 0x8
#define PRBS_CTRL__PRBS_MANUAL_SYNC_bp 3
#define PRBS_CTRL__PRBS_MANUAL_SYNC_bw 1
#define PRBS_CTRL__PRBS_MANUAL_SYNC_reset 0x0
#define PRBS_CTRL__PRBS_RESERVED_bm 0xfff0
#define PRBS_CTRL__PRBS_RESERVED_bp 4
#define PRBS_CTRL__PRBS_RESERVED_bw 12
#define PRBS_CTRL__PRBS_RESERVED_reset 0x0
#define PRBS_CTRL__PRBS_SYNC_THRESHOLD_bm 0xffff0000
#define PRBS_CTRL__PRBS_SYNC_THRESHOLD_bp 16
#define PRBS_CTRL__PRBS_SYNC_THRESHOLD_bw 16
#define PRBS_CTRL__PRBS_SYNC_THRESHOLD_reset 0x0

// Reg - config_prbs_seed
#define CONFIG_PRBS_SEED__CONFIG_DATA_bm 0xffffffff
#define CONFIG_PRBS_SEED__CONFIG_DATA_bp 0
#define CONFIG_PRBS_SEED__CONFIG_DATA_bw 32
#define CONFIG_PRBS_SEED__CONFIG_DATA_reset 0x0

// Reg - config_prbs_poly
#define CONFIG_PRBS_POLY__CONFIG_DATA_bm 0xffffffff
#define CONFIG_PRBS_POLY__CONFIG_DATA_bp 0
#define CONFIG_PRBS_POLY__CONFIG_DATA_bw 32
#define CONFIG_PRBS_POLY__CONFIG_DATA_reset 0x0

// Reg - config_prbs_errmask
#define CONFIG_PRBS_ERRMASK__CONFIG_DATA_bm 0xffffffff
#define CONFIG_PRBS_ERRMASK__CONFIG_DATA_bp 0
#define CONFIG_PRBS_ERRMASK__CONFIG_DATA_bw 32
#define CONFIG_PRBS_ERRMASK__CONFIG_DATA_reset 0x0

// Reg - stat_32_bits
#define STAT_32_BITS__STATUS_DATA_bm 0xffffffff
#define STAT_32_BITS__STATUS_DATA_bp 0
#define STAT_32_BITS__STATUS_DATA_bw 32
#define STAT_32_BITS__STATUS_DATA_reset 0x0

// Reg - stat_32_errs
#define STAT_32_ERRS__STATUS_DATA_bm 0xffffffff
#define STAT_32_ERRS__STATUS_DATA_bp 0
#define STAT_32_ERRS__STATUS_DATA_bw 32
#define STAT_32_ERRS__STATUS_DATA_reset 0x0

// Reg - stat_32_lpf_acc_desc_8cebc7dc_name_f20c6670
#define STAT_32_LPF_ACC_DESC_8CEBC7DC_NAME_F20C6670__STATUS_DATA_bm 0xffffffff
#define STAT_32_LPF_ACC_DESC_8CEBC7DC_NAME_F20C6670__STATUS_DATA_bp 0
#define STAT_32_LPF_ACC_DESC_8CEBC7DC_NAME_F20C6670__STATUS_DATA_bw 32
#define STAT_32_LPF_ACC_DESC_8CEBC7DC_NAME_F20C6670__STATUS_DATA_reset 0x0

// Reg - stat_32_lpf_acc_desc_dea6bd99_name_758fd0ce
#define STAT_32_LPF_ACC_DESC_DEA6BD99_NAME_758FD0CE__STATUS_DATA_bm 0xffffffff
#define STAT_32_LPF_ACC_DESC_DEA6BD99_NAME_758FD0CE__STATUS_DATA_bp 0
#define STAT_32_LPF_ACC_DESC_DEA6BD99_NAME_758FD0CE__STATUS_DATA_bw 32
#define STAT_32_LPF_ACC_DESC_DEA6BD99_NAME_758FD0CE__STATUS_DATA_reset 0x0

// Reg - msk_stat_3
#define MSK_STAT_3__XFER_COUNT_bm 0xffffffff
#define MSK_STAT_3__XFER_COUNT_bp 0
#define MSK_STAT_3__XFER_COUNT_bw 32
#define MSK_STAT_3__XFER_COUNT_reset 0x0

// Reg - rx_sample_discard
#define RX_SAMPLE_DISCARD__RX_SAMPLE_DISCARD_bm 0xff
#define RX_SAMPLE_DISCARD__RX_SAMPLE_DISCARD_bp 0
#define RX_SAMPLE_DISCARD__RX_SAMPLE_DISCARD_bw 8
#define RX_SAMPLE_DISCARD__RX_SAMPLE_DISCARD_reset 0x0
#define RX_SAMPLE_DISCARD__RX_NCO_DISCARD_bm 0xff00
#define RX_SAMPLE_DISCARD__RX_NCO_DISCARD_bp 8
#define RX_SAMPLE_DISCARD__RX_NCO_DISCARD_bw 8
#define RX_SAMPLE_DISCARD__RX_NCO_DISCARD_reset 0x0

// Addrmap - msk_top_regs
typedef struct __attribute__ ((__packed__)) {
    uint32_t Hash_ID_Low;
    uint32_t Hash_ID_High;
    uint32_t MSK_Init;
    uint32_t MSK_Control;
    uint32_t MSK_Status;
    uint32_t Tx_Bit_Count;
    uint32_t Tx_Enable_Count;
    uint32_t Fb_FreqWord;
    uint32_t TX_F1_FreqWord;
    uint32_t TX_F2_FreqWord;
    uint32_t RX_F1_FreqWord;
    uint32_t RX_F2_FreqWord;
    uint32_t LPF_Config_0;
    uint32_t LPF_Config_1;
    uint32_t Tx_Data_Width;
    uint32_t Rx_Data_Width;
    uint32_t PRBS_Control;
    uint32_t PRBS_Initial_State;
    uint32_t PRBS_Polynomial;
    uint32_t PRBS_Error_Mask;
    uint32_t PRBS_Bit_Count;
    uint32_t PRBS_Error_Count;
    uint32_t LPF_Accum_F1;
    uint32_t LPF_Accum_F2;
    uint32_t axis_xfer_count;
    uint32_t Rx_Sample_Discard;
} msk_top_regs_t;

// Addrmap - Pluto_MSK_Modem
typedef struct __attribute__ ((__packed__)) {
    uint8_t RESERVED_0_43bfffff[0x43c00000];
    msk_top_regs_t pluto_msk_regs;
} Pluto_MSK_Modem_t;


static_assert(sizeof(Pluto_MSK_Modem_t) == 0x43c00068, "Packing error");

#ifdef __cplusplus
}
#endif

#endif /* MSK_TOP_REGS_H */
