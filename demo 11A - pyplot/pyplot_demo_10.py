
from matplotlib import pyplot
import math

pyplot.ion()  # Switch on interactive mode  
# Use pyplot.ioff() to switch off

for i in range(100):
	x = i/10.0
	pyplot.plot(x, math.sin(x), 'ro')   # plot each point as a red dot
	pyplot.draw()                	# Show result

pyplot.ioff()
pyplot.show()
