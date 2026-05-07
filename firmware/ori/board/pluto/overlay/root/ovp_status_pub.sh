#!/bin/sh
#
# ovp_status_pub.sh - canonical OVP telemetry publisher
#
# Publishes everything useful about the running OVP modem and AD9361 chip
# state to MQTT. Subscribers (Speculator, future dashboards, monitoring
# tools, etc.) build on this single source of truth.
#
# TOPIC STRUCTURE (Pattern A - by source):
#
#   pluto/status/ovp/register/<name>          Raw hex from devmem
#   pluto/status/ovp/derived/<name>/<aspect>  Parsed/computed values
#   pluto/status/ovp/iio/<category>/<attr>    IIO sysfs values
#   pluto/status/ovp/heartbeat                Liveness signal (timestamp)
#   pluto/status/ovp/publisher/<aspect>       Publisher metadata
#
# Update rate: 1 Hz uniform. May be split into multiple rates later if
# dashboards need finer time resolution for dynamic indicators.
#
# Both raw register hex AND parsed values are published. Bandwidth on a
# LAN is irrelevant; raw values aid forensic debugging.
#
# History:
#   This file replaces the original msk_status.sh which used the wrong
#   register layout for the current OVP build. The msk_status.sh in the
#   overlay is kept for now as a historical artifact but is not started
#   at boot. See S95bgcript.

set -u

ADDR_BASE=0x43C00000
RX_POWER_MAX=8388607   # 23-bit field maximum
INTERVAL=1             # seconds between publish cycles

# =====================================================================
# Register table
# =====================================================================
# Format: "offset:friendly_name"
# Every register the modem exposes that's potentially interesting.
# Listed in address order so output is predictable.
REGISTERS="
0x00:hash_lo
0x04:hash_hi
0x08:msk_init
0x0c:msk_control
0x10:msk_status
0x14:tx_bit_count
0x18:tx_enable_count
0x1c:fb_freqword
0x20:tx_f1_freqword
0x24:tx_f2_freqword
0x28:rx_f1_freqword
0x2c:rx_f2_freqword
0x30:lpf_config_0
0x34:lpf_config_1
0x38:tx_data_width
0x3c:rx_data_width
0x40:prbs_control
0x44:prbs_initial_state
0x48:prbs_polynomial
0x4c:prbs_error_mask
0x50:prbs_bit_count
0x54:prbs_error_count
0x58:lpf_accum_f1
0x5c:lpf_accum_f2
0x60:axis_xfer_count
0x64:rx_sample_discard
0x68:lpf_config_2
0x6c:f1_nco_adjust
0x70:f2_nco_adjust
0x74:f1_error
0x78:f2_error
0x7c:tx_sync_ctrl
0x80:tx_sync_cnt
0x84:tx_sync_pat
0x88:lowpass_ema_alpha1
0x8c:lowpass_ema_alpha2
0x90:rx_power
0x94:tx_async_fifo_rd_wr_ptr
0x98:rx_async_fifo_rd_wr_ptr
0x9c:rx_frame_sync_status
0xa0:symbol_lock_control
0xa4:symbol_lock_status
0xa8:symbol_lock_time
"

# =====================================================================
# Helpers
# =====================================================================

# Convert rx_power register value (decimal) to dBFS string.
# Uses integer math approximation since busybox awk often lacks log().
# Worst case error ~0.5 dB across the range; sufficient for verdicts.
to_dbfs() {
    P=$1
    if [ "$P" -le 0 ]; then
        echo "-inf"
        return
    fi
    BITS=0
    TMP=$P
    while [ $TMP -gt 1 ]; do
        TMP=$((TMP >> 1))
        BITS=$((BITS + 1))
    done
    POW2_LOW=$((1 << BITS))
    POW2_HIGH=$((1 << (BITS + 1)))
    if [ $POW2_HIGH -gt $POW2_LOW ]; then
        FRAC_NUM=$(( (P - POW2_LOW) * 30 / (POW2_HIGH - POW2_LOW) ))
    else
        FRAC_NUM=0
    fi
    DB_TIMES_10=$(( BITS * 30 + FRAC_NUM ))
    # 10*log10(8388607)*10 = 692
    DBFS_TIMES_10=$(( DB_TIMES_10 - 692 ))
    if [ $DBFS_TIMES_10 -ge 0 ]; then
        WHOLE=$((DBFS_TIMES_10 / 10))
        FRAC=$((DBFS_TIMES_10 % 10))
        printf "%d.%d" $WHOLE $FRAC
    else
        ABS=$((0 - DBFS_TIMES_10))
        WHOLE=$((ABS / 10))
        FRAC=$((ABS % 10))
        echo "-${WHOLE}.${FRAC}" | tr -d '\n'
    fi
}

