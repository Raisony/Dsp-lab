# write_sin_01
# 
# Make a wave file (.wav) consisting of a sine wave
# Adapted from http://www.swharden.com/blog/2011-07-08-create-mono-and-stereo-wave-files-with-python/

# 16 bits per sample

# For 'wave' functions, see:
# https://docs.python.org/3/library/wave.html

# For 'pack' function see:
# https://docs.python.org/3/library/struct.html

from struct import pack
from math import cos, sin, pi
import wave

Fs = 8000

# Write a mono wave file

wf = wave.open('sin_01_mono.wav', 'w')		# wf : wave file
wf.setnchannels(1)			# one channel (mono)
wf.setsampwidth(2)			# two bytes per sample (16 bits per sample)
wf.setframerate(Fs)			# samples per second
print('signal length:', wf.getnframes())
A = 2**15 - 1.0 			# amplitude
f = 261.6					# frequency in Hz (middle C)
N = int(0.5*Fs)				# half-second in samples
for n in range(0, N):	    # half-second loop 
	x = A * sin(2*pi*f/Fs*n)       	# signal value (float)
	byte_string = pack('h', int(x))   
	# 'h' stands for 'short integer' (16 bits)
	wf.writeframes(byte_string)
wf.close()

# Write a stereo wave file

wf = wave.open('sin_03_stereo.wav', 'w')
wf.setnchannels(2)			# two channels (stereo)
wf.setsampwidth(4)			# two bytes per sample (16 bits per sample)
wf.setframerate(Fs)			# samples per second
f1 = 261.6					# frequency in Hz (middle C)
f2 = 440.0 
f3 = 261.6
f4 = 440.0   				# note A4
for n in range(0, N):		# half-second loop 

	# left channel
	x = A * sin(2*pi*f1/Fs*n)
	byte_string = pack('h', int(x))
	# 'h' stands for 'short integer' (16 bits)

	# right channel
	x = A * sin(2*pi*f2/Fs*n)
	byte_string = byte_string + pack('h', int(x))  # concatenation


	# left channel
	y = A * cos(2*pi*f3/Fs*n)
	byte_string = pack('h', int(y))
	# 'h' stands for 'short integer' (16 bits)

	# right channel
	y = A * cos(2*pi*f4/Fs*n)
	byte_string = byte_string + pack('h', int(y))  # concatenation



	wf.writeframes(byte_string)
print('signal length:', wf.getnframes())
print('number of channels:', wf.getnchannels())
print('number of frames per second:', wf.getframerate())

print('number of bytes per frame:', wf.getsampwidth())
wf.close()

