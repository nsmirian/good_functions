


# Feed back program for POLARIX,
# Najmeh Mirian
# 12th May 2024


import time
from matplotlib.animation import FuncAnimation
import psutil
import collections
import pydoocs
# animation pyplot

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


#now we write animation function:


#tem=doocswrite(add_phase, phase_XTDS+2);

def animate(i):

    PHASE_DP = "FLASH.RF/LLRF.CONTROLLER/CTRL.POLARIX/SP.PHASE"
    SPECTRUM_X = "FLASH.DIAG/CAMERA/OTR9FL2XTDS/SPECTRUM.X.MEAN"
    y= pydoocs.read(PHASE_DP)["data"]
    x = pydoocs.read( SPECTRUM_X)["data"]
    ax1.clear()
    ax1.scatter(x, y, 'o', markersize=9)

    #graph_data = open('example.txt','r').read()
    #lines = graph_data.split('\n')
    #xs = []
    #ys = []
    #for line in lines:
    #    if len(line) > 1:
    #        x, y = line.split(',')
    #        xs.append(float(x))
    #        ys.append(float(y))
    #ax1.clear()
    #ax1.scatter(xs, ys,'o', markersize=9)

phase=pydoocs.read(PHASE_DP)["data"]
x0 = pydoocs.read( SPECTRUM_X)["data"]
pahse_tep=pydoocs.write( PHASE_DP, phase+2 )
x1 = pydoocs.read( SPECTRUM_X)["data"]

if x1>x1 :
    delta_phase=0.5
else:
    delta_phase=-0.5

while 1>0:

    x = pydoocs.read( SPECTRUM_X)["data"]

    if x> 11:
        while x > 11:
            phase=pydoocs.read(PHASE_DP)["data"]
            pahse_tep=pydoocs.write( PHASE_DP, phase-delta_phase )
            x = pydoocs.read( SPECTRUM_X)["data"]

    if x<5:
        while x <5:
            phase=pydoocs.read(PHASE_DP)["data"]
            pahse_tep=pydoocs.write( PHASE_DP, phase+delta_phase )
            x = pydoocs.read( SPECTRUM_X)["data"]

    time.sleep( 1 )

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()




#We run the animation, putting the animation to the figure (fig), running the
#animation function of "animate," and then finally we have an interval of 1000,
#which is 1000 milliseconds, or one second.
