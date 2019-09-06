# FFT_demo_01.py

import numpy as np

x = [3, 7, 2, 5, 1]
X = np.fft.fft(x)         # Fourier transform
g = np.fft.ifft(X)        # inverse Fourier transform

print('x = ', x)
print('X = ', X)
print('g = ', g)

print('x is a', type(x))
print('X is a', type(X))
print('g is a', type(g))

err = x - g                # reconstruction error

print('err = ', err)
print('err is a', type(err))

print('max(abs(err)) = ', np.max(np.abs(err)))

