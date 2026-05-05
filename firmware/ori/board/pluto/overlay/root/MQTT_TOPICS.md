# OVP MQTT Topic Surface

This document describes the MQTT topic structure published by `ovp_status_pub.sh`. Subscribe at `mqtt://<libresdr-ip>:1883` (TCP) or `ws://<libresdr-ip>:9001/wss` (WebSockets, browser-friendly). Anonymous, no auth, broker is `mosquitto`.

## Namespace structure

Pattern A — organized by data source:

```
pluto/status/ovp/register/<name>          Raw hex from devmem
pluto/status/ovp/derived/<name>/<aspect>  Parsed/computed values
pluto/status/ovp/iio/<category>/<attr>    IIO sysfs values
pluto/status/ovp/heartbeat                Liveness signal (ISO 8601 timestamp)
pluto/status/ovp/publisher/<aspect>       Publisher metadata
```

Update rate is approximately 0.5 Hz on the LibreSDR (Z7020 + AD9361). The publisher loop walks ~60 topics per cycle, each invoking `mosquitto_pub` as a separate process, plus a `sleep 1`. Total cycle time is dominated by process-forking overhead and runs slower than the nominal 1 Hz target. Sufficient for visual dashboards; insufficient for catching millisecond-scale transients. A future optimization could use a single persistent broker connection to dramatically increase rate. See `ovp_status_pub.sh`.

Both raw register values and derived values are always published; bandwidth is irrelevant on a LAN and the raw values aid forensic debugging.

## How to subscribe

From a Linux/Mac machine with `mosquitto-clients` installed:

```sh
# All OVP topics
mosquitto_sub -h <libresdr-ip> -t 'pluto/status/ovp/#' -v

# Just the dBFS reading
mosquitto_sub -h <libresdr-ip> -t 'pluto/status/ovp/derived/rx_power/dbfs' -v

# Just AGC state
mosquitto_sub -h <libresdr-ip> -t 'pluto/status/ovp/iio/rx/#' -v
```

From a browser, use Paho MQTT JavaScript library connecting to `ws://<libresdr-ip>:9001/wss`. See `speculator.html` for a reference implementation.

## Raw register topics

Every FPGA register from `0x00` through `0xA8` is published. Topic pattern: `pluto/status/ovp/register/<name>`. Payload is the raw hex string as returned by `devmem` (e.g. `0xAAAA5555`). One topic per register. Useful for forensic captures and for any subscriber that wants its own parsing.

Full register list is in `ovp_status_pub.sh`. Highlights for active monitoring:

| Register | Address | Notes |
|---|---|---|
| `hash_lo` | 0x00 | Should be `0xAAAA5555` if bitstream loaded |
| `hash_hi` | 0x04 | Build hash high word |
| `msk_init` | 0x08 | Init control bits |
| `msk_control` | 0x0C | PTT, loopback, rx_invert, tx_shift |
| `lpf_config_1` | 0x34 | PI controller integral gain + shift |
| `lpf_config_2` | 0x68 | PI controller proportional gain + shift |
| `f1_error` / `f2_error` | 0x74 / 0x78 | Costas loop error signals (signed) |
| `rx_power` | 0x90 | RX power detector EMA output (23-bit) |
| `rx_frame_sync_status` | 0x9C | Frame sync detector state |
| `symbol_lock_status` | 0xA4 | Per-loop lock state bits |
| `symbol_lock_time` | 0xA8 | F1 + F2 first-lock symbol counts (16-bit each) |

## Derived topics

These are pre-parsed for convenient subscription. Topic pattern: `pluto/status/ovp/derived/<area>/<aspect>`.

### Signal health
| Topic | Type | Meaning |
|---|---|---|
| `derived/signature` | string | `OK` if hash_lo matches `0xAAAA5555`, else `WRONG` |
| `derived/rx_power/value` | int | rx_power register as decimal |
| `derived/rx_power/dbfs` | string | Estimated dBFS (e.g. `-55.4`, `-inf`) |
| `derived/rx_power/saturated` | 0/1 | True if value ≥ 6,700,000 (~80% of full scale) |

### MSK init/control
| Topic | Type | Meaning |
|---|---|---|
| `derived/init/txrxinit` | 0/1 | Combined TX/RX init bit |
| `derived/init/txinit` | 0/1 | TX init bit |
| `derived/init/rxinit` | 0/1 | RX init bit |
| `derived/control/ptt` | 0/1 | Push-to-talk enable |
| `derived/control/loopback_ena` | 0/1 | Modem digital TX→RX loopback |
| `derived/control/rx_invert` | 0/1 | RX data invert |
| `derived/control/clear_counts` | 0/1 | Clear status counters (singlepulse) |
| `derived/control/diff_encoder_loopback` | 0/1 | Differential encoder→decoder loopback |
| `derived/control/tx_shift` | 0-7 | TX sample left-shift (0-4 valid) |

### PI controller
| Topic | Type | Meaning |
|---|---|---|
| `derived/pi/i_gain` | int | Integral gain (24 bits) |
| `derived/pi/i_shift` | int | Integral shift (8 bits) |
| `derived/pi/p_gain` | int | Proportional gain (24 bits) |
| `derived/pi/p_shift` | int | Proportional shift (8 bits) |

### Costas loop errors (signed-32 interpretation)
| Topic | Type | Meaning |
|---|---|---|
| `derived/f1_error/signed` | int | F1 loop error, signed |
| `derived/f2_error/signed` | int | F2 loop error, signed |
| `derived/f1_nco_adjust/signed` | int | F1 NCO adjustment, signed |
| `derived/f2_nco_adjust/signed` | int | F2 NCO adjustment, signed |
| `derived/lpf_accum_f1/signed` | int | F1 LPF accumulator, signed |
| `derived/lpf_accum_f2/signed` | int | F2 LPF accumulator, signed |

