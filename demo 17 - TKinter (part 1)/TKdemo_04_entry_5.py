# Tk entry demo: show entry text in label upon button press.
# Use configure method.

import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def fun1():
    L2.configure(text = 'You entered: ' + E1.get())

top = Tk.Tk()

# Define widgets
L1 = Tk.Label(top, text = 'Enter text')
E1 = Tk.Entry(top)
B1 = Tk.Button(top, text = 'Click here', command = fun1)
L2 = Tk.Label(top)
B2 = Tk.Button(top, text = 'Quit', command = top.quit)

# Place widgets
L1.pack()
E1.pack()
B1.pack()
L2.pack()
B2.pack()

top.mainloop()
