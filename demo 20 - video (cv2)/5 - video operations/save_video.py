# save_video.py
# Record a video in real-time, and writes it to a file

import numpy as np
import cv2

cap = cv2.VideoCapture(0)                       # Initialize video capture. 

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)       # Width of video frames
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)     # Height of video frames
shape = (int(width), int(height))               # tuple of integers

print('Frames are of size: ', shape)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

# In Windows, replace the above line of code with this one:
# fourcc = cv2.VideoWriter_fourcc(*'XVID')

FPS = 20.0          # Frames per second (of saved video)
out = cv2.VideoWriter('output.avi', fourcc, FPS, shape)

print("Switch to video window. Press 'q' to quit")

while cap.isOpened():

    [ok, frame] = cap.read()

    if ok == True:
        frame = cv2.flip(frame, 1)
        out.write(frame)                # write frame to video file
        cv2.imshow('Live video', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'): 
            break                   # Stop when 'q' key is pressed
    else:
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()

