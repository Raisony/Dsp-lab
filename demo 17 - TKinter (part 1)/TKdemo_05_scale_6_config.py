# Slider demo: Slider with variable.
# The variable is displayed in a label.
# Uses configure method

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

top = Tk.Tk()

# Define Tk variable
x = Tk.DoubleVar() 		# floating point value

def update_label(event):
	L1.config(text = str(x.get()))

# Define widgets
S1 = Tk.Scale(top, variable = x, command = update_label)
L1 = Tk.Label(top)

# Place widgets
S1.pack()
L1.pack()

top.mainloop()
