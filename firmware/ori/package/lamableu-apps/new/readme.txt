# Another kind of alias
#function send() {  pv | iio_writedev -b 1000000 cf-ad9361-dds-core-lpc }
sendssb() { /root/wav2ssb.armv7 "$1" "$2"  | pv | iio_writedev -b 1000000 cf-ad9361-dds-core-lpc; }