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

import math
import random
import numpy as np 
import matplotlib.pyplot as plt
import sys
import inspect

from msk_top_regs.reg_model.msk_top_regs import msk_top_regs_cls
from msk_top_regs.lib import AsyncCallbackSet, AsyncCallbackSetLegacy

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


    async def read(self, addr, width, accesswidth):

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


    async def write(self, addr, width, accesswidth, data):

        self.dut.s_axi_awvalid.value = 1
        self.dut.s_axi_wvalid.value = 1
        self.awaddr.value = addr
        self.wdata.value = data
        self.wstrb.value = 15
        self.bready.value = 1

        await RisingEdge(self.aclk)

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

    def __init__(self, dut, clk, tx_samples_I, tx_samples_Q, rx_sample_clk, rx_samples):

        self.dut = dut
        self.sim_run = False

        self.tx_samples_I = tx_samples_I 
        self.tx_samples_Q = tx_samples_Q 
        self.rx_samples   = rx_samples
        self.rx_sample_clk = rx_sample_clk
        self.clk = clk

        self.tx_samples_I_arr = []
        self.tx_samples_Q_arr = []
        self.rx_samples_arr   = []
        self.time = []

    async def tx_sample_capture(self):

        self.dut._log.info("tx sample capture - waiting for start...")

        while self.sim_run == False:
            await RisingEdge(self.clk)

        self.dut._log.info("tx sample capture - starting...")

        while self.sim_run:
            self.tx_samples_I_arr.append(int(self.tx_samples_I.value.signed_integer))
            self.tx_samples_Q_arr.append(int(self.tx_samples_Q.value.signed_integer))
            self.time.append(get_sim_time("us"))
            await RisingEdge(self.clk)

        self.dut._log.info("...tx sample capture - done")

    async def rx_sample_capture(self):

        self.dut._log.info("rx sample capture - waiting for start...")

        while self.sim_run == False:
            await RisingEdge(self.clk)

        self.dut._log.info("rx sample capture - starting...")

        while self.sim_run:
            if self.rx_sample_clk.value.integer == 1:
                self.rx_samples_arr.append(int(self.rx_samples.value.signed_integer))
            await RisingEdge(self.clk)

        self.dut._log.info("...rx sample capture - done")

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
            self.dut._log.info("Data: %s", hex(data))
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
#------------------------------------------------------------------------------------------------------

class duc:

    def __init__(self, dut, msk, lo, sample_period):

        self.dut = dut 
        self.msk = msk
        self.clk = dut.clk
        self.lo = lo
        self.sample_period = sample_period
        self.time = 0
        self.tx_samples_I_up = []
        self.tx_samples_Q_up = []
        self.tx_samples_IQ_mod = []

    async def upconvert(self):

        self.dut._log.info("duc - waiting for start...")

        while self.msk.sim_run == False:
            await RisingEdge(self.clk)

        self.dut._log.info("duc - starting...")

        while self.msk.sim_run:

            await RisingEdge(self.clk)

            self.time += self.sample_period

            self.sin = math.sin(2*math.pi*self.lo*self.time)
            self.cos = math.cos(2*math.pi*self.lo*self.time)

            self.tx_samples_I_up.append(self.cos * self.dut.tx_samples_I.value.signed_integer)
            self.tx_samples_Q_up.append(self.sin * self.dut.tx_samples_Q.value.signed_integer)
            self.tx_samples_IQ_mod.append(self.tx_samples_I_up[-1] + self.tx_samples_Q_up[-1])

        self.dut._log.info("...duc - done")


#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

