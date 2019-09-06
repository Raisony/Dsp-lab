import sys

if sys.version_info[0] < 3:
	import Tkinter as Tk
else:
	import tkinter as Tk

top = Tk.Tk()

x1 = Tk.DoubleVar()
x1.set(100.0)
x2 = Tk.StringVar()
x2.set(str(x1.get()))
a1 = Tk.StringVar()

def increase_fun():
	x1.set(x1.get() + 10)
	x2.set(str(x1.get()))
def decrease_fun():
	x1.set(x1.get() - 10)
	x2.set(str(x1.get()))
def show_text_fun():
	x1.set(float(x1.get()) + float(s2.get()))
	x2.set(str(x1.get()))
def scale_update(event):
	L6.config(text = str(a1.get()))
def fun_1(event):
	F1.focus_set()
	print('You clicked at position %d %d' % (event.x, event.y))
def fun_2(event):
	F1.focus_set()
	print('You pressed key %s' % repr(event.char))

s1 = Tk.StringVar()
s1.set('NetID: js9902\n')
s2 = Tk.DoubleVar()

L1 = Tk.Label(top, text = 'This is Jingjie Sheng.', foreground ='blue')
L1.pack()
L2 = Tk.Label(top, textvariable = s1, foreground ='blue')
L2.pack()
L3 = Tk.Label(top, textvariable = x2, background ='yellow')
L3.pack()

B1 = Tk.Button(top, text = 'Increase: +10', command = increase_fun)
B2 = Tk.Button(top, text = 'Decrease: -10', command = decrease_fun)
B1.pack(fill = Tk.X)
B2.pack(fill = Tk.X)

L4 = Tk.Label(top, text = '\nPlease entry the number you want to add: ',foreground ='red')
L4.pack()
E1 = Tk.Entry(top, textvariable = s2)
E1.pack()
B4 = Tk.Button(top, text = 'Show the added result', command = show_text_fun)
B4.pack(fill = Tk.X)

L5 = Tk.Label(top, text = '\nThe scale is a independent part: ', foreground ='red')
L5.pack()
S1 = Tk.Scale(top, variable = a1, command = scale_update)
S1.pack()
L6 = Tk.Label(top)
L6.pack()
# S2.pack(side = Tk.RIGHT)
# B5 = Tk.Button(top, text = 'show the minused result', command = show_text_fun)
# B5.pack(side = Tk.LEFT, fill = Tk.X)

L7 = Tk.Label(top, text = '\n-------This is the clicking area-------',foreground ='red')
L7.pack()
L8 = Tk.Label(top, text = '------Please click on keyboard------', foreground = 'red')
L8.pack()
F1 = Tk.Frame(top, width = 200, height = 100)
F1.bind("<Button-1>", fun_1)
F1.bind("<Key>", fun_2)
F1.pack()
F1.focus_set()

L9 = Tk.Label(top, text = '------This is Listbox (without function)------', foreground = 'red')
L9.pack()
LB = Tk.Listbox(top)
LB.pack()
for item in ["Listbox_1", "Listbox_2", "Listbox_3", "Listbox_4"]:
    LB.insert(Tk.END, item)

B3 = Tk.Button(top, text = 'Quit', command = top.quit)
B3.pack(side = Tk.BOTTOM,fill = Tk.X)


top.mainloop()
