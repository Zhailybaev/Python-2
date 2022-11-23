import numpy as np
import matplotlib.pyplot as plt
from random import *


ax = plt.figure().add_subplot(projection='3d')

# Prepare arrays x, y, z
theta = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 100)
z = np.linspace(-2, 16, 100)
x = np.sin(theta)
y = np.cos(theta)

ax.plot(x, y, z)
n=10
for m, zlow, zhigh in [('o', -1, 15)]:
    xs = np.random.uniform( -0.9, 0.9 , 40)
    ys = np.random.uniform( -0.9, 0.9, 40)
    zs = np.random.uniform(zlow, zhigh, 40)
    ax.scatter(xs, ys, zs,c='g', marker=m)

ax.legend()

plt.show()