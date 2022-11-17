import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


delta = 0.05
x = np.arange(-10.0, 10.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)

Z = (np.sin(X * 0.3) * np.cos(Y * 0.75) /
    (1 + np.abs(X * Y) * 0.05))


fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)


plt.show()