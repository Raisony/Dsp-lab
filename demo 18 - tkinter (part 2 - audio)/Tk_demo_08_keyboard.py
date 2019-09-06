# Tk_demo_08_keyboard.py
# TKinter demo
# Play a note (via a second-order difference equation)
# whenever the user presses a key on the keyboard.

import pyaudio
import struct
import numpy as np
from scipy import signal
from math import sin, cos, pi
import sys

if sys.version_info[0] < 3:
    # for Python 2
    import Tkinter as Tk
else:
    # for Python 3
    import tkinter as Tk    

BLOCKLEN   = 64        # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 8000      # Frames per second

MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Parameters
Ta = 2      # Decay time (seconds)
f1 = 250    # Frequency (Hz)

# Pole radius and angle
r = 0.01**(1.0/(Ta*RATE))       # 0.01 for 1 percent amplitude
om1 = 2.0 * pi * float(f1)/RATE

# Filter coefficients (second-order IIR)
a1 = -2*r*cos(om1)
a2 = r**2
b0 = sin(om1)

# Open the audio output stream
p = pyaudio.PyAudio()
PA_FORMAT = pyaudio.paInt16
stream = p.open(
        format      = PA_FORMAT,
        channels    = CHANNELS,
        rate        = RATE,
        input       = False,
        output      = True,
        frames_per_buffer = 128)
# specify low frames_per_buffer to reduce latency

PLAY = True
KEYPRESS = False

def my_function(event):
    global PLAY
    global KEYPRESS
    print('You pressed ' + event.char)
    if event.char == 'q':
      print('I quit')
      PLAY = False
    KEYPRESS = True

top = Tk.Tk()
top.bind("<Key>", my_function)

ORDER = 2   # filter order
states = np.zeros(ORDER)
x = np.zeros(BLOCKLEN)

print('Switch to Python window. Then press keys for sound.')
print('Press "q" to quit')

while PLAY:

    top.update()

    if KEYPRESS and PLAY:
        # Some key (not 'q') was pressed
        x[0] = 10000.0

    [y, states] = signal.lfilter([b0], [1, a1, a2], x, zi = states)

    x[0] = 0.0        
    KEYPRESS = False

    y = np.clip(y.astype(int), -MAXVALUE, MAXVALUE)     # Clipping

    binary_data = struct.pack('h' * BLOCKLEN, *y);    # Convert to binary binary_data
    stream.write(binary_data, BLOCKLEN)               # Write binary binary_data to audio output

print('* Done.')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()
