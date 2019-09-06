# Slider demo: Two sliders.
# Their sum is displayed in a label.
# Uses Tk string variable.

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def update_sum(event):
	z = x.get() + y.get()
	s.set('Sum = ' + str(z))

top = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar()
y = Tk.DoubleVar()
s = Tk.StringVar()

# Define widgets
S1 = Tk.Scale(top, variable = x, command = update_sum)
S2 = Tk.Scale(top, variable = y, command = update_sum)
L1 = Tk.Label(top, textvariable = s)

# Place widgets
L1.pack(side = Tk.BOTTOM)
S1.pack(side = Tk.LEFT)
S2.pack(side = Tk.LEFT)

top.mainloop()
