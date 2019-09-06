# show_hsv.py
# Show the three channels of a color image represented as HSV.
# The channels are: Hue, Saturation, Value.
# Value encodes brightness information
# Hue and Saturation encode color informaiton.

import cv2
import numpy as np 

img = cv2.imread('fruit.jpg', 1)   
# 1 means import image in color

# Convert to different color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(type(img_hsv))
print(img_hsv.shape)
print(img_hsv.dtype)

cv2.imshow('Original image', img)
cv2.imshow('Channel 0 (Hue)', img_hsv[:,:,0])
cv2.imshow('Channel 1 (Saturation)', img_hsv[:,:,1])
cv2.imshow('Channel 2 (Value)', img_hsv[:,:,2])

print('Switch to images. Then press any key to stop')

cv2.waitKey(0)   # 0 means wait forever for keystroke.
cv2.destroyAllWindows()

# Reference
# http://docs.opencv.org/3.2.0/df/d9d/tutorial_py_colorspaces.html
