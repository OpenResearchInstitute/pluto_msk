#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#--  _______                             ________                                            ______
#--  __  __ \________ _____ _______      ___  __ \_____ _____________ ______ ___________________  /_
#--  _  / / /___  __ \_  _ \__  __ \     __  /_/ /_  _ \__  ___/_  _ \_  __ `/__  ___/_  ___/__  __ \
#--  / /_/ / __  /_/ //  __/_  / / /     _  _, _/ /  __/_(__  ) /  __// /_/ / _  /    / /__  _  / / /
#--  \____/  _  .___/ \___/ /_/ /_/      /_/ |_|  \___/ /____/  \___/ \__,_/  /_/     \___/  /_/ /_/
#--          /_/
#--                   ________                _____ _____ _____         _____
#--                   ____  _/_______ __________  /____(_)__  /_____  ____  /______
#--                    __  /  __  __ \__  ___/_  __/__  / _  __/_  / / /_  __/_  _ \
#--                   __/ /   _  / / /_(__  ) / /_  _  /  / /_  / /_/ / / /_  /  __/
#--                   /___/   /_/ /_/ /____/  \__/  /_/   \__/  \__,_/  \__/  \___/
#--
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#-- Copyright
#------------------------------------------------------------------------------------------------------
#--
#-- Copyright 2024 by M. Wishek <matthew@wishek.com>
#--
#------------------------------------------------------------------------------------------------------
#-- License
#------------------------------------------------------------------------------------------------------
#--
#-- This source describes Open Hardware and is licensed under the CERN-OHL-W v2.
#--
#-- You may redistribute and modify this source and make products using it under
#-- the terms of the CERN-OHL-W v2 (https://ohwr.org/cern_ohl_w_v2.txt).
#--
#-- This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
#-- OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.
#-- Please see the CERN-OHL-W v2 for applicable conditions.
#--
#-- Source location: TBD
#--
#-- As per CERN-OHL-W v2 section 4.1, should You produce hardware based on this
#-- source, You must maintain the Source Location visible on the external case of
#-- the products you make using this source.
#--
#------------------------------------------------------------------------------------------------------
#-- Description
#------------------------------------------------------------------------------------------------------
#--
#-- This file implements a Cocotb based Python testbench for testing the MSK Modem
#--
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
#         __   __   __  ___  __ 
# | |\/| |__) /  \ |__)  |  (_  
# | |  | |    \__/ | \   |  __) 
#                               
#------------------------------------------------------------------------------------------------------
import cocotb
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock    import Clock
from cocotb.utils    import get_sim_time

import random
import numpy as np 
import matplotlib.pyplot as plt
import sys
import inspect

from desyrdl import addrmap_ch0

#------------------------------------------------------------------------------------------------------
#  __       __  ___    __            __ ___    __        __ 
# |__) |   /  \  |    |_  /  \ |\ | /    |  | /  \ |\ | (_  
# |    |__ \__/  |    |   \__/ | \| \__  |  | \__/ | \| __) 
#                                                           
#------------------------------------------------------------------------------------------------------

def fftPlot(sig, dt=None, plot=True):
    # Here it's assumes analytic signal (real signal...) - so only half of the axis is required

    if dt is None:
        dt = 1
        t = np.arange(0, sig.shape[-1])
        xLabel = 'samples'
    else:
        t = np.arange(0, sig.shape[-1]) * dt
        xLabel = 'freq [Hz]'

    if sig.shape[0] % 2 != 0:
        warnings.warn("signal preferred to be even in size, autoFixing it...")
        t = t[0:-1]
        sig = sig[0:-1]

    sigFFT = np.fft.fft(sig) / t.shape[0]  # Divided by size t for coherent magnitude

    freq = np.fft.fftfreq(t.shape[0], d=dt)

    # Plot analytic signal - right half of frequence axis needed only...
    firstNegInd = np.argmax(freq < 0)
    freqAxisPos = freq[0:firstNegInd]
    sigFFTPos = 2 * sigFFT[0:firstNegInd]  # *2 because of magnitude of analytic signal

    if plot:
        plt.figure()
        plt.plot(freqAxisPos, np.abs(sigFFTPos))
        plt.xlabel(xLabel)
        plt.ylabel('mag')
        plt.title('Analytic FFT plot')
        plt.show()

    return sigFFTPos, freqAxisPos


