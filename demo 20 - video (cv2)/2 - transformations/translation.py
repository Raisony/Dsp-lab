# translation.py

import cv2
import numpy as np

img = cv2.imread('cat.jpg')

M = np.float32([[1,0,200],[0,1,50]])

print(M)

translated_image = cv2.warpAffine(img, M, (img.shape[1],img.shape[0]))

cv2.imshow('Translated image', translated_image)
cv2.imwrite('cat_translated.jpg', translated_image)

print('Switch to image view. Then press any key to close')

cv2.waitKey(0)
cv2.destroyAllWindows()