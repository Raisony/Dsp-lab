
import wave

wf = wave.open('cat01.wav')

print('number of channels:', wf.getnchannels() ) 
print('number of frames per second:', wf.getframerate() )
print('signal length:', wf.getnframes() )
print('number of bytes per frame:', wf.getsampwidth() )

print()

# Printing with prescribed format 
print('number of channels: %d' %  wf.getnchannels() ) 
print('number of frames per second: %d' % wf.getframerate() )
print('signal length: %d' % wf.getnframes() )
print('number of bytes per frame: %d' % wf.getsampwidth() )

wf.close()