#------------------------------------------------------------------------------------------------------
#             __    __        __              __ ___  __  __     __   __      
#  /\  \_/ | (_    |__) /  \ (_    |\/|  /\  (_   |  |_  |__)   |__) |_  |\/| 
# /--\ / \ | __)   |__) \__/ __)   |  | /--\ __)  |  |__ | \    |__) |   |  | 
#                                                                             
#------------------------------------------------------------------------------------------------------

class axis_bus:

    def __init__(self, dut):

        self.dut       = dut
        self.aclk_freq = 100e6

        self.aclk_per  = int(1/self.aclk_freq * 1e9)
        self.aclk_per_units = "ns"

        self.aclk           = dut.s_axis_aclk
        self.aresetn        = dut.s_axis_aresetn
        self.tvalid         = dut.s_axis_valid
        self.tready         = dut.s_axis_ready
        self.tdata          = dut.s_axis_data

        self.aresetn.value  = 1
        self.tvalid.value   = 0 
        self.tdata.value    = 0 

    async def init(self):
        await self._clock();
        await self._reset();

    async def _clock(self):

        self.dut._log.info("starting aclk with period %d %s" % (self.aclk_per, self.aclk_per_units))
        await cocotb.start(Clock(self.aclk, self.aclk_per, units=self.aclk_per_units).start())

    async def _reset(self):

        self.aresetn.value = 0

        await Timer(50, "ns")

        await RisingEdge(self.aclk)

        self.aresetn.value = 1

    async def send(self, data):

        self.tvalid.value = 1
        self.tdata.value = data

        await RisingEdge(self.aclk)

        while self.tready.value == 0:
            await RisingEdge(self.aclk)


#------------------------------------------------------------------------------------------------------
#                                     __        __              __ ___  __  __     __   __      
#  /\  \_/ |  |__|  __ |   . |_  _   |__) /  \ (_    |\/|  /\  (_   |  |_  |__)   |__) |_  |\/| 
# /--\ / \ |     |     |__ | |_ (-   |__) \__/ __)   |  | /--\ __)  |  |__ | \    |__) |   |  | 
#                                                                                               
#------------------------------------------------------------------------------------------------------

class axi_bus:

    def __init__(self, dut):

        self.dut       = dut
        self.aclk_freq = 100e6

        self.aclk_per  = int(1/self.aclk_freq * 1e9)
        self.aclk_per_units = "ns"

        self.aclk      = dut.s_axi_aclk
        self.aresetn   = dut.s_axi_aresetn

        self.awaddr    = dut.s_axi_awaddr 
        self.awvalid   = dut.s_axi_awvalid
        self.awready   = dut.s_axi_awready

        self.wdata     = dut.s_axi_wdata  
        self.wstrb     = dut.s_axi_wstrb  
        self.wvalid    = dut.s_axi_wvalid
        self.wready    = dut.s_axi_wready 

        self.bready    = dut.s_axi_bready 

        self.araddr    = dut.s_axi_araddr 
        self.arvalid   = dut.s_axi_arvalid
        self.arready   = dut.s_axi_arready

        self.rready    = dut.s_axi_rready 
        self.rdata     = dut.s_axi_rdata  
        self.rresp     = dut.s_axi_rresp  
        self.rvalid    = dut.s_axi_rvalid 

        self.bresp     = dut.s_axi_bresp  
        self.bvalid    = dut.s_axi_bvalid 

        self.awprot    = dut.s_axi_awprot
        self.arprot    = dut.s_axi_arprot


        self.awaddr.value = 0
        self.awvalid.value = 0

        self.wdata.value = 0
        self.wstrb.value = 0
        self.wvalid.value = 0

        self.bready.value = 0

        self.araddr.value = 0
        self.arvalid.value = 0

        self.rready.value = 0

        self.awprot.value = 0
        self.arprot.value = 0


    async def init(self):
        await self._clock();
        await self._reset();

    async def _clock(self):

        self.dut._log.info("starting aclk with period %d %s" % (self.aclk_per, self.aclk_per_units))
        await cocotb.start(Clock(self.aclk, self.aclk_per, units=self.aclk_per_units).start())

    async def _reset(self):

        self.aresetn.value = 0

        await Timer(50, "ns")

        await RisingEdge(self.aclk)

        self.aresetn.value = 1

    async def read_dwords(self, addr, count):
        data = await self.read(addr)
        return data

    async def write_dwords(self,addr, data):
        await self.write(addr, data[0])


    async def read(self, addr):

        await RisingEdge(self.aclk)

        self.arvalid.value = 1
        self.araddr.value = addr

        self.rready.value = 1

        await RisingEdge(self.aclk)

        while self.arready.value == 0:
            await RisingEdge(self.aclk)

        self.arvalid.value = 0

        while self.rvalid.value == 0:
            await RisingEdge(self.aclk)

        self.rready.value = 0

        await RisingEdge(self.aclk)
        await RisingEdge(self.aclk)
        await RisingEdge(self.aclk)

        return self.rdata.value.integer


    async def write(self, addr, data):

        self.awaddr.value = addr
        self.wdata.value = data
        self.wstrb.value = 15
        self.bready.value = 1

        await RisingEdge(self.aclk)

        self.dut.s_axi_awvalid.value = 1
        self.dut.s_axi_wvalid.value = 1

        while self.awready.value == 0 and self.wready.value == 0:
             await RisingEdge(self.aclk)

        self.dut.s_axi_awvalid.value = 0
        self.dut.s_axi_wvalid.value = 0

        while self.bvalid.value == 0:
            await RisingEdge(self.aclk)

        self.bready.value = 0

        await RisingEdge(self.aclk)
        await RisingEdge(self.aclk)
        await RisingEdge(self.aclk)


