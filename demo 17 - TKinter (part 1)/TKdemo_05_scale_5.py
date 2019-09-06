# Demo: Slider with variable.
# The slider value is printed to the console.

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

top = Tk.Tk()

# Define a Tk variable
x = Tk.DoubleVar()		# floating point value

def myfun1(event):
	print(x.get())

# Define slider
S1 = Tk.Scale(top, variable = x, command = myfun1)
S1.pack()

top.mainloop()
