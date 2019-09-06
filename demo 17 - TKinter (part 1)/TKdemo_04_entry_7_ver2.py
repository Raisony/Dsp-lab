# Tk entry demo: Adds two entered numbers, shows result in a label.
# Uses Tk variables.

import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def fun1():
    c = float(s1.get()) + float(s2.get())
    s3.set(str(c))

top = Tk.Tk()

# Define Tk variables
s1 = Tk.StringVar()
s2 = Tk.StringVar()
s3 = Tk.StringVar()

# Define widgets
L1 = Tk.Label(top, text = 'Enter two numbers')
E1 = Tk.Entry(top, textvariable = s1)
E2 = Tk.Entry(top, textvariable = s2) 
B1 = Tk.Button(top, text = 'Add', command = fun1)
L2 = Tk.Label(top, textvariable = s3)
B2 = Tk.Button(top, text = 'Quit', command = top.quit)

# Place widgets
L1.pack()
E1.pack()
E2.pack()
B1.pack()
L2.pack()
B2.pack()

top.mainloop()
