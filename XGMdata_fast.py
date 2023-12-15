

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


def animate(i):
    x=i
    XFGM_DP='FLASH.FEL/XGM.INTENSITY/FL2.TUNNEL/INTENSITY.RAW.TRAIN'
    y = pydoocs.read( XFGM_DP )["data"]

    ax1.clear()
    ax1.plot(x, y, 'o')
    
    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)




ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()

#We run the animation, putting the animation to the figure (fig), running the 
#animation function of "animate," and then finally we have an interval of 1000, 
#which is 1000 milliseconds, or one second.