#------------------------------------------------------------------------------------------------------
#       __                              __             
# |\/| (_  |_/   |\/|  _   _|  _  _    /   |  _   _  _ 
# |  | __) | \   |  | (_) (_| (- |||   \__ | (_| _) _) 
#                                                      
#------------------------------------------------------------------------------------------------------

class msk:

    def __init__(self, dut, clk, tx_sample_bus):

        self.dut = dut
        self.sim_run = False

        self.tx_sample_bus = tx_sample_bus 
        self.clk = clk

        self.tx_samples = []
        self.time = []

    async def tx_sample_capture(self):

        self.dut._log.info("tx sample capture - waiting for start...")

        while self.sim_run == False:
            await RisingEdge(self.clk)

        self.dut._log.info("tx sample capture - starting...")

        while self.sim_run:
            self.tx_samples.append(int(self.tx_sample_bus.value.signed_integer))
            self.time.append(get_sim_time("us"))
            await RisingEdge(self.clk)

        self.dut._log.info("...tx sample capture - done")


#------------------------------------------------------------------------------------------------------
#  __   __   __   __    __                                              __                    
# |__) |__) |__) (_    / _   _  _   _  _  _  |_  _   _    _   _   _|   /   |_   _  _ |   _  _ 
# |    | \  |__) __)   \__) (- | ) (- |  (_| |_ (_) |    (_| | ) (_|   \__ | ) (- (_ |( (- |  
#                                                                                             
#------------------------------------------------------------------------------------------------------

