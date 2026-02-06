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
        self.tvalid         = dut.s_axis_tvalid
        self.tready         = dut.s_axis_tready
        self.tdata          = dut.s_axis_tdata
        self.tlast          = dut.s_axis_tlast
        self.tkeep          = dut.s_axis_tkeep

        self.aresetn.value  = 1
        self.tvalid.value   = 0 
        self.tdata.value    = 0 

    async def init(self):
        await self._clock();
        await self._reset();

    async def _clock(self):

        self.dut._log.info("starting aclk with period %d %s ..." % (self.aclk_per, self.aclk_per_units))
        self.aclk_clk = Clock(self.aclk, self.aclk_per, unit=self.aclk_per_units)
        self.aclk_clk.start()
        self.dut._log.info("...aclk started")

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

        self.dut._log.info("starting aclk with period %d %s ..." % (self.aclk_per, self.aclk_per_units))
        self.aclk_clk = Clock(self.aclk, self.aclk_per, unit=self.aclk_per_units)
        self.aclk_clk.start()
        self.dut._log.info("...aclk started")

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
        await RisingEdge(self.aclk)
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

        read_data = self.rdata.value

        await RisingEdge(self.aclk)

        return read_data


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
            if self.rx_sample_clk.value == 1:
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
                rx_data = self.rx_data.value
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

    dut._log.info("msk_test_1 starting...")

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

    print("Instantiate registers...")
    axi  = axi_bus(dut)
    regs = msk_top_regs_cls(callbacks=AsyncCallbackSet(read_callback=axi.read, write_callback=axi.write))

    tx_samples = []
    tx_time = []

    tx_sample_per = int(round(1/tx_sample_rate * 1e14))*10

    rx_sample_rate = tx_sample_rate / tx_rx_sample_ratio

    tx_data_width = 8
    rx_data_width = 8

    dut._log.info("starting clock...")
    clk_mdm = Clock(dut.clk, tx_sample_per, unit="fs")
    clk_mdm.start()
    dut._log.info("... clock started")

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

    dut._log.info("instantiating AXI bus...")
    axis = axis_bus(dut)

    await axi.init()
    await axis.init()
    
    dut._log.info("configuring...")
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
    await regs.symbol_lock_control.write((11000 << 10) + 100)


    hash_id  = await regs.Hash_ID_Low.read()
    hash_id  = await regs.Hash_ID_Low.read()
    hash_id  = await regs.Hash_ID_Low.read()
    hash_id  = await regs.Hash_ID_Low.read()
    hash_id  = await regs.Hash_ID_Low.read()
    print("Hash ID Low: ", hex(hash_id))
    hash_id  = await regs.Hash_ID_High.read()
    print("Hash ID High: ", hex(hash_id))

    ltf1f2 = await regs.symbol_lock_time.read()
    print("F1 lock time: ", ltf1f2[15:0].to_unsigned())
    print("f2 lock time: ", ltf1f2[31:15].to_unsigned())

    await Timer(100, unit="ns")

    await RisingEdge(dut.clk)

    dut._log.info("releasing init...")
    await regs.MSK_Init.write(0)    
    dut._log.info("asserting ptt...")
    await regs.MSK_Control.write((diff_enc_loopback << 4) + (rx_invert <<2) + ptt)    

    await RisingEdge(dut.clk)

    msksim = msk(dut, dut.clk, dut.tx_samples_I, dut.tx_samples_Q, dut.rx_sample_clk, dut.rx_samples_dec)
    pn = prbs(dut, dut.clk, axis, tx_data_width, rx_data_width, dut.m_axis_tdata, dut.m_axis_tvalid)

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

    pn.sim_run = True
    pn.sync = 100

    while sim_time < run_time: #sim_start + run_time:

        # if sim_time_d <= sim_start + 1000 and sim_time >= sim_start + 1000:
        #     data = await regs.read("msk_top_regs", "PRBS_Control")
        #     data = data | 0x4
        #     dut.s_axi_wvalid.value = 1
        #     dut.s_axi_awvalid.value = 1
        #     await regs.write("msk_top_regs", "PRBS_Control", data)    

        # if sim_time_d <= sim_start + 30000 and sim_time >= sim_start + 30000:
        #     data = await regs.tx_async_fifo_rd_wr_ptr.read()
        #     print("Tx FIFO Pointers", hex(data))
        #     data = await regs.rx_async_fifo_rd_wr_ptr.read()
        #     print("Rx FIFO Pointers", hex(data))

        if sim_time_d <= sim_start + 20000 and sim_time >= sim_start + 20000:
            data = await regs.PRBS_Control.read()
            data = data.to_unsigned() | 0x2
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

        await regs.f1_nco_adjust.write(0)
        data = await regs.f1_nco_adjust.read()
        print("F1 NCO Adjust: ", hex(data))
        await regs.f2_nco_adjust.write(0)
        data = await regs.f2_nco_adjust.read()
        print("F2 NCO Adjust: ", hex(data))
        await regs.f1_error.write(0)
        data = await regs.f1_error.read()
        print("F1 Error: ", hex(data))
        await regs.f2_error.write(0)
        data = await regs.f2_error.read()
        print("F2 Error: ", hex(data))
        await regs.tx_async_fifo_rd_wr_ptr.write(0)
        data = await regs.tx_async_fifo_rd_wr_ptr.read()
        print("Tx FIFO Pointers", hex(data))
        await regs.rx_async_fifo_rd_wr_ptr.write(0)
        data = await regs.rx_async_fifo_rd_wr_ptr.read()
        print("Rx FIFO Pointers", hex(data))
        await regs.rx_power.write(0)
        data = await regs.rx_power.read()
        print("Rx Power", hex(data))
        await regs.rx_frame_sync_status.write(0xFFFF_0000)
        data = await regs.rx_frame_sync_status.read()
        print("Frame Sync Status", hex(data))
        data = await regs.symbol_lock_status.read()
        print("Raw lock data: ", data.to_unsigned())
        print("F1 and F2 Lock", data[0])
        print("F1 Lock", data[1])
        print("F1 Lock", data[2])
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

    await regs.PRBS_Error_Count.write(0)
    errs = await regs.PRBS_Error_Count.read()
    print("Bit errors: ", errs.to_unsigned())
    await regs.PRBS_Bit_Count.write(0)
    bits = await regs.PRBS_Bit_Count.read()
    print("Bit count:  ", bits.to_unsigned())
    print("BER:        ", (1.0*errs.to_unsigned())/bits.to_unsigned())
    ltf1f2 = await regs.symbol_lock_time.read()
    print("F1 lock time: ", ltf1f2[15:0].to_unsigned())
    print("f2 lock time: ", ltf1f2[31:16].to_unsigned())

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


