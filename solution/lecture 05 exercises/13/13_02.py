# filter_wav_file.py
# filter a wave file and save the output to a wave file.
# Blocking

import pyaudio, struct
import wave, math
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

CHANNELS = 1
RATE = 16000
WIDTH = 2

T = 10 # 5 second
N = T * RATE
BLOCKLEN = 1024
# BLOCKLEN = 64
NumBlocks = int( N / BLOCKLEN)
MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)
# wavfile = 'author.wav'

# print('Play the wave file %s.' % wavfile)

# # Open wave file (should be mono channel)
# wf = wave.open( wavfile, 'rb' )

# # Read the wave file properties
# CHANNELS        = wf.getnchannels()     # Number of channels
# RATE            = wf.getframerate()     # Sampling rate (frames/second)
# signal_length   = wf.getnframes()       # Signal length
# WIDTH           = wf.getsampwidth()     # Number of bytes per sample

# print('The file has %d channel(s).'            % CHANNELS)
# print('The frame rate is %d frames/second.'    % RATE)
# print('The file has %d frames.'                % signal_length)
# print('There are %d bytes per sample.'         % WIDTH)


# output_wavfile = wavfile[:-4] + '_output_blocking_fixed.wav'
output_wavfile = 'microphone_output_blocking_fixed.wav'
output_wf = wave.open(output_wavfile, 'w')      # wave file
output_wf.setframerate(RATE)
output_wf.setsampwidth(WIDTH)
output_wf.setnchannels(CHANNELS)


# Difference equation coefficients
b0 =  0.008442692929081
b2 = -0.016885385858161
b4 =  0.008442692929081
b = [b0, 0.0, b2, 0.0, b4]

# a0 =  1.000000000000000
a1 = -3.580673542760982
a2 =  4.942669993770672
a3 = -3.114402101627517
a4 =  0.757546944478829
a = [1.0, a1, a2, a3, a4]

# initialization plot
x = [0 for i in range(BLOCKLEN)]
y = [0 for i in range(BLOCKLEN)]

plt.ion()
fig = plt.figure(1)
plt.subplot(2,1,1)
line1, = plt.plot(x)
plt.ylim(-MAXVALUE, MAXVALUE)
plt.xlim(0, BLOCKLEN)
plt.xlabel('Time (n)')
plt.title('input signal')

plt.subplot(2,1,2)
line2, = plt.plot(y)
plt.ylim(-MAXVALUE,MAXVALUE)
plt.xlim(0,BLOCKLEN)
plt.xlabel('Time (n)')
plt.title('output signal')

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = pyaudio.paInt16,
    channels    = CHANNELS,
    rate        = RATE,
    input       = True,
    output      = True )

ORDER = 4   # filter is fourth order
states = np.zeros(ORDER)
print('* start *')
for n in range(0, NumBlocks):
    
    # convert binary data to numbers
    input_string = stream.read(BLOCKLEN,exception_on_overflow = False)
    input_block = struct.unpack('h' * BLOCKLEN, input_string) 
    # filter
    output_block, states = signal.lfilter(b, a, input_block, zi = states)

    # clipping
    output_block = np.clip(output_block, -MAXVALUE, MAXVALUE)     

    # convert to integer
    output_block = output_block.astype(int)     

    # Convert output value to binary data
    output_string = struct.pack('h' * BLOCKLEN, *output_block)  

    # Write binary data to audio stream
    stream.write(output_string)                     

    # Write binary data to output wave file
    output_wf.writeframes(output_string)
    # plot
    line2.set_ydata(output_block)
    line1.set_ydata(input_block)
    plt.setp(line1, color = 'red')
    plt.setp(line2, color = 'blue')
    plt.title('Block {0:d}'.format(n))
    plt.pause(0.001)
    plt.draw()

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()

# Close wavefiles
# wf.close()
output_wf.close()
