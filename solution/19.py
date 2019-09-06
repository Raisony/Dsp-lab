#coding=utf-8
import sys
import Tkinter as Tk

top = Tk.Tk()

x1 = Tk.DoubleVar()
x1.set(0.0)
x2 = Tk.StringVar()
x2.set(str(x1.get()))
a1 = Tk.StringVar()

def increase_num():
	x1.set(x1.get() + 2)
	x2.set(str(x1.get()))
def decrease_num():
	x1.set(x1.get() - 2)
	x2.set(str(x1.get()))
def show_text():
	x1.set(float(x1.get()) + float(s2.get()))
	x2.set(str(x1.get()))
def scale_update(event):
	Label5.config(text = str(a1.get()))


Label1 = Tk.Label(top, text = '😜!WECLCOME!👻')
Label1.pack()

Lable2 = Tk.Label(top, textvariable = x2)
Lable2.pack()

s2 = Tk.DoubleVar()
Lable3 = Tk.Label(top, text = 'Enter a number:')
Lable3.pack()
Enter1 = Tk.Entry(top, textvariable = s2)
Enter1.pack()
Button3 = Tk.Button(top, text = 'Your input is 😱', command = show_text)
Button3.pack(fill = Tk.X)


Button1 = Tk.Button(top, text = 'Decrease: -2 🙃', command = decrease_num)
Button2 = Tk.Button(top, text = 'Increase: +2 😊', command = increase_num)
Button1.pack(fill = Tk.X)
Button2.pack(fill = Tk.X)



Label4 = Tk.Label(top, text = 'Scale: ')
Label4.pack()
S1 = Tk.Scale(top, variable = a1, command = scale_update)
S1.pack(side = Tk.LEFT)
Label5 = Tk.Label(top)
Label5.pack()


top.mainloop()
