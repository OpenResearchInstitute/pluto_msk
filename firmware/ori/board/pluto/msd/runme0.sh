# runme0.sh examples
# uncomment then eject PlutoSDR USB drive to run.


### Quick status report, available as txt file on USB mass storage.
#ps > /mnt/msd/status.txt 
#echo " " >> /mnt/msd/status.txt
#uptime >> /mnt/msd/status.txt
#echo " " >> /mnt/msd/status.txt 
#mount >> /mnt/msd/status.txt

### Start WBFM stream (Luaradio)

## Pluto streams audio to 0.0.0.0:4444/TCP. Goto host-scripts to listen radio.
#/root/wbfmradio-stdout 100500000 | /usr/bin/nmux -p 4444 -a 0.0.0.0 &
## or using nc :
#while true; do /root/wbfmradio-stdout 87900000 | /usr/bin/nc -l -p 4444; done &

## listening on remote computer :
## cvlc tcp://pluto.local:4444 --demux=rawaud --rawaud-channels 1 --rawaud-samplerate 48000
## or : nc pluto.local 4444 | ffplay -f s16le -ar 48k -ac 1 -
## or using vlc:  --demux=rawaud --rawaud-channels 1 --rawaud-samplerate 48000 tcp://pluto.local:4444

### Kill WBFM streamer
#killall -9 nmux wbfmradio

### Send sample picture SSTV
#/root/tx-sstv.sh 434000000 /tmp/send.png.wav

### Send your own SSTV picture (drag sstv.png picture to USB mass storage, then eject)
#/root/send-sstv.sh 434000000 

### RTL_433 (use 'telnet pluto.local 1234' on host computer for log)
#/usr/bin/rtl_433 -d driver=plutosdr,uri=local: -l 110 -g 58  -C si | nmux -a 0.0.0.0 -p 1234 &

### Kill RTL_433
#killall -9 rtl_433 nmux

### Send CW message
#/usr/bin/python /root/CW-pluto.py -f 144250000 -w 15 "TEST TEST TEST DE $CALLSIGN $CALLSIGN"

### Plot 100MHz BW spectrum centered on 900MHz, spacing 50kHz. Resulting plot : http://pluto.local/plot.html
#/root/signal.sh 750 850 50
