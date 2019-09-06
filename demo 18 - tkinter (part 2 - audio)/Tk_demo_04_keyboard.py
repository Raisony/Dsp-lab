# Tk_demo_04_keyboard.py
# TKinter demo
# Read characters from the keyboard

import sys

if sys.version_info[0] < 3:
  import Tkinter as Tk 		# for Python 2
else:
  import tkinter as Tk    	# for Python 3

def fun1(event):
    print(event)
    print('You pressed ' + event.char)
    if event.char == 'q':
    	print('I quit')
    	root.quit()

# Define Tk root
root = Tk.Tk()

# Bind keyboard to root
root.bind("<Key>", fun1)

print('Switch to Python window, then press keys on keyboard. Press q to quit.')

root.mainloop()