# Sign-extend a 32-bit value read as hex that should be interpreted signed.
# devmem returns unsigned; for registers that hold signed values (errors,
# accumulators, NCO adjustments) we want to publish the signed form too.
to_signed32() {
    V=$1
    if [ $V -ge 2147483648 ]; then
        echo $((V - 4294967296))
    else
        echo $V
    fi
}

# Publish a derived topic if the value is non-empty
pub_derived() {
    [ -z "$2" ] && return
    mosquitto_pub -t "pluto/status/ovp/derived/$1" -m "$2"
}

# Publish an IIO topic if the attribute exists and is readable
pub_iio() {
    TOPIC=$1
    PATH_=$2
    if [ -r "$PATH_" ]; then
        VAL=$(cat "$PATH_" 2>/dev/null)
        [ -n "$VAL" ] && mosquitto_pub -t "pluto/status/ovp/iio/$TOPIC" -m "$VAL"
    fi
}

# Strip "dB" suffix to get bare numeric value
strip_db() {
    echo "$1" | awk '{print $1}'
}

# Find the AD9361 IIO device dynamically (number can change after rebind)
find_ad9361_dev() {
    for d in /sys/bus/iio/devices/iio:device*; do
        [ -e "$d/name" ] || continue
        if [ "$(cat $d/name 2>/dev/null)" = "ad9361-phy" ]; then
            echo "$d"
            return 0
        fi
    done
    return 1
}

# =====================================================================
# Register publishing
# =====================================================================

