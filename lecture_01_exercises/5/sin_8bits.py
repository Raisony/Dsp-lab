from struct import pack
from math import sin, pi
import wave

Fs = 8000

wf = wave.open('sin_8bits_mono.wav','w')
wf.setnchannels(1)#mono
wf.setsampwidth(1)#8 bits per sample - 1 bytes
wf.setframerate(Fs)#frequency I choosed is 8000Hz
maxAmp = 2**7 - 1.0#8 bits - 0~7
f = 200
for n in range(0, int(0.5*Fs)):
#'B'-unsigned 8-bit wav and it standard size is 1
	binary_string = pack('B', maxAmp * sin(n*2*pi*f/Fs)+128)
	wf.writeframesraw(binary_string)
wf.close()
