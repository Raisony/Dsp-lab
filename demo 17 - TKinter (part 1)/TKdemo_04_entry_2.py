# Tk entry demo: entry field and button.
# Prints entry text to console upon button press.

import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def fun1():
    print('You entered: ' + E1.get())

top = Tk.Tk()

# Define label
L1 = Tk.Label(top, text = 'Enter text')

# Define entry widget
E1 = Tk.Entry(top)

# Define button
B1 = Tk.Button(top, text = 'Click here', command = fun1)

# Place widgets
L1.pack()
E1.pack()
B1.pack()

top.mainloop()