publish_registers() {
    echo "$REGISTERS" | while IFS=: read OFFSET NAME; do
        [ -z "$OFFSET" ] && continue
        [ -z "$NAME" ] && continue

        ADDR=$((ADDR_BASE + OFFSET))
        VAL_HEX=$(devmem $ADDR 2>/dev/null)
        [ -z "$VAL_HEX" ] && continue

        # Always publish raw hex
        mosquitto_pub -t "pluto/status/ovp/register/${NAME}" -m "$VAL_HEX"

        # Derived/parsed values for specific registers
        VAL_DEC=$(printf "%d" "$VAL_HEX")

        case "$NAME" in
            hash_lo)
                # Should be 0xAAAA5555 if bitstream loaded correctly
                if [ "$VAL_HEX" = "0xAAAA5555" ]; then
                    pub_derived "signature" "OK"
                else
                    pub_derived "signature" "WRONG"
                fi
                ;;
            msk_init)
                # bit 0: txrxinit, bit 1: txinit, bit 2: rxinit
                pub_derived "init/txrxinit" "$((VAL_DEC & 1))"
                pub_derived "init/txinit"   "$(((VAL_DEC >> 1) & 1))"
                pub_derived "init/rxinit"   "$(((VAL_DEC >> 2) & 1))"
                ;;
            msk_control)
                # bit 0:    ptt
                # bit 1:    loopback_ena
                # bit 2:    rx_invert
                # bit 3:    clear_counts (singlepulse)
                # bit 4:    diff_encoder_loopback
                # bits 5-7: reserved
                # bits 8-10: tx_shift (3 bits, shift left 0-4)
                pub_derived "control/ptt"                   "$((VAL_DEC & 1))"
                pub_derived "control/loopback_ena"          "$(((VAL_DEC >> 1) & 1))"
                pub_derived "control/rx_invert"             "$(((VAL_DEC >> 2) & 1))"
                pub_derived "control/clear_counts"          "$(((VAL_DEC >> 3) & 1))"
                pub_derived "control/diff_encoder_loopback" "$(((VAL_DEC >> 4) & 1))"
                pub_derived "control/tx_shift"              "$(((VAL_DEC >> 8) & 0x7))"
                ;;
            lpf_config_1)
                # bits 0-23: i_gain, bits 24-31: i_shift
                pub_derived "pi/i_gain"  "$((VAL_DEC & 0xFFFFFF))"
                pub_derived "pi/i_shift" "$(((VAL_DEC >> 24) & 0xFF))"
                ;;
            lpf_config_2)
                # bits 0-23: p_gain, bits 24-31: p_shift
                pub_derived "pi/p_gain"  "$((VAL_DEC & 0xFFFFFF))"
                pub_derived "pi/p_shift" "$(((VAL_DEC >> 24) & 0xFF))"
                ;;
            f1_error|f2_error|f1_nco_adjust|f2_nco_adjust|lpf_accum_f1|lpf_accum_f2)
                # Signed 32-bit values
                pub_derived "${NAME}/signed" "$(to_signed32 $VAL_DEC)"
                ;;
            rx_power)
                # 23-bit unsigned value, derive dBFS and saturation flag
                DBFS=$(to_dbfs $VAL_DEC)
                pub_derived "rx_power/value"     "$VAL_DEC"
                pub_derived "rx_power/dbfs"      "$DBFS"
                if [ $VAL_DEC -ge 6700000 ]; then
                    pub_derived "rx_power/saturated" "1"
                else
                    pub_derived "rx_power/saturated" "0"
                fi
                ;;
            rx_frame_sync_status)
                # Bit 0:    frame_sync_locked (HDL-asserted "sync acquired",
                #           but in practice rarely sustained — frame arrival
                #           is better tracked via the counter below)
                # Bit 1:    frame_buffer_overflow (sticky)
                # Bits 2-25: frames_received (24-bit, rolls over at ~16M)
                # Bits 26-31: frame_sync_errors (6-bit, rolls over at 64)
                pub_derived "frame_sync/locked"           "$((VAL_DEC & 1))"
                pub_derived "frame_sync/buffer_overflow"  "$(((VAL_DEC >> 1) & 1))"
                pub_derived "frame_sync/frames_received"  "$(((VAL_DEC >> 2) & 0xFFFFFF))"
                pub_derived "frame_sync/sync_errors"      "$(((VAL_DEC >> 26) & 0x3F))"
                ;;
            symbol_lock_status)
                # bit 0: f1f2 (both locked)
                # bit 1: f1 locked
                # bit 2: f2 locked
                # bit 3: unlock_f1 (cleared on read - publisher reads each cycle)
                # bit 4: unlock_f2 (cleared on read)
                pub_derived "symlock/f1_locked"        "$(((VAL_DEC >> 1) & 1))"
                pub_derived "symlock/f2_locked"        "$(((VAL_DEC >> 2) & 1))"
                pub_derived "symlock/both_locked"      "$((VAL_DEC & 1))"
                pub_derived "symlock/f1_unlock_event"  "$(((VAL_DEC >> 3) & 1))"
                pub_derived "symlock/f2_unlock_event"  "$(((VAL_DEC >> 4) & 1))"
                ;;
            symbol_lock_time)
                # Lower 16 bits = f1 time, upper 16 bits = f2 time.
                # Note: meaningful only if f{1,2}_locked is true; otherwise
                # this is "elapsed symbols since init with no lock yet".
                pub_derived "symlock/f1_time" "$((VAL_DEC & 0xFFFF))"
                pub_derived "symlock/f2_time" "$(((VAL_DEC >> 16) & 0xFFFF))"
                ;;
            symbol_lock_control)
                # bits 0-9:    symbol_lock_count (default 128)
                # bits 10-25:  symbol_lock_threshold (16-bit; widening to 32
                #              bits is pending Item 5)
                pub_derived "symlock/count"     "$((VAL_DEC & 0x3FF))"
                pub_derived "symlock/threshold" "$(((VAL_DEC >> 10) & 0xFFFF))"
                ;;
        esac
    done
}

# =====================================================================
# IIO publishing - AD9361 chip state
# =====================================================================

