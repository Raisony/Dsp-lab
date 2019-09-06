# video_rgb.py
# Captures video from camera, displays original
# and R, G, B components in real-time

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

print("Switch to images. Then press 'q' to stop")

while True:
    [ok, frame] = cap.read()        # Capture frame

    # Shrink frames (if necessary) to fit 4 frames on screen
    frame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5)

    # Display frame and its color components
    cv2.imshow('Original', frame)
    cv2.imshow('Blue component', frame[:,:,0])
    cv2.imshow('Green component', frame[:,:,1])
    cv2.imshow('Red component', frame[:,:,2])

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
