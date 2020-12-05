import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

r = 1
th0_deg = 75 #Initial point (Degrees)
th = [th0_deg/180*np.pi]
x, y = [r*np.cos(th[0])], [r*np.sin(th[0])]
omega = [0] #Rotational Velocity
dt = .005
m = 10
g = 9.81

def a_th(th): #Rotational Accelaretion
    return -g*np.cos(th)/r

n = 2000
for i in range(n):
    omega.append(omega[i]+a_th(th[i])*dt)
    th.append(th[i]+omega[i+1]*dt)
    x.append(x[i]-omega[i+1]*dt*np.sin(th[i+1])*r)
    y.append(y[i]+omega[i+1]*dt*np.cos(th[i+1])*r)

#plt.plot(x, y)
#plt.show()

#Animating
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-r-1, r+1), ylim=(-r-1, r+1))
ax.set_aspect('equal')
ax.grid()
line, = ax.plot([], [], 'bo', linestyle="")

def init():
    line.set_data([], [])
    return line,

def animate(i):
    thisx = [x[i]]
    thisy = [y[i]]
    line.set_data(thisx, thisy)
    return line,

ani = anim.FuncAnimation(fig, animate, n, interval=.1, blit=True, init_func=init)
plt.show()