class prbs:

    def __init__(self, dut, clk, saxis, txw, rxw, rx_data, rx_dvalid, width=8, seed=255, prbs=31):


        self.dut = dut 
        self.clk = clk 
        self.saxis = saxis

        self.txw = txw 
        self.rxw = rxw 

        self.rx_data = rx_data 
        self.rx_dvalid = rx_dvalid

        self.width = width
        self.seed = seed 

        self.state_gen = seed
        self.state_mon = 0

        self.sim_run = False

        self.sync = 4
        self.data_count = 0
        self.err_count = 0

        self.ones_count = 0
        self.zeros_count = 0

        if prbs == 31:
            self.taps = [30, 27]


    async def init_gen(self):

        await RisingEdge(self.clk)

        self.state_gen = self.seed


    async def gen(self):

        state = self.state_gen

        for i in range(self.width):
            bit = ((state >> self.taps[0]) ^ (state >> self.taps[1])) & 1
            state = ((state << 1) | bit) & ((2**32) -1)

        self.state_gen = state & ((2**32) -1)

        print("gen: ", hex(state))
        print("tx_data: ", hex(self.state_gen & 0xFFFFFFFF))

        data = self.state_gen & 0xFFFFFFFF

        self.ones_count += data.bit_count()
        self.zeros_count += 8 - data.bit_count()

        return data


    async def resync(self):

        self.sync = 4
        self.data_count = 0
        self.err_count = 0


    async def mon(self, data):

        timenow = get_sim_time("us")

        #print("------ Monitor ------")
        #print("Time: ", timenow)
        #print("rx data: ", hex(data))

        if self.sync > 0:
            self.state_mon = ((self.state_mon << 8) | data) & ((2**32) -1)
            self.sync -= 1
            #print("sync: ", self.sync)
            #print("mon sync: ", hex(self.state_mon))
        else:
            #print("mon state at start: ", hex(self.state_mon))
            state = self.state_mon
            #print("mon: ", hex(state))
            for i in range(self.width):
                bit = ((state >> 31) ^ (state >> 28)) & 1
                #print("bit: ", bit)
                state = ((state << 1) | bit) & ((2**32) -1)
                #print("update state: ", hex(state))

            self.state_mon = state
            self.data_count += self.width

            #print("mon: ", hex(state))

            errored_bits = (self.state_mon & 0xFF) ^ data

            if errored_bits > 0:
                for i in range(self.width):
                    self.err_count += ((errored_bits >> i) & 1)
                print("Time: ", timenow, "us; error count: ", self.err_count, "; data count: ", self.data_count, "; BER = ", 100*round(self.err_count/self.data_count, 3), "%")

        #assert errored_bits == 0, "PRBS: Bit-error(s)" 

    async def generate_data(self):

        self.dut._log.info("prbs generator - waiting for start...")

        while self.sim_run == False:
            await RisingEdge(self.clk)

        self.dut._log.info("prbs generator - starting...")

        while self.sim_run:
            data = await self.gen()
            print("Data: ", data)
            await self.saxis.send(data)

        self.dut._log.info("...prbs generator - done")


    async def check_data(self):

        self.dut._log.info("prbs mon - waiting for start...")

        while self.sim_run == False:
            await RisingEdge(self.clk)

        self.dut._log.info("prbs mon - starting...")

        while self.sim_run:
            if self.rx_dvalid.value == 1:
                rx_data = self.rx_data.value.integer
                await self.mon(rx_data)
            await RisingEdge(self.clk)

        self.dut._log.info("...prbs mon - done")



#------------------------------------------------------------------------------------------------------
#       __                             ___          
# |\/| (_  |_/   |\/|  _   _|  _  _     |   _  _ |_ 
# |  | __) | \   |  | (_) (_| (- |||    |  (- _) |_ 
#                                                   
#------------------------------------------------------------------------------------------------------

