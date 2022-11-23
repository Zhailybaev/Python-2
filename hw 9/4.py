import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Germany', 'India', 'UK', 'US', 'South Korea', 'Australia'

sizes = [16.5, 27.7, 24.6, 18.5, 9.2, 3.4]
explode = (0, 0, 0, 0.1,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=40)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()