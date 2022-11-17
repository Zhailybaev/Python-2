import numpy as np
import matplotlib.pyplot as plt
from random import *
N=300
y1=np.random.randint(8000, size=(N))
y2=np.random.randint(8000, size=(N))
y3=np.random.randint(8000, size=(N))
y4=np.random.randint(8000, size=(N))
x = np.random.rand(N)



fig, axes = plt.subplots(2, 2)
size = 20*np.random.rand(N)
axes[0][0].scatter(x, y1, c = 'green', s=size)
axes[0][0].set_title('Spring')
plt.xlim([0,1])
plt.ylim([0,8000])

axes[0][1].scatter(x, y2, c = 'yellow', s=size)
axes[0][1].set_title('Summer')
plt.xlim([0,1])
plt.ylim([0,8000])

axes[1][0].scatter(x, y2, c = 'red', s=size)
axes[1][0].set_title('Fall or Autumn')
plt.xlim([0,1])
plt.ylim([0,8000])

axes[1][1].scatter(x, y1, c = 'blue', s=size)
axes[1][1].set_title('Winter')
plt.xlim([0,1])
plt.ylim([0,8000])


plt.show()