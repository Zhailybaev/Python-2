import matplotlib.pyplot as plt
import numpy as np
def gen():
    a=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return [np.random.choice(a,70)]
def gen_c():
    a=["green", "red" , "yellow", "skyblue", "blue", "black", "brown"]
    return [np.random.choice(a)]
x =gen()
y=7

plt.hist(x,y, rwidth=0.5, color=np.random.choice(["green", "red" , "yellow", "skyblue", "blue", "black", "brown"]))
#plt.hist(x,y, rwidth=0.5, color=np.random.rand(10))
plt.show() 