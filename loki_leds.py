#from loki.loki1Dv import *
#from midivis.mapped_fairy_lights import *

import cv2
import loki.loki1Dv as loki
import midivis.mapped_fairy_lights as mfl
import numpy as np

if __name__ == '__main__':

  # mfl.bouncer(colours=((255,10,3),(10,255,23)))

  # config = loki.get_config(show_lock=True,
  #         extraction_method='mean', width=128, num_1d_history=240,
  #         display='headless', render_texture='energy_up')
  config = loki.get_config(width=25,
      height=None,
      render_colour='rgb',
      # render_texture='energy_down',  # 'flat', 'energy_up', 'energy_down'

      display='headless',
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

      extraction_method='mean',
      show_lock=False,
      # display='headless',
      save_frames=False,
      log_data=None,
      landscape='wobbly')

  sim = loki.Loki(config)
  leds = mfl.MappedFairyLights(num_lights=150,
      calib_file='bedroom.npy')
      # calib_file='office_vertical_calib.npy')

  while(True):
    frame = sim.step_frame()
    # print(np.array(frame).mean())
    # print(sim._bitmap.mean())
    bitmap = sim._bitmap
    # print(bitmap.shape)
    bitmap = bitmap[:, 8:, :]
    #bitmap = cv2.transpose(bitmap)
    #bitmap = cv2.flip(bitmap, 0)
    #bitmap = cv2.transpose(bitmap)
    #bitmap = cv2.transpose(bitmap)
    leds.show_image2(bitmap, format='rgb')
