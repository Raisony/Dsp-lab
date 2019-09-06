# Tk entry demo: show entry text in label with continuous update.
# Use Tk variable

import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

top = Tk.Tk()

# Define Tk string variable
s = Tk.StringVar()

# Define widgets
L1 = Tk.Label(top, text = 'Enter text')
E1 = Tk.Entry(top, textvariable = s)
L2 = Tk.Label(top, textvariable = s)

# Place widgets
L1.pack()
E1.pack()
L2.pack()

top.mainloop()
