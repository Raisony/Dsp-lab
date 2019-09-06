# demo_weightedsum.py

import cv2
import numpy as np 

img1 = cv2.imread('dog.jpg', 1)
img2 = cv2.imread('cat.jpg', 1)

print(img1.shape)
print(img2.shape)

img2 = img2[0:img1.shape[0], 0:img1.shape[1], :]
print(img2.shape)

# quit()

cv2.imshow('Weighted image', img1)

print('Switch to image window. Then press any key to continue.')

cv2.waitKey(0)   # Wait for key press

N = 10
for i in range(N):
    y = cv2.addWeighted(img1, 1-i/(N-1), img2, i/(N-1), 0)
    # y : weighted sum of two images
    cv2.imshow('Weighted image', y)
    cv2.waitKey(500)   # Wait 0.5 seconds
    
cv2.destroyAllWindows()
