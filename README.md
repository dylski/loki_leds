# loki_leds

To start artwork:
$ ./start_artwork

To monitor:

$ screen -R Loki


--- OLD STUFF ---

To start run headless for window display:
sudo LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0 ../midivis/venv/bin/python3 loki_leds.py -d headless -l

Otherwise:
sudo LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0 ../midivis/venv/bin/python3 loki_leds.py


