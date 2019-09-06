# rotation.py

import cv2
import numpy as np

img = cv2.imread('cat.jpg')
rows, cols = img.shape[0], img.shape[1]

M = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1)
print(M)

rotated_image = cv2.warpAffine(img, M, (cols,rows))

cv2.imshow('Rotated image', rotated_image)
cv2.imwrite('cat_rotated.jpg', rotated_image)

print('Switch to image view. Then press any key to close')

cv2.waitKey(0)
cv2.destroyAllWindows()