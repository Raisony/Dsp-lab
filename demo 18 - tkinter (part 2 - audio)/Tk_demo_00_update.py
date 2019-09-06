# Tk_demo_00_update.py
# TKinter demo
# The .update function

import sys

if sys.version_info[0] < 3:
	# for Python 2
	import Tkinter as Tk
else:
	# for Python 3
	import tkinter as Tk   	

def fun_up():
  global x
  x = x + 1
  print('Increase x to', x)

def fun_down():
  global x
  x = x - 1
  print('Decrease x to', x)

def fun_quit():
  global PLAY
  print('I quit')
  PLAY = False

# Define TK root
top = Tk.Tk()

# Define widgets
Lab1 = Tk.Label(top, text = 'Value adjustment')
Bup = Tk.Button(top, text = 'Increase', command = fun_up)
Bdown = Tk.Button(top, text = 'Decrease', command = fun_down)
Bquit = Tk.Button(top, text = 'Quit', command = fun_quit)

# Place buttons
Lab1.pack()
Bup.pack()
Bdown.pack()
Bquit.pack()

x = 200            # value to be adjusted
print('x = ', x)

PLAY = True

while PLAY:
  top.update()

print('* Finished')

