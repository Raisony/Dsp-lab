from struct import pack
from math import sin, pi
import wave

Fs = 8000

# Write a mono wave file 

wf = wave.open('sin_8bits_mono.wav', 'w')		# wf : wave file
wf.setnchannels(1)		# one channel (mono)
wf.setsampwidth(1)		# four bytes per sample
wf.setframerate(Fs)		# samples per second
maxAmp = 2**7 - 1.0 	# maximum amplitude
f = 261.625565  		# Hz (middle C)
for n in range(0, int(0.5*Fs)):	# 1 second duration
	binary_string = pack('B', maxAmp * sin(n*2*pi*f/Fs)+128) 
    # i indicate 'integer'  ('<i' or '>i' for different Endians)
	wf.writeframesraw(binary_string)
wf.close()

# Write a stereo wave file

wf = wave.open('sin_8bits_morethanstereo.wav', 'w')
wf.setnchannels(3)		# two channels (stereo)
wf.setsampwidth(1)		# four bytes per sample
wf.setframerate(Fs)		# samples per second
maxAmp = 2**7-1.0 		# maximum amplitude
f1 = 261.625565  		# 261.625565 Hz (middle C)
f2 = 293.665  			# note A4
f3 = 329.628
for n in range(0, int(0.5*Fs)):	# 1 second duration
	binary_string = pack('B', maxAmp * sin(n*2*pi*f1/Fs)+128) # left channel
	binary_string += pack('B', maxAmp * sin(n*2*pi*f2/Fs)+128) # right channel
        binary_string += pack('B', maxAmp * sin(n*2*pi*f3/Fs)+128) # right channel
	wf.writeframesraw(binary_string)
wf.close()
