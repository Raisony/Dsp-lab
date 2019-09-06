# Slider demo: Two sliders and a button.

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def myfun():
   string1 = 'Sum = ' + str(x.get() + y.get())
   L1.config(text = string1)

top = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar()
y = Tk.DoubleVar()

# Define widgets
S1 = Tk.Scale(top, variable = x)
S2 = Tk.Scale(top, variable = y)
B1 = Tk.Button(top, text = 'Add', command = myfun)
L1 = Tk.Label(top, text = 'Click the button')

# Place widgets
S1.pack(side = Tk.LEFT)
S2.pack(side = Tk.LEFT)
B1.pack(side = Tk.LEFT)
L1.pack(side = Tk.RIGHT)

top.mainloop()
