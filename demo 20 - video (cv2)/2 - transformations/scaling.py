# scaling.py

import cv2
import numpy as np

img = cv2.imread('cat.jpg')

scaled_image = cv2.resize(img, (0,0), fx = 0.8, fy = 1.3)
# fx is scaling factor in x (horizontal) direction
# fy is scaling factor in y (vertical) direction

cv2.imshow('Resized image', scaled_image)
cv2.imwrite('cat_scaled.jpg', scaled_image)

print('Original image size:', img.shape)
print('After resizing:', scaled_image.shape)

print('Switch to image view. Then press any key to close')

cv2.waitKey(0)
cv2.destroyAllWindows()

