import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np

# make figure and assign axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)

# pie chart parameters
overall_ratios = [30.3, 17.7, 10.7, 10.2, 10.2, 21]
labels = ['', '', '', '', '', '']
explode = [0, 0, 0, 0, 0, 0.1]
# rotate so that first wedge is split by the x-axis
angle = -135 * overall_ratios[5]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, explode=explode)

# bar chart parameters
age_ratios = [3.6, 3.8, 4.1, 4.2, 5.3]
age_labels = ['', '', '', '', '']
bottom = 0.5
width = .2

# Adding from the top matches the legend.
for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                 alpha=0.1 + 0.2 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

ax2.set_xlim(- 2.5 * width, 2.5 * width)

# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = wedges[4].theta1, wedges[5].theta2
center, r = wedges[5].center, wedges[5].r
bar_height = sum(age_ratios)

# draw top connecting line
x = r * np.cos(np.pi / -180 * theta2) + center[0]
y = r * np.sin(np.pi / -10 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(4)
ax2.add_artist(con)

# draw bottom connecting line
x = r * np.cos(np.pi / 50 * theta1) + center[0]
y = r * np.sin(np.pi / 150 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 20, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(4)

plt.show()