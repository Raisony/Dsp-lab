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

BLOCKSIZE = 32      # Number of frames per block
WIDTH = 2           # Bytes per sample
CHANNELS = 1        # Mono
RATE = 16000        # Frames per second

MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Parameters
Ta = 2    # Decay time (seconds)
# f1 = 350    # Frequency (Hz) 
k = 13
f = [float(440*2**(float(i)/12)) for i in range(k)]
r = 0.01**(1.0/(Ta*RATE))       # 0.01 for 1 percent amplitude
om1 = [float(2.0 * pi * float(f[i])/RATE) for i in range(k)]
a1 = [-2*r*cos(om1[i]) for i in range(k)]
a2 = r**2
b0 = [sin(om1[i]) for i in range(k)]
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
y0 = np.zeros(BLOCKSIZE)
y1 = np.zeros(BLOCKSIZE)
y2 = np.zeros(BLOCKSIZE)
y3 = np.zeros(BLOCKSIZE)
y4 = np.zeros(BLOCKSIZE)
y5 = np.zeros(BLOCKSIZE)
y6 = np.zeros(BLOCKSIZE)
y7 = np.zeros(BLOCKSIZE)
y8 = np.zeros(BLOCKSIZE)
y9 = np.zeros(BLOCKSIZE)
y10 = np.zeros(BLOCKSIZE)
y11 = np.zeros(BLOCKSIZE)
y12 = np.zeros(BLOCKSIZE)

x = np.zeros(BLOCKSIZE)
x0 = np.zeros(BLOCKSIZE)
x1 = np.zeros(BLOCKSIZE)
x2 = np.zeros(BLOCKSIZE)
x3 = np.zeros(BLOCKSIZE)
x4 = np.zeros(BLOCKSIZE)
x5 = np.zeros(BLOCKSIZE)
x6 = np.zeros(BLOCKSIZE)
x7 = np.zeros(BLOCKSIZE)
x8 = np.zeros(BLOCKSIZE)
x9 = np.zeros(BLOCKSIZE)
x10 = np.zeros(BLOCKSIZE)
x11 = np.zeros(BLOCKSIZE)
x12 = np.zeros(BLOCKSIZE)
stop = False

