# video_rgb_keys.py
# Capture video from camera and display original and R, G, B
# components live, and switch them on and off with the keys r, g, and b
# Original version by Gerald Schuller, November 2015

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

BLUE = True
GREEN = True
RED = True

FONT = cv2.FONT_HERSHEY_SIMPLEX
onoff = {True:'On', False:'Off'}   # Define a dictionary

print("Switch to images. Use keys r, g, b to control colors. Use 'q' to stop")

while True:
    [ok, frame] = cap.read()   # capture frame
    cv2.imshow('Original',frame)

    # Set prescribed color components to zero
    # The order is Blue, Gree, Red
    if BLUE == False:
      frame[:,:,0] = np.zeros(frame[:,:,0].shape);
    if GREEN == False:
      frame[:,:,1] = np.zeros(frame[:,:,1].shape);
    if RED == False:
      frame[:,:,2] = np.zeros(frame[:,:,2].shape);

    # Display resulting video with legend (use putText)
    # putText(frame, text string, position, fontFace, fontScale, color, thickness)
    cv2.putText(frame, "Blue is " + onoff[BLUE],   (20,150), FONT, 1, (255,255,255), 2)
    cv2.putText(frame, "Green is " + onoff[GREEN], (20,100), FONT, 1, (255,255,255), 2)
    cv2.putText(frame, "Red is " + onoff[RED],     (20, 50), FONT, 1, (255,255,255), 2)

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Selected components',frame)

    key = cv2.waitKey(1) & 0xFF;

    if key == ord('b'):     
      BLUE = not BLUE
    if key == ord('g'):     
      GREEN = not GREEN
    if key == ord('r'):     
      RED = not RED

    if key == ord('q'):
        break

# When done, release capture and close windows
cap.release()
cv2.destroyAllWindows()

