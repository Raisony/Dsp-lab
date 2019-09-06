# waitkey_demo_02.py

import cv2

img = cv2.imread('image_01.png')

cv2.imshow('image', img)

print('Select the image window, then press a key on the keyboard')
print('Press q key to quit')

while True:

	key = cv2.waitKey(0)			# 0 means wait until key press

	print('You pressed key', key)

	if key == ord('q'):
		break

print('Good bye')

cv2.destroyAllWindows()
