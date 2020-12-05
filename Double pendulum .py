import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

r1 = 1
r2 = 1
th0_deg1 = 180 #Initial point m1 (Degrees)
th0_deg2 = 0 #Initial point m2 (Degrees)
th1 = [th0_deg1/180*np.pi]
th2 = [th0_deg2/180*np.pi]
x1, y1 = [r1*np.sin(th1[0])], [-r1*np.cos(th1[0])]
x2, y2 = [x1[0]+r2*np.sin(th2[0])], [y1[0]-r2*np.cos(th2[0])]
X2, Y2 = [x2-x1[0]], [y2-y1[0]]

omega1 = [0] #Rotational Velocity m1
omega2 = [0] #Rotational Velocity m2
dt = .0001
m1 = 1
m2 = 1
g = 9.81

def a_th1(th1, th2, omega1, omega2): #Rotational Accelaretion m1
    return -(r2/r1)*(m2/(m1+m2))*omega2**2*np.sin(th1-th2)-(g/r1)*np.sin(th1)-(r2/r1)*(m2/(m1+m2))*np.cos(th1-th2)

def a_th2(th1, th2, omega1, omega2): #Rotational Accelaretion m2
    return (r1/r2)*omega1**2*np.sin(th1-th2)-(g/r2)*np.sin(th2)-(r1/r2)*np.cos(th1-th2)

n = 100000
for i in range(n):
    omega1.append(omega1[i]+a_th1(th1[i], th2[i], omega1[i], omega2[i])*dt)
    omega2.append(omega2[i]+a_th2(th1[i], th2[i], omega1[i], omega2[i])*dt)
    th1.append(th1[i]+omega1[i+1]*dt)
    th2.append(th2[i]+omega2[i+1]*dt)
    x1.append(x1[i]+omega1[i+1]*dt*np.cos(th1[i+1])*r1)
    x2.append(x1[i+1]+X2[i]+omega2[i+1]*dt*np.cos(th2[i+1])*r2)
    X2.append(x2[i+1]-x1[i+1])
    y1.append(y1[i]+omega1[i+1]*dt*np.sin(th1[i+1])*r1)
    y2.append(y1[i+1]+Y2[i]+omega2[i+1]*dt*np.sin(th2[i+1])*r2)
    Y2.append(y2[i+1]-y1[i+1])

#plt.plot(x, y)
#plt.show()

#Animating
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-(r1+r2+1), (r1+r2+1)), ylim=(-(r1+r2+1), (r1+r2+1)))


ax.grid()
ax.axis()
line, = ax.plot([], [], 'o-',  lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    return line,

m = 200
def animate(t):
    i = t*m
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    
    return line, time_text

ani = anim.FuncAnimation(fig, animate, frames=int(n/m), interval=.5, blit=True, init_func=init)
plt.show()









