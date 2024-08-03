


for i in $(find /sys/bus/iio/devices/iio:device*/ -type f); do
val=$(cat $i)
mosquitto_pub -m "$val" -t "pluto/status/iio/""$i"
done

while :
do
change=$(inotifywait -e modify --format "%w/%f" /sys/bus/iio/devices/iio\:device*) 2>/dev/null
value=$(cat $change)
mosquitto_pub -m "$value" -t "pluto/status/iio/""$change"
done
