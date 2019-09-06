# show_rgb.py
# Show the three color channels of a color image.
# The colors are ordered Blue, Green, Red.
# Each color channel is bright where that color is present in the image

import cv2
import numpy as np 

img = cv2.imread('fruit.jpg', 1)   
# 1 means import image in color

print(type(img))
print(img.shape)
print(img.dtype)

cv2.imshow('Original image', img)
cv2.imshow('Channel 0 (Blue)', img[:,:,0])
cv2.imshow('Channel 1 (Green)', img[:,:,1])
cv2.imshow('Channel 2 (Red)', img[:,:,2])

print('Switch to images. Then press any key to stop')

cv2.waitKey(0)   # 0 means wait forever for keystroke.
cv2.destroyAllWindows()
