import pywt
import sys
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1]
prefix = filename.split("_")[0]


data = np.genfromtxt("./{}_condensed.csv".format(prefix), delimiter=",", skip_header=1)
scales = np.exp(np.linspace(np.log(1e1), np.log(1e5), 50))
time = (data[:, 0] - data[0, 0]) / 3600

print("Calculating CWT")
coef, freqs = pywt.cwt(data[:, 5], scales, "gaus1", sampling_period=np.mean(np.diff(time))* 3600)
coef = abs(coef)

print(1  / np.min(freqs) / 3600, 1 / 3600 / np.max(freqs))

print("Plotting CWT")
plt.figure()
x, y = np.meshgrid(time, freqs)
plt.pcolormesh(x, y, coef)
plt.axhline(1 / (24 * 3600))
plt.yscale("log")
plt.xlabel("Time (hour)")
plt.ylabel("Frequency (Hz)")
plt.colorbar()
plt.savefig("{}_Spectrogram.png".format(prefix))
'''
plt.imshow(coef,
        aspect=10,
        extent=[time[0], time[-1], np.log(freqs[-1]), np.log(freqs[0])],
        #extent=[0, 10, 0.1, 100],
        interpolation="bilinear")
plt.colorbar()
'''

#plt.figure()
#plt.plot(time, data[:, 5])

plt.show()
