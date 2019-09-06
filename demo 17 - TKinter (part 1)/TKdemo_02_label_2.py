# Tk label demo: Two labels

import sys

if sys.version_info[0] < 3:
	import Tkinter as Tk 	# for Python 2
else:
	import tkinter as Tk   	# for Python 3

top = Tk.Tk()

# Define label
L1 = Tk.Label(top, text = 'Hello. How are you?')
L1.pack()

# Define label
L2 = Tk.Label(top, text = 'This is another label')
L2.pack()

top.mainloop()
