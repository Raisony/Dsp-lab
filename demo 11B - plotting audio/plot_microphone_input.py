# plot_microphone_input.py

import pyaudio
import struct
from matplotlib import pyplot

WIDTH = 2           # bytes per sample
CHANNELS = 1        # mono
RATE = 8000
BLOCKLEN = 1024
DURATION = 10        # Duration in seconds

K = int( DURATION * RATE / BLOCKLEN )   # Number of blocks

print('Block length: ', BLOCKLEN)
print('Number of blocks to read: ', K)

# exit()

# Set up plotting...

pyplot.ion()           # Turn on interactive mode so plot gets updated

pyplot.figure(1)
pyplot.ylim(-10000, 10000)        # set y-axis limits
pyplot.xlim(0, BLOCKLEN)         # set x-axis limits
pyplot.xlabel('Time (n)')
t = range(0, BLOCKLEN)

# # Time axis in units of milliseconds:
# pyplot.xlim(0, 1000.0 * BLOCKLEN/RATE)         # set x-axis limits
# pyplot.xlabel('Time (msec)')
# t = [n*1000/float(RATE) for n in range(BLOCKLEN)]

line, = pyplot.plot([], [], color = 'blue')  # Create empty line
line.set_xdata(t)                       # x-data of plot (time)
signal_block = [0 for n in range(BLOCKLEN)]
line.set_ydata(signal_block)            # y-data of plot (signal values)
pyplot.show()

# exit()     # If you exit here, then comment out pyplot.ion to see plot


# Open the audio stream

p = pyaudio.PyAudio()

PA_FORMAT = p.get_format_from_width(WIDTH)

stream = p.open(
    format = PA_FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = False)

# Read microphone, plot audio signal

for i in range(K):

    # Read audio input stream
    # input_string = stream.read(BLOCKLEN)                     
    binary_data = stream.read(BLOCKLEN, exception_on_overflow = False)                     

    signal_block = struct.unpack('h' * BLOCKLEN, binary_data)  # Convert
    line.set_ydata(signal_block)                               # Update y-data of plot
    pyplot.pause(0.0001)
    pyplot.draw()

# Close up

pyplot.close()
stream.stop_stream()
stream.close()
p.terminate()

print('* Finished')

