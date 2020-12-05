import numpy as np
from numpy.random import random as rn
import matplotlib.pyplot as plt
import matplotlib.animation as anime
from matplotlib.widgets import Slider, Button, RadioButtons
import time

n = 100 #population
w = 10 #width
x, y = np.random.rand(n)*w, np.random.rand(n)*w
vx, vy = (np.random.rand(n)-.5)*10, (np.random.rand(n)-.5)*10
dt = .01

"""Animation"""
fig = plt.figure(facecolor='black')
ax = plt.axes(frameon=False, xlim=(0,w), ylim=(0,w))
line, = ax.plot(x[-1], y[-1], 'o')

"""sliders axis"""
'''radius'''
dr_slider_ax = fig.add_axes([0.13, .01, .7, 0.02])
dr_slider = Slider(dr_slider_ax, 'Attraction Radius', valmin = 0, valmax = 2.5, valinit = 0.5, color='blue')
dr_slider.label.set_size(10)
dr_slider.label.set_color('red')
'''noise'''
noise_slider_ax = fig.add_axes([0.13, .035, .7, 0.02])
noise_slider = Slider(noise_slider_ax, 'Some Noise', valmin = 0, valmax = 5, valinit = 0, color='blue')
noise_slider.label.set_size(10)
noise_slider.label.set_color('red')

def animate(i):
    global x,y,vx,vy,dr,con,j,vx_temp,vy_temp
    vx_temp, vy_temp = [], []
    dr = dr_slider.val
    #vx += ((rn(n)-.5)*noise_slider.val)*5
    #vy += ((rn(n)-.5)*noise_slider.val)*5
    for j in range(n):
        con = ((x<x[j]+dr) & (x>x[j]-dr) & (y<y[j]+dr) & (y>y[j]-dr))#it indicates if there is someone near or not
        if sum(con)!=0:
            vx_temp.append(sum(con*vx)/sum(con)+(rn()-.5)*noise_slider.val)
            vy_temp.append(sum(con*vy)/sum(con)+(rn()-.5)*noise_slider.val)
        else:
            vx_temp.append(vx[j]+(rn()-.5)/10)
            vy_temp.append(vy[j]+(rn()-.5)/10)
    vx = np.array(vx_temp.copy())
    vy = np.array(vy_temp.copy())
    
    x = (x+vx*dt)%w #+(rn(n)-.5)*noise_slider.val
    y = (y+vy*dt)%w #+(np.sin(rn(n))-.5)/10

    line.set_xdata(x)
    line.set_ydata(y)
    
    return line,
anim = anime.FuncAnimation(fig, animate, interval=1)
plt.show()

