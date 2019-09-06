# find_green_in_image.py
# Detect pixels similar to a prescribed color.
# This can be done usg HSV color space.

import cv2
import numpy as np 

img = cv2.imread('parrot.jpg', 1)   
# 1 : import image in color

# Convert to different color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(type(img_hsv))
print(img_hsv.shape)
print(img_hsv.dtype)

green = np.uint8([[[0, 255, 0]]])   # 3D array
green_hsv = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
h = green_hsv[0,0,0]
print('Blue in HSV color space:', green_hsv)
print('Hue = ', h)   # see that h = 120

lower = np.array([h-20, 50, 50])
upper = np.array([h+20, 255, 255])
print('lower = ', lower)
print('upper = ', upper)

# quit()

# Determine binary mask
green_mask = cv2.inRange(img_hsv, lower, upper)

# Apply mask to color image
output = cv2.bitwise_and(img, img, mask = green_mask)

# Show images:
cv2.imshow('Original image', img)
cv2.imshow('Mask', green_mask)
cv2.imshow('Segmented image', output)

print('Switch to images. Then press any key to stop')

cv2.waitKey(0)
cv2.destroyAllWindows()

# Write the image to a file
cv2.imwrite('parrot_mask.jpg', green_mask)   
cv2.imwrite('parrot_green.jpg', output)   


# Reference
# http://docs.opencv.org/3.2.0/df/d9d/tutorial_py_colorspaces.html
