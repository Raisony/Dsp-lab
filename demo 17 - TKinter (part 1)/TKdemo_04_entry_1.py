# Tk entry demo: Minimal demo.
# Does not do anything.

import sys

if sys.version_info[0] < 3:
	import Tkinter as Tk 	# for Python 2
else:
	import tkinter as Tk   	# for Python 3

top = Tk.Tk()

# Define label
L1 = Tk.Label(top, text = 'Enter your name')

# Define entry widget
E1 = Tk.Entry(top)

# Place widgets
L1.pack()
E1.pack()

top.mainloop()
