# filter_twice
# Filter twice with same filter.

from math import cos, pi
import pyaudio
import struct

# 16 bit/sample

Fs = 8000   # Fs : Sampling frequency (samples/second)

T = 2       # T : Duration of audio to play (seconds)
N = T*Fs    # N : Number of samples to play

# Pole location
f1 = 400
om1 = 2.0*pi * float(f1)/Fs
r = 0.997      # Try other values, 0.998, 0.9995, 1.0

# Difference equation coefficients
a1 = -2*r*cos(om1)
a2 = r**2

# Initialization
y11 = 0.0
y12 = 0.0
y21 = 0.0
y22 = 0.0
gain = 20.0

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,  
                channels = 1, 
                rate = Fs,
                input = False, 
                output = True)
 
for n in range(0, N):

    # Use impulse as input signal
    if n == 0:
        x0 = 1.0
    else:
        x0 = 0.0

    # Difference equation (stage 1)
    y10 = x0 - a1 * y11 - a2 * y12

    # Delays
    y12 = y11
    y11 = y10

    # Difference equation (stage 2)
    y20 = y10 - a1 * y21 - a2 * y22

    # Delays
    y22 = y21
    y21 = y20

    # Output
    output_value = gain * y20
    output_string = struct.pack('h', int(output_value) )    # 'h' for 16 bits
    stream.write(output_string)

print("* done *")
print(N)

stream.stop_stream()
stream.close()
p.terminate()
