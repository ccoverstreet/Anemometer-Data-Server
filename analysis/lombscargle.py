import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.signal import lombscargle
import sys

filename = sys.argv[1]
prefix = filename.split("_")[0]
#prefix = "171A1701AF3D90D046E25D1FBCEEF43A"

data = np.genfromtxt("./{}_condensed.csv".format(prefix), skip_header=1, delimiter=",")

print(data)
start = 0
trimmed_data = data[start:]
trimmed_data[:, 0] = trimmed_data[:, 0] - np.min(trimmed_data[:, 0])

fig = plt.figure()
gs = GridSpec(2, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, :])
ax1.set_title("Anemometer {}".format(prefix))
ax1.plot(trimmed_data[:, 0] / 3600, trimmed_data[:, 5])
ax1.set_ylabel("Wind Speed (m/s)")
ax1.set_xlabel("Time (hours)")
ax1.axhline(np.mean(trimmed_data[:, 5]), color="y")

time = np.copy(trimmed_data[:, 0])
wind = np.copy(trimmed_data[:, 5])
start = 1 / trimmed_data[-1, 0] * 2 * np.pi
end = 1e-2 * 2 * np.pi

freqs = np.exp(np.linspace(np.log(start), np.log(end), 1000))
periodogram = lombscargle(time, wind, freqs, normalize=True)

ax2 = fig.add_subplot(gs[1, 0])
ax2.plot(np.power(freqs / (2*np.pi) * 3600, -1), periodogram)
ax2.set_ylabel("Intensity")
ax2.set_xlabel("Period (hours)")

ax3 = fig.add_subplot(gs[1, 1])
cutoff = 0
#ax3.plot(1 / (freqs / (2 * np.pi) * 3600), periodogram)
ax3.set_xscale('log')
#ax3.plot(np.power(np.log(freqs / (2*np.pi) * 3600), -1)[cutoff:], periodogram[cutoff:])
ax3.set_ylabel("Intensity")
ax3.set_xlabel("Period (hours)")

plt.tight_layout()
plt.subplots_adjust(left=0.05)
plt.show()
