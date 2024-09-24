
import numpy as np
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger()
logger.setLevel(logging.INFO)



class AddrmapItem ():
    def __init__(self, name, bus, address, size, bits, fixp, signed, access):
        self.name = name
        self.bus = bus
        self.address = address
        self.size = size
        self.bits = bits
        self.fixp = fixp
        self.access = access
        self.scaling = 1;
        if fixp == "IEEE754":
            self.dtype = np.float32
        elif fixp == 0 and signed == 0:
            self.dtype = np.uint32
        elif fixp == 0 and signed == 1:
            self.dtype = np.int32
        else:
            self.scaling = 1/pow(2, fixp)
            self.dtype = np.float32

    async def read(self, count, offset):
        data = await self.bus.read_dwords(self.address+offset*4, count)
        return np.array(data * self.scaling, dtype=self.dtype)

    async def read_raw(self, count, offset):
        data = await self.bus.read_dwords(self.address+offset*4, count)
        return np.array(data, dtype=np.uint32)

    async def write(self, value, offset):
        val_np = np.array(value)
        if val_np.size > 1:
            data = np.uint32(np.round(val_np / self.scaling)).tolist()
        else:
            data = []
            data.append(np.uint32(np.round(val_np / self.scaling)).tolist())
        await self.bus.write_dwords(self.address+offset*4, data)

    async def write_raw(self, value, offset):
        val_np = np.array(value)
        if val_np.size > 1:
            data = np.uint32(np.round(val_np)).tolist()
        else:
            data = []
            data.append(np.uint32(np.round(val_np)).tolist())
        await self.bus.write_dwords(self.address+offset*4, data)

class Addrmap:
    def __init__(self, bus):
        self.addrmap ={}
        self.addrmap['msk_top_regs.Hash_ID_Low'] = AddrmapItem("msk_top_regs.Hash_ID_Low", bus, 0, 4, 32, 0, 0, "RO")
        self.addrmap['msk_top_regs.Hash_ID_High'] = AddrmapItem("msk_top_regs.Hash_ID_High", bus, 4, 4, 32, 0, 0, "RO")
        self.addrmap['msk_top_regs.MSK_Init'] = AddrmapItem("msk_top_regs.MSK_Init", bus, 8, 4, 1, 0, 0, "RW")
        self.addrmap['msk_top_regs.MSK_Control'] = AddrmapItem("msk_top_regs.MSK_Control", bus, 12, 4, 12, 0, 0, "RW")
        self.addrmap['msk_top_regs.MSK_Status'] = AddrmapItem("msk_top_regs.MSK_Status", bus, 16, 4, 3, 0, 0, "RO")
        self.addrmap['msk_top_regs.Tx_Bit_Count'] = AddrmapItem("msk_top_regs.Tx_Bit_Count", bus, 20, 4, 32, 0, 0, "RO")
        self.addrmap['msk_top_regs.Tx_Enable_Count'] = AddrmapItem("msk_top_regs.Tx_Enable_Count", bus, 24, 4, 32, 0, 0, "RO")
        self.addrmap['msk_top_regs.Fb_FreqWord'] = AddrmapItem("msk_top_regs.Fb_FreqWord", bus, 28, 4, 32, 0, 0, "RW")
        self.addrmap['msk_top_regs.TX_F1_FreqWord'] = AddrmapItem("msk_top_regs.TX_F1_FreqWord", bus, 32, 4, 32, 0, 0, "RW")
        self.addrmap['msk_top_regs.TX_F2_FreqWord'] = AddrmapItem("msk_top_regs.TX_F2_FreqWord", bus, 36, 4, 32, 0, 0, "RW")
        self.addrmap['msk_top_regs.RX_F1_FreqWord'] = AddrmapItem("msk_top_regs.RX_F1_FreqWord", bus, 40, 4, 32, 0, 0, "RW")
        self.addrmap['msk_top_regs.RX_F2_FreqWord'] = AddrmapItem("msk_top_regs.RX_F2_FreqWord", bus, 44, 4, 32, 0, 0, "RW")
        self.addrmap['msk_top_regs.LPF_Config_0'] = AddrmapItem("msk_top_regs.LPF_Config_0", bus, 48, 4, 32, 0, 0, "RW")
        self.addrmap['msk_top_regs.LPF_Config_1'] = AddrmapItem("msk_top_regs.LPF_Config_1", bus, 52, 4, 32, 0, 0, "RW")
        self.addrmap['msk_top_regs.Tx_Data_Width'] = AddrmapItem("msk_top_regs.Tx_Data_Width", bus, 56, 4, 8, 0, 0, "RW")
        self.addrmap['msk_top_regs.Rx_Data_Width'] = AddrmapItem("msk_top_regs.Rx_Data_Width", bus, 60, 4, 8, 0, 0, "RW")
        self.addrmap['msk_top_regs.PRBS_Control'] = AddrmapItem("msk_top_regs.PRBS_Control", bus, 64, 4, 32, 0, 0, "RW")
        self.addrmap['msk_top_regs.PRBS_Initial_State'] = AddrmapItem("msk_top_regs.PRBS_Initial_State", bus, 68, 4, 32, 0, 0, "RW")
        self.addrmap['msk_top_regs.PRBS_Polynomial'] = AddrmapItem("msk_top_regs.PRBS_Polynomial", bus, 72, 4, 32, 0, 0, "RW")
        self.addrmap['msk_top_regs.PRBS_Error_Mask'] = AddrmapItem("msk_top_regs.PRBS_Error_Mask", bus, 76, 4, 32, 0, 0, "RW")
        self.addrmap['msk_top_regs.PRBS_Bit_Count'] = AddrmapItem("msk_top_regs.PRBS_Bit_Count", bus, 80, 4, 32, 0, 0, "RO")
        self.addrmap['msk_top_regs.PRBS_Error_Count'] = AddrmapItem("msk_top_regs.PRBS_Error_Count", bus, 84, 4, 32, 0, 0, "RO")
        self.addrmap['msk_top_regs.LPF_Accum_F1'] = AddrmapItem("msk_top_regs.LPF_Accum_F1", bus, 88, 4, 32, 0, 0, "RO")
        self.addrmap['msk_top_regs.LPF_Accum_F2'] = AddrmapItem("msk_top_regs.LPF_Accum_F2", bus, 92, 4, 32, 0, 0, "RO")

    def get_path(self, module, name):
        path = module + "." + name
        if path not in self.addrmap:
            msg = f"Cannot find `{path}` in register dict"
            logger.error(msg)
            assert False
        return path

    async def read(self, module, name, count=1, offset=0):
        path = self.get_path(module, name)
        return await self.addrmap[path].read(count, offset)

    async def write(self, module, name, value, offset=0):
        path = self.get_path(module, name)
        return await self.addrmap[path].write(value, offset)
    async def read_raw(self, module, name, count=1, offset=0):
        path = self.get_path(module, name)
        return await self.addrmap[path].read_raw(count, offset)
    async def write_raw(self, module, name, value, offset=0):
        path = self.get_path(module, name)
        return await self.addrmap[path].write_raw(value, offset)