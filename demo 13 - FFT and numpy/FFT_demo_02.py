# FFT_demo_02.py

import numpy as np

x = np.array([3, 7, 2, 5, 1])
X = np.fft.fft(x)
g = np.fft.ifft(X)
err = x - g                 # reconstruction error


print('x is a', type(x))
print('X is a', type(X))
print('g is a', type(g))
print('err is a', type(err))

print('x = ', x)
print('X = ', X)
print('max(abs(err) = ', max(abs(err)))
