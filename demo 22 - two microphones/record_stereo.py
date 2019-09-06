# record_stereo.py
"""
Record stereo input (mics) to wave file.
"""

import pyaudio
import struct
import math
import wave

filename = 'stereo_audio.wav'

RATE = 48000        # RATE: Frames per second
CHANNELS = 2        # Stereo
BLOCKLEN = 1024    # Number of frames in a block
WIDTH = 2           # Number of bytes per sample
RECORD_SECONDS = 4  # Duration of recording

# Open wave file
wf = wave.open(filename, 'w')
wf.setnchannels(CHANNELS)
wf.setsampwidth(WIDTH)
wf.setframerate(RATE)

p = pyaudio.PyAudio()

number_of_devices = p.get_device_count()
print('There are {0:d} devices'.format(number_of_devices))


property_list = ['defaultSampleRate', 'maxInputChannels', 'maxOutputChannels']
for i in range(0, number_of_devices):
    print('Device {0:d} has:'.format(i))
    for s in property_list:
        print(' ', s, '=', p.get_device_info_by_index(i)[s])
        
stream = p.open(format = pyaudio.paInt16,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True)
                # frames_per_buffer = FPB)

# Create output buffer
samples = [0 for i in range(0, CHANNELS * BLOCKLEN)]

print('* Recording for {0:.3f} seconds'.format(RECORD_SECONDS))

# Start loop
for i in range(int(RATE / BLOCKLEN * RECORD_SECONDS)):

    # Get frames from audio input stream
    binary_input_data = stream.read(BLOCKLEN,  exception_on_overflow = False)   # BLOCKLEN = number of frames read

    # Convert binary string to tuple of numbers
    input_tuple = struct.unpack('h' * CHANNELS * BLOCKLEN, binary_input_data);    # WIDTH = 2
   
    # Loop through the samples
    for n in range(0, CHANNELS * BLOCKLEN, CHANNELS):    # increment by 2 for stereo (1 for mono)
        # No processing (stereo):
        samples[n] = input_tuple[n]           # channel 0 (left)
        samples[n+1] = input_tuple[n+1]       # channel 1 (right)

    # convert samples to binary string
    binary_output_data = struct.pack('h' * CHANNELS * BLOCKLEN, *samples)       # WIDTH = 2

    # Write to wave file
    wf.writeframes(binary_output_data)

print('* Done')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()

# Close wave file
wf.close()
