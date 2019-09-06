# Tk button demo: buttons change text displayed in label.
# Uses configure method.

import sys

if sys.version_info[0] < 3:
	# for Python 2
	import Tkinter as Tk
else:
	# for Python 3
	import tkinter as Tk   	


def fun1():
	L1.configure(text = 'The dog is brown')

def fun2():
	L1.configure(text = 'The cat is red')

top = Tk.Tk()

# Define widgets
L1 = Tk.Label(top, text = 'Press the buttons')
B1 = Tk.Button(top, text = 'Press me', command = fun1)
B2 = Tk.Button(top, text = 'Press me also...', command = fun2)
B3 = Tk.Button(top, text = 'Quit', command = top.quit)

# Place widgets
L1.pack()
B1.pack(fill = Tk.X)
B2.pack(fill = Tk.X)
B3.pack(fill = Tk.X)

top.mainloop()
