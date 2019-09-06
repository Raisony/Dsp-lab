# filter_16.py
# 
# Implement the second-order recursive difference equation
# y(n) = x(n) - a1 y(n-1) - a2 y(n-2)
# 
# 16 bit/sample

from math import cos, pi 
import pyaudio
import struct


# Fs : Sampling frequency (samples/second)
Fs = 8000
# Also try other values of 'Fs'. What happens? Why?
# Fs = 16000
# Fs = 32000
# Fs = 5000

T = 1       # T : Duration of audio to play (seconds)
N = T*Fs    # N : Number of samples to play

# Difference equation coefficients
a1 = -1.9
a2 = 0.998
a11 = 1.99
a21 = 0.9977


# Initialization
y1 = 0.0
y2 = 0.0
y11 = 0.0 
y21 = 0.0
gain = 1000
# Also try other values of 'gain'. What is the effect?
# gain = 1000.0

# Create an audio object and open an audio stream for output
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,  
                channels = 2, 
                rate = Fs,
                input = False, 
                output = True)

# paInt16 is 16 bits/sample

# Run difference equation
for n in range(0, N):

    # Use impulse as input signal
    if n == 0:
        x0 = 1.0
    else:
        x0 = 0.0

    # Difference equation
    y0 = x0 - a1 * y1 - a2 * y2
    y01 = x0 -a11 * y11 - a21 * y21


    # Delays
    y2 = y1
    y1 = y0
    y21 = y11
    y11 = y01

    # Output
    output_value = gain * y0
    output_value2 = gain * y01
    output_string = struct.pack('hh', int(output_value), int(output_value2))
    stream.write(output_string)

print("* Finished *")


stream.stop_stream()
stream.close()
p.terminate()
