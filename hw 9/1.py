import numpy as np
import matplotlib.pyplot as plt


np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(90*np.random.rand(30), '^-b', label="a")

ax.set_xlabel('This is the X Axis')
ax.set_ylabel('This is the Y Axis')
ax.set_title("This is the title")

plt.legend()
plt.grid(True)
plt.show()