
from matplotlib import pyplot

x = [1, 3, 9, 8, 4, 6]
y = [5, 1, 4, 2, 2, 4]
z = [6, 3, 6, 8, 5, 9]

# Two different line styles 
pyplot.figure(1)
pyplot.plot(x, y, 'r-')			# red solid line
pyplot.plot(x, z, 'b--')		# blue dashed line
pyplot.xlabel('Time (n)')

# Two different marker styles 
pyplot.figure(2)
pyplot.plot(x, y, 'ro-')		# red solid line with circle marker
pyplot.plot(x, z, 'bs--')		# blue dashed line with square markers
pyplot.xlabel('Time (n)')

# Specify marker size, line width
pyplot.figure(3)
pyplot.plot(x, y, 'r-', linewidth = 4)
pyplot.plot(x, z, 'bo--', markersize = 8, linewidth = 3)
pyplot.xlabel('Time (n)')

pyplot.figure(4)
pyplot.plot(x, y, 'r-')
pyplot.plot(x, z, 'b--')
pyplot.xlabel('Time (n)')
pyplot.xlim(-2, 12)
pyplot.ylim(0, 10)


pyplot.show()

