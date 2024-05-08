# test_my_design.py (simple)

import cocotb
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock
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

@cocotb.test()
async def msk_test_1(dut):

    tx_samples = []
    tx_time = []

    await cocotb.start(Clock(dut.clk, 10, units="ns").start())

    bitrate = 1e6
    freq_if = 10e6
    sample_rate = 160e6

    f1 =  9e6
    f2 = 11e6

    FFT = 8192

    await RisingEdge(dut.clk)

    dut.clk.value = 0
    dut.init.value = 1
    dut.freq_word_ft.value = int(bitrate / sample_rate * 2.0**32)
    dut.freq_word_f1.value = int(f1 / sample_rate * 2.0**32);
    dut.freq_word_f2.value = int(f2 / sample_rate * 2.0**32);
    dut.tx_data.value = 0

    await Timer(100, units="ns")

    await RisingEdge(dut.clk)

    dut.init.value = 1

    await RisingEdge(dut.clk)

    dut.init.value = 0

    await RisingEdge(dut.clk)

    sim_time = 0

    dut._log.info("starting...")

    while sim_time < 2000:

        if dut.tx_req.value == 1:
            dut.tx_data.value = random.randrange(1000) % 2

        await RisingEdge(dut.clk)

        tx_samples.append(dut.tx_samples.value.signed_integer)
        tx_time.append(sim_time)

        sim_time = get_sim_time("us")

    # S    = np.fft.fft(tx_samples)
    # freq = np.fft.fftfreq(len(tx_samples), tx_time[1] - tx_time[0])

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
