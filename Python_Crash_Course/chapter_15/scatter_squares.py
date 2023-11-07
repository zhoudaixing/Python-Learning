import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.axis([0, 1100, 0, 1_100_000])

plt.savefig('squares_plot.png', bbox_inches='tight')