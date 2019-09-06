# AM_blocking.py
# Play a wave file with amplitude modulation. 
# Assumes wave file is mono.
# This implementation reads and plays a block at a time (blocking).
# Assignment: modify file so it works for both mono and stereo wave files
#  (where does this file have an error when wave file is stereo and why? )
"""
Read a signal from a wave file, do amplitude modulation, play to output
Original: pyrecplay_modulation.py by Gerald Schuller, Octtober 2013
Modified to read a wave file - Ivan Selesnick, September 2015
"""

import pyaudio
import struct
import wave
import math

# f0 = 0      # Normal audio
f0 = 400    # 'Duck' audio

BLOCKLEN = 64      # Number of frames per block

# Open wave file (mono)
input_wavefile = 'author.wav'
# input_wavefile = 'sin01_mono.wav'
# input_wavefile = 'sin01_stereo.wav'

wf          = wave.open( input_wavefile, 'rb')
RATE        = wf.getframerate()
WIDTH       = wf.getsampwidth()
LEN         = wf.getnframes() 
CHANNELS    = wf.getnchannels() 

print('The sampling rate is {0:d} samples per second'.format(RATE))
print('Each sample is {0:d} bytes'.format(WIDTH))
print('The signal is {0:d} samples long'.format(LEN))
print('The signal has {0:d} channel(s)'.format(CHANNELS))

# Open audio stream
p = pyaudio.PyAudio()
stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = False,
    output      = True)

# Create block (initialize to zero)
output_block = [0 for n in range(0, BLOCKLEN)]

# Number of blocks in wave file
num_blocks = int(math.floor(LEN/BLOCKLEN))

print('* Playing...')

# Loop through wave file 
for i in range(0, num_blocks):

    # Get block of samples from wave file
    binary_data = wf.readframes(BLOCKLEN)     # BLOCKLEN = number of frames to read

    # Convert binary data to tuple of numbers    
    input_tuple = struct.unpack('h' * BLOCKLEN, binary_data)
            # (h: two bytes per sample (WIDTH = 2))

    # Go through block
    for n in range(0, BLOCKLEN):
        # Amplitude modulation  (f0 Hz cosine)
        output_block[n] = int(input_tuple[n] * math.cos(2*math.pi*n*f0/RATE))
        # output_block[n] = input_tuple[n]  # for no processing

    # Convert values to binary data
    binary_data = struct.pack('h' * BLOCKLEN, *output_block)

    # Write binary data to audio output stream
    stream.write(binary_data)

print('* Finished *')

stream.stop_stream()
stream.close()
p.terminate()

# Close wavefiles
wf.close()
# output_wf.close()
