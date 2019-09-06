# Tk_demo_01_buttons.py
# TKinter demo
# Play a sinusoid using Pyaudio. Use buttons to adjust the frequency.

from math import cos, pi 
import pyaudio
import struct
import sys

if sys.version_info[0] < 3:
	# for Python 2
	import Tkinter as Tk
else:
	# for Python 3
	import tkinter as Tk   	

Fs = 8000           # rate (samples/second)
f1 = 200            # f1 : frequency of sinusoid (Hz)
gain = 0.2 * 2**15

def fun_up():
  global f1
  print('UP')
  f1 = f1 + 20

def fun_dn():
  global f1
  print('DOWN')
  f1 = f1 - 20

def fun_quit():
  global PLAY
  print('QUIT')
  PLAY = False

# Define TK root
top = Tk.Tk()

# Define widgets
Lab1 = Tk.Label(top, text = 'Frequency adjustment')
Bup = Tk.Button(top, text = 'Increase', command = fun_up)
Bdn = Tk.Button(top, text = 'Decrease', command = fun_dn)
Bquit = Tk.Button(top, text = 'Quit', command = fun_quit)

# Place buttons
Lab1.pack()
Bup.pack()
Bdn.pack()
Bquit.pack()

# Create Pyaudio object
p = pyaudio.PyAudio()
stream = p.open(
    format = pyaudio.paInt16,  
    channels = 1, 
    rate = Fs,
    input = False, 
    output = True,
    frames_per_buffer = 128)            
    # specify low frames_per_buffer to reduce latency

BLOCKLEN = 512
output_block = [0 for n in range(0, BLOCKLEN)]
theta = 0
PLAY = True

while PLAY:
  top.update()
  om1 = 2.0 * pi * f1 / Fs
  for i in range(0, BLOCKLEN):
    output_block[i] = int( gain * cos(theta) )
    theta = theta + om1
  while theta > pi:
  	theta = theta - 2.0 * pi
  binary_data = struct.pack('h' * BLOCKLEN, *output_block)   # 'h' for 16 bits
  stream.write(binary_data)
print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
