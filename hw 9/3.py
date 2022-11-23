from cycler import cycler
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 50)
offsets = np.linspace(0, 2 * np.pi, 4, endpoint=False)
yy = np.transpose([np.sin(x + phi) for phi in offsets])

plt.rc('lines', linewidth=4)


custom_cycler = (cycler(color=['b', 'orange', 'g', 'r']) +
                 cycler(lw=[2, 2, 2, 2]))

fig, ax1 = plt.subplots()

ax1.set_prop_cycle(custom_cycler)
ax1.plot(yy)

plt.grid(True)
plt.show()