# Tk button demo: buttons change text displayed in label.
# Uses Tk string variable

import sys

if sys.version_info[0] < 3:
	# for Python 2
	import Tkinter as Tk
else:
	# for Python 3
	import tkinter as Tk   	


def fun1():
	s1.set('The dog is brown')

def fun2():
	s1.set('The cat is red')

top = Tk.Tk()

s1 = Tk.StringVar()
s1.set('I will change')

# Define widgets
L1 = Tk.Label(top, textvariable = s1)
B1 = Tk.Button(top, text = 'Press me', command = fun1)
B2 = Tk.Button(top, text = 'Press me also...', command = fun2)
B3 = Tk.Button(top, text = 'Quit', command = top.quit)

# Place widgets
L1.pack()
B1.pack(fill = Tk.X)
B2.pack(fill = Tk.X)
B3.pack(fill = Tk.X)

top.mainloop()
