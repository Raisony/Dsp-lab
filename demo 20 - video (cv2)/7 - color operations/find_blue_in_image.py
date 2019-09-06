# find_blue_in_image.py
# Detect pixels similar to a prescribed color.
# This can be done usg HSV color space.

import cv2
import numpy as np 

img = cv2.imread('fruit.jpg', 1)   
# 1 : import image in color

# Convert to different color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(type(img_hsv))
print(img_hsv.shape)
print(img_hsv.dtype)

Green = np.uint8([[[0, 255, 0]]])   # 3D array
Green_hsv = cv2.cvtColor(Green, cv2.COLOR_BGR2HSV)
h = Green_hsv[0, 0, 0]
print('Green in HSV color space:', Green_hsv)
print('Hue = ', h)   # see that h = 120

lower = np.array([h-30, 40, 40 ])
upper = np.array([h+30, 250, 250])
print('lower = ', lower)
print('upper = ', upper)

# quit()

# Determine binary mask
blue_mask = cv2.inRange(img_hsv, lower, upper)

# Apply mask to color image
output = cv2.bitwise_and(img, img, mask = blue_mask)

# Show images:
cv2.imshow('Original image', img)
cv2.imshow('Mask', blue_mask)
cv2.imshow('Segmented image', output)

print('Switch to images. Then press any key to stop')

cv2.waitKey(0)
cv2.destroyAllWindows()

# Write the image to a file
cv2.imwrite('fruit_mask.jpg', blue_mask)   
cv2.imwrite('fruit_blue.jpg', output)


# Reference
# http://docs.opencv.org/3.2.0/df/d9d/tutorial_py_colorspaces.html
