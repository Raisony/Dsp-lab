import pyaudio
import struct
import random
from math import sin, cos, pi
from matplotlib import pyplot as plt
from myfunctions import clip16

BLOCKSIZE   = 1024      # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Number of channels
RATE        = 8000      # Sampling rate in Hz
f0 = 400
# Parameters
T = 10       # Total play time (seconds)
# Ta = 0.2    # Decay time (seconds)
# f1 = 350    # Frequency (Hz)
N = T*RATE

NumBlocks = int( T * RATE / BLOCKSIZE )

x = [0 for i in range(BLOCKSIZE)]
y = [0 for i in range(BLOCKSIZE)]
output = [0 for i in range(BLOCKSIZE)]

plt.ion()           # Turn on interactive mode so plot can be updated
plt.figure(1)
plt.subplot(2,1,1)
line1, = plt.plot(x)
plt.ylim(-32000, 32000)
plt.xlim(0, BLOCKSIZE)
plt.xlabel('Time (n)')
plt.title('input signal')

plt.subplot(2,1,2)
line2, = plt.plot(y)
plt.ylim(-32000, 32000)
plt.xlim(0, BLOCKSIZE)
plt.xlabel('Time (n)')
plt.title('output signal')

plt.show()

# Open the audio output stream
p = pyaudio.PyAudio()

stream = p.open(format      = p.get_format_from_width(WIDTH),
                channels    = CHANNELS,
                rate        = RATE,
                input       = True,
                output      = True)

print('Playing for {0:f} seconds ...'.format(T))

# Loop through blocks
for i in range(0, NumBlocks):

    input_string = stream.read(BLOCKSIZE,exception_on_overflow = False)
    input_block = struct.unpack('h'*BLOCKSIZE,input_string)
    for n in range(0, BLOCKSIZE):
        output[n] = input_block[n]*cos(2*pi*f0*(i*BLOCKSIZE+n)/RATE)
        # output[n] = input_block[n]*cos(2*pi*f0*(n)/RATE)
        
        output[n] = int(clip16(output[n]))
    line2.set_ydata(output)
    line1.set_ydata(input_block)
    plt.setp(line1, color = 'red')
    plt.setp(line2, color = 'blue')
    plt.title('Block {0:d}'.format(i))
    plt.pause(0.001)
    plt.draw()

    # Convert numeric list to binary string
    output_string = struct.pack('h' * BLOCKSIZE, *output);

    # Write binary string to audio output stream
    stream.write(output_string)

print('* Finished *')

stream.stop_stream()
stream.close()
p.terminate()