@cocotb.test()
async def msk_test_1(dut):

    print("Instantiate registers")
    axi  = axi_bus(dut)
    regs = addrmap_ch0.Addrmap(axi)

    tx_samples = []
    tx_time = []

    bitrate = 54200
    freq_if = bitrate * 20
    tx_sample_rate = 61.44e6
    tx_sample_per = int(1/tx_sample_rate * 1e9)

    tx_rx_sample_ratio = 1

    rx_sample_rate = tx_sample_rate / tx_rx_sample_ratio

    tx_data_width = 32
    rx_data_width = 32

    await cocotb.start(Clock(dut.clk, tx_sample_per, units="ns").start())

    f1 = freq_if - bitrate
    f2 = freq_if + bitrate

    print("Bit Rate NCO Freq Word: ", hex(int(bitrate / tx_sample_rate * 2.0**32)))
    print("TX F1 NCO Freq Word: ", hex(int(f1 / tx_sample_rate * 2.0**32)))
    print("TX F2 NCO Freq Word: ", hex(int(f2 / tx_sample_rate * 2.0**32)))
    print("RX F1 NCO Freq Word: ", hex(int(f1 / rx_sample_rate * 2.0**32)))
    print("RX F2 NCO Freq Word: ", hex(int(f2 / rx_sample_rate * 2.0**32)))

    FFT = 8192 * 4

    await RisingEdge(dut.clk)

    axis = axis_bus(dut)

    await axi.init()
    await axis.init()
    
    dut.tx_enable.value = 1
    dut.rx_enable.value = 1
    dut.rx_svalid.value = 1
    dut.tx_valid.value  = 1

    hash_id = await regs.read("msk_top_regs", "Hash_ID_Low")

    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1

    # await axi.write( 4, 1)                                         # assert on init
    # await regs.write("msk_top_regs", "MSK_Init", 1)
    # await axi.write(12, 1)                                         # loopback
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "MSK_Control", (tx_rx_sample_ratio-1 << 8) + 3)    
    # await axi.write(16, int(bitrate / sample_rate * 2.0**32))      # bit rate frequency word
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "Fb_FreqWord", int(bitrate / tx_sample_rate * 2.0**32))    
    # await axi.write(20, int(f1 / sample_rate * 2.0**32))           # F1 frequency word
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "TX_F1_FreqWord", int(f1 / tx_sample_rate * 2.0**32))    
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "TX_F2_FreqWord", int(f2 / tx_sample_rate * 2.0**32))    
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "RX_F1_FreqWord", int(f1 / rx_sample_rate * 2.0**32))    
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "RX_F2_FreqWord", int(f2 / rx_sample_rate * 2.0**32))    
    # await axi.write(28, (50 << 16) + 20)                             # p-gain / i-gain
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "LPF_Config_0", (2 << 16))    
    # await axi.write(32, (2 << 16))                                   # low-pass filter alpha
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "LPF_Config_1", (100 << 16) + 40)    
    # await axi.write(36, 8)
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "Tx_Data_Width", tx_data_width)    
    # await axi.write(40, 8)
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "Rx_Data_Width", rx_data_width)    
    # await axi.write(44, 1)                                          # Select PRBS data path
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "PRBS_Control", (400 << 16) + 1)    
    # await axi.write(48, (1 << 31) + (1 << 28))                      # Polynomial 
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "PRBS_Polynomial", (1 << 30) + (1 << 27))    
    # await axi.write(52, 65535)                                      # initial state
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "PRBS_Initial_State", 0x8E7589FD)    
    # await axi.write(56, 1)                                          # Error Mask
    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "PRBS_Error_Mask", 1)    
    # await axi.write(60, 0)


    hash_id = await regs.read("msk_top_regs", "Hash_ID_Low")
    #print("Hash ID: ", hex(hash_id))
    hash_id = await regs.read("msk_top_regs", "Hash_ID_Low")
    #print("Hash ID: ", hex(hash_id))
    hash_id = await regs.read("msk_top_regs", "Hash_ID_Low")
    #print("Hash ID: ", hex(hash_id))
    hash_id = await regs.read("msk_top_regs", "Hash_ID_Low")
    #print("Hash ID: ", hex(hash_id))
    hash_id = await regs.read("msk_top_regs", "Hash_ID_Low")
    print("Hash ID Low: ", hex(hash_id))
    hash_id = await regs.read("msk_top_regs", "Hash_ID_High")
    print("Hash ID High: ", hex(hash_id))

    await Timer(100, units="ns")

    await RisingEdge(dut.clk)

    dut.s_axi_wvalid.value = 1
    dut.s_axi_awvalid.value = 1
    await regs.write("msk_top_regs", "MSK_Init", 0)    

    await RisingEdge(dut.clk)

    msksim = msk(dut, dut.clk, dut.tx_samples)
    pn = prbs(dut, dut.clk, axis, tx_data_width, rx_data_width, dut.rx_data, dut.rx_dvalid)

    await cocotb.start(msksim.tx_sample_capture())
    await cocotb.start(pn.generate_data())
    await cocotb.start(pn.check_data())

    sim_time = get_sim_time("us")
    sim_start = sim_time
    sim_time_d = sim_time

    dut._log.info("starting...")

    msksim.sim_run = True

    pn.sim_run = True
    pn.sync = 100

    while sim_time < sim_start + 20000:

        # if sim_time_d <= sim_start + 1000 and sim_time >= sim_start + 1000:
        #     data = await regs.read("msk_top_regs", "PRBS_Control")
        #     data = data | 0x4
        #     dut.s_axi_wvalid.value = 1
        #     dut.s_axi_awvalid.value = 1
        #     await regs.write("msk_top_regs", "PRBS_Control", data)    

        if sim_time_d <= sim_start + 10000 and sim_time >= sim_start + 10000:
            data = await regs.read("msk_top_regs", "PRBS_Control")
            data = data ^ 0x8
            dut.s_axi_wvalid.value = 1
            dut.s_axi_awvalid.value = 1
            await regs.write("msk_top_regs", "PRBS_Control", data)    

        # if sim_time_d <= sim_start + 3000 and sim_time >= sim_start + 3000:
            # await pn.resync()
