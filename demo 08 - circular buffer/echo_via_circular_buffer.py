# echo_via_circular_buffer.py
# Reads a specified wave file (mono) and plays it with an echo.
# This implementation uses a circular buffer.

import pyaudio
import wave
import struct
from myfunctions import clip16

WIDTH       = 2         # Number of bytes per sample
CHANNELS    = 1         # mono
RATE        = 16000     # Sampling rate (frames/second)
DURATION    = 10         # duration of processing (seconds)

N = DURATION * RATE     # N : Number of samples to process
K = 0.99
# Open the wave file





# print('The file has %d channel(s).'            % CHANNELS)
# print('The frame rate is %d frames/second.'    % RATE)
# print('The file has %d frames.'                % SIGNAL_LEN)
# print('There are %d bytes per sample.'         % WIDTH)

ww = wave.open('test.wav', 'wb')
ww.setnchannels(1)
ww.setsampwidth(2)
ww.setframerate(RATE)


# Set parameters of delay system
Gdp = 1.0           # direct-path gain
Gff = -0.495           # feed-forward gain
delay_sec = 0.05    # 50 milliseconds
# delay_sec = 0.02
delay_samples = int( RATE * delay_sec )      #800

print('The delay of {0:.3f} seconds is {1:d} samples.'.format(delay_sec, delay_samples))

# Create a buffer to store past values. Initialize to zero.
BUFFER_LEN = delay_samples   # set the length of buffer
buffer = [ 0 for i in range(BUFFER_LEN) ]
input_string = 800

# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = RATE,
                input       = False,
                output      = True )


# Get first frame (sample)
# input_string = ww.readframes(1)

k = 0       # buffer index (circular index)
print(BUFFER_LEN)
print(int(RATE * delay_sec))
print("* Start *")


while len(input_string) > 0:    #2

    # Convert string to number
    input_value = struct.unpack('h', int(input_string))

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

    ww.writeframes(output_string)

    # Write output value to audio stream
    stream.write(output_string)

    # Get next frame (sample)

print("* Finished *")

stream.stop_stream()
ww.close()
stream.close()
p.terminate()
