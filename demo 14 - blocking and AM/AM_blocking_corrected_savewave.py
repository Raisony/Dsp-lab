# AM_blocking_corrected_savewave.py
# Like AM_blocking_corrected.py
# but additionally saves output signal to a wave file


# f0 = 0      # Normal audio
f0 = 400    # 'Duck' audio

BLOCKLEN = 64      # Number of frames per block

import pyaudio
import struct
import wave
import math

# Open wave file (mono)
input_wavefile = 'author.wav'
# input_wavefile = 'sin01_mono.wav'
# input_wavefile = 'sin01_stereo.wav'

input_wf    = wave.open( input_wavefile, 'rb')
RATE        = input_wf.getframerate()
WIDTH       = input_wf.getsampwidth()
LEN         = input_wf.getnframes() 
CHANNELS    = input_wf.getnchannels() 

print('The sampling rate is {0:d} samples per second'.format(RATE))
print('Each sample is {0:d} bytes'.format(WIDTH))
print('The signal is {0:d} samples long'.format(LEN))
print('The signal has {0:d} channel(s)'.format(CHANNELS))

output_wavefile = input_wavefile[:-4] + '_AM_corrected.wav'
output_wf = wave.open(output_wavefile, 'w')      # wave file
output_wf.setframerate(RATE)
output_wf.setsampwidth(WIDTH)
output_wf.setnchannels(CHANNELS)

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

# Initialize phase
om = 2*math.pi*f0/RATE
theta = 0

print('* Playing...')

# Go through wave file 
for i in range(0, num_blocks):

    # Get block of samples from wave file
    binary_data = input_wf.readframes(BLOCKLEN)     # BLOCKLEN = number of frames read

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

    # Write to output wave file also
    output_wf.writeframes(binary_data)

print('* Finished *')

# Close PyAudio stream
stream.stop_stream()
stream.close()
p.terminate()

# Close wavefiles
input_wf.close()
output_wf.close()
