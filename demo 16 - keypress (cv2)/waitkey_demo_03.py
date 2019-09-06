# waitkey_demo_03.py

import cv2

img = cv2.imread('image_01.png')

cv2.imshow('image', img)

print('Select the image window, then press a key on the keyboard')
print('Press q key to quit')

while True:

	key = cv2.waitKey(1)
  # 1 means wait for 1 millisecond for key press
	# If there is no key press in 1 millisecond, then return -1

	if key != -1:
		print('You pressed key', key)
	# else:									# Try uncommenting this part. What happens?
	# 	print('You did not press a key')

	if key == ord('q'):
		break

print('Good bye')

cv2.destroyAllWindows()
