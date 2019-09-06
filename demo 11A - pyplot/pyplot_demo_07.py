
from matplotlib import pyplot

x = [1, 3, 9, 8, 4, 6]
y = [5, 1, 4, 2, 2, 4]
z = [6, 3, 6, 8, 5, 9]

pyplot.figure(1)

line1, = pyplot.plot(x, y)     # line1 is first (and only) element of list returned by pyplot.plot
line2, = pyplot.plot(x, z)

# Set parameters of line1
line1.set_label('apple')

# Set parameters of line2
line2.set_label('pear')

# Create legend
pyplot.legend()

pyplot.show()

