# color.py
# Read an image from a file as a colour image and write it to a file

import cv2 
import numpy as np 

img = cv2.imread('cat.jpg', 1)      # 1 means the image as a color image

print(img.shape)					# shape (size) of image (why is it a 3D array?)

cv2.imshow('A cat', img)            # Display the image 

print('Switch to image view. Then press any key to close')

cv2.waitKey(0)                      # 0 means wait forever for a keystroke. When a key is pressed, the program proceeds
cv2.destroyAllWindows()             # Close the image window

cv2.imwrite('cat_color.jpg', img)   # Write the image to a file

#reference - https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image