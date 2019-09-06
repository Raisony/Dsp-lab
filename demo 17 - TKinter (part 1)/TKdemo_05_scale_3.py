# Slider demo: Two sliders and a quit button

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

top = Tk.Tk()

# Define widgets
B1 = Tk.Button(top, text = 'Quit', command = top.quit)
S1 = Tk.Scale(top, label = 'Slider 1')
S2 = Tk.Scale(top, label = 'Slider 2')

# Place widgets
B1.pack(side = Tk.BOTTOM, fill = Tk.X)
S1.pack(side = Tk.LEFT)
S2.pack(side = Tk.LEFT)

top.mainloop()
