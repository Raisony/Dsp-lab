# Demo: Slider with variable
# (but the variable is not used)

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

top = Tk.Tk()

# Define a Tk variable
x = Tk.DoubleVar()		# floating point value

# Define slider
S1 = Tk.Scale(top, variable = x)
S1.pack()

top.mainloop()

