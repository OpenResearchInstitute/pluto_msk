#!/bin/sh

ADDR_BASE=0x43C00000
#addr,value
writereg () 
{
   ADDR=$(($ADDR_BASE + $1))
   VALUE=$2
   devmem $ADDR 32 $VALUE 
}

readreg () 
{
    ADDR=$(($ADDR_BASE + $1))
    echo $(devmem $ADDR)
}

MAGIC_DETECT="$(readreg 0)"

if [ "$MAGIC_DETECT" = "0xAAAA5555" ]; then
    echo "Opulent FPGA is detected"
else
    echo "Opulent seems not present"
fi


writereg 4  1           # Assert INIT
writereg 12 1           # Enable Loopback                         
writereg 16 3788854     # Bitrate NCO Frequency Word                       
writereg 20 71988237    # F1 NCO Frequency Word                      
writereg 24 79565946    # F2 NCO Frequency Word                      
writereg 28 320014      # P and I Loop Filter Gain Values                 
writereg 32 20000       # Low-pass Filter Alpha              
writereg 36 8           # AXIS Tx Data Width                   
writereg 40 8           # AXIS Rx Data Width           
sleep 1                                           
writereg 4 0            # De-assert INIT
sleep 1
writereg 8 1            # Assert PTT

