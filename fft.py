"""
A modification of the code snippet from https://pysdr.org/content/frequency_domain.html#fft-in-python
"""

import numpy as np
import matplotlib.pyplot as plt

Fs = 184.32e6 # Hz
N = 4096 # number of points to simulate, and our FFT size
t = np.arange(0, 1.0/Fs*N, 1.0/Fs) # time span of one symbol
s = np.sin(50.0e6*2*np.pi*t) # signal @50MHz
S = np.fft.fftshift(np.fft.fft(s))
S_mag = np.abs(S)
f = np.arange(Fs/-2, Fs/2, Fs/N)
plt.figure(0)
plt.plot(f/1.0e6, S_mag,'.-')
plt.xlabel("MHz")
plt.show()