# 
        # if sim_time_d <= sim_start + 4000 and sim_time >= sim_start + 4000:
            # await pn.resync()

        sim_time_d = sim_time
        sim_time = get_sim_time("us")

        data = await regs.read("msk_top_regs", "LPF_Accum_F1")
        print("F1 Acc: ", hex(data))
        data = await regs.read("msk_top_regs", "LPF_Accum_F2")
        print("F2 Acc: ", hex(data))
        data = await regs.read("msk_top_regs", "Tx_Bit_Count")
        print("Tx Bit Count: ", hex(data))
        data = await regs.read("msk_top_regs", "Tx_Enable_Count")
        print("Tx Enable Count: ", hex(data))
        data = await regs.read("msk_top_regs", "MSK_Status")
        print("MSK Status: ", hex(data))
        data = await regs.read("msk_top_regs", "axis_xfer_count")
        print("XFER Count: ", hex(data))
        # data = await regs.read("msk_top_regs", "Tx_Bit_Count")
        # print("Tx Bit Count: ", data)
        # data = await regs.read("msk_top_regs", "Tx_Enable_Count")
        # print("Tx Enabled: ", data)

    msksim.sim_run = False
    pn.sim_run = False

    await RisingEdge(dut.clk)

    tx_time        = msksim.time
    tx_samples     = msksim.tx_samples

    tx_samples_arr = np.asarray(tx_samples)
    tx_samples_2   = tx_samples_arr * tx_samples_arr

    # print("Ones: ", pn.ones_count)
    # print("Zeros: ", pn.zeros_count)

    errs = await regs.read("msk_top_regs", "PRBS_Error_Count")
    print("Bit errors: ", errs)
    bits = await regs.read("msk_top_regs", "PRBS_Bit_Count")
    print("Bit count:  ", bits)
    print("BER:        ", (1.0*errs)/bits)

    # print("Bit errors: ", pn.err_count)
    # print("Bit count:  ", pn.data_count)
    # print("BER:        ", pn.err_count/pn.data_count)

    blackman_window = np.blackman(len(tx_samples))

    fig = plt.figure(figsize=(7, 7), layout='constrained')
    axs = fig.subplot_mosaic([["signal", "signal"],
                              ["magnitude", "log_magnitude"],
                              ["psd", "psd"]])
    
    # plot time signal:
    axs["signal"].set_title("MSK Tx Samples")
    axs["signal"].plot(tx_time, tx_samples, color='C0')
    axs["signal"].set_xlabel("Time (s)")
    axs["signal"].set_ylabel("Amplitude")
    
    # plot different spectrum types:
    axs["magnitude"].set_title("Magnitude Spectrum Squared")
    axs["magnitude"].magnitude_spectrum(tx_samples_2, Fs=tx_sample_rate, window=blackman_window, color='C1')
    
    axs["log_magnitude"].set_title("Log. Magnitude Spectrum Squared")
    axs["log_magnitude"].magnitude_spectrum(tx_samples_2, Fs=tx_sample_rate, scale='dB', window=blackman_window, color='C1')
    
    axs["psd"].set_title("Power Spectral Density")
    axs["psd"].psd(tx_samples, Fs=tx_sample_rate, window=np.blackman(FFT), NFFT=FFT, color='C2')
        
    plt.show()

    #fftPlot(np.asarray(tx_samples), dt=1/sample_rate)
