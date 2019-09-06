# Tk entry demo: horizontal widgets

import sys

if sys.version_info[0] < 3:
	import Tkinter as Tk 	# for Python 2
else:
	import tkinter as Tk   	# for Python 3

top = Tk.Tk()

# Define widgets
L1 = Tk.Label(top, text = 'Enter text:')
E1 = Tk.Entry(top)

# Place widgets
L1.pack(side = Tk.LEFT)
E1.pack(side = Tk.RIGHT)

top.mainloop()