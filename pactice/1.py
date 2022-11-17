import matplotlib.pyplot as plt
import numpy as np

x= np.arange(-1,1.1,0.1)
y=[x**2 for x in x]

plt.plot(x,y)

plt.show()
