# mic_filter.py
# Record from micrphone, filter signal, play output to speaker

import pyaudio
import struct
import math
import wave

from math import pi
from myfunctions import clip16

WIDTH       = 2         # Number of bytes per sample
CHANNELS    = 1         # mono
RATE        = 16000     # Sampling rate (frames/second)
DURATION    = 10         # duration of processing (seconds)

N = DURATION * RATE     # N : Number of samples to process


# Set parameters of delay system
Gdp = 1.0           # direct-path gain
Gff = 0.8           # feed-forward gain
delay_sec = 0.5    # 50 milliseconds
# delay_sec = 0.02
delay_samples = int( RATE * delay_sec )

# Create a buffer to store past values. Initialize to zero.
BUFFER_LEN = delay_samples   # set the length of buffer
buffer = [ 0 for i in range(BUFFER_LEN) ]    

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = True,
    output      = True)

k = 0  
print('* Start')

w = wave.open("testwave43.wav","wb")
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(RATE) 

for n in range(0, N):

    # Get one frame from audio input (microphone)
    # input_string = stream.read(1)
    # If you get run-time time input overflow errors, try:
    input_string = stream.read(1, exception_on_overflow = False)

    # Convert binary string to tuple of numbers
    input_tuple = struct.unpack('h', input_string)

    # Convert one-element tuple to number
    input_value = input_tuple[0]


    # Compute output value
    output_value = int(clip16(Gdp * input_value + Gff * buffer[k]))    # Number


        # Update buffer
    buffer[k] = input_value

    # Increment buffer index
    k = k + 1
    if k >= BUFFER_LEN:
        # The index has reached the end of the buffer. Circle the index back to the front.
        k = 0

        
    # Convert output value to binary string
    output_string = struct.pack('h', int(clip16(output_value)))  

    # Write binary string to audio stream
    stream.write(output_string)    

    w.writeframes(output_string)

print('* Finished')

stream.stop_stream()
stream.close()
w.close()
p.terminate()
