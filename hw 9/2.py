import random
import matplotlib.pyplot as plt
import numpy as np


plt.figure(figsize=(5, 4))
ax = plt.axes()
N=20

x= [0.28, 0.6, 0.11, 0.47, 0.15, 0.45, 0.51, 0.41, 0.62, 0.34, 0.63, 0.37, 0.56, 0.36, 0.60, 0.65, 0.50, 0.67, 0.61, 0.67]
y= [0.4, 0.5, 0.2, 0.42, 0.22, 0.51, 0.55, 0.4, 0.55, 0.4, 0.52, 0.4, 0.62, 0.37, 0.65, 0.72, 0.55, 0.55, 0.57, 0.65]

ax.scatter(x,y, c='b')

model = np.polyfit(x, y, 1)
predict = np.poly1d(model)
x_value = 20
predict(x_value)


x_axis =np.random.uniform(0,0.7, size=(N))
y_axis = predict(x_axis)
plt.scatter(x, y)
plt.plot(x_axis, y_axis, c = 'r')

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title("Best fit line using regression method")

plt.show()