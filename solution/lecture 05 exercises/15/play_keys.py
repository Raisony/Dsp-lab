# play_keys.py

"""
PyAudio Example: Generate random pulses and input them to an IIR filter of 2nd order.
Gerald Schuller, March 2015 
Modified - Ivan Selesnick, October 2015
"""

import pyaudio
import struct
import pygame
import numpy as np
from math import sin, cos, pi

BLOCKSIZE = 1024      # Number of frames per block
WIDTH = 2           # Bytes per sample
CHANNELS = 1        # Mono
RATE = 16000        # Frames per second

MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Parameters
Ta = 1.2    # Decay time (seconds)
# f1 = 350    # Frequency (Hz) 
fk = 440
k = 13
f = [float(440*2**(float(i)/12)) for i in range(k)]
# Pole radius and angle

# Open the audio output stream
p = pyaudio.PyAudio()
PA_FORMAT = pyaudio.paInt16
stream = p.open(format = PA_FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = False,
                output = True)


pygame.init()  # Initializes pygame

print("Press keys for sound. Press 'q' to quit.")
print("OK go...")

y = np.zeros(BLOCKSIZE)
x = np.zeros(BLOCKSIZE)

stop = False

while stop == False:

    x[0] = 0.0

    for event in pygame.event.get():
    
        # Any key press counts as playing a note
        if event.type == pygame.KEYDOWN:
            x[0] = 15000
            if event.key == pygame.K_a: # do
                fk = f[0]
            elif event.key == pygame.K_w: 
                fk = f[1]
            elif event.key == pygame.K_s: # re
                fk = f[2]
            elif event.key == pygame.K_e:
                fk = f[3]
            elif event.key == pygame.K_d: # mi
                fk = f[4]
            elif event.key == pygame.K_f: # fa
                fk = f[5]
            elif event.key == pygame.K_t:
                fk = f[6]
            elif event.key == pygame.K_g: # sol
                fk = f[7]
            elif event.key == pygame.K_y:
                fk = f[8]
            elif event.key == pygame.K_h: # la
                fk = f[9]
            elif event.key == pygame.K_u:
                fk = f[10]
            elif event.key == pygame.K_j: # si
                fk = f[11]
            elif event.key == pygame.K_k: # do
                fk = f[12]
            elif event.key == pygame.K_q:
                stop = True
    r = 0.01**(1.0/(Ta*RATE))       # 0.01 for 1 percent amplitude
    om1 = 2.0 * pi * float(fk)/RATE
            # Filter coefficients (second-order IIR)
    a1 = -2*r*cos(om1)
    a2 = r**2
    b0 = sin(om1)
    for n in range(BLOCKSIZE):
        y[n] = b0 * x[n] - a1 * y[n-1] - a2 * y[n-2] 

    y = np.clip(y.astype(int), -MAXVALUE, MAXVALUE)     # Clipping

    # Convert numeric list to binary string
    data = struct.pack('h' * BLOCKSIZE, *y);

    # Write binary string to audio output stream
    stream.write(data, BLOCKSIZE)

print('* Done.')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()

pygame.quit()
