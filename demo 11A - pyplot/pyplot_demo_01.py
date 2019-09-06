
from matplotlib import pyplot

# matplotlib.use('TKAgg')		# might be needed for mac...

x = [1, 3, 9, 8, 4, 6]
y = [5, 1, 4, 2, 2, 4]

# One plot
pyplot.figure(1)
pyplot.plot(x, y)
pyplot.xlabel('Time (n)')
pyplot.ylabel('Amplitude')
pyplot.title('Data')
  
pyplot.show()

