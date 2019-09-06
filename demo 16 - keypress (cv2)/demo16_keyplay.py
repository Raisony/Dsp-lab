
# coding: utf-8

# In[ ]:

#Wei Han, N16422093
import pyaudio
import struct
import numpy as np
from math import sin, cos, pi
import cv2

BLOCKSIZE   = 1024        # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 8000      # Frames per second

MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Parameters
Ta=  2    # Decay time (seconds)
a= 2**(1/12)
r = 0.01**(1.0/(Ta*RATE))
f1=440
a9= r**2

b0=0
b1=0
b2=0
b3=0
b4=0
b5=0
b6=0
b7=0

a0=0
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0


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

print('Select the image window, then press keys for sound.')
print('Press "q" to quit')

img = cv2.imread('image_01.png')
cv2.imshow('image', img)

y = np.zeros(BLOCKSIZE)
x = np.zeros(BLOCKSIZE)

ya = np.zeros(BLOCKSIZE)
xa = np.zeros(BLOCKSIZE)
ys= np.zeros(BLOCKSIZE)
xs = np.zeros(BLOCKSIZE)
yd= np.zeros(BLOCKSIZE)
xd = np.zeros(BLOCKSIZE)
yf= np.zeros(BLOCKSIZE)
xf = np.zeros(BLOCKSIZE)
yg= np.zeros(BLOCKSIZE)
xg = np.zeros(BLOCKSIZE)
yh = np.zeros(BLOCKSIZE)
xh = np.zeros(BLOCKSIZE)
yj = np.zeros(BLOCKSIZE)
xj = np.zeros(BLOCKSIZE)
yk = np.zeros(BLOCKSIZE)
xk= np.zeros(BLOCKSIZE)


while True:

    key = cv2.waitKey(1)

    if key == -1:
        # No key was pressed
        xa[0] = 0.0
        xs[0] = 0.0
        xd[0] = 0.0
        xf[0] = 0.0
        xg[0] = 0.0
        xh[0] = 0.0
        xj[0] = 0.0
        xk[0] = 0.0

    elif key == ord('a'):
        f= (a**0)*f1
        om1 = 2.0 * pi * float(f)/RATE
        a0 = -2*r*cos(om1)
        b0 = sin(om1)
        xa[0]= 15000
    elif key == ord('s'):
        f= (a**1)*f1
        om1 = 2.0 * pi * float(f)/RATE
        a1 = -2*r*cos(om1)
        b1 = sin(om1)
        xs[0]= 15000
    elif key == ord('d'):
        f= (a**2)*f1
        om1 = 2.0 * pi * float(f)/RATE
        a2 = -2*r*cos(om1)
        b2 = sin(om1)
        xd[0]= 15000
    elif key == ord('f'):
        f= (a**3)*f1
        om1 = 2.0 * pi * float(f)/RATE
        a3 = -2*r*cos(om1)
        b3 = sin(om1)
        xf[0]= 15000
    elif key == ord('g'):
        f= (a**4)*f1
        om1 = 2.0 * pi * float(f)/RATE
        a4 = -2*r*cos(om1)
        b4 = sin(om1)
        xg[0]= 15000
    elif key == ord('h'):
        f= (a**5)*f1
        om1 = 2.0 * pi * float(f)/RATE
        a5 = -2*r*cos(om1)
        b5 = sin(om1)
        xh[0]= 15000
    elif key == ord('j'):
        f= (a**6)*f1
        om1 = 2.0 * pi * float(f)/RATE
        a6 = -2*r*cos(om1)
        b6 = sin(om1)
        xj[0]= 15000
    elif key == ord('k'):
        f= (a**7)*f1
        om1 = 2.0 * pi * float(f)/RATE
        a7 = -2*r*cos(om1)
        b7 = sin(om1)
        xk[0]= 15000
    elif key == ord('q'):
        break

    # Run difference equation for block
    for n in range(BLOCKSIZE):
        ya[n] = b0 * xa[n] - a0 * ya[n-1] - a9* ya[n-2]
        ys[n] = b1 * xs[n] - a1 * ys[n-1] - a9 *ys[n-2]
        yd[n] = b2 * xd[n] - a2 * yd[n-1] - a9* yd[n-2]
        yf[n] = b3 * xf[n] - a3 * yf[n-1] - a9* yf[n-2]
        yg[n] = b4 * xg[n] - a4 * yg[n-1] - a9* yg[n-2]
        yh[n] = b5 * xh[n] - a5 * yh[n-1] - a9* yh[n-2]
        yj[n] = b6 * xj[n] - a6 * yj[n-1] - a9* yj[n-2]
        yk[n] = b7 * xk[n] - a7 * yk[n-1] - a9* yk[n-2]

    y= ya + ys + yd + yf + yg + yh + yj + yk
    y= np.clip(y.astype(int), -MAXVALUE, MAXVALUE)
    print(len(y))

    # Convert numeric list to binary string
    data = struct.pack('h' * BLOCKSIZE, *y);

    # Write binary string to audio output stream
    stream.write(data, BLOCKSIZE)


print('* Done.')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()




# In[ ]:



