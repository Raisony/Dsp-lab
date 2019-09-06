# -*- coding: utf-8 -*-
# Tk_demo_03_slider.py
# TKinter demo
# Play a sinusoid using Pyaudio. Use two sliders to adjust the frequency and gain.

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

def fun_quit():
  global PLAY
  print('QUIT')
  PLAY = False

def clip16( x ):    
    # Clipping for 16 bits
    if x > 32767:
        x = 32767
    elif x < -32768:
        x = -32768
    else:
        x = x        
    return (x)


Fs = 8000     # rate (samples/second)
gain = 0.2 * 2**8

# Define Tkinter root
top = Tk.Tk()

# Define Tk variables
f1 = Tk.DoubleVar()
gain = Tk.DoubleVar()

# Initialize Tk variables
f1.set(200)   # f1 : frequency of sinusoid (Hz)
gain.set(0.2 * 2**8)

# Define buttons
S_freq = Tk.Scale(top, label = 'Frequency', variable = f1, from_ = 0, to = 400, tickinterval = 100)
S_gain = Tk.Scale(top, label = 'Gain', variable = gain, from_ = 0, to = 2**10-1)
Bquit = Tk.Button(top, text = 'Quit', command = fun_quit)

# Place buttons
Bquit.pack(side = Tk.BOTTOM, fill = Tk.X)
S_freq.pack(side = Tk.LEFT)
S_gain.pack(side = Tk.LEFT)

# Create Pyaudio object
p = pyaudio.PyAudio()
stream = p.open(
  format = pyaudio.paInt16,  
  channels = 1, 
  rate = Fs,
  input = True, 
  output = True,
  frames_per_buffer = 128)  #这里是什么意思来的？          
  # specify low frames_per_buffer to reduce latency

# BLOCKSIZE = 256
BLOCKSIZE = 1024
output_block = [0 for n in range(0, BLOCKSIZE)]
input_block = [0 for n in range(0, BLOCKSIZE)]
theta = 0
PLAY = True
gain_save = 0

print('* Start')
while PLAY:
  top.update()
  om1 = 2.0 * pi * f1.get() / Fs
  
  input_string = stream.read(BLOCKSIZE, exception_on_overflow = False)
  input_block = struct.unpack('h'*BLOCKSIZE, input_string)
  
  for i in range(0, BLOCKSIZE):

    output_block[i] = int( ((gain.get()-gain_save)/BLOCKSIZE*i+gain_save) * input_block[i] * cos(theta) )
    # output_block[i] = int( ((gain.get()-gain_save)/BLOCKSIZE*i+gain_save) * cos(theta) )
    # output_block[i] = int( gain.get() * cos(theta) )
    output_block[i] = clip16(output_block[i])
    theta = theta + om1
  gain_save = gain.get();
  if theta > pi:
  	theta = theta - 2.0 * pi

  output_string = struct.pack('h'*BLOCKSIZE, *output_block)   # 'h' for 16 bits
  stream.write(output_string)
print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
