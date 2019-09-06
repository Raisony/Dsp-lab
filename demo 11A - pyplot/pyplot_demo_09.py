
from matplotlib import pyplot

pyplot.figure(1)

pyplot.xlim(0, 20)
pyplot.ylim(0, 10)

line1, = pyplot.plot([], [])   # Create empty line

x = [1, 5, 9, 16, 19]
y = [1, 6, 8, 7, 4]

pyplot.setp(line1, xdata = x, ydata = y)

# OR 

# pyplot.setp(line1, xdata = x)
# pyplot.setp(line1, ydata = y)

# OR

# line1.set_data( x, y )

# OR

# line1.set_xdata( x )
# line1.set_ydata( y )

pyplot.show()

