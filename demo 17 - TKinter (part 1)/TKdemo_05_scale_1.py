# Slider demo: Minimal.
# Does not do anything.

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

top = Tk.Tk()

# Define slider
S1 = Tk.Scale(top)

# Place slider
S1.pack()

top.mainloop()

