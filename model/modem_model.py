"""
Top-level MSK modem loopback model.

Chains: PRBS Generator -> MSK Modulator -> MSK Demodulator -> PRBS Monitor

Matches the RTL loopback path in msk_top.vhd:
  - PRBS gen output feeds modulator tx_data input
  - Modulator I samples are sign-extended to 16 bits, truncated to 12 bits
  - Sample decimation (discard counter) generates rx_sample_clk
  - Demodulator receives decimated samples
  - Demodulator rx_bit feeds PRBS monitor

Each call to step() models one clock cycle. The model can run indefinitely.

Usage:
    python modem_model.py [--clocks N] [--fixed]
"""

import os
import sys
import argparse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from model_utils import signed, unsigned
from prbs.model.prbs import PrbsGenerator, PrbsMonitor
from msk_modulator.model.msk_modulator import MskModulator
from msk_demodulator.model.msk_demodulator import MskDemodulator


class ModemModel:
    """Top-level MSK modem with PRBS loopback — one step() per clock cycle."""

    def __init__(self, fixed_point=True,
                 # Modem parameters
                 nco_w=32, phase_w=10, sinusoid_w=12, sample_w=16,
                 acc_w=32, gain_w=24, shift_w=8, data_w=16,
                 # PRBS parameters
                 generator_w=31, counter_w=32,
                 # Sync
                 sync_cnt_w=24):

        self.fixed_point = fixed_point
        self.NCO_W = nco_w
        self.SAMPLE_W = sample_w
        self.SINUSOID_W = sinusoid_w

        # Submodule instances
        self.prbs_gen = PrbsGenerator(data_w=1, generator_w=generator_w,
                                      toggle_control=True)
        self.prbs_mon = PrbsMonitor(data_w=1, generator_w=generator_w,
                                    counter_w=counter_w, toggle_control=True)
        self.modulator = MskModulator(nco_w=nco_w, phase_w=phase_w,
                                      sinusoid_w=sinusoid_w, sample_w=sample_w,
                                      sync_cnt_w=sync_cnt_w,
                                      fixed_point=fixed_point)
        self.demodulator = MskDemodulator(nco_w=nco_w, acc_w=acc_w,
                                          phase_w=phase_w,
                                          sinusoid_w=sinusoid_w,
                                          sample_w=12,  # RTL uses 12-bit RX
                                          data_w=data_w, gain_w=gain_w,
                                          shift_w=shift_w,
                                          fixed_point=fixed_point)

        # Configuration registers (set via configure())
        self.cfg = {
            # Frequency control words
            'freq_word_tclk': 0,
            'freq_word_tx_f1': 0,
            'freq_word_tx_f2': 0,
            'freq_word_rx_f1': 0,
            'freq_word_rx_f2': 0,
            # Loop filter
            'lpf_p_gain': 80,
            'lpf_i_gain': 9,
            'lpf_p_shift': 5,
            'lpf_i_shift': 9,
            'lpf_alpha': 0,
            'lpf_freeze': 0,
            'lpf_zero': 0,
            # PRBS
            'prbs_polynomial': (1 << 30) | (1 << 27),
            'prbs_initial_state': 0x8E7589FD,
            'prbs_sel': 1,
            'prbs_error_mask': 1,
            'prbs_autosync_threshold': 50,
            # Control
            'ptt': 1,
            'tx_enable': 1,
            'rx_enable': 1,
            'tx_sync_ena': 1,
            'tx_sync_cnt': 192,
            'tx_sync_force': 0,
            # Sample decimation
            'discard_rxsamples': 24,  # tx_rx_sample_ratio - 1
            'discard_rxnco': 0,
            # Lock detector
            'symbol_lock_count': 100,
            'symbol_lock_threshold': 11000,
        }

        # Internal state
        self.clock_count = 0
        self.discard_count = 0
        self.rx_sample_clk = 0
        self.rx_samples_dec = 0
        self.tx_req = 0
        self.prbs_data_bit = 0
        self.rx_bit = 0
        self.rx_dvalid = 0
        self.prbs_manual_sync = 0

    def configure(self, **kwargs):
        """Update configuration parameters. Call before reset() or during operation."""
        for k, v in kwargs.items():
            if k not in self.cfg:
                raise KeyError(f"Unknown config parameter: {k}")
            self.cfg[k] = v

    def configure_from_frequencies(self, bitrate=54200, freq_if_mult=32,
                                   rx_offset=100, tx_sample_rate=61.44e6,
                                   tx_rx_sample_ratio=25):
        """Compute frequency control words from physical parameters.

        Matches the cocotb testbench configuration.
        """
        delta_f = bitrate / 4
        freq_if = bitrate / 4 * freq_if_mult

        f1 = freq_if - delta_f
        f2 = freq_if + delta_f

        br_fcw = int(bitrate / tx_sample_rate * 2.0**32)
        f1_fcw_tx = int(f1 / tx_sample_rate * 2.0**32)
        f2_fcw_tx = int(f2 / tx_sample_rate * 2.0**32)
        f1_fcw_rx = int((f1 + rx_offset) / tx_sample_rate * 2.0**32)
        f2_fcw_rx = int((f2 + rx_offset) / tx_sample_rate * 2.0**32)

        self.configure(
            freq_word_tclk=br_fcw,
            freq_word_tx_f1=f1_fcw_tx,
            freq_word_tx_f2=f2_fcw_tx,
            freq_word_rx_f1=f1_fcw_rx,
            freq_word_rx_f2=f2_fcw_rx,
            discard_rxsamples=tx_rx_sample_ratio - 1,
            discard_rxnco=0,
        )

        return {
            'bitrate': bitrate,
            'freq_if': freq_if,
            'f1': f1, 'f2': f2,
            'br_fcw': br_fcw,
            'f1_fcw_tx': f1_fcw_tx, 'f2_fcw_tx': f2_fcw_tx,
            'f1_fcw_rx': f1_fcw_rx, 'f2_fcw_rx': f2_fcw_rx,
            'tx_rx_sample_ratio': tx_rx_sample_ratio,
        }

    def reset(self):
        """Reset all submodules. Call after configure()."""
        cfg = self.cfg

        self.prbs_gen.reset(
            initial_state=cfg['prbs_initial_state'],
            polynomial=cfg['prbs_polynomial']
        )
        self.prbs_mon.reset(
            initial_state=cfg['prbs_initial_state'],
            polynomial=cfg['prbs_polynomial']
        )
        self.modulator.reset()
        self.demodulator.reset()

        self.clock_count = 0
        self.discard_count = 0
        self.rx_sample_clk = 0
        self.rx_samples_dec = 0
        self.tx_req = 0
        self.prbs_data_bit = 0
        self.rx_bit = 0
        self.rx_dvalid = 0
        self.prbs_manual_sync = 0

    def step(self):
        """Execute one clock cycle. Returns dict with all observable outputs."""
        cfg = self.cfg

        # -- PRBS Generator --
        # tx_req comes from modulator (previous cycle output)
        gen_out = self.prbs_gen.step(
            data_req=self.tx_req,
            prbs_sel=cfg['prbs_sel'],
            data_in=0,
            error_insert=0,
            error_mask=cfg['prbs_error_mask'],
        )
        self.prbs_data_bit = gen_out['data_out']

        # -- MSK Modulator --
        mod_out = self.modulator.step(
            tx_data=self.prbs_data_bit,
            tx_enable=cfg['tx_enable'],
            tx_valid=1,  # Always valid in loopback
            ptt=cfg['ptt'],
            freq_word_tclk=cfg['freq_word_tclk'],
            freq_word_f1=cfg['freq_word_tx_f1'],
            freq_word_f2=cfg['freq_word_tx_f2'],
            tx_sync_ena=cfg['tx_sync_ena'],
            tx_sync_cnt=cfg['tx_sync_cnt'],
            tx_sync_force=cfg['tx_sync_force'],
        )
        self.tx_req = mod_out['tx_req']
        tx_I = mod_out['tx_samples_I']

        # -- Loopback path: TX I -> RX samples --
        # RTL: rx_samples_mux <= resize(signed(tx_samples_I_int), 16)
        #      rx_samples_dec <= rx_samples_mux(11 downto 0)
        if self.fixed_point:
            rx_mux = signed(tx_I, self.SAMPLE_W)
            rx_dec = signed(rx_mux, 12)  # truncate to 12 bits
        else:
            rx_dec = tx_I

        # -- RX sample decimation (discard counter) --
        # RTL: if discard_count = 0 then sample; else decrement
        if self.discard_count == 0:
            self.discard_count = cfg['discard_rxsamples']
            self.rx_samples_dec = rx_dec
            self.rx_sample_clk = 1
        else:
            self.discard_count -= 1
            self.rx_sample_clk = 0

        # -- MSK Demodulator --
        demod_out = self.demodulator.step(
            rx_samples=self.rx_samples_dec,
            rx_enable=cfg['rx_enable'],
            rx_svalid=self.rx_sample_clk,
            rx_freq_word_f1=cfg['freq_word_rx_f1'],
            rx_freq_word_f2=cfg['freq_word_rx_f2'],
            discard_rxnco=cfg['discard_rxnco'],
            lpf_p_gain=cfg['lpf_p_gain'],
            lpf_i_gain=cfg['lpf_i_gain'],
            lpf_p_shift=cfg['lpf_p_shift'],
            lpf_i_shift=cfg['lpf_i_shift'],
            lpf_alpha=cfg['lpf_alpha'],
            lpf_freeze=cfg['lpf_freeze'],
            lpf_zero=cfg['lpf_zero'],
            symbol_lock_count=cfg['symbol_lock_count'],
            symbol_lock_threshold=cfg['symbol_lock_threshold'],
        )
        self.rx_bit = demod_out['rx_data']
        self.rx_dvalid = demod_out['rx_dvalid']

        # -- PRBS Monitor --
        mon_out = self.prbs_mon.step(
            data_in=self.rx_bit,
            data_in_valid=self.rx_dvalid,
            sync_manual=self.prbs_manual_sync,
            sync_threshold=cfg['prbs_autosync_threshold'],
            count_reset=0,
        )

        self.clock_count += 1

        return {
            # TX side
            'tx_req': self.tx_req,
            'tx_data': self.prbs_data_bit,
            'tx_I': tx_I,
            'tx_Q': mod_out['tx_samples_Q'],
            # Loopback
            'rx_sample_clk': self.rx_sample_clk,
            'rx_samples_dec': self.rx_samples_dec,
            # RX side
            'rx_bit': self.rx_bit,
            'rx_dvalid': self.rx_dvalid,
            'rx_soft': demod_out['rx_data_soft'],
            # Costas loop status
            'lpf_accum_f1': demod_out['lpf_accum_f1'],
            'lpf_accum_f2': demod_out['lpf_accum_f2'],
            'f1_nco_adjust': demod_out['f1_nco_adjust'],
            'f2_nco_adjust': demod_out['f2_nco_adjust'],
            'cst_lock_f1': demod_out['cst_lock_f1'],
            'cst_lock_f2': demod_out['cst_lock_f2'],
            # BER
            'prbs_data_count': mon_out['data_count'],
            'prbs_error_count': mon_out['error_count'],
            # Clock
            'clock': self.clock_count,
        }

    def trigger_prbs_sync(self):
        """Trigger a manual PRBS sync (toggle-controlled)."""
        self.prbs_manual_sync = 1 - self.prbs_manual_sync

    def run(self, num_clocks, report_interval=None, callback=None):
        """Run the model for num_clocks cycles.

        Args:
            num_clocks: Number of clock cycles to simulate.
            report_interval: Print status every N clocks. None = no periodic reports.
            callback: Optional function(clock, outputs) called each cycle.
                      Return False from callback to stop early.

        Returns:
            Final cycle's output dict.
        """
        out = None
        for _ in range(num_clocks):
            out = self.step()

            if callback is not None:
                if callback(self.clock_count, out) is False:
                    break

            if report_interval and self.clock_count % report_interval == 0:
                print(f"  clk={self.clock_count:>10d}  "
                      f"bits={out['prbs_data_count']:>8d}  "
                      f"errors={out['prbs_error_count']:>6d}  "
                      f"lock_f1={out['cst_lock_f1']}  "
                      f"lock_f2={out['cst_lock_f2']}")

        return out


