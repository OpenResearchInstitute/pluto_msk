

print_status () {
  name=$1
  base_addr=$2
  word_width=$3

  if [ -z "$word_width" ]; then
    word_width=1
  fi

  frame_count=$(devmem $((base_addr + 4)))

  last_frame_lenght=$(devmem $((base_addr + 8)))

  min_max=$(devmem $((base_addr + 12)))
  max_length=$((min_max / 65536))
  min_length=$((min_max & 0xffff))

  if [ "$max_length" = "0" ]; then
    max_length="-"
    max_length_bytes="-"
  else
    max_length=$(printf "%7d" $max_length)
    max_length_bytes=$(printf "%7d" $((max_length * word_width)))
  fi

  if [ "$min_length" = "65535" ]; then
    min_length="-"
    min_length_bytes="-"
  else
    min_length=$(printf "%7d" $min_length)
    min_length_bytes=$(printf "%7d" $((min_length * word_width)))
  fi

  word_count=$(devmem $((base_addr + 16)))

  strobes=$(devmem $((base_addr + 20)))
  in_vld=$((strobes & 1))
  in_rdy=$(((strobes >> 1) & 1))
  out_vld=$(((strobes >> 2) & 1))
  out_rdy=$(((strobes >> 3) & 1))

  printf "%015s |" "$name"
  printf "%10d |" "$frame_count"
  printf "%7d beats / %7d bytes |" "$last_frame_lenght" $((last_frame_lenght * word_width))
  printf "%7s / %7s |" "$min_length" "$min_length_bytes"
  printf "%7s / %7s |" "$max_length" "$max_length_bytes"
  printf "%7d / %8d |" "$word_count" "$((word_count * word_width))"
  printf "%7d |" $in_vld
  printf "%7d |" $in_rdy
  printf "%8d |" $out_vld
  printf "%8d" $out_rdy
  printf "\n"
}

print_ldpc_fifo_status () {
  status=$(devmem 0x43c10004)
  entries=$((status & 0x3fff))
  empty=$(((status >> 16) & 1))
  full=$(((status >> 17) & 1))
  printf "LDPC FIFO: "
  printf "entries: %d, " $entries
  printf "empty: %d, " $empty
  printf "full: %d" $full
}


printf "Frames in flight: %d" "$(devmem 0x43c10008)"

print_ldpc_fifo_status

printf "%015s |" "Waypoint"
printf "%010s |" "Frames"
printf "      Last frame length       |"
printf "       From       |"
printf "       To         |"
printf "      Pending      |"
printf " in_vld | in_rdy | out_vld | out_rdy\n"

print_status "input"            0x43C10D00 1
print_status "BB scrambler"     0x43C10E00 1
print_status "BCH encoder"      0x43C10F00 1
print_status "LDPC encoder"     0x43C11000 1
print_status "Bit interleaver"  0x43C11100 1
print_status "plframe"          0x43C11200 4
print_status "output"           0x43C11300 4
