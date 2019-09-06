# Slider demo: Two sliders.
# Their sum and product are displayed in two different labels.
#Reigns 0.1
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

top = Tk.Tk()

def update(event):
	z1 = a.get()
	z2 = b.get()
	z3 = c.get()
	z4 = d.get()
	s1.set( 'Religion ' + str(z1))
	s2.set( 'Force ' + str(z2))
	s3.set( 'Populance ' + str(z3))
	s4.set( 'Capital ' + str(z4))

# Define Tk variables
a = Tk.DoubleVar()
b = Tk.DoubleVar()
c = Tk.DoubleVar()
d = Tk.DoubleVar()

s1 = Tk.StringVar()
s2 = Tk.StringVar()
s3 = Tk.StringVar()
s4 = Tk.StringVar()

# Define widgets
S1 = Tk.Scale(top, variable = a, command = update)
S2 = Tk.Scale(top, variable = b, command = update)
S3 = Tk.Scale(top, variable = c, command = update)
S4 = Tk.Scale(top, variable = d, command = update)
L1 = Tk.Label(top, textvariable = s1)
L2 = Tk.Label(top, textvariable = s2)
L3 = Tk.Label(top, textvariable = s3)
L4 = Tk.Label(top, textvariable = s4)
B1 = Tk.Button(top, text = 'Close', command = top.quit)

# Place widgets
S1.pack(side = Tk.LEFT)
S2.pack(side = Tk.LEFT)
S3.pack(side = Tk.LEFT)
S4.pack(side = Tk.LEFT)
L1.pack(side = Tk.TOP)
L2.pack(side = Tk.TOP)
L3.pack(side = Tk.TOP)
L4.pack(side = Tk.TOP)
B1.pack(side = Tk.BOTTOM, fill = Tk.X)

# Define the label
L1 = Tk.Label(top, text = 'Reigns 0.1')

# Place the label
L1.pack()

def fun1():
	L1.configure(text = 'The dog is brown')

def fun2():
	L1.configure(text = 'The cat is red')

def fun3():
	L1.configure(text= 'The dog is brown')

def fun4():
	L1.configure(text= 'The cat is red')


# Define widgets

L1 = Tk.Label(top, text = 'Press the buttons')
B1 = Tk.Button(top, text = 'Press this one', command = fun1)
B2 = Tk.Button(top, text = 'Press this one', command = fun2)
B3 = Tk.Button(top, text = 'Press this one', command = fun3)
B4 = Tk.Button(top, text = 'Press this one', command = fun4)
B3 = Tk.Button(top, text = 'Quit', command = top.quit)

# Place widgets
L1.pack()
B1.pack(fill = Tk.X)
B2.pack(fill = Tk.X)
B3.pack(fill = Tk.X)


top.mainloop()
