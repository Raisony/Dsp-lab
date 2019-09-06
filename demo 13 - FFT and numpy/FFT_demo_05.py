# FFT_demo_05.py

# Real FFT

import numpy as np
from matplotlib import pyplot

N = 20
n = np.linspace(0, N-1, N)  # N points from 0 to N-1 inclusive
x = np.cos(2.5 * 2.0 * np.pi / N * n)
X = np.fft.rfft(x)
g = np.fft.irfft(X)
err = x - g                 # reconstruction error

print('max(abs(err)) = ', np.max(np.abs(err)))

fig = pyplot.figure(1)

pyplot.subplot(2, 1, 1)
pyplot.stem(n, x)
pyplot.xlim(-1, N)
pyplot.title('Signal')

k = range(len(X))

pyplot.subplot(2, 1, 2)
pyplot.stem(k, abs(X))
pyplot.xlim(-1, N)
pyplot.title('Spectrum')

fig.savefig('FFT_demo_05.pdf')
pyplot.show()

