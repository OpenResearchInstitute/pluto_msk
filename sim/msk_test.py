# test_my_design.py (simple)

import cocotb
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock    import Clock
from cocotb.utils    import get_sim_time

import random
import numpy as np 
import matplotlib.pyplot as plt

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

        await RisingEdge(self.aclk)

        self.dut.s_axis_tvalid.value = 1
        self.tdata.value = data

        while self.tready.value == 0:
            await RisingEdge(self.aclk)

        self.tvalid = 0


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


        self.awaddr.value = 0
        self.awvalid.value = 0

        self.wdata.value = 0
        self.wstrb.value = 0
        self.wvalid.value = 0

        self.bready.value = 0

        self.araddr.value = 0
        self.arvalid.value = 0

        self.rready.value = 0


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


    async def read(self, addr):

        await RisingEdge(self.aclk)

        self.arvalid.value = 1
        self.araddr.value = addr

        self.rready.value = 1

        await RisingEdge(self.aclk)

        while self.rvalid.value == 0 or self.arready.value == 0:
            await RisingEdge(self.aclk)

        self.arvalid = 0

        return self.rdata.value.integer


    async def write(self, addr, data):

        await RisingEdge(self.aclk)

        self.awvalid.value = 1
        self.awaddr.value = addr

        self.wstrb.value = 15
        self.wdata.value = data
        self.wvalid.value = 1

        self.bready.value = 1

        await RisingEdge(self.aclk)

        while self.awready == 0:
            await RisingEdge(self.aclk)

        while self.bvalid.value == 0:
            await RisingEdge(self.aclk)

        self.awvalid.value = 0

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
            self.tx_samples.append(self.tx_sample_bus.value.to_signed())
            self.time.append(get_sim_time("us"))
            await RisingEdge(self.clk)

        self.dut._log.info("...tx sample capture - done")


@cocotb.test()
async def msk_test_1(dut):

    tx_samples = []
    tx_time = []

    bitrate = 1e6
    freq_if = 10e6
    sample_rate = 3*61.46e6
    sample_per = int(1/sample_rate * 1e9)

    await cocotb.start(Clock(dut.clk, sample_per, units="ns").start())

    f1 =  9e6
    f2 = 11e6

    FFT = 8192

    await RisingEdge(dut.clk)

    axi  = axi_bus(dut)
    axis = axis_bus(dut)

    await axi.init()
    await axis.init()

    await axi.write( 0, 1)                                         # tun on init

    await axi.write( 8, 1)                                         # loopback
    await axi.write(12, int(bitrate / sample_rate * 2.0**32))      # bit rate frequency word
    await axi.write(16, int(f1 / sample_rate * 2.0**32))           # F1 frequency word
    await axi.write(20, int(f2 / sample_rate * 2.0**32))           # F2 frequency word
    await axi.write(24, (50 << 16) + 20)                             # p-gain / i-gain
    await axi.write(28, (2 << 16))                                   # low-pass filter alpha

    await Timer(100, units="ns")

    await RisingEdge(dut.clk)

    await axi.write(0, 0)                                         # turn off init

    await RisingEdge(dut.clk)

    await Timer(105, "us")
    await axi.write(4, 1)

    msksim = msk(dut, dut.clk, dut.tx_samples)

    await cocotb.start(msksim.tx_sample_capture())

    sim_time = get_sim_time("us")
    sim_start = sim_time

    dut._log.info("starting...")

    msksim.sim_run = True

    while sim_time < sim_start + 30000:

        await axis.send(random.randrange(1000) % 256)
        sim_time = get_sim_time("us")

    msksim.sim_run = False

    await RisingEdge(dut.clk)

    tx_time        = msksim.time
    tx_samples     = msksim.tx_samples

    tx_samples_arr = np.asarray(tx_samples)
    tx_samples_2   = tx_samples_arr * tx_samples_arr

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
    axs["magnitude"].magnitude_spectrum(tx_samples_2, Fs=sample_rate, window=blackman_window, color='C1')
    
    axs["log_magnitude"].set_title("Log. Magnitude Spectrum Squared")
    axs["log_magnitude"].magnitude_spectrum(tx_samples_2, Fs=sample_rate, scale='dB', window=blackman_window, color='C1')
    
    axs["psd"].set_title("Power Spectral Density")
    axs["psd"].psd(tx_samples, Fs=sample_rate, window=np.blackman(FFT), NFFT=FFT, color='C2')
        
    plt.show()

    #fftPlot(np.asarray(tx_samples), dt=1/sample_rate)
