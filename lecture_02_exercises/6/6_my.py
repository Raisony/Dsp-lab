#16 bit/sample
#y(n) = x(n) -a1 y(n-1) -a2 y(n-2)
from math import cos, pi
import struct
import pyaudio

Fs = 8000
T = 1
N = T * Fs
f1 = 800 
f2 = 100
om1 = 2 * pi * float(f1) / Fs
om2 = 2 * pi * float(f2) / Fs
r = 0.998
#channel-1(with _1)
a0_1 = 1
a1_1 = -2 * r * cos(om1)
a2_1 = r**2
b0_1 = 1
b1_1 = 0
b2_1 = 0
#channel-2(with _2)
a0_2 = 1
a1_2 = -2 * r * cos(om2)
a2_2 = r**2
b0_2 = 1
b1_2 = 0
b2_2 = 0

y1_1 = 0.0
y2_1 = 0.0
y1_2 = 0.0
y2_2 = 0.0
gain = 10000.0

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,  #16 bits
				channels = 2,  #stereo
				rate = Fs,
				input = False,
				output = True)

for n in range(0, N):
	if n == 0:
		x0 = 1.0
	else:
		x0 = 0.0
	y0_1 = x0 - a1_1 * y1_1 - a2_1 * y2_1  #channel-1
	y0_2 = x0 - a1_2 * y1_2 - a2_2 * y2_2  #channel-2
	#delays
	y2_1 = y1_1
	y1_1 = y0_1
	y2_2 = y1_2
	y1_2 = y0_2

	output_value_1 = gain * y0_1
	if output_value_1 > 2**15-1:
		output_value_1 = 2**15-1
	elif output_value_1 < -2**15:
		output_value_1 = -2**15

	output_value_2 = gain * y0_2
	if output_value_2 > 2**15-1:
		output_value_2 = 2**15-1
	elif output_value_2 < -2**15:
		output_value_2 = -2**15

	output_string = struct.pack('h', int(output_value_1))
	output_string += struct.pack('h', int(output_value_2))
	stream.write(output_string)

print(" * finished * ")

stream.stop_stream()
stream.close()

p.terminate()