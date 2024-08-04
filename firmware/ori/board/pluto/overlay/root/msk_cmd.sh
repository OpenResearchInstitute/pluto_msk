ADDR_BASE=0x43C00000

while true :
reg=0
do
cmd=$(mosquitto_sub -t pluto/cmd/msk/register/# -C 1 -v)
reg=$(echo $cmd | cut -d ' ' -f 1)
reg1=$(echo $reg | awk -F "/" '{print $NF}')
val=$(echo $cmd | cut -d ' ' -f 2)
echo $reg1
address=$(($reg1 + $ADDR_BASE))
devmem $address 32 $val
done


