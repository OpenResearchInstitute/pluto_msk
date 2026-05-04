#!/bin/sh
#
# ovp_status_pub.sh - publish OVP-specific FPGA registers to MQTT
#
# The original msk_status.sh from the SD card image only reads registers
# 0x00-0x5C, which predates the OVP modem layout. The current OVP build
# has critical registers above that range:
#   - rx_power      at 0x90 (23-bit power detector output)
#   - rx_frame_sync at 0x9C
#   - symlock_ctrl  at 0xA0
#   - symlock_status at 0xA4
#   - symlock_time  at 0xA8 (lo16=f1, hi16=f2)
#   - LPF_Config_1  at 0x34 (PI controller integral gain + shift)
#   - LPF_Config_2  at 0x68 (PI controller proportional gain + shift)
#   - f1_error      at 0x74
#   - f2_error      at 0x78
#
# Publishes to topics under pluto/status/ovp/ to keep separate from
# msk_status.sh's pluto/status/msk/ namespace.
#
# Run alongside msk_status.sh, not as a replacement.

ADDR_BASE=0x43C00000
RX_POWER_MAX=8388607
INTERVAL=1   # seconds between updates

# Address offsets to publish (offset, friendly_name)
# Format: "offset:name"
REGISTERS="
0x34:lpf_config_1
0x68:lpf_config_2
0x74:f1_error
0x78:f2_error
0x90:rx_power
0x9c:rx_frame_sync
0xa0:symlock_ctrl
0xa4:symlock_status
0xa8:symlock_time
"

# Convert rx_power to dBFS without floating-point math
# (busybox awk often lacks math support).
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

# Sanity: confirm the bitstream is loaded before we start publishing
MAGIC=$(devmem $ADDR_BASE 2>/dev/null)
if [ "$MAGIC" != "0xAAAA5555" ]; then
    echo "ERROR: FPGA magic at $ADDR_BASE = $MAGIC, expected 0xAAAA5555" >&2
    echo "       Bitstream not loaded? Refusing to start." >&2
    exit 1
fi

# Publish a static "publisher started" event with timestamp
mosquitto_pub -t "pluto/status/ovp/publisher/started" -m "$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
mosquitto_pub -t "pluto/status/ovp/publisher/pid" -m "$$"

