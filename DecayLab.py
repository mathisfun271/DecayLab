#Decay Lab!

from random import getrandbits,random
from time import time
import numpy as np
import matplotlib.pyplot as plt
from math import log
from math import factorial

start = 1000#Set this to the starting value.
count = 0

yaxis = [start]
xaxis = [0]

tst = time()

cur = start
while cur != 0:
    st = time()
    new = 0
    for n in range(0,cur):
        new += getrandbits(1)#This is what is random. Adds either 1 or 0, with equal chance

    cur = new
    
    print('Remaining: %s, Stage time: %.3f' % (cur,time()-st))
    
    count += 1
    xaxis.append(10*count)
    yaxis.append(cur)

print(time()-tst)


x = np.linspace(0, 10*count, 500)
y = start*np.exp(-log(2)*x/10)

fig, ax = plt.subplots()
plt.grid(color='lightgray', linestyle='-', linewidth=1)

ax.plot(x,y,color='r')
ax.scatter(xaxis,yaxis)
ax.set_xlabel('Seconds')
ax.set_ylabel('Amount of Particles')
plt.title('Computer Generated Decay of Candium (Linear)')
fig.savefig('/Users/nathanmihm/Math Graphics/Decay1.png',dpi=200)

plt.title('Computer Generated Decay of Candium (Logarithmic)')
ax.set_yscale('log')
fig.savefig('/Users/nathanmihm/Math Graphics/Decay2.png',dpi=200)
