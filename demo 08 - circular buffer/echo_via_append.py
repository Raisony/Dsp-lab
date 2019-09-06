# echo_via_append.py
# Reads a specified wave file (mono) and plays it with an echo.
# This implementation does not use a circular bufffer, 
# it uses 'append' and 'remove'

import pyaudio
import wave
import struct
from myfunctions import clip16

wavfile = 'author.wav'
print('Play the wave file %s.' % wavfile)

# Open the wave file
wf = wave.open( wavfile, 'rb')

# Read the wave file properties
num_channels    = wf.getnchannels()     # Number of channels
RATE            = wf.getframerate()     # Sampling rate (frames/second)
signal_length   = wf.getnframes()       # Signal length
width           = wf.getsampwidth()     # Number of bytes per sample

print('The file has %d channel(s).'            % num_channels)
print('The frame rate is %d frames/second.'    % RATE)
print('The file has %d frames.'                % signal_length)
print('There are %d bytes per sample.'         % width)

# Set parameters of delay system
gain = 1.0
gain_delay = 0.8
delay_sec = 0.05 # 50 milliseconds
delay_samples = int( RATE * delay_sec )

print('The delay of {0:.3f} seconds is {1:d} samples.'.format(delay_sec, delay_samples))

# Create a buffer to store past values. Initialize to zero.
buffer = [ 0 for i in range(delay_samples) ]    

# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = RATE,
                input       = False,
                output      = True )

# Get first frame (sample)
input_string = wf.readframes(1)

print('* Start')

while len(input_string) > 0:

    # Convert string to number
    input_value = struct.unpack('h', input_string)
    input_value = input_value[0]

    # Compute output value
    output_value = gain * input_value + gain_delay * buffer[0]

    # y(n) = gain x(n) + gain_delay x(n-N)

    # Update buffer
    buffer.append(input_value)
    buffer[0:1] = []

    # Convert output value to binary string
    output_string = struct.pack('h', int(clip16(output_value)))
    # output_string = struct.pack('h', int(clip16(input_value)))

    # Write output value to audio stream
    stream.write(output_string)

    # Get next frame (sample)
    input_string = wf.readframes(1)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
