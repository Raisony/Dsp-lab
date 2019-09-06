# plot_wave_file_and_play.py

import pyaudio
import struct
import wave
from matplotlib import pyplot

# Specify wave file
wavfile = 'author.wav'
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

pyplot.ion()           # Turn on interactive mode so plot gets updated

fig = pyplot.figure(1)

signal_block = struct.unpack('h' * BLOCKLEN, binary_data)
line, = pyplot.plot(signal_block)
line1, = pyplot.plot(signal_block)

pyplot.ylim(-32000, 32000)
pyplot.xlim(0, BLOCKLEN)

# pyplot.show()
pyplot.draw()

# exit()
# Difference equation coefficients
b0 =  0.008442692929081
b2 = -0.016885385858161
b4 =  0.008442692929081

# a0 =  1.000000000000000
a1 = -3.580673542760982
a2 =  4.942669993770672
a3 = -3.114402101627517
a4 =  0.757546944478829

# Initialization
x1 = 0.0
x2 = 0.0
x3 = 0.0
x4 = 0.0
y1 = 0.0
y2 = 0.0
y3 = 0.0
y4 = 0.0



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

    line.set_ydata(signal_block)

    pyplot.pause(0.0000000001)
    # pyplot.show()
    # pyplot.draw()

    # Write binary string to audio output stream
    stream.write(binary_data, BLOCKLEN)

    # Get block of samples from wave file
    binary_data = wf.readframes(BLOCKLEN)
    output_list = [0 for i in range(BLOCKLEN)] 
    for i in range(0,BLOCKLEN):

        # Convert string to number
        input_value = signal_block[i]                    # Number

        # Set input to difference equation
        x0 = input_value

        # Difference equation
        y0 = b0*x0 + b2*x2 + b4*x4 - a1*y1 - a2*y2 - a3*y3 - a4*y4 

        # y(n) = b0 x(n) + b2 x(n-2) + b4 x(n-4) - a1 y(n-1) 
        # - a2 y(n-2) - a3 y(n-3) - a4 y(n-4)

        # Delays
        x4 = x3
        x3 = x2
        x2 = x1
        x1 = x0
        y4 = y3
        y3 = y2
        y2 = y1
        y1 = y0

        # Compute output value
        output_value = int(y0)    # Integer in allowed range

        # Convert output value to binary string
        output_string = struct.pack('h', output_value)     

        output_list[i] = output_value
        
        output_tuple = tuple(output_list)
    line1.set_ydata(output_tuple)   
        

    


stream.stop_stream()
stream.close()
p.terminate()

wf.close()


