#!/bin/bash

sshpass -p analog ssh root@pluto.local '/usr/sbin/device_reboot ram;'
sleep 7
dfu-util -D build/pluto.dfu -a firmware.dfu
dfu-util -e --alt=1
