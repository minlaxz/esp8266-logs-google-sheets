#!/bin/bash

# deploy MicroPython to esp32
esp32(){
esptool.py \
    --chip esp32 \
    --port /dev/ttyUSB0 \
    --baud 460800 \
    write_flash -z 0x1000 esp32-20190529-v1.11.bin
}

# deploy MicroPython to esp8266
esp8266(){
esptool.py \
    --port /dev/ttyUSB0 \
    --baud 460800 \
    write_flash --flash_size=detect 0 esp8266-20200421-v1.12-388-g388d419ba.bin
}

if [[ "$(id -u)" -ne 0 ]]; then 
  echo "need 'root' to use /dev/*"
  echo "you may try with 'sudo'."
  exit
fi

if [ $# -eq 0 ]; then
    printf "./flash.sh --chip32 or {32}\n"
    printf "./flash.sh --chip8266 or {8266}\n"
else
    case "$1" in
        --chip32 | 32) esp32 ;;
        --chip8266 | 8266) esp8266 ;;
        *) printf "not an option <$1>"
    esac

fi