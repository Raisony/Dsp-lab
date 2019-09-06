# echo_via_circular_buffer.py
# Reads a specified wave file (mono) and plays it with an echo.
# This implementation uses a circular buffer.

import pyaudio
import wave
import struct
from myfunctions import clip16
from math import random

wavfile = 'author.wav'
print('Play the wave file %s.' % wavfile)

# Open the wave file
wf = wave.open( wavfile, 'rb')

# Read wave file properties
RATE        = wf.getframerate()     # Frame rate (frames/second)
WIDTH       = wf.getsampwidth()     # Number of bytes per sample
SIGNAL_LEN  = wf.getnframes()       # Signal length
CHANNELS    = wf.getnchannels()     # Number of channels
K = -0.99
print('The file has %d channel(s).'            % CHANNELS)
print('The frame rate is %d frames/second.'    % RATE)
print('The file has %d frames.'                % SIGNAL_LEN)
print('There are %d bytes per sample.'         % WIDTH)

# Set parameters of delay system
Gdp = 1.0           # direct-path gain
Gff = K / 2        # feed-forward gain
delay_sec = 0.05    # 50 milliseconds
# delay_sec = 0.02
delay_samples = int( RATE * delay_sec )

print('The delay of {0:.3f} seconds is {1:d} samples.'.format(delay_sec, delay_samples))

# Create a buffer to store past values. Initialize to zero.
BUFFER_LEN = delay_samples   # set the length of buffer
buffer = [ 0 for i in range(BUFFER_LEN) ]    

# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(
    format      = pyaudio.paInt16,
    channels    = 1,
    rate        = RATE,
    input       = False,
    output      = True )

# Get first frame (sample)
input_string = wf.readframes(1)

k = 0       # buffer index (circular index)

print("* Start *")

while len(input_string) > 0:

    # Convert string to number
    input_value = struct.unpack('h', input_string)[0]

    # Compute output value
    output_value = Gdp * input_value + Gff * buffer[k] + Gff * buffer[k + 1]

    # Update buffer
    buffer[k] = input_value
    buffer[k + 1] = input_value

    # Increment buffer index
    k = k + 1
    if k >= BUFFER_LEN:
        # The index has reached the end of the buffer. Circle the index back to the front.
        k = 0

    # Convert output value to binary string
    output_string = struct.pack('h', int(clip16(output_value)))

    # Write output value to audio stream
    stream.write(output_string)

    # Get next frame (sample)
    input_string = wf.readframes(1)     

print("* Finished *")

stream.stop_stream()
stream.close()
p.terminate()
