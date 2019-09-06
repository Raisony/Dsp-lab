# Tk button demo: two buttons.
# Prints text to console.

import sys

if sys.version_info[0] < 3:
	# for Python 2
	import Tkinter as Tk
else:
	# for Python 3
	import tkinter as Tk   	


def fun1():
	print('Hello World')

def fun2():
	print('How are you?')

top = Tk.Tk()

# Define buttons
B1 = Tk.Button(top, text = 'Press me', command = fun1)
B2 = Tk.Button(top, text = 'Press me also...', command = fun2)

# Place buttons
B1.pack()
B2.pack()

top.mainloop()
