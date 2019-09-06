# demo_filter_blocking_corrected.py
# filter a wave file and save the output to a wave file.
# Blocking, corrected

import pyaudio, struct
import wave, math
import numpy as np
from scipy import signal

wavfile = 'author.wav'

print('Play the wave file %s.' % wavfile)

# Open wave file (should be mono channel)
wf = wave.open( wavfile, 'rb' )

# Read the wave file properties
CHANNELS        = wf.getnchannels()     # Number of channels
RATE            = wf.getframerate()     # Sampling rate (frames/second)
signal_length   = wf.getnframes()       # Signal length
WIDTH           = wf.getsampwidth()     # Number of bytes per sample

print('The file has %d channel(s).'            % CHANNELS)
print('The frame rate is %d frames/second.'    % RATE)
print('The file has %d frames.'                % signal_length)
print('There are %d bytes per sample.'         % WIDTH)


output_wavfile = wavfile[:-4] + '_output_blocking_corrected.wav'
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

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = pyaudio.paInt16,
    channels    = CHANNELS,
    rate        = RATE,
    input       = False,
    output      = True )

BLOCKLEN = 64
MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Get first set of frame from wave file
binary_data = wf.readframes(BLOCKLEN)

ORDER = 4   # filter is fourth order
states = np.zeros(ORDER)

while len(binary_data) >= BLOCKLEN:

    # convert binary data to numbers
    input_block = struct.unpack('h' * BLOCKLEN, binary_data) 

    # filter
    output_block, states = signal.lfilter(b, a, input_block, zi = states)

    # clipping
    output_block = np.clip(output_block, -MAXVALUE, MAXVALUE)     

    # convert to integer
    output_block = output_block.astype(int)     

    # Convert output value to binary data
    binary_data = struct.pack('h' * BLOCKLEN, *output_block)  

    # Write binary data to audio stream
    stream.write(binary_data)                     

    # Write binary data to output wave file
    output_wf.writeframes(binary_data)

    # Get next frame from wave file
    binary_data = wf.readframes(BLOCKLEN)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()

# Close wavefiles
wf.close()
output_wf.close()
