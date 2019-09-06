
from matplotlib import pyplot

x = [1, 3, 9, 8, 4, 6]
y = [5, 1, 4, 2, 2, 4]
z = [6, 3, 6, 8, 5, 9]

pyplot.figure(1)

line1, line2 = pyplot.plot(x, y, x, z)

# setp : set parameter
pyplot.setp(line1, linewidth = 3)
pyplot.setp(line1, color = 'red')

pyplot.setp(line2, linewidth = 2, color = 'blue',
	linestyle = '--', marker = 'o', markersize = 8)

pyplot.show()

# To display line properties you can set: 
# pyplot.setp(line1)
