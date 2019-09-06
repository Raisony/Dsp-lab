
import wave

wf=wave.open('jjs16.wav')

a = wf.getnchannels()
print ("number of channels is: ", a)

b = wf.getframerate()
print ("frame rate (number of frames per second) is: ",b)

c = wf.getnframes()
print ("total number of frames (length of signal) is", c)

d = wf.getsampwidth()
print ("number of bytes per frame is :", d)

