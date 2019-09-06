# write_sin_02
# 
# Make a wave file (.wav) consisting of a sine wave
# Adapted from http://www.swharden.com

# 32 bits per sample

from struct import pack
from math import sin, pi
import wave

Fs = 8000

# Write a mono wave file 

wf = wave.open('sin_02_mono.wav', 'w')		# wf : wave file
wf.setnchannels(1)			# one channel (mono)
wf.setsampwidth(4)			# four bytes per sample (32 bits per sample)
wf.setframerate(Fs)			# samples per second
A = 2**31 - 1.0 			# amplitude
f = 261.6					# frequency in Hz (middle C)
N = int(0.5*Fs)				# half-second in samples
for n in range(0, N):	    # half-second loop 
	x = A * sin(2*pi*f/Fs*n)
	byte_string = pack('i', int(x)) 
	# 'i' stands for 'integer' (32 bits)
	wf.writeframesraw(byte_string)
wf.close()

# Write a stereo wave file

wf = wave.open('sin_02_stereo.wav', 'w')
wf.setnchannels(2)			# two channels (stereo)
wf.setsampwidth(4)			# four bytes per sample (32 bits per sample)
wf.setframerate(Fs)			# samples per second
f1 = 261.6					# frequency in Hz (middle C)
f2 = 440.0  				# note A4
for n in range(0, N):	    # half-second loop 

	# left channel
	x = A * sin(2*pi*f1/Fs*n)
	byte_string = pack('i', int(x))  # 'i' stands for 'integer' (32 bits)

	# right channel
	x = A * sin(2*pi*f2/Fs*n)
	byte_string = byte_string + pack('i', int(x)) # concatenation

	wf.writeframes(byte_string)
wf.close()
