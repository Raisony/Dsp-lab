
from matplotlib import pyplot

x = [1, 3, 9, 8, 4, 6]
y = [5, 1, 4, 2, 2, 4]
z = [6, 3, 6, 8, 5, 9]

# Two plots
pyplot.figure(1)
pyplot.plot(x, y)
pyplot.plot(x, z)
pyplot.xlabel('Time (n)')

# Specify colors
pyplot.figure(2)
pyplot.plot(x, y, color = 'red')
pyplot.plot(x, z, color = 'blue')
pyplot.xlabel('Time (n)')

# Specify colors, short method
pyplot.figure(3)
pyplot.plot(x, y, 'red')
pyplot.plot(x, z, 'blue')
pyplot.xlabel('Time (n)')

# Create legend
pyplot.figure(4)
pyplot.plot(x, y, 'red', label = 'apples')
pyplot.plot(x, z, 'blue', label = 'bananas')
pyplot.xlabel('Time (n)')
pyplot.legend()

pyplot.show()

