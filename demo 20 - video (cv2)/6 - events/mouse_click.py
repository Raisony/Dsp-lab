# mouse_click.py

import cv2
import numpy as np

RADIUS = 50    			# circle radius (in pixels)
COLOR = (0, 255, 0)    # circle color

# Define callback function
def draw_circle(event, x, y, flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), RADIUS, COLOR, -1)      # -1 for filled circle; 0 for boundary only

# Read an image
img = cv2.imread('cat.jpg', 1)
cv2.namedWindow('Live video')
cv2.setMouseCallback('Live video', draw_circle)    # Connect the callback function

print("Switch to video window. Then use left mouse button. Quit via 'q'")

while True:
    cv2.imshow('Live video', img)

    key = cv2.waitKey(1)
    # key = key & 0xFF		# (Might not be necessary)

    if key == ord('q'):      # Stop if 'q' pressed
        break

cv2.destroyAllWindows()