def main():
    parser = argparse.ArgumentParser(description='MSK Modem Loopback Model')
    parser.add_argument('--clocks', type=int, default=500_000,
                        help='Number of clock cycles to simulate (default: 500000)')
    parser.add_argument('--fixed', action='store_true', default=True,
                        help='Use fixed-point mode (default)')
    parser.add_argument('--float', action='store_true',
                        help='Use floating-point mode')
    parser.add_argument('--bitrate', type=float, default=54200,
                        help='Bit rate in bps (default: 54200)')
    parser.add_argument('--rx-offset', type=float, default=100,
                        help='RX frequency offset in Hz (default: 100)')
    parser.add_argument('--report', type=int, default=50_000,
                        help='Report interval in clocks (default: 50000)')
    args = parser.parse_args()

    fixed = not args.float

    print(f"MSK Modem Loopback Model ({'fixed-point' if fixed else 'floating-point'})")
    print(f"  Simulating {args.clocks:,} clock cycles")
    print()

    modem = ModemModel(fixed_point=fixed)
    freqs = modem.configure_from_frequencies(
        bitrate=args.bitrate,
        rx_offset=args.rx_offset,
    )

    print(f"  Bitrate:       {freqs['bitrate']:.0f} bps")
    print(f"  IF frequency:  {freqs['freq_if']:.0f} Hz")
    print(f"  F1 (mark):     {freqs['f1']:.0f} Hz")
    print(f"  F2 (space):    {freqs['f2']:.0f} Hz")
    print(f"  TX/RX ratio:   {freqs['tx_rx_sample_ratio']}")
    print(f"  BR FCW:        0x{freqs['br_fcw']:08x}")
    print(f"  TX F1 FCW:     0x{freqs['f1_fcw_tx']:08x}")
    print(f"  TX F2 FCW:     0x{freqs['f2_fcw_tx']:08x}")
    print(f"  RX F1 FCW:     0x{freqs['f1_fcw_rx']:08x}")
    print(f"  RX F2 FCW:     0x{freqs['f2_fcw_rx']:08x}")
    print()

    modem.reset()

    # Trigger initial PRBS sync after a few clocks of settling
    sync_triggered = False

    def on_cycle(clock, out):
        nonlocal sync_triggered
        if clock == 1000 and not sync_triggered:
            modem.trigger_prbs_sync()
            sync_triggered = True
            print(f"  [clk {clock}] PRBS sync triggered")

    print("Running simulation...")
    print(f"  {'clk':>10s}  {'bits':>8s}  {'errors':>6s}  lock_f1  lock_f2")
    print(f"  {'-'*10}  {'-'*8}  {'-'*6}  -------  -------")

    out = modem.run(args.clocks, report_interval=args.report, callback=on_cycle)

    print()
    print("Final results:")
    print(f"  Clock cycles:  {modem.clock_count:,}")
    print(f"  PRBS bits:     {out['prbs_data_count']:,}")
    print(f"  PRBS errors:   {out['prbs_error_count']:,}")
    print(f"  F1 lock:       {out['cst_lock_f1']}")
    print(f"  F2 lock:       {out['cst_lock_f2']}")

    if out['prbs_data_count'] > 0:
        ber = out['prbs_error_count'] / out['prbs_data_count']
        print(f"  BER:           {ber:.2e}")
    else:
        print(f"  BER:           N/A (no bits received)")


if __name__ == "__main__":
    main()
