import time
import matplotlib.pyplot as plt
import matplotlib.animation as anim

m1 , x1 , v1 = 1 , [5] , [0]    #blue
m2 , x2 , v2 = 100 , [7] , [-1]   #red

n = m2/m1

#audio_samples = np.ndarray(...)

def CoM(v1n_1 , v2n_1): #Conservation of Momentum.
    newV2 = (n-1)/(n+1)*v2n_1 + 2/(n+1)*v1n_1
    newV1 = v1n_1 + n*v2n_1 - n*newV2
    return newV1, newV2  #(v1, v2)

dt = .01     #No affection on the conting result. But affects the video and the running duration.
i = 0
collision_count = 0
t1 = time.time()
while True:
    x1.append(x1[i]+dt*v1[i])
    x2.append(x2[i]+dt*v2[i])
    if v2[i]<=0 and v1[i]>=0 and x1[i+1]>=x2[i+1]:
        #print('Coll #1')
        v1.append(CoM(v1[i],v2[i])[0])
        v2.append(CoM(v1[i],v2[i])[1])
        collision_count+=1
        
    elif v2[i]>=0 and v1[i]>=0 and x1[i+1]>=x2[i+1]:
        #print('Coll #2')
        v1.append(CoM(v1[i],v2[i])[0])
        v2.append(CoM(v1[i],v2[i])[1])
        collision_count+=1

    elif x1[i+1]<=0:
        #print('Coll #Wall')
        v1.append(-v1[i])
        v2.append(v2[i])
        collision_count+=1

    else:
        v1.append(v1[i])
        v2.append(v2[i])

    i+=1
    if v1[-1]>=0 and v1[-1]<=v2[-1] and abs(x1[-1]-x2[-1])>3: break

t2 = time.time()
print("Duration: {} Sec".format(t2-t1))
print('collision counts: {} collisions'.format(collision_count))

"""Visualization"""
"""Plots"""
'''
plt.plot(x1)
plt.plot(x2)
plt.show()
'''
'''
plt.subplot(211)
plt.plot(x1)
plt.plot(x2)
plt.subplot(212)
plt.plot(v1)
plt.plot(v2)
plt.show()
'''
"""Animation"""

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-3, x2[0]+5), ylim=(-1,1))
ax.set_aspect('equal')
ax.grid()
ax.axis()
line1, = ax.plot([], [], 'bo', linestyle="")
line2, = ax.plot([], [], 'ro', linestyle="")
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

fraction = int(.01/dt)
def animate(i):
    t=i*fraction
    thex1 = [x1[t]]
    thex2 = [x2[t]]
    line1.set_data(thex1[0], 0)
    line2.set_data(thex2[0], 0)
    time_text.set_text(time_template % (t*dt))

    return line1, line2, time_text

ani = anim.FuncAnimation(fig, animate, frames=int(i/fraction), interval=5, blit=True, init_func=init) #, audio=audio_samples)
plt.show()

