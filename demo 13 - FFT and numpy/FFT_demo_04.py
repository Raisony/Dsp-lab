# FFT_demo_04.py

import numpy as np
from matplotlib import pyplot

N = 20
n = np.linspace(0, N-1, N)  # N points from 0 to N-1 inclusive
x = np.cos(2.0 * 2.0 * np.pi / N * n)
# x = np.cos(2.5 * 2.0 * np.pi / N * n)
X = np.fft.fft(x)

fig = pyplot.figure(1)

pyplot.subplot(2, 1, 1)
pyplot.stem(n, x)
pyplot.xlim(-1, N)
pyplot.title('Signal')

pyplot.subplot(2, 1, 2)
pyplot.stem(n, abs(X))
# pyplot.stem(n, np.angle(X))  # for phase
pyplot.xlim(-1, N)
pyplot.title('Spectrum')

pyplot.show()
fig.savefig('FFT_demo_04.pdf')


