
from matplotlib import pyplot

x = [1, 3, 9, 8, 4, 6]
y = [5, 1, 4, 2, 2, 4]
z = [6, 3, 6, 8, 5, 9]

pyplot.figure(1)

lines = pyplot.plot(x, y, x, z) 

line0, line1 = lines		# assign elements of list 

line0.set_linewidth(3)
line1.set_color('red')

# Equivalently:

pyplot.figure(2)

line0, line1 = pyplot.plot(x, y, x, z)   # assign elements directly

line0.set_linewidth(5)
line1.set_color('red')

pyplot.show()

