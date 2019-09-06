# Tk button demo: simple demo.
# Prints text to console.

import sys

if sys.version_info[0] < 3:
	# for Python 2
	import Tkinter as Tk
else:
	# for Python 3
	import tkinter as Tk   	


def fun1():
	print('Hello World')

top = Tk.Tk()

# Define button
B1 = Tk.Button(top, text = 'Press me', command = fun1)

# Place button
B1.pack()

top.mainloop()
