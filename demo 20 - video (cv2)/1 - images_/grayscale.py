# grayscale.py
# Read an image from a file as a gray-scale image and write it to a file.

import cv2 
import numpy as np 

img = cv2.imread('cat.jpg', 0) 		# 0 means the image is read as a gray-scale image

print(type(img))					# data type?
print(img.shape)					# shape (size) of image
print(np.shape(img))				# equivalent to img.shape
print(img.size)

# quit()

cv2.imshow('This the title', img)	# Display the image 

print('Switch to image view. Then press any key to close')

cv2.waitKey(0)                      # 0 means wait forever for a keystroke. When a key is pressed, the program proceeds
cv2.destroyAllWindows()             # Close the image window

cv2.imwrite('cat_grayscale.jpg', img)   # Write the image to a file

#reference - https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image