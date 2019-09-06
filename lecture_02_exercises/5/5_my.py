#16 bit/sample
#y(n) = x(n) -a1 y(n-1) -a2 y(n-2)
from math import cos, pi
import struct
import pyaudio

Fs = 8000
T = 1
N = T * Fs
f = 800
om = 2.0 * pi * float(f) / Fs
r = 0.998

a0 = 1
a1 = -2 * r * cos(om)
a2 = r**2
b0 = 1
b1 = -r * cos(om)
b2 = 0

x1 = 0.0
y1 = 0.0
y2 = 0.0
gain = 10000.0

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,  #16 bits
				channels = 1,  
				rate = Fs,
				input = False,
				output = True)

# 
for n in range(0, N):
	if n == 0:
		x0 = 1.0
	else:
		x0 = 0.0
	
	y0 = x0 + b1 * x1 - a1 * y1 - a2 * y2
	
	#delays
	x1 = x0
	y2 = y1
	y1 = y0

	output_value = gain * y0
	if output_value > 2**15-1:
		output_value = 2**15-1
	elif output_value < -2**15:
		output_value = -2**15

	output_string = struct.pack('h', int(output_value))
	stream.write(output_string)

print(" * finished * ")

stream.stop_stream()
stream.close()

p.terminate()