#!/bin/bash

# press Ctrl-A and then Q to quit minicom
#minicom --capturefile=device.log --device /dev/ttyUSB0 -b 115200
echo "try with these to connect esp devices."
echo "minicom --capturefile=device.log --device /dev/ttyUSB0 -b 115200"
echo "picocom /dev/ttyUSB0 -b115200"