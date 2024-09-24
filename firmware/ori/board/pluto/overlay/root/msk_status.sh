ADDR_BASE=0x43C00000

parse_status()
{
    case $1 in
    00)
    if [ "$2" = "aaaa5555" ]
    then
    mosquitto_pub -t "pluto/status/msk/signature" -m "OK"
    else
    mosquitto_pub -t "pluto/status/msk/signature" -m "WRONG"
    fi
    ;;
    08)
    mosquitto_pub -t "pluto/status/msk/init" -m "$2"
    ;;
     0C)
     ptt=$(($2 & 1))
     loopback=$((($2 & 2)>>1))
     rxinvert=$((($2 & 4)>>2))
     clearcount=$((($2 & 8)>>3))
     samplediscard=$((($2 & 0xFF00)>>8))
     mosquitto_pub -t "pluto/status/msk/ptt" -m "$ptt"
     mosquitto_pub -t "pluto/status/msk/loopback" -m "$loopback"
     mosquitto_pub -t "pluto/status/msk/clearcount" -m "$clearcount"
     mosquitto_pub -t "pluto/status/msk/samplediscard" -m "$samplediscard"
     ;;
    esac
}

while true :
reg=0
do
while [ $reg -le 92 ]; do
    address=$(($reg + $ADDR_BASE))
    readval=$(devmem $address)
    if [ $reg -le 76 ]
    then
        read=$(printf %0x $readval)
    else

        read=$(printf %0d $readval)
        if [ $read -ge 2147483648 ]
        then
        read=$(( $read - 4294967296 ))
        fi

    fi
    reghex=$(printf %02x $reg)

#    echo $read
    mosquitto_pub -t "pluto/status/msk/register/$reghex" -m "$read"
    parse_status $reghex $read
    reg=$((reg+4))
done
sleep 1
done

