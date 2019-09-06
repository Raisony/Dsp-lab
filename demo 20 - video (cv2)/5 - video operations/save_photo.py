# save_photo.py
# Capture a photograph when user presses 'p'

import numpy as np
import cv2

cap = cv2.VideoCapture(0)    # Initialize video capture. 

print("Switch to video window. Then press 'p' to save image, 'q' to quit")

while cap.isOpened():

    [ok, frame] = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow('Live video', frame)

    key = cv2.waitKey(1)
    # key = key & 0xFF		# (Might not be necessary)

    if key == ord('p'):
	    # Save image when 'p' key is pressed
        cv2.imwrite('photo.jpg', frame)
    elif key == ord('q'):
	    # Stop when 'q' key is pressed
        break

cv2.destroyAllWindows()			# close windows created by cv2

