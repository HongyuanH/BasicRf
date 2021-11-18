import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 184.32e6 # Hz
n = 4096 # FFT size
t = np.arange(0, n/sampling_rate, 1.0/sampling_rate) # time span of one symbol
f = np.arange(sampling_rate/-2, sampling_rate/2, sampling_rate/n) # frequency span
x = np.sin(50.0e6 * 2*np.pi*t) # signal @50MHz
fft_x = np.fft.fftshift(np.fft.fft(x, norm="ortho")) # same as  np.fft.fft(x) / np.sqrt(n)
y = np.fft.fftshift(np.fft.ifft(fft_x, norm="ortho")) # same as np.fft.ifft(fft_x) * np.sqrt(n)

# Parseval's Theorem
x_energy = np.sum( np.abs(x) ** 2 )
fft_x_energy = np.sum( np.abs(fft_x) ** 2 )
y_energy = np.sum( np.abs(y) ** 2 )
print(x_energy, fft_x_energy, y_energy) # 2048, 2048, 2048

fig, axes = plt.subplots(3, 1)
axes[0].plot(t*1.0e6, np.abs(x))
axes[0].set_xlabel("us")
axes[1].plot(f/1.0e6, np.abs(fft_x))
axes[1].set_xlabel("MHz")
axes[2].plot(t*1.0e6, np.abs(y))
axes[2].set_xlabel("us")
plt.show()

