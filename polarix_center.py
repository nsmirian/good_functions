#!/usr/bin/env python3

import time
import numpy as np

import pydoocs


TARGET = 6
PHASE_STEP = 0.2

PHASE_DP = "FLASH.RF/LLRF.CONTROLLER/CTRL.POLARIX/SP.PHASE"
CENTER_DP = "FLASH.DIAG/CAMERA/OTR9FL2XTDS/SPECTRUM.X.MEAN"

if __name__ == "__main__":
 
  center = np.zeros( 10 )
  cntr = 0
 
  while True:
    try:
      center[:-1] = center[1:]
      center[-1] = pydoocs.read( CENTER_DP )["data"]
      
      cntr += 1

      if cntr >= 10:
        phase = pydoocs.read( PHASE_DP )["data"]
        cntr = 0

        mean = center.mean()
        print( mean, phase )

        if mean - TARGET < -0.5:
          phase += PHASE_STEP
          print( "up", PHASE_DP, phase )
          pydoocs.write( PHASE_DP, phase )
        elif mean - TARGET > 0.5:
          phase -= PHASE_STEP
          print( "down", PHASE_DP, phase )
          pydoocs.write( PHASE_DP, phase )

    except Exception as e:
      print( sys.exc_info()[0], str( e ))
    
    time.sleep( 1 )
    
