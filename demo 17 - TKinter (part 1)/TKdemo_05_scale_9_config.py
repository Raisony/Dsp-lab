# Slider demo: Slider and button.
# Uses configure method.

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def myfun():
   string1 = 'Value = ' + str(x.get())
   L1.config(text = string1)

top = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar()


# Define widgets
S1 = Tk.Scale(top, variable = x)     
B1 = Tk.Button(top, text = 'Press to display value', command = myfun)
L1 = Tk.Label(top)

# Place widgets
S1.pack()
B1.pack()
L1.pack()

top.mainloop()
