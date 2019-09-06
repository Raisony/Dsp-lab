# TKdemo_02_button.py

import sys

if sys.version_info[0] < 3:
	# for Python 2
	import Tkinter as Tk
	import tkMessageBox

	def fun1():
		tkMessageBox.showinfo('Message box title', 'Hello World')

else:
	# for Python 3
	import tkinter as Tk   	
	import tkinter.messagebox

	def fun1():
		tkinter.messagebox.showinfo('Message box title', 'Hello World')


top = Tk.Tk()

# Define button
B1 = Tk.Button(top, text = 'Press me', command = fun1)

# Place button.  pack() organizes widgets as blocks
B1.pack()

top.mainloop()
