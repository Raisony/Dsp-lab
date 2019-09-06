# plot_microphone_input_spectrum.py

"""
Using Pyaudio, get audio input and plot real-time FFT of blocks.
Ivan Selesnick, October 2015
Based on program by Gerald Schuller
"""

import pyaudio
import struct
import math
from matplotlib import pyplot as plt
import numpy as np

plt.ion()           # Turn on interactive mode so plot gets updated
f0 = 2000
WIDTH     = 2         # bytes per sample
CHANNELS  = 1         # mono
RATE      = 8000     # Sampling rate (samples/second)
BLOCKSIZE = 1024      # length of block (samples)
DURATION  = 10        # Duration (seconds)
om = 2*math.pi*f0/RATE
theta = 0

NumBlocks = int( DURATION * RATE / BLOCKSIZE )

print('BLOCKSIZE =', BLOCKSIZE)
print('NumBlocks =', NumBlocks)
print('Running for ', DURATION, 'seconds...')

# DBscale = False
DBscale = True

# Initialize plot window:
plt.figure(1)
if DBscale:
    plt.ylim(0, 150)
else:
    plt.ylim(0, 20*RATE)

# Frequency axis (Hz)
plt.xlim(0, 0.5*RATE)         # set x-axis limits
# plt.xlim(0, 2000)         # set x-axis limits
plt.xlabel('Frequency (Hz)')
f = RATE/BLOCKSIZE * np.arange(0, BLOCKSIZE)

line, = plt.plot([], [], color = 'blue')  # Create empty line
line.set_xdata(f)                         # x-data of plot (frequency)
line0, = plt.plot([], [], color = 'red')  # Create empty line
line0.set_xdata(f)                         # x-data of plot (frequency)
# Open audio device:
p = pyaudio.PyAudio()
PA_FORMAT = p.get_format_from_width(WIDTH)

stream = p.open(
    format    = PA_FORMAT,
    channels  = CHANNELS,
    rate      = RATE,
    input     = True,
    output    = True)

output_block = [0 for i in range(0, BLOCKSIZE)]


for i in range(0, NumBlocks):
    input_string = stream.read(BLOCKSIZE, exception_on_overflow = False)                     # Read audio input stream
    input_tuple = struct.unpack('h' * BLOCKSIZE, input_string)  # Convert
    X = np.fft.fft(input_tuple)
    #
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
    output_tuple = struct.unpack('h' * BLOCKSIZE, output_string)  # Convert
    Y = np.fft.fft(output_tuple)
    # Write binary string to audio output stream
    stream.write(output_string)
    #
    # Update y-data of plot
    if DBscale:
        line.set_ydata(20*np.log10(abs(X)))
    else:
        line.set_ydata(abs(X))
    if DBscale:
        line0.set_ydata(20 * np.log10(abs(Y)))
    else:
        line0.set_ydata(abs(Y))
    plt.pause(0.01)
    plt.draw()

plt.close()

stream.stop_stream()
stream.close()
p.terminate()

print('* Finished')