### Symbol lock state
| Topic | Type | Meaning |
|---|---|---|
| `derived/symlock/f1_locked` | 0/1 | F1 currently locked |
| `derived/symlock/f2_locked` | 0/1 | F2 currently locked |
| `derived/symlock/both_locked` | 0/1 | Both loops locked simultaneously |
| `derived/symlock/f1_unlock_event` | 0/1 | F1 unlocked since last read (cleared on read) |
| `derived/symlock/f2_unlock_event` | 0/1 | F2 unlocked since last read (cleared on read) |
| `derived/symlock/f1_time` | int | Symbols to F1 first lock (or elapsed if not locked) |
| `derived/symlock/f2_time` | int | Symbols to F2 first lock (or elapsed if not locked) |
| `derived/symlock/count` | int | Lock detector window size |
| `derived/symlock/threshold` | int | Lock detector threshold (16-bit; widening pending Item 5) |

Important semantic note on `f1_time`/`f2_time`: these are meaningful only if the corresponding `f{1,2}_locked` bit is true. Otherwise the value represents "elapsed symbols since init with no lock yet" — both counters will read identical values in this state because they free-run from the same init clock until lock latches them. Subscribers should always pair lock state with lock time when displaying.

### Frame sync
| Topic | Type | Meaning |
|---|---|---|
| `derived/frame_sync/locked` | 0/1 | Frame sync detector currently locked |

## IIO topics (AD9361 chip state)

Topic pattern: `pluto/status/ovp/iio/<category>/<attr>`. Values come directly from the AD9361 IIO sysfs interface, with units/suffixes preserved. Numeric versions of `dB`-suffixed attributes have a `_db` suffix in the topic and contain bare numbers.

### RX path
| Topic | Type | Meaning |
|---|---|---|
| `iio/rx/lo_frequency_hz` | int | RX local oscillator frequency in Hz |
| `iio/rx/sampling_frequency` | int | RX sample rate in Hz |
| `iio/rx/rf_bandwidth` | int | RX analog filter bandwidth in Hz |
| `iio/rx/rf_port_select` | string | Active RX port (e.g. `A_BALANCED`) |
| `iio/rx/fir_filter_enabled` | 0/1 | FIR filter on/off |
| `iio/rx/gain_control_mode` | string | `fast_attack`, `slow_attack`, `manual`, `hybrid` |
| `iio/rx/hardwaregain_db` | float | Current LNA+mixer gain in dB |
| `iio/rx/rssi_db` | float | Chip's internal RSSI (high = weak signal) |
| `iio/rx/cal_rf_dc_offset_tracking` | 0/1 | RF DC offset cal tracking enabled |
| `iio/rx/cal_bb_dc_offset_tracking` | 0/1 | BB DC offset cal tracking enabled |
| `iio/rx/cal_quadrature_tracking` | 0/1 | Quadrature cal tracking enabled |

### TX path
| Topic | Type | Meaning |
|---|---|---|
| `iio/tx/lo_frequency_hz` | int | TX local oscillator frequency in Hz |
| `iio/tx/sampling_frequency` | int | TX sample rate in Hz |
| `iio/tx/rf_bandwidth` | int | TX analog filter bandwidth in Hz |
| `iio/tx/rf_port_select` | string | Active TX port |
| `iio/tx/fir_filter_enabled` | 0/1 | FIR filter on/off |
| `iio/tx/hardwaregain_db` | float | TX attenuation in dB (negative = attenuation, e.g. `-10`) |

### System / chip state
| Topic | Type | Meaning |
|---|---|---|
| `iio/system/ensm_mode` | string | Enable State Machine: `fdd`, `tdd`, `alert`, `sleep`, etc. |
| `iio/system/calib_mode` | string | Current calibration mode |
| `iio/system/xo_correction` | int | Crystal oscillator correction value |
| `iio/system/temperature_mdeg` | int | Die temperature in millidegrees |

## Heartbeat and publisher metadata

| Topic | Type | Meaning |
|---|---|---|
| `heartbeat` | ISO 8601 string | Published once per cycle; absence indicates publisher dead |
| `publisher/started` | ISO 8601 string | Published once at startup |
| `publisher/pid` | int | PID of publisher process |
| `publisher/version` | string | Version of `ovp_status_pub.sh` |

## What's NOT here

The `iiostatus_pub.sh` publisher (which runs alongside this one) publishes raw IIO file contents under `pluto/status/iio/<full-sysfs-path>`. That namespace is verbose and inotify-driven; it captures every IIO change but is awkward to subscribe to from a dashboard. For dashboard use, prefer `pluto/status/ovp/iio/...` topics from this publisher, which are organized and continuously refreshed.

The `msk_status.sh` and `msk_cmd.sh` publishers from the original SD card image are no longer started at boot. They used an older register layout and the `pluto/status/msk/...` namespace; the files remain in the overlay as historical artifacts but are not running.

## Adding new topics

To add a new topic, edit `ovp_status_pub.sh`. Two patterns:

For a new register-derived value, add a `case` arm in `publish_registers()` that publishes via `pub_derived "subtopic" "value"`.

For a new IIO attribute, add a `pub_iio "subtopic" "/sys/path"` line in `publish_iio()`. The `pub_iio` helper handles missing-or-unreadable files gracefully.

For attributes returning values with units (like `73.000000 dB`), use the `strip_db` helper to publish a numeric-only `_db`-suffixed topic alongside the raw one.

After editing, sanity-check with `sh -n ovp_status_pub.sh` before deploying. Increment the `publisher/version` string when shipping changes; subscribers can use it to detect stale publisher versions.
