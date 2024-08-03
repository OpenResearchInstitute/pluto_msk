ADDR_BASE=0x43C00000

while true :
reg=0
do
while [ $reg -le 84 ]; do
    address=$(($reg + $ADDR_BASE))
    readval=$(devmem $address)
    read=$(printf %0x $readval)
#    echo $read
    mosquitto_pub -t "pluto/status/msk/$reg" -m "$read"
    reg=$((reg+4))
done
sleep 1
done


