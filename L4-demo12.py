# echo_via_circular_buffer.py
# Reads a specified wave file (mono) and plays it with an echo.
# This implementation uses a circular buffer.

import pyaudio
import wave
import struct
import random

def clip(x):
    #clipping at 16
    maxoutput = 2**15 - 1
    if x > maxoutput:
        x = maxoutput
    elif x < (maxoutput*-1)-1:
        x = (maxoutput*-1)-1
    return x

Ts = 10000
T = 2
K = 0.99         
N = 60
delay_samples = int( Ts * T )
Gff = -K/2

# Create a buffer to store past values. Initialize to zero.
BUFFER_LEN = delay_samples  # set the length of buffer
buffer = [ 0 for i in range(BUFFER_LEN) ]   
 

input = []
for i in range(N+2):
    a = random.randint(0, 10000)
    input.append(a)
for i in range(N+2, delay_samples) :
    input.append(0)

# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = Ts,
                input       = False,
                output      = True )



k = 0       # buffer index (circular index)

print("* Start *")

for i in range(BUFFER_LEN):

    input_value = input[i]
    # Compute output value
    output_value =  input_value + Gff * buffer[k] + Gff*buffer[k+1]

    # Update buffer
    buffer[k] = output_value
    # Increment buffer index
    k = k + 1
    if k >= 62:
        # The index has reached the end of the buffer. Circle the index back to the front.
        k = 0

    # Convert output value to binary string
    output_string = struct.pack('h', int(clip(output_value)))

    # Write output value to audio stream
    stream.write(output_string)
    

print("* Finished *")

stream.stop_stream()
stream.close()
p.terminate()