while :; do
    TS=$(date -u +'%Y-%m-%dT%H:%M:%SZ')

    # Iterate over the register list
    echo "$REGISTERS" | while IFS=: read OFFSET NAME; do
        [ -z "$OFFSET" ] && continue
        [ -z "$NAME" ] && continue

        ADDR=$((ADDR_BASE + OFFSET))
        VAL_HEX=$(devmem $ADDR 2>/dev/null)
        [ -z "$VAL_HEX" ] && continue

        # Publish raw hex value
        mosquitto_pub -t "pluto/status/ovp/register/${NAME}" -m "$VAL_HEX"

        # For specific registers, publish derived/parsed values too
        case "$NAME" in
            rx_power)
                VAL_DEC=$(printf "%d" "$VAL_HEX")
                DBFS=$(to_dbfs $VAL_DEC)
                mosquitto_pub -t "pluto/status/ovp/rx_power/value" -m "$VAL_DEC"
                mosquitto_pub -t "pluto/status/ovp/rx_power/dbfs" -m "$DBFS"
                # Saturation flag for easy alerting
                if [ $VAL_DEC -ge 6700000 ]; then
                    mosquitto_pub -t "pluto/status/ovp/rx_power/saturated" -m "1"
                else
                    mosquitto_pub -t "pluto/status/ovp/rx_power/saturated" -m "0"
                fi
                ;;
            symlock_time)
                VAL_DEC=$(printf "%d" "$VAL_HEX")
                F1=$((VAL_DEC & 0xFFFF))
                F2=$(((VAL_DEC >> 16) & 0xFFFF))
                mosquitto_pub -t "pluto/status/ovp/symlock_time/f1" -m "$F1"
                mosquitto_pub -t "pluto/status/ovp/symlock_time/f2" -m "$F2"
                ;;
            symlock_status)
                # Bits per RDL definition:
                #   bit 0: f1f2 (both locked)
                #   bit 1: f1 (F1 locked)
                #   bit 2: f2 (F2 locked)
                #   bit 3: unlock_f1 (set if F1 unlocked since last read; clears on read)
                #   bit 4: unlock_f2 (set if F2 unlocked since last read; clears on read)
                # NOTE: reading this register clears bits 3 and 4. The publisher reads
                # every cycle, so unlock events between cycles are detected and
                # republished; longer gaps would lose events.
                VAL_DEC=$(printf "%d" "$VAL_HEX")
                LOCK_F1=$(( (VAL_DEC >> 1) & 1 ))
                LOCK_F2=$(( (VAL_DEC >> 2) & 1 ))
                LOCK_BOTH=$(( VAL_DEC & 1 ))
                UNLOCK_F1=$(( (VAL_DEC >> 3) & 1 ))
                UNLOCK_F2=$(( (VAL_DEC >> 4) & 1 ))
                mosquitto_pub -t "pluto/status/ovp/symlock/f1_locked" -m "$LOCK_F1"
                mosquitto_pub -t "pluto/status/ovp/symlock/f2_locked" -m "$LOCK_F2"
                mosquitto_pub -t "pluto/status/ovp/symlock/both_locked" -m "$LOCK_BOTH"
                mosquitto_pub -t "pluto/status/ovp/symlock/f1_unlock_event" -m "$UNLOCK_F1"
                mosquitto_pub -t "pluto/status/ovp/symlock/f2_unlock_event" -m "$UNLOCK_F2"
                ;;
            lpf_config_1)
                VAL_DEC=$(printf "%d" "$VAL_HEX")
                I_GAIN=$((VAL_DEC & 0xFFFFFF))
                I_SHIFT=$(((VAL_DEC >> 24) & 0xFF))
                mosquitto_pub -t "pluto/status/ovp/pi/i_gain" -m "$I_GAIN"
                mosquitto_pub -t "pluto/status/ovp/pi/i_shift" -m "$I_SHIFT"
                ;;
            lpf_config_2)
                VAL_DEC=$(printf "%d" "$VAL_HEX")
                P_GAIN=$((VAL_DEC & 0xFFFFFF))
                P_SHIFT=$(((VAL_DEC >> 24) & 0xFF))
                mosquitto_pub -t "pluto/status/ovp/pi/p_gain" -m "$P_GAIN"
                mosquitto_pub -t "pluto/status/ovp/pi/p_shift" -m "$P_SHIFT"
                ;;
        esac
    done

    # Publish AD9361 AGC state from IIO sysfs.
    # Find the ad9361-phy device dynamically — its iio:device number can change
    # after a driver rebind, so we don't hardcode the path.
    AD9361_DEV=""
    for d in /sys/bus/iio/devices/iio:device*; do
        [ -e "$d/name" ] || continue
        if [ "$(cat $d/name 2>/dev/null)" = "ad9361-phy" ]; then
            AD9361_DEV="$d"
            break
        fi
    done

    if [ -n "$AD9361_DEV" ]; then
        # Gain control mode: fast_attack, slow_attack, manual, hybrid
        AGC_MODE=$(cat "$AD9361_DEV/in_voltage0_gain_control_mode" 2>/dev/null)
        [ -n "$AGC_MODE" ] && mosquitto_pub -t "pluto/status/ovp/agc/mode" -m "$AGC_MODE"

        # Hardware gain — strip "dB" suffix to publish as numeric.
        # IIO returns e.g. "73.000000 dB" — we want just "73.000000".
        HG_RAW=$(cat "$AD9361_DEV/in_voltage0_hardwaregain" 2>/dev/null)
        if [ -n "$HG_RAW" ]; then
            HG_NUM=$(echo "$HG_RAW" | awk '{print $1}')
            mosquitto_pub -t "pluto/status/ovp/agc/hardwaregain_db" -m "$HG_NUM"
        fi

        # AD9361 internal RSSI — same format, strip "dB".
        # Note: high RSSI value (e.g. 123 dB) means weak signal, low value means strong.
        # The chip reports it as "loss from full scale" not absolute dBm.
        RSSI_RAW=$(cat "$AD9361_DEV/in_voltage0_rssi" 2>/dev/null)
        if [ -n "$RSSI_RAW" ]; then
            RSSI_NUM=$(echo "$RSSI_RAW" | awk '{print $1}')
            mosquitto_pub -t "pluto/status/ovp/agc/rssi_db" -m "$RSSI_NUM"
        fi

        # ENSM mode — useful for distinguishing "chip in fdd" from
        # "chip in sleep with stale rx_power latched"
        ENSM=$(cat "$AD9361_DEV/ensm_mode" 2>/dev/null)
        [ -n "$ENSM" ] && mosquitto_pub -t "pluto/status/ovp/agc/ensm_mode" -m "$ENSM"
    fi

    # Heartbeat with timestamp so subscribers know publisher is alive
    mosquitto_pub -t "pluto/status/ovp/heartbeat" -m "$TS"

    sleep $INTERVAL
done
