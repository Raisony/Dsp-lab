# play_vibrato_ver2.py
# Reads a specified wave file (mono) and plays it with a vibrato effect.
# (Sinusoidal time-varying delay)
# This implementation uses a circular buffer with two buffer indices.
# Uses linear interpolation

import pyaudio
import wave
import struct
import math
from myfunctions import clip16

f0 = 400    # 'Duck' audio

BLOCKSIZE = 64  # Number of frames per block

WIDTH = 2       # Number of bytes per sample
CHANNELS = 1    # mono
RATE = 32000    # Sampling rate (samples/second)
RECORD_SECONDS = 5

# Open wave file

# Vibrato parameters
f0 = 2
W = 0.2
# W = 0 # for no effct

# f0 = 10
# W = 0.2

# OR
# f0 = 20
# ratio = 1.06
# W = (ratio - 1.0) / (2 * math.pi * f0 )
# print W

# Create a buffer (delay line) for past values
buffer_MAX =  1024                          # Buffer length
buffer = [0.0 for i in range(buffer_MAX)]   # Initialize to zero

# Buffer (delay line) indices
kr = 0  # read index
kw = int(0.5 * buffer_MAX)  # write index (initialize to middle of buffer)
kw = buffer_MAX/2

# print('The delay of {0:.3f} seconds is {1:d} samples.'.format(delay_sec, delay_samples))
print('The buffer is {0:d} samples long.'.format(buffer_MAX))
#
#
#
p = pyaudio.PyAudio()

number_of_devices = p.get_device_count()
print('There are {0:d} devices'.format(number_of_devices))

property_list = ['defaultSampleRate', 'maxInputChannels', 'maxOutputChannels']
for i in range(0, number_of_devices):
    print('Device {0:d} has:'.format(i))
    for s in property_list:
        print(' ', s, '=', p.get_device_info_by_index(i)[s])


stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = True,
    output      = True)


output_block = [0 for i in range(0, BLOCKSIZE)]

# Initialize phase
om = 2*math.pi*f0/RATE
theta = 0

# Number of blocks to run for
num_blocks = int(RATE / BLOCKSIZE * RECORD_SECONDS)

print('* Recording for {0:.3f} seconds'.format(RECORD_SECONDS))

for i in range(0, num_blocks):

    # Get frames from audio input stream
    # input_string = stream.read(BLOCKSIZE)       # BLOCKSIZE = number of frames read
    input_string = stream.read(BLOCKSIZE, exception_on_overflow=False)  # BLOCKSIZE = number of frames read

    # Convert binary string to tuple of numbers
    input_tuple = struct.unpack('h' * BLOCKSIZE, input_string)

    # Go through block
    for n in range(0, BLOCKSIZE):
        # No processing:
        # output_block[n] = input_tuple[n]
        # OR
        # Amplitude modulation:
        theta = theta + om
        output_block[n] = int(input_tuple[n] * math.cos(theta))

    # keep theta betwen -pi and pi
    while theta > math.pi:
        theta = theta - 2 * math.pi

    # Convert values to binary string
    output_string = struct.pack('h' * BLOCKSIZE, *output_block)

    # Write binary string to audio output stream
    stream.write(output_string)


print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()

#
#
#
# Open an output audio stream
# p = pyaudio.PyAudio()
# stream = p.open(format      = pyaudio.paInt16,
#                 channels    = 1,
#                 rate        = RATE,
#                 input       = False,
#                 output      = True )
#
# # output_all = ''            # output signal in all (string)
# output_all = bytes([])            # output signal in all (string)
#
# print ('* Playing...')
#
# # Loop through wave file
# for n in range(0, LEN):
#
#     # Get sample from wave file
#     input_string = wf.readframes(1)
#
#     # Convert string to number
#     input_value = struct.unpack('h', input_string)[0]
#
#     # Get previous and next buffer values (since kr is fractional)
#     kr_prev = int(math.floor(kr))
#     kr_next = kr_prev + 1
#     frac = kr - kr_prev    # 0 <= frac < 1
#     if kr_next >= buffer_MAX:
#         kr_next = kr_next - buffer_MAX
#
#     # Compute output value using interpolation
#     output_value = (1-frac) * buffer[kr_prev] + frac * buffer[kr_next] + input_value
#
#     # Update buffer (pure delay)
#     buffer[int(kw)] = input_value
#
#     # Increment read index
#     kr = kr + 1 + W * math.sin( 2 * math.pi * f0 * n / RATE )
#         # Note: kr is fractional (not integer!)
#
#     # Ensure that 0 <= kr < buffer_MAX
#     if kr >= buffer_MAX:
#         # End of buffer. Circle back to front.
#         kr = 0
#
#     # Increment write index
#     kw = kw + 1
#     if kw == buffer_MAX:
#         # End of buffer. Circle back to front.
#         kw = 0
#
#     # Clip and convert output value to binary string
#     output_string = struct.pack('h', int(clip16(output_value)))
#
#     # Write output to audio stream
#     stream.write(output_string)
#
#     output_all = output_all + output_string     # append new to total
#
# print('* Finished')
#
# stream.stop_stream()
# stream.close()
# p.terminate()
# wf.close()
#
# output_wavefile = wavfile[:-4] + '_vibrato.wav'
# print('Writing to wave file', output_wavefile)
# wf = wave.open(output_wavefile, 'w')      # wave file
# wf.setnchannels(1)      # one channel (mono)
# wf.setsampwidth(2)      # two bytes per sample
# wf.setframerate(RATE)   # samples per second
# wf.writeframes(output_all)
# wf.close()
# print('* Finished')

