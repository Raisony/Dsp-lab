# plot_wave_file_and_play.py

import pyaudio
import struct
import wave
from matplotlib import pyplot

# Specify wave file
wavfile = 'DSP Lab\\demo 11B - plotting audio\\author.wav'
# wavfile = 'decay_cosine_mono.wav'
# wavfile = 'sin01_mono.wav'
print('Play the wave file: {0:s}.'.format(wavfile))

# Open wave file
wf = wave.open( wavfile, 'rb')

# Read wave file properties
RATE        = wf.getframerate()     # Frame rate (frames/second)
WIDTH       = wf.getsampwidth()     # Number of bytes per sample
LEN         = wf.getnframes()       # Signal length
CHANNELS    = wf.getnchannels()     # Number of channels

print('The file has %d channel(s).'         % CHANNELS)
print('The file has %d frames/second.'      % RATE)
print('The file has %d frames.'             % LEN)
print('The file has %d bytes per sample.'   % WIDTH)

# exit()

BLOCKLEN = 1000    # Blocksize
# BLOCKLEN = 500    # Blocksize

# Get block of samples from wave file
binary_data = wf.readframes(BLOCKLEN)

# Set up plotting...

# pyplot.ion()           # Turn on interactive mode so plot gets updated

# fig = pyplot.figure(1)

# signal_block = struct.unpack('h' * BLOCKLEN, binary_data)
# line0, = pyplot.plot(signal_block)

# pyplot.ylim(-32000, 32000)
# pyplot.xlim(0, BLOCKLEN)

# # pyplot.show()
# pyplot.draw()

# # exit()

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

line0, = pyplot.plot([], [], color = 'blue')  # Create empty line
line0.set_xdata(t)                   # x-data of plot (time)
signal_block = [0 for n in range(BLOCKLEN)]
line0.set_ydata(signal_block)   # y-data of plot (signal values)

# pyplot.figure(2)
# pyplot.ylim(-10000, 10000)        # set y-axis limits
# pyplot.xlim(0, BLOCKLEN)         # set x-axis limits
# pyplot.xlabel('Time (n)')
# t = range(0, BLOCKLEN)
line1, = pyplot.plot([], [], color = 'red')
line1.set_xdata(t)                   # x-data of plot (time)
signal_block = [0 for n in range(BLOCKLEN)]
line1.set_ydata(signal_block)   # y-data of plot (signal values)
pyplot.show()

# Open the audio output stream
p = pyaudio.PyAudio()

PA_FORMAT = p.get_format_from_width(WIDTH)

# Explore: effect of Frames_Per_Buffer:

# Frames_Per_Buffer = 16
# Frames_Per_Buffer = 32
# Frames_Per_Buffer = 64
# Frames_Per_Buffer = 128
Frames_Per_Buffer = 256
# Frames_Per_Buffer = 512
# Frames_Per_Buffer = 1024
# Frames_Per_Buffer = 2048

# Explore: effect of modifying RATE
# RATE = int(RATE/2)   

stream = p.open(
    format = PA_FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = False,
    output = True,
    frames_per_buffer = Frames_Per_Buffer)

while len(binary_data) >= BLOCKLEN * WIDTH:

    # Convert binary data to number sequence (tuple)
    signal_block = struct.unpack('h' * BLOCKLEN, binary_data)
    # print(signal_block)
    line0.set_ydata(signal_block)
    for n in range(0, BLOCKLEN):
        line1.set_ydata(signal_block[n])
    pyplot.pause(0.0000000001)
    # pyplot.show()
    # pyplot.draw()
    # Write binary string to audio output stream
    stream.write(binary_data, BLOCKLEN)
    # Get block of samples from wave file
    binary_data = wf.readframes(BLOCKLEN)


stream.stop_stream()
stream.close()
p.terminate()

wf.close()


