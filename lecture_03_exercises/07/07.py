import math
import struct
import pyaudio
import wave

WIDTH = 2
CHANNELS = 1
RATE = 16000
DURATION = 10
f0 = 400

N = DURATION * RATE

def clip16( x ):    
    if x > 32767:
        x = 32767
    elif x < -32768:
        x = -32768
    else:
        x = x        
    return (x)

p = pyaudio.PyAudio()

stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = True,
    output      = True)

print('* Start')

newwf = wave.open('JingjieSheng_7.wav', 'w')
newwf.setnchannels(CHANNELS)
newwf.setsampwidth(WIDTH)
newwf.setframerate(RATE)

for n in range(0, N):

    input_string = stream.read(1, exception_on_overflow = False)
    input_tuple = struct.unpack('h', input_string)
    input_value = input_tuple[0]

    x0 = input_value
    y0 = math.cos(2*math.pi*f0*n/RATE)*x0

    output_value = int(clip16(y0))
    output_string = struct.pack('h', output_value)  
    stream.write(output_string)                     
    newwf.writeframesraw(output_string)
print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
