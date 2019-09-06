# play_wave_stereo.py

import pyaudio
import wave
import struct
import math

def clip16( x ):    
    # Clipping for 16 bits
    if x > 32767:
        x = 32767
    elif x < -32768:
        x = -32768
    else:
        x = x        
    return (x)

gain = 0.5

# wavefile = "cat01.wav"
# wavefile = 'sin01_mono.wav'
wavefile = 'sin01_stereo.wav'

print('Play the wave file %s.' % wavefile)

wf = wave.open( wavefile, 'rb' )

# Read the wave file properties
num_channels    = wf.getnchannels()     # Number of channels
RATE            = wf.getframerate()     # Sampling rate (frames/second)
signal_length   = wf.getnframes()       # Signal length
width           = wf.getsampwidth()     # Number of bytes per sample

print('The file has %d channel(s).'            % num_channels)
print('The frame rate is %d frames/second.'    % RATE)
print('The file has %d frames.'                % signal_length)
print('There are %d bytes per sample.'         % width)

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = pyaudio.paInt16,
    channels    = num_channels,
    rate        = RATE,
    input       = False,
    output      = True )

# Read first frame
input_string = wf.readframes(1)          

while len(input_string) > 0:

    # Convert string to numbers
    input_tuple = struct.unpack('hh', input_string)  # produces a two-element tuple

    # Compute output values
    output_value0 = int(clip16(gain * input_tuple[0]))
    output_value1 = int(clip16(gain * input_tuple[1]))

    # Convert output value to binary string
    output_string = struct.pack('hh', output_value0, output_value1)

    # Write output value to audio stream
    stream.write(output_string)

    # Get next frame
    input_string = wf.readframes(1)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
