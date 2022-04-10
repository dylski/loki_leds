# Run Loki sim and display on LED strings
import argparse
import cv2
import datetime
from loki.loki1Dv import Loki
from loki.main import get_config
import midivis.mapped_fairy_lights as mfl
import numpy as np
import time


if __name__ == '__main__':
  ap = argparse.ArgumentParser()
  ap.add_argument('-d', '--display', help='[windowed|headless]')
  ap.add_argument('-l', '--leds', help='Control the LEDs', action='store_true')
  # mfl.bouncer(colours=((255,10,3),(10,255,23)))
  args = vars(ap.parse_args())
  display = args.get('display')
  show_leds = args.get('leds')

  config = get_config(width=25,
      height=None,
      render_colour='rgb',
      # render_texture='energy_down',  # 'flat', 'energy_up', 'energy_down'

      display=display,
      # display='headless',
      # display='windowed',

      # num_1d_history=80,  # 48, 192
      # render_texture='rgb',
      # extraction_rate=0.2,
      # lock_mutation=0.01,

      num_1d_history=96,  # 48, 192
      render_texture='rgb',
      # render_texture='energy_down',
      extraction_rate=0.2,
      lock_mutation=0.01,

      # num_1d_history=80,  # 48, 192
      # render_texture='energy_down',
      # extraction_rate=0.01,
      # lock_mutation=0.001,

      key_mean_mutation=0.1,
      key_sigma_mutation=0.1,
      extraction_method='mean',
      show_lock=False,
      save_frames=False,
      log_data=None,
      landscape_roughness=1,
      landscape='wobbly')

  show_leds = show_leds

  # import pdb; pdb.set_trace()
  sim = Loki(config)
  if show_leds:
    leds = mfl.MappedFairyLights(num_lights=150,
        calib_file='calib/bedroom.npy')
        # calib_file='office_vertical_calib.npy')

  force_on = False

  # time(hour, minute and second)
  start = datetime.time(16, 00, 00)
  end = datetime.time(21, 00, 00)
  on = False
  while(True):
    now = datetime.datetime.now().time()
    if (now >= start and now < end) or force_on:
      if on == False:
        on = True
        print('Running')
      frame = sim.step_frame()
      if show_leds:
        bitmap = sim._bitmap
        # print(bitmap.shape)
        bitmap = bitmap[:, 8:, :]
        # bitmap = cv2.transpose(bitmap)
        # bitmap = cv2.flip(bitmap, 0)
        # bitmap = cv2.transpose(bitmap)
        # bitmap = cv2.transpose(bitmap)
        leds.show_image2(bitmap, format='rgb')
    else:
      if on:
        print('Ended')
      on = False
      if show_leds:
        leds.blank()
      # tomorrow_start = datetime.datetime.combine(
      #     datetime.date.today() + datetime.timedelta(days=1),
      #     start)
      # wait_secs = (int)((
      #     tomorrow_start - datetime.datetime.now()).total_seconds())

      wait_secs = 1
      # print('Waiting {} seconds'.format(wait_secs))
      time.sleep(wait_secs)


