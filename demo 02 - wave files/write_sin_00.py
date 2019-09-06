from struct import pack
from math import sin, pi
import wave

Fs=8000

wf = wave.open('sin_00_mono.wav','w')

wf.setnchannels(1)
wf.setsampwidth(1)
wf.setframerate(Fs)

A = 2**15-1
f = 500
N = int (0.5*Fs)

for n in range(0,N):
	x = A*sin(2*pi*f/Fs*n)
	byte_string = pack('h',int(x))
	wf.writeframes(byte_string)
wf.close()

