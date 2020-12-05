import matplotlib.pyplot as plt
import numpy as np
import time as t
tc = 1000000000    #total_cash
pop = 1000    #population

t1 = t.time()

ind_wlth = (np.zeros(pop)+1)*tc/pop   #Each individual's wealth
index = np.arange(len(ind_wlth))

for day in range(10000):
    half_1 = np.random.choice(len(ind_wlth), int(pop/2), replace=False)
    half_2 = np.delete(index, half_1)
    R = np.random.ranf(len(half_1))
    W = ind_wlth[half_1]
    ind_wlth[half_1] -= R*W
    ind_wlth[half_2] += R*W

t2 = t.time()

plt.plot(np.sort(ind_wlth)[::-1])
print('Duration: {} Sec'.format(t2-t1))
print('The wealthiest has: ',max(np.sort(ind_wlth)))
print('The pooret has: ',min(np.sort(ind_wlth)))
plt.show()