class ddc:

    def __init__(self, dut, msk, duc, lo, sample_period):

        self.dut = dut 
        self.msk = msk
        self.clk = dut.clk
        self.duc = duc
        self.lo = lo
        self.sample_period = sample_period
        self.time = 0
        self.rx_samples_I_dn = []
        self.rx_samples_Q_dn = []

    async def downconvert(self):

        self.dut._log.info("ddc - waiting for start...")

        while self.msk.sim_run == False:
            await RisingEdge(self.clk)

        self.dut._log.info("ddc - starting...")

        while self.msk.sim_run:

            await RisingEdge(self.clk)

            self.time += self.sample_period

            rx_sample = self.duc.tx_samples_IQ_mod[-1]

            self.sin = math.sin(2*math.pi*self.lo*self.time)
            self.cos = math.cos(2*math.pi*self.lo*self.time)

            rx_sample_I_dn = self.cos * rx_sample
            rx_sample_Q_dn = self.sin * rx_sample

            self.rx_samples_I_dn.append(rx_sample_I_dn)
            self.rx_samples_Q_dn.append(rx_sample_Q_dn)

            self.dut.rx_samples_I.value = int(round(rx_sample_I_dn))
            self.dut.rx_samples_Q.value = int(round(rx_sample_Q_dn))

        self.dut._log.info("...ddc - done")


#------------------------------------------------------------------------------------------------------
#       __                             ___          
# |\/| (_  |_/   |\/|  _   _|  _  _     |   _  _ |_ 
# |  | __) | \   |  | (_) (_| (- |||    |  (- _) |_ 
#                                                   
#------------------------------------------------------------------------------------------------------

