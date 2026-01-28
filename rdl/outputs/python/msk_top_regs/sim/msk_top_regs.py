


"""
Python Wrapper for the msk_top_regs register model

This code was generated from the PeakRDL-python package version 2.3.0

"""





from typing import Union

from ..sim_lib.register import Register, MemoryRegister
from ..sim_lib.memory import Memory
from ..sim_lib.simulator import MemoryEntry
from ..sim_lib.field import FieldDefinition, FieldType
from ..sim_lib.simulator import AsyncSimulator as Simulator


class msk_top_regs_simulator_cls(Simulator):

    def _build_registers(self) -> dict[int, Union[list[Union[MemoryRegister, Register]], Union[MemoryRegister, Register]]]:
        return {
            0 : 
    Register(width=32, full_inst_name='msk_top_regs.Hash_ID_Low', readable=True, writable=False,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='hash_id_lo', field_type=FieldType.READONLY),
                                                ]),
            4 : 
    Register(width=32, full_inst_name='msk_top_regs.Hash_ID_High', readable=True, writable=False,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='hash_id_hi', field_type=FieldType.READONLY),
                                                ]),
            8 : 
    Register(width=32, full_inst_name='msk_top_regs.MSK_Init', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='txrxinit', field_type=FieldType.READWRITE),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='txinit', field_type=FieldType.READWRITE),FieldDefinition(high=2, low=2, msb=2, lsb=2, inst_name='rxinit', field_type=FieldType.READWRITE),
                                                ]),
            12 : 
    Register(width=32, full_inst_name='msk_top_regs.MSK_Control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='ptt', field_type=FieldType.READWRITE),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='loopback_ena', field_type=FieldType.READWRITE),FieldDefinition(high=2, low=2, msb=2, lsb=2, inst_name='rx_invert', field_type=FieldType.READWRITE),FieldDefinition(high=3, low=3, msb=3, lsb=3, inst_name='clear_counts', field_type=FieldType.READWRITE),FieldDefinition(high=4, low=4, msb=4, lsb=4, inst_name='diff_encoder_loopback', field_type=FieldType.READWRITE),
                                                ]),
            16 : 
    Register(width=32, full_inst_name='msk_top_regs.MSK_Status', readable=True, writable=False,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='demod_sync_lock', field_type=FieldType.READONLY),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='tx_enable', field_type=FieldType.READONLY),FieldDefinition(high=2, low=2, msb=2, lsb=2, inst_name='rx_enable', field_type=FieldType.READONLY),FieldDefinition(high=3, low=3, msb=3, lsb=3, inst_name='tx_axis_valid', field_type=FieldType.READONLY),
                                                ]),
            20 : 
    Register(width=32, full_inst_name='msk_top_regs.Tx_Bit_Count', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            24 : 
    Register(width=32, full_inst_name='msk_top_regs.Tx_Enable_Count', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            28 : 
    Register(width=32, full_inst_name='msk_top_regs.Fb_FreqWord', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data', field_type=FieldType.READWRITE),
                                                ]),
            32 : 
    Register(width=32, full_inst_name='msk_top_regs.TX_F1_FreqWord', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data', field_type=FieldType.READWRITE),
                                                ]),
            36 : 
    Register(width=32, full_inst_name='msk_top_regs.TX_F2_FreqWord', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data', field_type=FieldType.READWRITE),
                                                ]),
            40 : 
    Register(width=32, full_inst_name='msk_top_regs.RX_F1_FreqWord', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data', field_type=FieldType.READWRITE),
                                                ]),
            44 : 
    Register(width=32, full_inst_name='msk_top_regs.RX_F2_FreqWord', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data', field_type=FieldType.READWRITE),
                                                ]),
            48 : 
    Register(width=32, full_inst_name='msk_top_regs.LPF_Config_0', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='lpf_freeze', field_type=FieldType.READWRITE),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='lpf_zero', field_type=FieldType.READWRITE),FieldDefinition(high=7, low=2, msb=7, lsb=2, inst_name='prbs_reserved', field_type=FieldType.READWRITE),FieldDefinition(high=31, low=8, msb=31, lsb=8, inst_name='lpf_alpha', field_type=FieldType.READWRITE),
                                                ]),
            52 : 
    Register(width=32, full_inst_name='msk_top_regs.LPF_Config_1', readable=True, writable=True,
                                         fields=[FieldDefinition(high=23, low=0, msb=23, lsb=0, inst_name='i_gain', field_type=FieldType.READWRITE),FieldDefinition(high=31, low=24, msb=31, lsb=24, inst_name='i_shift', field_type=FieldType.READWRITE),
                                                ]),
            56 : 
    Register(width=32, full_inst_name='msk_top_regs.Tx_Data_Width', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='data_width', field_type=FieldType.READWRITE),
                                                ]),
            60 : 
    Register(width=32, full_inst_name='msk_top_regs.Rx_Data_Width', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='data_width', field_type=FieldType.READWRITE),
                                                ]),
            64 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='prbs_sel', field_type=FieldType.READWRITE),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='prbs_error_insert', field_type=FieldType.WRITEONLY),FieldDefinition(high=2, low=2, msb=2, lsb=2, inst_name='prbs_clear', field_type=FieldType.WRITEONLY),FieldDefinition(high=3, low=3, msb=3, lsb=3, inst_name='prbs_manual_sync', field_type=FieldType.WRITEONLY),FieldDefinition(high=15, low=4, msb=15, lsb=4, inst_name='prbs_reserved', field_type=FieldType.READWRITE),FieldDefinition(high=31, low=16, msb=31, lsb=16, inst_name='prbs_sync_threshold', field_type=FieldType.READWRITE),
                                                ]),
            68 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Initial_State', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data', field_type=FieldType.READWRITE),
                                                ]),
            72 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Polynomial', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data', field_type=FieldType.READWRITE),
                                                ]),
            76 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Error_Mask', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data', field_type=FieldType.READWRITE),
                                                ]),
            80 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Bit_Count', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            84 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Error_Count', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            88 : 
    Register(width=32, full_inst_name='msk_top_regs.LPF_Accum_F1', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            92 : 
    Register(width=32, full_inst_name='msk_top_regs.LPF_Accum_F2', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            96 : 
    Register(width=32, full_inst_name='msk_top_regs.axis_xfer_count', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            100 : 
    Register(width=32, full_inst_name='msk_top_regs.Rx_Sample_Discard', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='rx_sample_discard', field_type=FieldType.READWRITE),FieldDefinition(high=15, low=8, msb=15, lsb=8, inst_name='rx_nco_discard', field_type=FieldType.READWRITE),
                                                ]),
            104 : 
    Register(width=32, full_inst_name='msk_top_regs.LPF_Config_2', readable=True, writable=True,
                                         fields=[FieldDefinition(high=23, low=0, msb=23, lsb=0, inst_name='p_gain', field_type=FieldType.READWRITE),FieldDefinition(high=31, low=24, msb=31, lsb=24, inst_name='p_shift', field_type=FieldType.READWRITE),
                                                ]),
            108 : 
    Register(width=32, full_inst_name='msk_top_regs.f1_nco_adjust', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            112 : 
    Register(width=32, full_inst_name='msk_top_regs.f2_nco_adjust', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            116 : 
    Register(width=32, full_inst_name='msk_top_regs.f1_error', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            120 : 
    Register(width=32, full_inst_name='msk_top_regs.f2_error', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            124 : 
    Register(width=32, full_inst_name='msk_top_regs.Tx_Sync_Ctrl', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tx_sync_ena', field_type=FieldType.READWRITE),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='tx_sync_force', field_type=FieldType.READWRITE),
                                                ]),
            128 : 
    Register(width=32, full_inst_name='msk_top_regs.Tx_Sync_Cnt', readable=True, writable=True,
                                         fields=[FieldDefinition(high=23, low=0, msb=23, lsb=0, inst_name='tx_sync_cnt', field_type=FieldType.READWRITE),
                                                ]),
            132 : 
    Register(width=32, full_inst_name='msk_top_regs.lowpass_ema_alpha1', readable=True, writable=True,
                                         fields=[FieldDefinition(high=17, low=0, msb=17, lsb=0, inst_name='alpha', field_type=FieldType.READWRITE),
                                                ]),
            136 : 
    Register(width=32, full_inst_name='msk_top_regs.lowpass_ema_alpha2', readable=True, writable=True,
                                         fields=[FieldDefinition(high=17, low=0, msb=17, lsb=0, inst_name='alpha', field_type=FieldType.READWRITE),
                                                ]),
            140 : 
    Register(width=32, full_inst_name='msk_top_regs.rx_power', readable=True, writable=True,
                                         fields=[FieldDefinition(high=22, low=0, msb=22, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            144 : 
    Register(width=32, full_inst_name='msk_top_regs.tx_async_fifo_rd_wr_ptr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            148 : 
    Register(width=32, full_inst_name='msk_top_regs.rx_async_fifo_rd_wr_ptr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            152 : 
    Register(width=32, full_inst_name='msk_top_regs.rx_frame_sync_status', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='frame_sync_locked', field_type=FieldType.READONLY),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='frame_buffer_overflow', field_type=FieldType.READONLY),FieldDefinition(high=25, low=2, msb=25, lsb=2, inst_name='frames_received', field_type=FieldType.READWRITE),FieldDefinition(high=31, low=26, msb=31, lsb=26, inst_name='frame_sync_errors', field_type=FieldType.READWRITE),
                                                ]),
            156 : 
    Register(width=32, full_inst_name='msk_top_regs.symbol_lock_control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=9, low=0, msb=9, lsb=0, inst_name='symbol_lock_count', field_type=FieldType.READWRITE),FieldDefinition(high=25, low=10, msb=25, lsb=10, inst_name='symbol_lock_threshold', field_type=FieldType.READWRITE),
                                                ]),
            160 : 
    Register(width=32, full_inst_name='msk_top_regs.symbol_lock_status', readable=True, writable=False,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='f1f2', field_type=FieldType.READONLY),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='f1', field_type=FieldType.READONLY),FieldDefinition(high=2, low=2, msb=2, lsb=2, inst_name='f2', field_type=FieldType.READONLY),FieldDefinition(high=3, low=3, msb=3, lsb=3, inst_name='unlock_f1', field_type=FieldType.READONLY),FieldDefinition(high=4, low=4, msb=4, lsb=4, inst_name='unlock_f2', field_type=FieldType.READONLY),
                                                ]),
            164 : 
    Register(width=32, full_inst_name='msk_top_regs.symbol_lock_time', readable=True, writable=False,
                                         fields=[FieldDefinition(high=15, low=0, msb=15, lsb=0, inst_name='f1', field_type=FieldType.READONLY),FieldDefinition(high=31, low=16, msb=31, lsb=16, inst_name='f2', field_type=FieldType.READONLY),
                                                ]),
        }

    def _build_memories(self) -> list[MemoryEntry]:
        return [
        ]

if __name__ == '__main__':
    pass
