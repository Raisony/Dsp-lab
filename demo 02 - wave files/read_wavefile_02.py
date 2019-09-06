
import wave

# help(wave)

# web page: https://docs.python.org/2/library/wave.html

wf = wave.open('cat01.wav')

wf.getnchannels() 
# number of channels

wf.getframerate() 
# frame rate (number of frames per second)

wf.getnframes() 
# total number of frames (length of signal)

wf.getsampwidth() 
# number of bytes per frame

wf.close()
