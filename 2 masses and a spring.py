import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 10
m1 = 2
m2 = 1
l = 1

d = 1

r1 = [[0], [0]]
r2 = [[l], [0]]

dt = .01

def F(x1, y1, x2, y2):
    return k*abs(np.sqrt(abs((x1-x2)**2 + (y1-y2)**2))-l)

a1 = [[], []]
a2 = [[], []]

v1 = [[0], [d]]
v2 = [[0], [0]]

E = []
N = 2000
for i in range(N):
    r1[0].append(r1[0][i] + v1[0][i]*dt)
    r1[1].append(r1[1][i] + v1[1][i]*dt)
    r2[0].append(r2[0][i] + v2[0][i]*dt)
    r2[1].append(r2[1][i] + v2[1][i]*dt)
    
    a1[0].append(F(r1[0][i+1], r1[1][i+1], r2[0][i+1], r2[1][i+1])/m1*(r2[0][i]-r1[0][i+1])/(abs(np.sqrt((r1[0][i+1]-r2[0][i+1])**2 + (r1[1][i+1]-r2[1][i+1])**2))))
    a1[1].append(F(r1[0][i+1], r1[1][i+1], r2[0][i+1], r2[1][i+1])/m1*(r2[1][i]-r1[1][i+1])/(abs(np.sqrt((r1[0][i+1]-r2[0][i+1])**2 + (r1[1][i+1]-r2[1][i+1])**2))))
    a2[0].append(-a1[0][i]*m1/m2)
    a2[1].append(-a1[1][i]*m1/m2)
    
    v1[0].append(v1[0][i] + a1[0][i]*dt)
    v1[1].append(v1[1][i] + a1[1][i]*dt)
    v2[0].append(v2[0][i] + a2[0][i]*dt)
    v2[1].append(v2[1][i] + a2[1][i]*dt)

    #E.append(k*abs(np.sqrt(abs(np.sqrt((r1[0][i+1]-r2[0][i+1])**2 + (r1[1][i+1]-r2[1][i+1])**2))-l)**2 + .5*m1*(v1[0][i]**2+v1[1][i]**2) + .5*m2*(v2[0][i]**2+v2[1][i]**2)))

plt.plot(r1[0], r1[1])
plt.plot(r2[0], r2[1])
plt.show()

#plt.plot(E)
#plt.show()

'''For animating'''

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1, l+1), ylim=(min([min(r2[1]),min(r1[1])]), max([max(r2[1]),max(r1[1])])))
ax.set_aspect('equal')
ax.grid()
line1, = ax.plot([], [], 'r.', linestyle="")
line2, = ax.plot([], [], 'g.', linestyle="")

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

def animate(i):
    thisx = [r1[0][i], r2[0][i]]
    thisy = [r1[1][i], r2[1][i]]
    line1.set_data(thisx[0], thisy[0])
    line2.set_data(thisx[1], thisy[1])
    return line1, line2

ani = animation.FuncAnimation(fig, animate, N, interval=5, blit=True, init_func=init)
plt.show()