@cocotb.test()
async def msk_test_1(dut):

    plot = True

    run_time = 35000 # microseconds

    # p_gain = 579
    # i_gain = 128
    # p_shift = 6
    # i_shift = 6

    # p_gain  = 40
    # i_gain  = 9
    # p_shift = 0
    # i_shift = 0

    p_gain  = 80
    p_shift = 5

    i_gain  = 9
    i_shift = 9

    autosync_threshold = 50

    bitrate = 54200
    freq_if_mult = 32

    freq_if = bitrate/4 * freq_if_mult

    freq_carrier = 10e6
    period_carrier = 1/freq_carrier

    local_osc = freq_carrier -  freq_if

    tx_sample_rate = 61.44e6
    tx_sample_period = 1/tx_sample_rate

    tx_rx_sample_ratio = 25

    rx_offset = 100

    lpf_alpha = 0

    rx_invert = 0

    ptt = 1
    digital_loopback = 1
    diff_enc_loopback = 0

    print("Instantiate registers")
    axi  = axi_bus(dut)
    regs = msk_top_regs_cls(callbacks=AsyncCallbackSet(read_callback=axi.read, write_callback=axi.write))

    tx_samples = []
    tx_time = []

    tx_sample_per = int(round(1/tx_sample_rate * 1e14))*10

    rx_sample_rate = tx_sample_rate / tx_rx_sample_ratio

    tx_data_width = 8
    rx_data_width = 8

    await cocotb.start(Clock(dut.clk, tx_sample_per, units="fs").start())

    delta_f = bitrate/4

    f1 = freq_if - delta_f
    f2 = freq_if + delta_f

    br_fcw = int(bitrate / tx_sample_rate * 2.0**32)

    f1_fcw_tx = int(f1 / tx_sample_rate * 2.0**32)
    f2_fcw_tx = int(f2 / tx_sample_rate * 2.0**32)
    f1_fcw_rx = int((f1+rx_offset) / tx_sample_rate * 2.0**32)
    f2_fcw_rx = int((f2+rx_offset) / tx_sample_rate * 2.0**32)

    print("Bit Rate NCO Freq Word: ", hex(br_fcw))
    print("TX F1 NCO Freq Word: ", hex(f1_fcw_tx))
    print("TX F2 NCO Freq Word: ", hex(f2_fcw_tx))
    print("RX F1 NCO Freq Word: ", hex(f1_fcw_rx))
    print("RX F2 NCO Freq Word: ", hex(f2_fcw_rx))

    FFT = 8192 * 4

    await RisingEdge(dut.clk)

    axis = axis_bus(dut)

    await axi.init()
    await axis.init()
    
    dut.tx_enable.value = 1
    dut.rx_enable.value = 1
    dut.rx_svalid.value = 1
    dut.tx_valid.value  = 1
    dut.rx_samples_I.value = 0
    dut.rx_samples_Q.value = 0

    hash_low  = await regs.Hash_ID_Low.read()
    hash_high = await regs.Hash_ID_High.read()

    await regs.Fb_FreqWord.write(br_fcw)
    await regs.TX_F1_FreqWord.write(f1_fcw_tx)    
    await regs.TX_F2_FreqWord.write(f2_fcw_tx)    
    await regs.RX_F1_FreqWord.write(f1_fcw_rx)    
    await regs.RX_F2_FreqWord.write(f2_fcw_rx)
    await regs.Rx_Sample_Discard.write((tx_rx_sample_ratio-1 << 8) + tx_rx_sample_ratio-1)
    await regs.LPF_Config_0.write((lpf_alpha << 8))    
    await regs.LPF_Config_1.write((i_shift << 24) + i_gain)    
    await regs.LPF_Config_2.write((p_shift << 24) + p_gain)    
    await regs.Tx_Data_Width.write(tx_data_width)    
    await regs.Rx_Data_Width.write(rx_data_width)    
    await regs.PRBS_Control.write((autosync_threshold << 16) + 1)    
    await regs.PRBS_Polynomial.write((1 << 30) + (1 << 27))    
    await regs.PRBS_Initial_State.write(0x8E7589FD)    
    await regs.PRBS_Error_Mask.write(1)    
    await regs.lowpass_ema_alpha1.write(64)    
    await regs.lowpass_ema_alpha2.write(64)    
    await regs.Tx_Sync_Ctrl.write(0b0001)    
    await regs.Tx_Sync_Cnt.write(192)    


    hash_id  = await regs.Hash_ID_Low.read()
    hash_id  = await regs.Hash_ID_Low.read()
    hash_id  = await regs.Hash_ID_Low.read()
    hash_id  = await regs.Hash_ID_Low.read()
    hash_id  = await regs.Hash_ID_Low.read()
    print("Hash ID Low: ", hex(hash_id))
    hash_id = await regs.Hash_ID_High.read()
    print("Hash ID High: ", hex(hash_id))

    await Timer(100, units="ns")

    await RisingEdge(dut.clk)

    await regs.MSK_Init.write(0)    
    await regs.MSK_Control.write((diff_enc_loopback << 4) + (rx_invert <<2) + ptt)    

    await RisingEdge(dut.clk)

    msksim = msk(dut, dut.clk, dut.tx_samples_I, dut.tx_samples_Q, dut.rx_sample_clk, dut.rx_samples_dec)
    #pn = prbs(dut, dut.clk, axis, tx_data_width, rx_data_width, dut.rx_data, dut.rx_dvalid)

    ducsim = duc(dut, msksim, local_osc, tx_sample_period)
    ddcsim = ddc(dut, msksim, ducsim, local_osc, tx_sample_period)

    await cocotb.start(msksim.tx_sample_capture())
    await cocotb.start(msksim.rx_sample_capture())
    await cocotb.start(ducsim.upconvert())
    await cocotb.start(ddcsim.downconvert())
    await cocotb.start(pn.generate_data())
    await cocotb.start(pn.check_data())

    sim_time = get_sim_time("us")
    sim_start = sim_time
    sim_time_d = sim_time

    dut._log.info("starting...")

    msksim.sim_run = True

    #pn.sim_run = True
    #pn.sync = 100

    while sim_time < run_time: #sim_start + run_time:

        # if sim_time_d <= sim_start + 1000 and sim_time >= sim_start + 1000:
        #     data = await regs.read("msk_top_regs", "PRBS_Control")
        #     data = data | 0x4
        #     dut.s_axi_wvalid.value = 1
        #     dut.s_axi_awvalid.value = 1
        #     await regs.write("msk_top_regs", "PRBS_Control", data)    

        # if sim_time_d <= sim_start + 20000 and sim_time >= sim_start + 20000:
        #     data = await regs.read("msk_top_regs", "PRBS_Control")
        #     data = data ^ 0x8
        #     dut.s_axi_wvalid.value = 1
        #     dut.s_axi_awvalid.value = 1
        #     await regs.write("msk_top_regs", "PRBS_Control", data)    

        if sim_time_d <= sim_start + 20000 and sim_time >= sim_start + 20000:
            data = await regs.PRBS_Control.read()
            data = data | 0x2
            dut.s_axi_wvalid.value = 1
            dut.s_axi_awvalid.value = 1
            await regs.PRBS_Control.write(data)    

        # if sim_time_d <= sim_start + 3000 and sim_time >= sim_start + 3000:
            # await pn.resync()
