import numpy as np
import pywt
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 1000)
spike = np.sin(2 * np.pi * x)
spike[0:300] = 0
spike[500:-1] = 0
y1 = np.sin(np.pi * x)  + spike
y = y1



scales = np.exp(np.linspace(np.log(1e-1), np.log(100), 100))
coef, freqs = pywt.cwt(y, scales, 'gaus1', sampling_period = 100/1000)
print(freqs)

plt.figure()
plt.plot(x, y)

plt.figure()
plt.imshow(abs(coef), interpolation="bilinear",
        extent=[x[0], x[-1], freqs[-1], freqs[0]], 
        aspect=1)
plt.show()
