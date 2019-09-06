# Slider demo: Slider with variable.
# The variable is displayed in a label.
# Uses a Tk variable.

import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

top = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar() 		# floating point value
s = Tk.StringVar()		# text string

def update_label(event):
	s.set( str(x.get()) )

# Define widgets
S1 = Tk.Scale(top, variable = x, command = update_label)
L1 = Tk.Label(top, textvariable = s)

# Place widgets
S1.pack()
L1.pack()

top.mainloop()
