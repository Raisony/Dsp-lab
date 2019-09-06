# echo_via_circular_buffer.py
# Reads a specified wave file (mono) and plays it with an echo.
# This implementation uses a circular buffer.

import pyaudio
import wave
import struct
import random



Fs = 8000
T = 2
K = 0.99
N = 60
Q = int( Fs * T )
Gdp = 1
Gff = -K/2

# Create a buffer to store past values. Initialize to zero.
BUFFER_LEN = Q  # set the length of buffer
buffer = [ 0 for i in range(BUFFER_LEN) ]   
 

input_string = []
for i in range(N+2):
    a = random.randint(-10000, 10000)
    input_string.append(a)
for i in range(N+2, Q) :
    input_string.append(0)

# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = Fs,
                input       = False,
                output      = True )



k = 0       # buffer index (circular index)

print("* Start *")

for i in range(16000):

    input_value = input_string[i]
    # Compute output value
    output_value =  Gdp * input_value + Gff * buffer[k] + Gff * buffer[k+1]

    # Update buffer
    buffer[k] = output_value
    buffer[k+1] = output_value

    # Increment buffer index
    k = k + 1
    if k >= 60:
        # The index has reached the end of the buffer. Circle the index back to the front.
        k = 0

    # Convert output value to binary string
    output_string = struct.pack('h', int(output_value))

    # Write output value to audio stream
    stream.write(output_string)
    

print("* Finished *")

stream.stop_stream()
stream.close()
p.terminate()
