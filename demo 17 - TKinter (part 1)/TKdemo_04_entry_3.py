# Tk entry demo: entry and button.
# Prints entry text to console upon button press.
# Uses a Tk variable.

import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def fun1():
    print('You entered: ' + s.get())

top = Tk.Tk()

# Define Tk variable
s = Tk.StringVar()

# Define widgets
L1 = Tk.Label(top, text = 'Enter text')
E1 = Tk.Entry(top, textvariable = s)
B1 = Tk.Button(top, text = 'Click here', command = fun1)

# Place widgets
L1.pack()
E1.pack()
B1.pack()

top.mainloop()
