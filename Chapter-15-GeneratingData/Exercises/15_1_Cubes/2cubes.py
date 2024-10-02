import matplotlib.pyplot as plt

#plotting a series of points
x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(x_values,y_values,color='red', linewidth=3)

#Set chart title and label axes.
ax.set_title('5000 First Cube Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

#Set Size of tick labels.
ax.tick_params(labelsize=14)

ax.ticklabel_format(style='plain')

plt.show()