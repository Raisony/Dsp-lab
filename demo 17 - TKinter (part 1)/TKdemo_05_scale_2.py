# Slider demo: Two sliders

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

top = Tk.Tk()

# Define two sliders
S1 = Tk.Scale(top, label = 'Slider 1')
S2 = Tk.Scale(top, label = 'Slider 2')

# Place sliders
S1.pack()
S2.pack()

top.mainloop()

