# AM_blocking_corrected.py.py
# Play a mono wave file with amplitude modulation. 
# This implementation reads and plays a block at a time (blocking)
# and corrects for block-to-block angle mismatch.
# Assignment: modify this file so it works for both mono and stereo wave files

# f0 = 0      # Normal audio
f0 = 400    # 'Duck' audio

BLOCKLEN = 64      # Number of frames per block

import pyaudio
import struct
import wave
import math

# Open wave file (mono)
wave_file_name = 'author.wav'
# wave_file_name = 'sin01_mono.wav'
# wave_file_name = 'sin01_stereo.wav'

wf          = wave.open( wave_file_name, 'rb')
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

# Initialize phase
om = 2*math.pi*f0/RATE
theta = 0

# Go through wave file 
for i in range(0, num_blocks):

    # Get block of samples from wave file
    binary_data = wf.readframes(BLOCKLEN)     # BLOCKLEN = number of frames to read

    # Convert binary data to tuple of numbers    
    input_tuple = struct.unpack('h' * BLOCKLEN, binary_data)
            # (h: two bytes per sample (WIDTH = 2))

    # Go through block
    for n in range(0, BLOCKLEN):
        # Amplitude modulation  (f0 Hz cosine)
        theta = theta + om
        output_block[n] = int( input_tuple[n] * math.cos(theta) )
        # output_block[n] = input_tuple[n]  # for no processing

    # keep theta betwen -pi and pi
    while theta > math.pi:
        theta = theta - 2*math.pi

    # Convert values to binary data
    binary_data = struct.pack('h' * BLOCKLEN, *output_block)

    # Write binary data to audio output stream
    stream.write(binary_data)

print('* Finished *')

stream.stop_stream()
stream.close()
p.terminate()

# Close wavefile
wf.close()

# Original file by Gerald Schuller, October 2013
