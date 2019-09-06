import sys

if sys.version_info[0] < 3:
  import Tkinter as Tk  # for Python 2
else:
  import tkinter as Tk    # for Python 3

top = Tk.Tk()

def fun1(event):
    print('You clicked at position %d %d' % (event.x, event.y))
    x1.set(str(event.x))
    y1.set(str(event.y))
def fun2(event):
    print('You pressed key %s' % repr(event.char))
    s3.set(str(event.char))
x1 = Tk.StringVar()
y1 = Tk.StringVar()
s3 = Tk.StringVar()

F1 = Tk.Frame(top, width = 200, height = 100)
F1.bind("<Button-1>", fun1)		# "<Button-1>" refers to the mouse
F1.bind("<Key>", fun2)			# "<Key>" refers to the keyboard
F1.pack()
F1.focus_set()


# Define widgets
L1 = Tk.Label(top, text = 'X')
E1 = Tk.Entry(top, textvariable = x1)
L2 = Tk.Label(top, text = ', Y')
E2 = Tk.Entry(top, textvariable = y1)
L3 = Tk.Label(top, text = ', Press')
E3 = Tk.Entry(top, textvariable = s3)
# Place widgets
L1.pack(side = Tk.LEFT)
E1.pack(side = Tk.RIGHT)
L2.pack(side = Tk.LEFT)
E2.pack(side = Tk.RIGHT)
L3.pack(side = Tk.LEFT)
E3.pack(side = Tk.RIGHT)


top.mainloop()

