# f0 = 0      # Normal audio
# f0 = 400    # 'Duck' audio
f0 = 200
BLOCKSIZE = 1024      # Number of frames per block

import pyaudio
import struct
import wave
import math
from matplotlib import pyplot as plt
import numpy as np

CHANNELS = 1
WIDTH = 2
RATE = 8000

T = 10 # duration 10 seconds
N = T * RATE
# # Open wave file (mono)
# wave_file_name = 'author.wav'
# # wave_file_name = 'sin01_mono.wav'
# # wave_file_name = 'sin01_stereo.wav'

# wf          = wave.open( wave_file_name, 'rb')
# RATE        = wf.getframerate()
# WIDTH       = wf.getsampwidth()
# LEN         = wf.getnframes() 
# CHANNELS    = wf.getnchannels() 

# print('The sampling rate is {0:d} samples per second'.format(RATE))
# print('Each sample is {0:d} bytes'.format(WIDTH))
# print('The signal is {0:d} samples long'.format(LEN))
# print('The signal has {0:d} channel(s)'.format(CHANNELS))
f = [n*float(RATE)/BLOCKSIZE for n in range(BLOCKSIZE)]

plt.ion()
# DBscale = True
plt.figure(1)

plt.subplot(3,1,1)
plt.xlim(0, 0.5*RATE)
plt.ylim(0, 150)
plt.xlabel('frequency (Hz)')
line1, =plt.plot([],[],color = 'red')
line1.set_xdata(f)

plt.subplot(3,1,3)
plt.xlim(0, 0.5*RATE)
plt.ylim(0, 150)
plt.xlabel('frequency (Hz)')
line2, =plt.plot([],[],color = 'blue')
line2.set_xdata(f)

# Open audio stream
p = pyaudio.PyAudio()
stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = True,
    output      = True)


# Create block (initialize to zero)
output_block = [0 for n in range(0, BLOCKSIZE)]

# Number of blocks in wave file
num_blocks = int(math.floor(N/BLOCKSIZE))

print('* Playing...')

# Initialize phase
om = 2*math.pi*f0/RATE
theta = 0

# Go through wave file 
for i in range(0, num_blocks):

    # Get block of samples from wave file
    input_string = stream.read(BLOCKSIZE,exception_on_overflow = False)     # BLOCKSIZE = number of frames read

    # Convert binary string to tuple of numbers    
    input_tuple = struct.unpack('h' * BLOCKSIZE, input_string)
            # (h: two bytes per sample (WIDTH = 2))
    inputf = np.fft.fft(input_tuple)
    # Go through block
    for n in range(0, BLOCKSIZE):
        # Amplitude modulation  (f0 Hz cosine)
        theta = theta + om
        output_block[n] = int( input_tuple[n] * math.cos(theta) )
        # output_block[n] = ( input_tuple[n] * math.cos(theta) )
        # output_block[n] = input_tuple[n]  # for no processing
    
    # keep theta betwen -pi and pi
    while theta > math.pi:
        theta = theta - 2*math.pi
    
    outputf = np.fft.fft(output_block)

    line1.set_ydata(20*np.log10(abs(inputf)))
    line2.set_ydata(20*np.log10(abs(outputf)))
    # line1.set_ydata(abs(inputf))
    # line2.set_ydata(abs(outputf))
    # plt.title('Block {0:d}'.format(i))
    plt.pause(0.001)
    plt.draw()
    # Convert values to binary string
    output_string = struct.pack('h' * BLOCKSIZE, *output_block)

    # Write binary string to audio output stream
    stream.write(output_string)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()

# # Close wavefile
# wf.close()

# Original file by Gerald Schuller, October 2013
