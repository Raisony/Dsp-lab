# filter_16_T
# Like filter_16 with prescribed duration

# 16 bit/sample

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
f1 = 800    # Frequency
om1 = 2.0*pi * float(f1)/Fs

Ta = 1.0    # Ta : Time for envelope to decay to 1% (in seconds)
# Try different values of Ta like 0.5, 0.2, 1.5
Ta = 1.5
# Ta = 0.5
r = 0.01**(1.0/(Ta*Fs))

print('Fs = %f' % Fs)
print('r = %f' % r)

# Difference equation coefficients
a1 = -2*r*cos(om1)
a2 = r**2

print('a1 = %f' % a1)
print('a2 = %f' % a2)

# Initialization
y1 = 0.0
y2 = 0.0
gain = 5000.0

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
    output_string = struct.pack('h', int(output_value) )    # 'h' for 16 bits
    stream.write(output_string)

print("* Finished *")

stream.stop_stream()
stream.close()
p.terminate()
