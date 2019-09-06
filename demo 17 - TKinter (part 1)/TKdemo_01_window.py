# Minimal Tk demo

import sys

if sys.version_info[0] < 3:
	import Tkinter as Tk 	# for Python 2
else:
	import tkinter as Tk   	# for Python 3

print('Close the tk window to quit')

root = Tk.Tk()      # or 'top'
root.mainloop()
