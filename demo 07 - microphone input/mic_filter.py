# mic_filter.py
# Record from micrphone, filter signal, play output to speaker

import pyaudio
import struct
import math
import wave

from myfunctions import clip16

WIDTH       = 2         # Number of bytes per sample
CHANNELS    = 1         # mono
RATE        = 16000     # Sampling rate (frames/second)
DURATION    = 10         # duration of processing (seconds)

N = DURATION * RATE     # N : Number of samples to process


# Difference equation coefficients
b0 =  0.008442692929081
b2 = -0.016885385858161
b4 =  0.008442692929081

# a0 =  1.000000000000000
a1 = -3.580673542760982
a2 =  4.942669993770672
a3 = -3.114402101627517
a4 =  0.757546944478829

# Initialization
x1 = 0.0
x2 = 0.0
x3 = 0.0
x4 = 0.0
y1 = 0.0
y2 = 0.0
y3 = 0.0
y4 = 0.0

ww = wave.open('testwave43.wav', 'wb')

ww.setnchannels(1)
ww.setsampwidth(2)
ww.setframerate(RATE)


p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = True,
    output      = True)

print('* Start')


for n in range(0, N):

    # Get one frame from audio input (microphone)
    # input_string = stream.read(1)
    # If you get run-time time input overflow errors, try:
    input_string = stream.read(1, exception_on_overflow = False)

    # Convert binary string to tuple of numbers
    input_tuple = struct.unpack('h', input_string)

    # Convert one-element tuple to number
    input_value = input_tuple[0]

    # Set input to difference equation
    x0 = input_value*math.cos(2*math.pi*400*n)

    # Difference equation
    y0 = b0*x0 + b2*x2 + b4*x4 - a1*y1 - a2*y2 - a3*y3 - a4*y4 

    # Delays
    x4 = x3
    x3 = x2
    x2 = x1
    x1 = x0
    y4 = y3
    y3 = y2
    y2 = y1
    y1 = y0

    # Compute output value
    output_value = int(clip16(y0))    # Number

    # output_value = int(clip16(x0)   # Bypass filter (listen to input directly)

    # Convert output value to binary string
    output_string = struct.pack('h', output_value)
    ww.writeframes(output_string)



    # Write binary string to audio stream
    stream.write(output_string)                     

print('* Finished')

stream.stop_stream()
ww.close()
stream.close()
p.terminate()
