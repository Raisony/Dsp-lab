
from matplotlib import pyplot

x = [1, 3, 9, 8, 4, 6]
y = [5, 1, 4, 2, 2, 4]
z = [6, 3, 6, 8, 5, 9]

lines = pyplot.plot(x, y, x, z)   # 'lines' is a list

print(type(lines))		# list
print(type(lines[0]))	# line data type

# set values of line parameters
lines[0].set_color('black')
lines[1].set_color('blue')

lines[0].set_linewidth(6)

pyplot.show()

