# Tk label demo: Tk string variable

import sys

if sys.version_info[0] < 3:
	import Tkinter as Tk 	# for Python 2
else:
	import tkinter as Tk   	# for Python 3

top = Tk.Tk()

# Define a Tk variable (string)
s1 = Tk.StringVar()
s1.set('Hello. How are you?')

# Define label
L1 = Tk.Label(top, textvariable = s1)
L1.pack()

top.mainloop()
