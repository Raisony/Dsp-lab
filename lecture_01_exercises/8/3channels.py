# set the number of channels to be more than 2
from struct import pack
from math import pi, sin
import wave
fs = 16000
wf = wave.open('3channels.wav','w')
#3 channels
wf.setnchannels(3)
#32 bits per sample - 4 bytes
wf.setsampwidth(4)
#sampling frequency I choosed is 16000Hz
wf.setframerate(fs)
#32 bits - 0~1
maxAmp = 2**31 - 1.0
f1 = 200
f2 = 400
f3 = 800
for n in range(0, int(0.5*fs)):
#'B'-unsigned 8-bit wav and it standard size is 1
#first channel
	binary_string = pack('i', maxAmp*sin(n*2*pi*f1/fs))
#second channel
	binary_string += pack('i', maxAmp*sin(n*2*pi*f2/fs))
#third channel
	binary_string += pack('i', maxAmp*sin(n*2*pi*f3/fs))
	wf.writeframesraw(binary_string)
wf.close()