# filter_16_r
# Like filter_16 with adjustable pole radius

from math import cos, pi 
import pyaudio
import struct

# Fs : Sampling frequency (samples/second)
Fs = 8000
# Fs = 16000   
# Fs = 32000

T = 2       # T : Duration of audio to play (seconds)
N = T*Fs    # N : Number of samples to play

# Pole location
f1 = 400.0
om1 = 2.0*pi * f1/Fs
r = 0.999      # Try other values, 0.998, 0.9995, 1.0
# r = 0.998
# Qustion: how to set r to obtain desired time constant?

# Difference equation coefficients
a1 = -2*r*cos(om1)
a2 = r**2

print('a1 = %f' % a1)
print('a2 = %f' % a2)

# Initialization
y1 = 0.0
y2 = 0.0
gain = 10000.0

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

    # Difference equation
    y0 = x0 - a1 * y1 - a2 * y2

    # Delays
    y2 = y1
    y1 = y0

    # Output
    output_value = gain * y0
    output_string = struct.pack('h', int(output_value))     # 'h' for 16 bits
    stream.write(output_string)

print("* Finished *")

stream.stop_stream()
stream.close()
p.terminate()
