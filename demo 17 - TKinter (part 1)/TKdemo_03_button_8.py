# Tk button demo: buttons to change a value.
# Uses Tk variables.

import sys

if sys.version_info[0] < 3:
	# for Python 2
	import Tkinter as Tk
else:
	# for Python 3
	import tkinter as Tk   	


def fun1():
	x.set(x.get() + 1)
	s.set(str(x.get()))

def fun2():
	x.set(x.get() - 1)
	s.set(str(x.get()))

top = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar()              # floating point value
s = Tk.StringVar()				# text string

# Initialize TK variables
x.set(10)
s.set(str(x.get()))

# Define widgets
L1 = Tk.Label(top, textvariable = s)
B1 = Tk.Button(top, text = 'Increase', command = fun1)
B2 = Tk.Button(top, text = 'Decrease', command = fun2)
B3 = Tk.Button(top, text = 'Quit', command = top.quit)

# Place widgets
L1.pack()
B1.pack(fill = Tk.X)
B2.pack(fill = Tk.X)
B3.pack(fill = Tk.X)

top.mainloop()
