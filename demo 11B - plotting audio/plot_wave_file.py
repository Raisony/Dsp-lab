# plot_wave_file.py

import struct
import wave
from matplotlib import pyplot

# Specify wave file
wavfile = 'author.wav'
# wavfile = 'decay_cosine_mono.wav'
# wavfile = 'decay_cosine_mono_vibrato.wav'
# wavfile = 'sin01_mono.wav'
# wavfile = 'sin01_mono_vibrato.wav'
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

# Get block of samples from wave file
binary_data = wf.readframes(BLOCKLEN)

# Set up plotting...

# pyplot.ion()           # Turn on interactive mode so plot gets updated

fig = pyplot.figure(1)

signal_block = struct.unpack('h' * BLOCKLEN, binary_data)
line, = pyplot.plot(signal_block)

pyplot.ylim(-32000, 32000)
pyplot.xlim(0, BLOCKLEN)

# pyplot.show()       # comment out pyplot.ion to keep plot window open
# pyplot.draw()

# exit()

while len(binary_data) >= BLOCKLEN * WIDTH:

    # Convert binary data to number sequence (tuple)
    signal_block = struct.unpack('h' * BLOCKLEN, binary_data)

    # print(signal_block)

    line.set_ydata(signal_block)
    pyplot.pause(0.1)
    # pyplot.show()
    # pyplot.draw()

    # Get block of samples from wave file
    binary_data = wf.readframes(BLOCKLEN)

wf.close()