# 
        # if sim_time_d <= sim_start + 4000 and sim_time >= sim_start + 4000:
            # await pn.resync()

        #await Timer (10, "ms")
        #print("Sim time: ", sim_time, "us")
        #errs = await regs.read("msk_top_regs", "PRBS_Error_Count")
        #print("Bit errors: ", errs)
        #bits = await regs.read("msk_top_regs", "PRBS_Bit_Count")
        #print("Bit count:  ", bits)
        #print("BER:        ", round((1.0*errs)/bits *100, 3), "%")


        sim_time_d = sim_time
        sim_time = get_sim_time("us")

        data = await regs.f1_nco_adjust.read()
        print("F1 NCO Adjust: ", hex(data))
        data = await regs.f2_nco_adjust.read()
        print("F2 NCO Adjust: ", hex(data))
        data = await regs.f1_error.read()
        print("F1 Error: ", hex(data))
        data = await regs.f2_error.read()
        print("F2 Error: ", hex(data))
        #data = await regs.read("msk_top_regs", "LPF_Accum_F1")
        # print("F1 Acc: ", hex(data))
        # data = await regs.read("msk_top_regs", "LPF_Accum_F2")
        # print("F2 Acc: ", hex(data))
        # data = await regs.read("msk_top_regs", "Tx_Bit_Count")
        # print("Tx Bit Count: ", hex(data))
        # data = await regs.read("msk_top_regs", "Tx_Enable_Count")
        # print("Tx Enable Count: ", hex(data))
        # data = await regs.read("msk_top_regs", "MSK_Status")
        # print("MSK Status: ", hex(data))
        # data = await regs.read("msk_top_regs", "axis_xfer_count")
        # print("XFER Count: ", hex(data))
        # data = await regs.read("msk_top_regs", "Tx_Bit_Count")
        # print("Tx Bit Count: ", data)
        # data = await regs.read("msk_top_regs", "Tx_Enable_Count")
        # print("Tx Enabled: ", data)

    msksim.sim_run = False
    #pn.sim_run = False

    await RisingEdge(dut.clk)

    tx_time         = msksim.time

    tx_samples_if_arr   = np.array(msksim.tx_samples_I_arr,  dtype=complex)
    tx_samples_if_cmplx = np.array(msksim.tx_samples_I_arr,  dtype=complex) - 1j * np.array(msksim.tx_samples_Q_arr, dtype=complex)
    tx_samples_fc_cmplx = np.array(ducsim.tx_samples_I_up,   dtype=complex) - 1j * np.array(ducsim.tx_samples_Q_up,  dtype=complex)
    tx_samples_fc_real  = np.array(ducsim.tx_samples_IQ_mod, dtype=int)
    rx_samples_rx_real  = np.array(ddcsim.rx_samples_I_dn,   dtype=int)
    rx_samples_rx_cmplx = np.array(ddcsim.rx_samples_I_dn,   dtype=complex) - 1j * np.array(ddcsim.rx_samples_Q_dn,  dtype=complex)
    rx_samples_rx_dec   = np.array(msksim.rx_samples_arr,    dtype=int)
    #tx_samples_2   = tx_samples_arr * tx_samples_arr

    # print("Ones: ", pn.ones_count)
    # print("Zeros: ", pn.zeros_count)

    errs = await regs.PRBS_Error_Count.read()
    print("Bit errors: ", errs)
    bits = await regs.PRBS_Bit_Count.read()
    print("Bit count:  ", bits)
    print("BER:        ", (1.0*errs)/bits)

    # print("Bit errors: ", pn.err_count)
    # print("Bit count:  ", pn.data_count)
    # print("BER:        ", pn.err_count/pn.data_count)

    if plot:
        blackman_window = np.blackman(len(tx_samples))
    
        fig = plt.figure(figsize=(10, 7), layout='constrained')
        axs = fig.subplot_mosaic([ #["signal", "signal"],
                                   #["magnitude", "log_magnitude"],
                                   ["psd_if_real", "psd_if_real"], 
                                   ["psd_if_cmplx", "psd_if_cmplx"],
                                   ["psd_fc_cmplx", "psd_fc_cmplx"],
                                   ["psd_fc_real", "psd_fc_real"],
                                   ["psd_rx_cmplx", "psd_rx_cmplx"],
                                   ["psd_rx_real", "psd_rx_real"],
                                   ["psd_rx_dec", "psd_rx_dec"]], sharex=True)
        
        # plot time signal:
        # axs["signal"].set_title("MSK Tx Samples")
        # axs["signal"].plot(tx_time, tx_samples_if_arr, color='C0')
        # axs["signal"].set_xlabel("Time (s)")
        # axs["signal"].set_ylabel("Amplitude")
        
        # plot different spectrum types:
        # axs["magnitude"].set_title("Magnitude Spectrum Squared")
        # axs["magnitude"].magnitude_spectrum(tx_samples_2, Fs=tx_sample_rate, window=blackman_window, color='C1')
        
        # axs["log_magnitude"].set_title("Log. Magnitude Spectrum Squared")
        # axs["log_magnitude"].magnitude_spectrum(tx_samples_2, Fs=tx_sample_rate, scale='dB', window=blackman_window, color='C1')
        
        axs["psd_if_real"].set_title("Power Spectral Density - IF - Real - I")
        axs["psd_if_real"].psd(tx_samples_if_arr, Fs=tx_sample_rate, window=np.blackman(FFT), NFFT=FFT, color='C2', sides='twosided')
  
        axs["psd_if_cmplx"].set_title("Power Spectral Density - IF - Complex - I + jQ")
        axs["psd_if_cmplx"].psd(tx_samples_if_cmplx, Fs=tx_sample_rate, window=np.blackman(FFT), NFFT=FFT, color='C2', sides='twosided')
          
        axs["psd_fc_cmplx"].set_title("Power Spectral Density - Fc - Complex - I + jQ")
        axs["psd_fc_cmplx"].psd(tx_samples_fc_cmplx, Fs=tx_sample_rate, window=np.blackman(FFT), NFFT=FFT, color='C2', sides='twosided')

        axs["psd_fc_real"].set_title("Power Spectral Density - Fc - Real - I + Q")
        axs["psd_fc_real"].psd(tx_samples_fc_real, Fs=tx_sample_rate, window=np.blackman(FFT), NFFT=FFT, color='C2', sides='twosided')

        axs["psd_rx_cmplx"].set_title("Power Spectral Density - Rx - Complex - I + jQ")
        axs["psd_rx_cmplx"].psd(rx_samples_rx_cmplx, Fs=tx_sample_rate, window=np.blackman(FFT), NFFT=FFT, color='C2', sides='twosided')

        axs["psd_rx_real"].set_title("Power Spectral Density - Rx - Real - I")
        axs["psd_rx_real"].psd(rx_samples_rx_real, Fs=tx_sample_rate, window=np.blackman(FFT), NFFT=FFT, color='C2', sides='twosided')

        axs["psd_rx_dec"].set_title("Power Spectral Density - Rx - Real - Sample Discard")
        axs["psd_rx_dec"].psd(rx_samples_rx_dec, Fs=rx_sample_rate, window=np.blackman(FFT), NFFT=FFT, color='C2', sides='twosided')

        plt.show()
    
        #fftPlot(np.asarray(tx_samples), dt=1/sample_rate)
