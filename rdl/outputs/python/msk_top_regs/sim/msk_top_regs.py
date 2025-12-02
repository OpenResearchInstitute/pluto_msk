


"""
Python Wrapper for the msk_top_regs register model

This code was generated from the PeakRDL-python package version 1.4.0

"""

from typing import Union

from ..sim_lib.register import Register, MemoryRegister
from ..sim_lib.memory import Memory
from ..sim_lib.simulator import MemoryEntry
from ..sim_lib.field import FieldDefinition
from ..sim_lib.simulator import AsyncSimulator as Simulator


class msk_top_regs_simulator_cls(Simulator):

    def _build_registers(self) -> dict[int, Union[list[Union[MemoryRegister, Register]], Union[MemoryRegister, Register]]]:
        return {
            0 : 
    Register(width=32, full_inst_name='msk_top_regs.Hash_ID_Low', readable=True, writable=False,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='hash_id_lo'),
                                                ]),
            4 : 
    Register(width=32, full_inst_name='msk_top_regs.Hash_ID_High', readable=True, writable=False,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='hash_id_hi'),
                                                ]),
            8 : 
    Register(width=32, full_inst_name='msk_top_regs.MSK_Init', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='txrxinit'),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='txinit'),FieldDefinition(high=2, low=2, msb=2, lsb=2, inst_name='rxinit'),
                                                ]),
            12 : 
    Register(width=32, full_inst_name='msk_top_regs.MSK_Control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='ptt'),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='loopback_ena'),FieldDefinition(high=2, low=2, msb=2, lsb=2, inst_name='rx_invert'),FieldDefinition(high=3, low=3, msb=3, lsb=3, inst_name='clear_counts'),FieldDefinition(high=4, low=4, msb=4, lsb=4, inst_name='diff_encoder_loopback'),
                                                ]),
            16 : 
    Register(width=32, full_inst_name='msk_top_regs.MSK_Status', readable=True, writable=False,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='demod_sync_lock'),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='tx_enable'),FieldDefinition(high=2, low=2, msb=2, lsb=2, inst_name='rx_enable'),FieldDefinition(high=3, low=3, msb=3, lsb=3, inst_name='tx_axis_valid'),
                                                ]),
            20 : 
    Register(width=32, full_inst_name='msk_top_regs.Tx_Bit_Count', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            24 : 
    Register(width=32, full_inst_name='msk_top_regs.Tx_Enable_Count', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            28 : 
    Register(width=32, full_inst_name='msk_top_regs.Fb_FreqWord', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data'),
                                                ]),
            32 : 
    Register(width=32, full_inst_name='msk_top_regs.TX_F1_FreqWord', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data'),
                                                ]),
            36 : 
    Register(width=32, full_inst_name='msk_top_regs.TX_F2_FreqWord', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data'),
                                                ]),
            40 : 
    Register(width=32, full_inst_name='msk_top_regs.RX_F1_FreqWord', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data'),
                                                ]),
            44 : 
    Register(width=32, full_inst_name='msk_top_regs.RX_F2_FreqWord', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data'),
                                                ]),
            48 : 
    Register(width=32, full_inst_name='msk_top_regs.LPF_Config_0', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='lpf_freeze'),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='lpf_zero'),FieldDefinition(high=7, low=2, msb=7, lsb=2, inst_name='prbs_reserved'),FieldDefinition(high=31, low=8, msb=31, lsb=8, inst_name='lpf_alpha'),
                                                ]),
            52 : 
    Register(width=32, full_inst_name='msk_top_regs.LPF_Config_1', readable=True, writable=True,
                                         fields=[FieldDefinition(high=23, low=0, msb=23, lsb=0, inst_name='i_gain'),FieldDefinition(high=31, low=24, msb=31, lsb=24, inst_name='i_shift'),
                                                ]),
            56 : 
    Register(width=32, full_inst_name='msk_top_regs.Tx_Data_Width', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='data_width'),
                                                ]),
            60 : 
    Register(width=32, full_inst_name='msk_top_regs.Rx_Data_Width', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='data_width'),
                                                ]),
            64 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='prbs_sel'),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='prbs_error_insert'),FieldDefinition(high=2, low=2, msb=2, lsb=2, inst_name='prbs_clear'),FieldDefinition(high=3, low=3, msb=3, lsb=3, inst_name='prbs_manual_sync'),FieldDefinition(high=15, low=4, msb=15, lsb=4, inst_name='prbs_reserved'),FieldDefinition(high=31, low=16, msb=31, lsb=16, inst_name='prbs_sync_threshold'),
                                                ]),
            68 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Initial_State', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data'),
                                                ]),
            72 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Polynomial', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data'),
                                                ]),
            76 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Error_Mask', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='config_data'),
                                                ]),
            80 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Bit_Count', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            84 : 
    Register(width=32, full_inst_name='msk_top_regs.PRBS_Error_Count', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            88 : 
    Register(width=32, full_inst_name='msk_top_regs.LPF_Accum_F1', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            92 : 
    Register(width=32, full_inst_name='msk_top_regs.LPF_Accum_F2', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            96 : 
    Register(width=32, full_inst_name='msk_top_regs.axis_xfer_count', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            100 : 
    Register(width=32, full_inst_name='msk_top_regs.Rx_Sample_Discard', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='rx_sample_discard'),FieldDefinition(high=15, low=8, msb=15, lsb=8, inst_name='rx_nco_discard'),
                                                ]),
            104 : 
    Register(width=32, full_inst_name='msk_top_regs.LPF_Config_2', readable=True, writable=True,
                                         fields=[FieldDefinition(high=23, low=0, msb=23, lsb=0, inst_name='p_gain'),FieldDefinition(high=31, low=24, msb=31, lsb=24, inst_name='p_shift'),
                                                ]),
            108 : 
    Register(width=32, full_inst_name='msk_top_regs.f1_nco_adjust', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            112 : 
    Register(width=32, full_inst_name='msk_top_regs.f2_nco_adjust', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            116 : 
    Register(width=32, full_inst_name='msk_top_regs.f1_error', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            120 : 
    Register(width=32, full_inst_name='msk_top_regs.f2_error', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            124 : 
    Register(width=32, full_inst_name='msk_top_regs.Tx_Sync_Ctrl', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tx_sync_ena'),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='tx_sync_force'),
                                                ]),
            128 : 
    Register(width=32, full_inst_name='msk_top_regs.Tx_Sync_Cnt', readable=True, writable=True,
                                         fields=[FieldDefinition(high=23, low=0, msb=23, lsb=0, inst_name='tx_sync_cnt'),
                                                ]),
            132 : 
    Register(width=32, full_inst_name='msk_top_regs.lowpass_ema_alpha1', readable=True, writable=True,
                                         fields=[FieldDefinition(high=17, low=0, msb=17, lsb=0, inst_name='alpha'),
                                                ]),
            136 : 
    Register(width=32, full_inst_name='msk_top_regs.lowpass_ema_alpha2', readable=True, writable=True,
                                         fields=[FieldDefinition(high=17, low=0, msb=17, lsb=0, inst_name='alpha'),
                                                ]),
            140 : 
    Register(width=32, full_inst_name='msk_top_regs.rx_power', readable=True, writable=True,
                                         fields=[FieldDefinition(high=22, low=0, msb=22, lsb=0, inst_name='data'),
                                                ]),
            144 : 
    Register(width=32, full_inst_name='msk_top_regs.tx_async_fifo_rd_wr_ptr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            148 : 
    Register(width=32, full_inst_name='msk_top_regs.rx_async_fifo_rd_wr_ptr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data'),
                                                ]),
            152 : 
    Register(width=32, full_inst_name='msk_top_regs.rx_frame_sync_status', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='frame_sync_locked'),FieldDefinition(high=1, low=1, msb=1, lsb=1, inst_name='frame_buffer_overflow'),FieldDefinition(high=25, low=2, msb=25, lsb=2, inst_name='frames_received'),FieldDefinition(high=31, low=26, msb=31, lsb=26, inst_name='frame_sync_errors'),
                                                ]),
        }

    def _build_memories(self) -> list[MemoryEntry]:
        return [
        ]

if __name__ == '__main__':
    pass
