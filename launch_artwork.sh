#!/bin/bash
cd /home/pi/Projects/loki_leds
sudo LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0 ../midivis/venv/bin/python3 loki_leds.py -d headless -l