#------------------------------------------------------------------------------------------------------
#  Register Read/Write Test
#
#  Exercises all registers through the AXI-Lite CDC bridge.
#  - RW config registers: write a value, read it back, verify match
#  - RO status registers: read and verify no error
#  - Write-to-capture status registers: write (trigger capture), read back
#------------------------------------------------------------------------------------------------------

@cocotb.test()
async def reg_rw_test(dut):
    """Read and write all registers through the AXI-Lite CDC bridge."""

    tx_sample_rate = 61.44e6
    tx_sample_per = int(round(1/tx_sample_rate * 1e14))*10

    await cocotb.start(Clock(dut.clk, tx_sample_per, units="fs").start())

    axi  = axi_bus(dut)
    regs = msk_top_regs_cls(callbacks=AsyncCallbackSet(read_callback=axi.read, write_callback=axi.write))

    axis = axis_bus(dut)

    await axi.init()
    await axis.init()

    # Drive required input signals to known states
    dut.tx_enable.value = 1
    dut.rx_enable.value = 1
    dut.rx_svalid.value = 0
    dut.tx_valid.value  = 0
    dut.rx_samples_I.value = 0
    dut.rx_samples_Q.value = 0
    dut.s_axis_tvalid.value = 0
    dut.s_axis_tdata.value = 0
    dut.s_axis_tlast.value = 0
    dut.s_axis_tkeep.value = 0
    dut.m_axis_tready.value = 0

    await Timer(200, units="ns")

    errors = 0

    #------------------------------------------------------------------
    # 1. Read-only registers (Hash IDs)
    #------------------------------------------------------------------
    dut._log.info("--- Read-only registers ---")

    val = await regs.Hash_ID_Low.read()
    dut._log.info("Hash_ID_Low  = 0x%08X" % val)
    if val != 0xAAAA5555:
        dut._log.error("Hash_ID_Low mismatch: expected 0xAAAA5555, got 0x%08X" % val)
        errors += 1

    val = await regs.Hash_ID_High.read()
    dut._log.info("Hash_ID_High = 0x%08X" % val)
    if val != 0xFFFFCCCC:
        dut._log.error("Hash_ID_High mismatch: expected 0xFFFFCCCC, got 0x%08X" % val)
        errors += 1

    #------------------------------------------------------------------
    # 2. RW config registers — write then read back
    #------------------------------------------------------------------
    dut._log.info("--- RW config register write/readback ---")

    rw_tests = [
        # (register, write_value, readback_mask, name)
        (regs.MSK_Init,           0x00000007, 0x00000007, "MSK_Init"),
        (regs.MSK_Control,        0x00000013, 0x00000013, "MSK_Control"),
        (regs.Fb_FreqWord,        0x12345678, 0xFFFFFFFF, "Fb_FreqWord"),
        (regs.TX_F1_FreqWord,     0xABCD0001, 0xFFFFFFFF, "TX_F1_FreqWord"),
        (regs.TX_F2_FreqWord,     0xABCD0002, 0xFFFFFFFF, "TX_F2_FreqWord"),
        (regs.RX_F1_FreqWord,     0xABCD0003, 0xFFFFFFFF, "RX_F1_FreqWord"),
        (regs.RX_F2_FreqWord,     0xABCD0004, 0xFFFFFFFF, "RX_F2_FreqWord"),
        (regs.LPF_Config_0,       0x00000A03, 0xFFFFFF03, "LPF_Config_0"),
        (regs.LPF_Config_1,       0x0A000080, 0xFFFFFFFF, "LPF_Config_1"),
        (regs.LPF_Config_2,       0x05000050, 0xFFFFFFFF, "LPF_Config_2"),
        (regs.Tx_Data_Width,      0x00000010, 0x000000FF, "Tx_Data_Width"),
        (regs.Rx_Data_Width,      0x00000008, 0x000000FF, "Rx_Data_Width"),
        (regs.Rx_Sample_Discard,  0x00001818, 0x0000FFFF, "Rx_Sample_Discard"),
        (regs.PRBS_Control,       0x00320001, 0x00FF0001, "PRBS_Control"),
        (regs.PRBS_Initial_State, 0x8E7589FD, 0xFFFFFFFF, "PRBS_Initial_State"),
        (regs.PRBS_Polynomial,    0x48000000, 0xFFFFFFFF, "PRBS_Polynomial"),
        (regs.PRBS_Error_Mask,    0x00000001, 0xFFFFFFFF, "PRBS_Error_Mask"),
        (regs.Tx_Sync_Ctrl,       0x00000003, 0x00000003, "Tx_Sync_Ctrl"),
        (regs.Tx_Sync_Cnt,        0x000000C0, 0x00FFFFFF, "Tx_Sync_Cnt"),
        (regs.lowpass_ema_alpha1,  0x00000040, 0x0003FFFF, "lowpass_ema_alpha1"),
        (regs.lowpass_ema_alpha2,  0x00000080, 0x0003FFFF, "lowpass_ema_alpha2"),
    ]

    for reg, wr_val, mask, name in rw_tests:
        await reg.write(wr_val)
        rd_val = await reg.read()
        expected = wr_val & mask
        actual = rd_val & mask
        if actual != expected:
            dut._log.error("%s: wrote 0x%08X, read 0x%08X (expected 0x%08X, mask 0x%08X)"
                           % (name, wr_val, rd_val, expected, mask))
            errors += 1
        else:
            dut._log.info("%s: OK (0x%08X)" % (name, actual))

    #------------------------------------------------------------------
    # 3. RO status register — just read (driven by HW)
    #------------------------------------------------------------------
    dut._log.info("--- RO status register read ---")

    val = await regs.MSK_Status.read()
    dut._log.info("MSK_Status = 0x%08X (tx_enable=%d, rx_enable=%d)"
                  % (val, (val >> 1) & 1, (val >> 2) & 1))

    #------------------------------------------------------------------
    # 4. Write-to-capture status registers
    #    Write triggers data_capture snapshot; read returns captured value
    #------------------------------------------------------------------
    dut._log.info("--- Write-to-capture registers ---")

    wtc_regs = [
        (regs.Tx_Bit_Count,        "Tx_Bit_Count"),
        (regs.Tx_Enable_Count,     "Tx_Enable_Count"),
        (regs.PRBS_Bit_Count,      "PRBS_Bit_Count"),
        (regs.PRBS_Error_Count,    "PRBS_Error_Count"),
        (regs.LPF_Accum_F1,       "LPF_Accum_F1"),
        (regs.LPF_Accum_F2,       "LPF_Accum_F2"),
        (regs.axis_xfer_count,     "axis_xfer_count"),
        (regs.f1_nco_adjust,       "f1_nco_adjust"),
        (regs.f2_nco_adjust,       "f2_nco_adjust"),
        (regs.f1_error,            "f1_error"),
        (regs.f2_error,            "f2_error"),
        (regs.rx_power,            "rx_power"),
    ]

    for reg, name in wtc_regs:
        # Write any value to trigger capture
        await reg.write(0)
        # Read back captured value
        val = await reg.read()
        dut._log.info("%s: captured 0x%08X" % (name, val))

    #------------------------------------------------------------------
    # 5. FIFO pointer registers (write-to-capture with FIFO handshake)
    #------------------------------------------------------------------
    dut._log.info("--- FIFO pointer registers ---")

    await regs.tx_async_fifo_rd_wr_ptr.write(0)
    await Timer(500, units="ns")
    val = await regs.tx_async_fifo_rd_wr_ptr.read()
    dut._log.info("tx_async_fifo_rd_wr_ptr: 0x%08X" % val)

    await regs.rx_async_fifo_rd_wr_ptr.write(0)
    await Timer(500, units="ns")
    val = await regs.rx_async_fifo_rd_wr_ptr.read()
    dut._log.info("rx_async_fifo_rd_wr_ptr: 0x%08X" % val)

    #------------------------------------------------------------------
    # 6. Frame sync status register
    #------------------------------------------------------------------
    dut._log.info("--- Frame sync status ---")
    val = await regs.rx_frame_sync_status.read()
    dut._log.info("rx_frame_sync_status: 0x%08X" % val)

    #------------------------------------------------------------------
    # 7. Second pass — verify config registers survive multiple accesses
    #------------------------------------------------------------------
    dut._log.info("--- Re-read config registers (stability check) ---")

    # Write known patterns, read back twice to confirm stability
    await regs.Fb_FreqWord.write(0xCAFEBABE)
    rd1 = await regs.Fb_FreqWord.read()
    rd2 = await regs.Fb_FreqWord.read()
    if rd1 != rd2 or rd1 != 0xCAFEBABE:
        dut._log.error("Fb_FreqWord stability: rd1=0x%08X rd2=0x%08X expected 0xCAFEBABE" % (rd1, rd2))
        errors += 1
    else:
        dut._log.info("Fb_FreqWord stability: OK (0x%08X)" % rd1)

    await regs.PRBS_Initial_State.write(0x55AA55AA)
    rd1 = await regs.PRBS_Initial_State.read()
    rd2 = await regs.PRBS_Initial_State.read()
    if rd1 != rd2 or rd1 != 0x55AA55AA:
        dut._log.error("PRBS_Initial_State stability: rd1=0x%08X rd2=0x%08X expected 0x55AA55AA" % (rd1, rd2))
        errors += 1
    else:
        dut._log.info("PRBS_Initial_State stability: OK (0x%08X)" % rd1)

    #------------------------------------------------------------------
    # Done
    #------------------------------------------------------------------
    dut._log.info("Register test complete: %d error(s)" % errors)
    assert errors == 0, "Register read/write test failed with %d error(s)" % errors
