# demo_02_simple_wire.py
# Play microphone input to speaker using callback function
#
# Adapted from Wire(Callback) example
# https://people.csail.mit.edu/hubert/pyaudio/

import pyaudio
import time

CHANNELS = 1
RATE = 16000

# Define callback function
def my_callback_fun(binary_input_data, block_size, time_info, status):
	binary_output_data = binary_input_data
	return(binary_output_data, pyaudio.paContinue)    # Return data and status

# Create audio object
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format = pyaudio.paInt16,   	# 16 bits/sample
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                stream_callback = my_callback_fun)

stream.start_stream()

print('(1) Is the audio stream active?', stream.is_active())

print('The wire will be on for 5 seconds')
time.sleep(5)

# Close audio stream
stream.stop_stream()

print('(2) Is the audio stream active?', stream.is_active())

stream.close()
p.terminate()