while stop == False:

    x0[0] = 0.0
    x1[0] = 0.0
    x2[0] = 0.0
    x3[0] = 0.0
    x4[0] = 0.0
    x5[0] = 0.0
    x6[0] = 0.0
    x7[0] = 0.0
    x8[0] = 0.0
    x9[0] = 0.0
    x10[0] = 0.0
    x11[0] = 0.0
    x12[0] = 0.0

    for event in pygame.event.get():
    
        # Any key press counts as playing a note
        if event.type == pygame.KEYDOWN:
            # x[0] = 15000
            if event.key == pygame.K_a: # do
                x0[0] = 15000
                # fk = f[0]
            # else:
            #     x0[0] = 0
            if event.key == pygame.K_w: 
                x1[0] = 15000
                # fk = f[1]
            # else:
            #     x1[0] = 0
            if event.key == pygame.K_s: # re
                x2[0] = 15000
                # fk = f[2]
            # else:
            #     x2[0] = 0
            if event.key == pygame.K_e:
                x3[0] = 15000
                # fk = f[3]
            # else:
            #     x3[0] = 0
            if event.key == pygame.K_d: # mi
                x4[0] = 15000
                # fk = f[4]
            # else:
            #     x4[0] = 0
            if event.key == pygame.K_f: # fa
                x5[0] = 15000
                # fk = f[5]
            # else:
            #     x5[0] = 0
            if event.key == pygame.K_t:
                x6[0] = 15000
                # fk = f[6]
            # else:
            #     x6[0] = 0
            if event.key == pygame.K_g: # sol
                x7[0] = 15000
                # fk = f[7]
            # else:
            #     x7[0] = 0
            if event.key == pygame.K_y:
                x8[0] = 15000
                # fk = f[8]
            # else:
            #     x8[0] = 0
            if event.key == pygame.K_h: # la
                x9[0] = 15000
                # fk = f[9]
            # else:
            #     x9[0] = 0
            if event.key == pygame.K_u:
                x10[0] = 15000
                # fk = f[10]
            # else:
            #     x10[0] = 0
            if event.key == pygame.K_j: # si
                x11[0] = 15000
                # fk = f[11]
            # else:
            #     x11[0] = 0
            if event.key == pygame.K_k: # do
                x12[0] = 15000
                # fk = f[12]
            # f
            if event.key == pygame.K_q:
                stop = True
    # r = 0.01**(1.0/(Ta*RATE))       # 0.01 for 1 percent amplitude
    # om1 = [2.0 * pi * float(f[i])/RATE for i in range(k)]
    #         # Filter coefficients (second-order IIR)
    # a1 = [-2*r*cos(om1[i]) for i in range(k)]
    # a2 = r**2
    # b0 = [sin(om1[i]) for i in range(k)]
    for n in range(BLOCKSIZE):
        # if fk == f[0]:
        #     y0[n] = b0[0] * x0[n] - a1[0] * y0[n-1] - a2 * y0[n-2] 
        # if fk == f[1]:
        #     y1[n] = b0[1] * x1[n] - a1[1] * y1[n-1] - a2 * y1[n-2]
        # if fk == f[2]:
        #     y2[n] = b0[2] * x2[n] - a1[2] * y2[n-1] - a2 * y2[n-2]
        # if fk == f[3]:
        #     y3[n] = b0[3] * x3[n] - a1[3] * y3[n-1] - a2 * y3[n-2]
        # if fk == f[4]:
        #     y4[n] = b0[4] * x4[n] - a1[4] * y4[n-1] - a2 * y4[n-2]
        # if fk == f[5]:
        #     y5[n] = b0[5] * x5[n] - a1[5] * y5[n-1] - a2 * y5[n-2]
        # if fk == f[6]:
        #     y6[n] = b0[6] * x6[n] - a1[6] * y6[n-1] - a2 * y6[n-2]
        # if fk == f[7]:
        #     y7[n] = b0[7] * x7[n] - a1[7] * y7[n-1] - a2 * y7[n-2]
        # if fk == f[8]:
        #     y8[n] = b0[8] * x8[n] - a1[8] * y8[n-1] - a2 * y8[n-2]
        # if fk == f[9]:
        #     y9[n] = b0[9] * x9[n] - a1[9] * y9[n-1] - a2 * y9[n-2]
        # if fk == f[10]:
        #     y10[n] = b0[10] * x10[n] - a1[10] * y10[n-1] - a2 * y10[n-2]
        # if fk == f[11]:
        #     y11[n] = b0[11] * x11[n] - a1[11] * y11[n-1] - a2 * y11[n-2] 
        # if fk == f[12]:
        #     y12[n] = b0[12] * x12[n] - a1[12] * y12[n-1] - a2 * y12[n-2]
        y0[n] = b0[0] * x0[n] - a1[0] * y0[n-1] - a2 * y0[n-2] 
        y1[n] = b0[1] * x1[n] - a1[1] * y1[n-1] - a2 * y1[n-2]
        y2[n] = b0[2] * x2[n] - a1[2] * y2[n-1] - a2 * y2[n-2]
        y3[n] = b0[3] * x3[n] - a1[3] * y3[n-1] - a2 * y3[n-2]
        y4[n] = b0[4] * x4[n] - a1[4] * y4[n-1] - a2 * y4[n-2]
        y5[n] = b0[5] * x5[n] - a1[5] * y5[n-1] - a2 * y5[n-2]
        y6[n] = b0[6] * x6[n] - a1[6] * y6[n-1] - a2 * y6[n-2]
        y7[n] = b0[7] * x7[n] - a1[7] * y7[n-1] - a2 * y7[n-2]
        y8[n] = b0[8] * x8[n] - a1[8] * y8[n-1] - a2 * y8[n-2]
        y9[n] = b0[9] * x9[n] - a1[9] * y9[n-1] - a2 * y9[n-2]
        y10[n] = b0[10] * x10[n] - a1[10] * y10[n-1] - a2 * y10[n-2]
        y11[n] = b0[11] * x11[n] - a1[11] * y11[n-1] - a2 * y11[n-2] 
        y12[n] = b0[12] * x12[n] - a1[12] * y12[n-1] - a2 * y12[n-2]
    y = y0+y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12
    # nnnnnprint(y)
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
