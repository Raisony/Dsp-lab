# Tk label demo: Minimal demo

import sys

if sys.version_info[0] < 3:
	import Tkinter as Tk 	# for Python 2
else:
	import tkinter as Tk   	# for Python 3

top = Tk.Tk()

# Define the label
L1 = Tk.Label(top, text = 'Hello. How are you?')

# Place the label
L1.pack()

top.mainloop()
