# draw_rectangle.py

import cv2
import numpy as np 

RCOLOR = (255, 0, 0)    # Rectangle color

ix = -1
iy = -1
drawing = False

def draw_rectangle(event, x, y, params, flag):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:        # Start drawing once the left button is pressed
        ix = x
        iy = y
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:        # Changes the size of the rectangle as the cursor moves
        if drawing == True:
            cv2.rectangle(img, (ix,iy), (x,y), RCOLOR, -1)
    elif event == cv2.EVENT_LBUTTONUP:        # Creates the rectangle once the user releases the left button
        drawing = False
        cv2.rectangle(img, (ix,iy), (x,y), RCOLOR,-1)

cv2.namedWindow('Rectangles')
cv2.setMouseCallback('Rectangles', draw_rectangle)       # Set the callback function

img = cv2.imread('cat.jpg', 1)

# For blank initial image, use:
# img = np.zeros((512,512,3), np.uint8)

print("Switch to video window. Then use mouse to drag a rectangle. Quit via 'q'")

cv2.imshow('Rectangles', img)

while True:
    cv2.imshow('Rectangles', img)

    key = cv2.waitKey(1)
    # key = key & 0xFF      # (Might not be necessary)

    if key == ord('q'):      # Close the window by pressing 'q'
        break

cv2.destroyAllWindows()

# Reference
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_mouse_handling/py_mouse_handling.html#mouse-handling
