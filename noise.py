import numpy as np
import matplotlib.pyplot as plt

def qpsk(n):
    r = np.random.randint(0, 4, size=n)
    x = np.zeros(n, dtype=np.complex64)
    x[r==0] = + 0.707 + 0.707j
    x[r==1] = + 0.707 - 0.707j
    x[r==2] = - 0.707 + 0.707j
    x[r==3] = - 0.707 - 0.707j
    return x

def spectrum(x):
    fft_x = np.fft.fftshift(np.fft.fft(x, norm="ortho"))
    return 10 * np.log10(np.abs(fft_x))

n = 1024
signal_power = 1.0 # dBm
snr_db = 10 
snr_linear = 10.0**(snr_db/10.0)
noise_power = variance = signal_power / snr_linear # 0.1 dBm
std_deviation = np.sqrt(noise_power)
noise = 1.0/np.sqrt(2) * (np.random.randn(n) + 1j*np.random.randn(n)) * std_deviation
signal = qpsk(n) * np.sqrt(signal_power)
channel_coefficient = 1
received_signal = channel_coefficient * signal + noise
print(np.var(signal))  # signal_power -> 1.0 dBm
print(np.var(noise))   # noise_power -> 0.1 dBm

print(np.mean(spectrum(signal))) # should be 0, why -1?
print(np.mean(spectrum(noise)))

fig, axes = plt.subplots(1, 2)
axes[0].plot(spectrum(signal)) # 1.0 dBm -> spectrum around 0 dB
axes[1].plot(spectrum(noise))  # 0.1 dBm -> spectrum around -10 dB, why -5 dB?
plt.show()
