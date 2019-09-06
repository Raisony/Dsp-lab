import pyaudio
import wave
import struct
import math

from myfunctions import clip16

wavfile = 'author.wav'
# wavfile = 'sin01_mono.wav'

print('Play the wave file %s.' % wavfile)

# Open wave file (should be mono channel)
wf = wave.open( wavfile, 'rb' )

# Read the wave file properties
num_channels    = wf.getnchannels()     # Number of channels
RATE            = wf.getframerate()     # Sampling rate (frames/second)
signal_length   = wf.getnframes()       # Signal length
width           = wf.getsampwidth()     # Number of bytes per sample

print('The file has %d channel(s).'            % num_channels)
print('The frame rate is %d frames/second.'    % RATE)
print('The file has %d frames.'                % signal_length)
print('There are %d bytes per sample.'         % width)

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
w1 = 0.0
w2 = 0.0
w3 = 0.0
w4 = 0.0
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = pyaudio.paInt16,
    channels    = num_channels,
    rate        = RATE,
    input       = False,
    output      = True )

# Get first frame from wave file
input_string = wf.readframes(1)

nwf = wave.open('wav_canonical.wav','w')
nwf.setnchannels(num_channels)
nwf.setsampwidth(width)
nwf.setframerate(RATE)

while len(input_string) > 0:

    # Convert string to number
    input_tuple = struct.unpack('h', input_string)  # One-element tuple
    input_value = input_tuple[0]                    # Number

    # Set input to difference equation
    x0 = input_value
    
    # Difference equation
    w0 = x0 - a1*w1 - a2*w2 - a3*w3 - a4*w4
    y0 = b0*w0 + b2*w2 + b4*w4
    # Delays
    w4 = w3
    w3 = w2
    w2 = w1
    w1 = w0

    # Compute output value
    output_value = int(clip16(y0))    # Integer in allowed range

    # Convert output value to binary string
    output_string = struct.pack('h', output_value)  

    # Write binary string to audio stream
    stream.write(output_string)                     
    nwf.writeframes(output_string)

    # Get next frame from wave file
    input_string = wf.readframes(1)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
nwf.close()