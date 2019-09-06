# Tk_demo_05_keyboard.py
# TKinter demo
# Play a sinusoid using Pyaudio. Use keyboard to adjust the frequency.


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

def my_function(event):
    global PLAY
    global f1
    print('You pressed ' + event.char)
    print('Frequency = ' + str(f1))
    if event.char == 'q':
      print('I quit')
      PLAY = False
    if event.char == 'i':
      f1 = f1 + 20
    if event.char == 'd':
      f1 = f1 - 20

# Define Tkinter root
top = Tk.Tk()
top.bind("<Key>", my_function)

# No Tk widgets!

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

print('Switch to Python window.')
print('Press i to increase frequency.')
print('Press d to decrease frequency.')
print('Press q to quit.')

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
