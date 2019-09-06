# find_blue_in_video.py

import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

print('Switch to images. Then press q key to stop')

while True:

    [ok, frame] = cap.read()
    frame = cv2.flip(frame, 1)

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([100, 50, 50])     # lower 'blue'
    upper = np.array([150, 255, 255])   # upper 'blue'

    blue_mask = cv2.inRange(frame_hsv, lower, upper)

    output = cv2.bitwise_and(frame, frame, mask = blue_mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Color mask', blue_mask)
    cv2.imshow('Output image', output)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
