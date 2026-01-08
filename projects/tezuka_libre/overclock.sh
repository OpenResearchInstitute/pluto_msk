#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage $0: OVERCLOCK_CPU_MULT OVERCLOCK_DDR_MULT"
    echo "Note that we set frequency multipliers, rather than absolute frequency."
    echo "Multipliers are presented as decimal numbers."
    echo "Example: $0 40 28"
    exit 1
fi

SDK_PATH="build/sdk/fsbl"
PS7_INIT_FILE="${SDK_PATH}/src/ps7_init.c"

if [ ! -f "${PS7_INIT_FILE}" ]; then
    echo "${PS7_INIT_FILE} not found!"
    exit 2
fi


cpu_mult_template='EMIT_MASKWRITE\(0XF8000100, 0x0007F000U ,0x000XX000U\),'
cpu_mult_find='\s'"${cpu_mult_template/XX/(..)}"
ddr_mult_template='EMIT_MASKWRITE\(0XF8000104, 0x0007F000U ,0x000XX000U\),'
ddr_mult_find='\s'"${ddr_mult_template/XX/(..)}"

current_cpu_mult_hex=$(head -n 1 <<< $(sed -rn 's/'"${cpu_mult_find}"'/\1/p' "$PS7_INIT_FILE"))
current_ddr_mult_hex=$(head -n 1 <<< $(sed -rn 's/'"${ddr_mult_find}"'/\1/p' "$PS7_INIT_FILE"))

current_cpu_mult=$(echo "ibase=16; ${current_cpu_mult_hex}" | bc)
current_ddr_mult=$(echo "ibase=16; ${current_ddr_mult_hex}" | bc)

new_cpu_mult=$1
new_ddr_mult=$2

if ! [[ "$new_cpu_mult" =~ '^[0-9]+$' ]]; then
    if [ "$new_cpu_mult" -ge 128 ] || [ "$new_cpu_mult" -le 0 ]; then
	echo "CPU multiplier ${new_cpu_mult} is invalid. Must be >0 and <128"
	exit 3
    fi
fi

if ! [[ "$new_ddr_mult" =~ '^[0-9]+$' ]]; then
    if [ "$new_ddr_mult" -ge 128 ] || [ "$new_ddr_mult" -le 0 ]; then
	echo "DDR multiplier ${new_ddr_mult} is invalid. Must be >0 and <128"
	exit 4
    fi
fi

cpu_mult_replace="${cpu_mult_template/XX/${new_cpu_mult}}"

echo "Current CPU multiplier: ${current_cpu_mult}, new multiplier ${new_cpu_mult}"
echo "Current DDR multiplier: ${current_ddr_mult}, new multiplier ${new_ddr_mult}"

new_cpu_mult_hex=$(printf "%02X" $new_cpu_mult)
cpu_mult_replace="    ${cpu_mult_template/XX/${new_cpu_mult_hex}}"
new_ddr_mult_hex=$(printf "%02X" $new_ddr_mult)
ddr_mult_replace="    ${ddr_mult_template/XX/${new_ddr_mult_hex}}"

sed -i -r 's/'"${cpu_mult_find}"'/'"${cpu_mult_replace}"'/g' "$PS7_INIT_FILE"
sed -i -r 's/'"${ddr_mult_find}"'/'"${ddr_mult_replace}"'/g' "$PS7_INIT_FILE"

pushd "$SDK_PATH/Release"
make clean
make

mv fsbl.elf fsbl${new_cpu_mult}_${new_ddr_mult}.elf 
echo 'Done. Run "make sdimg" now to create overclocked firmware.'

