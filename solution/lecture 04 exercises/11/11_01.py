f1 = 50      # frequency 1
f2 = 1000    # frequency 2

import pyaudio
import struct
import wave
import math

input_wavefile = 'author.wav'

wf          = wave.open( input_wavefile, 'rb')
RATE        = wf.getframerate()
WIDTH       = wf.getsampwidth()
LEN         = wf.getnframes() 
CHANNELS    = wf.getnchannels() 

print('The sampling rate is {0:d} samples per second'.format(RATE))
print('Each sample is {0:d} bytes'.format(WIDTH))
print('The signal is {0:d} samples long'.format(LEN))
print('The signal has {0:d} channel(s)'.format(CHANNELS))

#write wave to wav
nwf = wave.open('wavefile_11_01.wav', 'w')
nwf.setnchannels(CHANNELS+1)
nwf.setsampwidth(WIDTH)
nwf.setframerate(RATE)
# Open audio stream
p = pyaudio.PyAudio()
stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS+1,
    rate        = RATE,
    input       = False,
    output      = True)

print('* Playing...')

# Loop through wave file 
for n in range(0, LEN):

    # Get sample from wave file
    input_string = wf.readframes(1)

    # Convert binary string to tuple of numbers
    input_tuple = struct.unpack('h', input_string)
        # (h: two bytes per sample (WIDTH = 2))

    # Use first value (of two if stereo)
    input_value = input_tuple[0]

    # Amplitude modulation  (f0 Hz cosine)
    output_value_1 = input_value * math.cos(2.0*math.pi*f1*n/RATE)
    output_value_2 = input_value * math.cos(2.0*math.pi*f2*n/RATE)
    # Convert value to binary string
    output_string = struct.pack('h', int(output_value_1))
    output_string += struct.pack('h', int(output_value_2))
    # Write binary string to audio output stream
    stream.write(output_string)
    #write the string to the file
    nwf.writeframes(output_string)
print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()

# Close wavefile
wf.close()
