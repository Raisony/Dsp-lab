# Tk_demo_07_keyboard.py
# TKinter demo
# Play a sinusoid using Pyaudio. Use keyboard to adjust the frequency and gain.

from math import cos, pi, fabs
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

MAXGAIN = 2**15-1  # Maximum allowed gain (because WIDTH = 2)

def my_function(event):
    global PLAY
    global f1, gain
    print('You pressed ' + event.char)
    if event.char == 'q':
      print('I quit')
      PLAY = False
    if event.char == 'i':
      f1 = f1 + 20
    if event.char == 'd':
      f1 = f1 - 20
    if event.char == 'l':
      gain = gain * 1.3
    if event.char == 's':
      gain = gain / 1.3
    if fabs(gain) > MAXGAIN:     # fabs : floating-point absolute value
      gain = MAXGAIN
      print('Maximum gain attained')
    f1_str.set('Frequency = ' + str(f1))
    gain_str.set('Gain = ' + str(int(gain)))

# Define Tkinter root
top = Tk.Tk()
top.bind("<Key>", my_function)

f1_str = Tk.StringVar()
gain_str = Tk.StringVar()

f1_str.set('Frequency = ' + str(f1))
gain_str.set('Gain = ' + str(int(gain)))

label_freq = Tk.Label(top, textvariable = f1_str)
label_freq.pack()

label_gain = Tk.Label(top, textvariable = gain_str)
label_gain.pack()

label_explain = Tk.Label(top, text = 'freq (i/d) ; gain (l/s) ; q to quit')
label_explain.pack()

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
print('Use i to increase frequency.')
print('Use d to decrease frequency.')
print('Use l to increase gain (louder).')
print('Use s to decrease gain (softer).')
print('Press q to quit.')

BLOCKSIZE = 512
output_block = [0 for n in range(0, BLOCKSIZE)]
theta = 0
PLAY = True

while PLAY:
  top.update()
  om1 = 2.0 * pi * f1 / Fs
  for i in range(0, BLOCKSIZE):
    output_block[i] = int( gain * cos(theta) )
    theta = theta + om1
  while theta > pi:
  	theta = theta - 2.0 * pi
  output_string = struct.pack('h' * BLOCKSIZE, *output_block)   # 'h' for 16 bits
  stream.write(output_string)
print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
