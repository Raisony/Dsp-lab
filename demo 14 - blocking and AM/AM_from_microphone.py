# AM_from_microphone.py
# Record audio and play it with amplitude modulation. 
# This implementation:
#   uses blocking, 
#   corrects for block-to-block angle mismatch,
#   assumes mono channel
"""
Read a signal from a wave file, do amplitude modulation, play to output
Original: pyrecplay_modulation.py by Gerald Schuller, Octtober 2013
Modified to read a wave file - Ivan Selesnick, September 2015
"""

import pyaudio
import struct
import math

# f0 = 0      # Normal audio
f0 = 400    # 'Duck' audio

BLOCKSIZE = 64  # Number of frames per block

WIDTH = 2       # Number of bytes per sample
CHANNELS = 1    # mono
RATE = 32000    # Sampling rate (samples/second)
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

# number_of_devices = p.get_device_count()
# print('There are {0:d} devices'.format(number_of_devices))
#
# property_list = ['defaultSampleRate', 'maxInputChannels', 'maxOutputChannels']
# for i in range(0, number_of_devices):
#     print('Device {0:d} has:'.format(i))
#     for s in property_list:
#         print(' ', s, '=', p.get_device_info_by_index(i)[s])


stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = True,
    output      = True)


output_block = [0 for i in range(0, BLOCKSIZE)]

# Initialize phase
om = 2*math.pi*f0/RATE
theta = 0

# Number of blocks to run for
num_blocks = int(RATE / BLOCKSIZE * RECORD_SECONDS)

print('* Recording for {0:.3f} seconds'.format(RECORD_SECONDS))

# Start loop
for i in range(0, num_blocks):

    # Get frames from audio input stream
    # input_string = stream.read(BLOCKSIZE)       # BLOCKSIZE = number of frames read
    input_string = stream.read(BLOCKSIZE, exception_on_overflow = False)   # BLOCKSIZE = number of frames read

    # Convert binary string to tuple of numbers
    input_tuple = struct.unpack('h' * BLOCKSIZE, input_string)
   
    # Go through block
    for n in range(0, BLOCKSIZE):
        # No processing:
        # output_block[n] = input_tuple[n]  
        # OR
        # Amplitude modulation:
        theta = theta + om
        output_block[n] = int( input_tuple[n] * math.cos(theta) )

    # keep theta betwen -pi and pi
    while theta > math.pi:
        theta = theta - 2*math.pi

    # Convert values to binary string
    output_string = struct.pack('h' * BLOCKSIZE, *output_block)

    # Write binary string to audio output stream
    stream.write(output_string)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
