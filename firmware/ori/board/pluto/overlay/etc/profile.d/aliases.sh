export PATH=$PATH:/root:/root/luaradio:/root/luaradio/radio
alias luaradio="cd /root/luaradio ; luaradio"
alias retrogram="retrogram-plutosdr --uri=local:"
alias rtl_433="rtl_433 -d driver=plutosdr,uri=local: -g 60 -C si"
alias ldd="LD_TRACE_LOADED_OBJECTS=1 $1"

