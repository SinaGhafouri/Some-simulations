import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

t = 1 #Lines distances
l = 1 #Length of needles
n = 5 #Size of plane

fig = plt.figure(figsize=(8, 6), facecolor='black')
ax = fig.add_subplot(111,frameon=False,xlim=(-.1,n+.1),ylim=(-.1,n+.1))
ax.set_title("P = 0")
ax.set_aspect('equal')
yticks = np.arange(0, n+.1, t)
ax.set_yticks(yticks)
ax.grid(axis='y', linestyle='--', alpha=0.2)
plt.style.use('dark_background')
line, = ax.plot([],[],'r-')
lines = []
lines.append(ax.plot([], [], 'g-',label='Between lines'))
lines.append(ax.plot([], [], 'r-',label='Crossed a line'))
ax.legend(loc='upper left',bbox_to_anchor=(1, 1))
counter = 0
def animate(i):
    global counter
    y1 = np.random.random()*n ; x1 = np.random.random()*n
    th = np.random.random()*2*np.pi
    y2 = y1 + l*np.sin(th)    ; x2 = x1 + l*np.cos(th)
    
    if abs(np.floor(y2/t)-np.floor(y1/t))>=t/t:
        line.set_data([x1,x2],[y1,y2])
        line.set_color('red')
        counter += 1
    else: 
        line.set_data([x1,x2],[y1,y2])
        line.set_color('green')
        
    if (i)%10==0:
        ax.set_title("Drops count = {}\nProbability = {:.4}\nError = {:.4}%".format(i+1, 1-counter/(i+1), 100*abs(-2/np.pi+counter/(i+1))/(1-2/np.pi)), color='white')
    return line

anim = animation.FuncAnimation(fig, animate, interval=1)
plt.show()

