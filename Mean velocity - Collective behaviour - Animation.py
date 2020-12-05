import numpy as np
from numpy.random import random as noise
import matplotlib.pyplot as plt
import matplotlib.animation as anime
from matplotlib.widgets import Slider, Button, RadioButtons
import time

n = 50 #population
w = 5 #width
x, y = np.random.rand(n)*w, np.random.rand(n)*w
vx, vy = (np.random.rand(n)-.5)*10, (np.random.rand(n)-.5)*10
dt = .01

"""Animation"""
fig = plt.figure(facecolor='black')
ax = plt.axes(frameon=False, xlim=(0,w), ylim=(0,w))
line, = ax.plot([], [], 'o')

def animate(i):
    global x,y,vx,vy,dr,j
    vx_temp = []
    vy_temp = []
    dr = .5
    for j in range(n):
        con = ((x<x[j]+dr) & (x>x[j]-dr) & (y<y[j]+dr) & (y>y[j]-dr))#it indicates if there is someone near or not
        if sum(con)!=0:
            vx_temp.append(sum(con*vx)/sum(con)+(noise()-.5)*3)
            vy_temp.append(sum(con*vy)/sum(con)+(noise()-.5)*3)
        else:
            vx_temp.append(vx)
            vy_temp.append(vy)

    vx = np.array(vx_temp.copy())
    vy = np.array(vy_temp.copy())
    
    x = (x+vx*dt)%w
    y = (y+vy*dt)%w

    line.set_xdata(x)
    line.set_ydata(y)
    
    return line,
anim = anime.FuncAnimation(fig, animate, interval=1)
plt.show()