publish_iio() {
    DEV=$(find_ad9361_dev)
    [ -z "$DEV" ] && return

    # ----- RX path -----
    pub_iio "rx/lo_frequency_hz"     "$DEV/out_altvoltage0_RX_LO_frequency"
    pub_iio "rx/sampling_frequency"  "$DEV/in_voltage_sampling_frequency"
    pub_iio "rx/rf_bandwidth"        "$DEV/in_voltage_rf_bandwidth"
    pub_iio "rx/rf_port_select"      "$DEV/in_voltage0_rf_port_select"
    pub_iio "rx/fir_filter_enabled"  "$DEV/in_voltage_filter_fir_en"
    pub_iio "rx/gain_control_mode"   "$DEV/in_voltage0_gain_control_mode"

    # Numeric-only versions (strip "dB" suffix)
    HG_RAW=$(cat "$DEV/in_voltage0_hardwaregain" 2>/dev/null)
    if [ -n "$HG_RAW" ]; then
        mosquitto_pub -t "pluto/status/ovp/iio/rx/hardwaregain_db" -m "$(strip_db "$HG_RAW")"
    fi
    RSSI_RAW=$(cat "$DEV/in_voltage0_rssi" 2>/dev/null)
    if [ -n "$RSSI_RAW" ]; then
        mosquitto_pub -t "pluto/status/ovp/iio/rx/rssi_db" -m "$(strip_db "$RSSI_RAW")"
    fi

    # Calibration tracking flags - going to 0 unexpectedly is suspicious
    pub_iio "rx/cal_rf_dc_offset_tracking" "$DEV/in_voltage_rf_dc_offset_tracking_en"
    pub_iio "rx/cal_bb_dc_offset_tracking" "$DEV/in_voltage_bb_dc_offset_tracking_en"
    pub_iio "rx/cal_quadrature_tracking"   "$DEV/in_voltage_quadrature_tracking_en"

    # ----- TX path -----
    pub_iio "tx/lo_frequency_hz"     "$DEV/out_altvoltage1_TX_LO_frequency"
    pub_iio "tx/sampling_frequency"  "$DEV/out_voltage_sampling_frequency"
    pub_iio "tx/rf_bandwidth"        "$DEV/out_voltage_rf_bandwidth"
    pub_iio "tx/rf_port_select"      "$DEV/out_voltage0_rf_port_select"
    pub_iio "tx/fir_filter_enabled"  "$DEV/out_voltage_filter_fir_en"

    HG_TX=$(cat "$DEV/out_voltage0_hardwaregain" 2>/dev/null)
    if [ -n "$HG_TX" ]; then
        mosquitto_pub -t "pluto/status/ovp/iio/tx/hardwaregain_db" -m "$(strip_db "$HG_TX")"
    fi

    # ----- System / chip state -----
    pub_iio "system/ensm_mode"        "$DEV/ensm_mode"
    pub_iio "system/calib_mode"       "$DEV/calib_mode"
    pub_iio "system/xo_correction"    "$DEV/xo_correction"
    pub_iio "system/temperature_mdeg" "$DEV/in_temp0_input"
}

# =====================================================================
# Startup
# =====================================================================

# Sanity check: bitstream loaded?
MAGIC=$(devmem $ADDR_BASE 2>/dev/null)
if [ "$MAGIC" != "0xAAAA5555" ]; then
    echo "ERROR: FPGA magic at $ADDR_BASE = $MAGIC, expected 0xAAAA5555" >&2
    echo "       Bitstream not loaded? Refusing to start." >&2
    exit 1
fi

# Publish startup metadata so subscribers know we restarted
mosquitto_pub -t "pluto/status/ovp/publisher/started" -m "$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
mosquitto_pub -t "pluto/status/ovp/publisher/pid"     -m "$$"
mosquitto_pub -t "pluto/status/ovp/publisher/version" -m "2.0"

# =====================================================================
# Main loop
# =====================================================================

while :; do
    TS=$(date -u +'%Y-%m-%dT%H:%M:%SZ')

    publish_registers
    publish_iio

    mosquitto_pub -t "pluto/status/ovp/heartbeat" -m "$TS"

    sleep $INTERVAL
done
