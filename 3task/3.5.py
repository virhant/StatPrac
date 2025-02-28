import numpy as np
import matplotlib.pyplot as plt

def rng(m = 2 ** 32, a = 1103515245, c = 12345):
    rng.current = (a * rng.current + c) % m
    return rng.current / m

rng.current = 1

sample = np.array(list(rng() for _ in range(1000))) # Имеет равномерное распределение на отрезке [0, 1]

ex_sample = -np.log(1 - sample) # Будем считать, что lambda = 1

x = np.linspace(0, 8, 100)

plt.figure(figsize = (16, 9))

plt.subplot(121)
plt.hist(ex_sample, bins = np.histogram_bin_edges(ex_sample, bins = "fd"), alpha = 0.7, density = True, label = "Sample's density")
plt.plot(x, np.exp(-x), "r-", label = "Exp density")
plt.title("Freedman-Diaconis rule")
plt.legend(loc = "best")


plt.subplot(122)
plt.hist(ex_sample, bins = np.histogram_bin_edges(ex_sample, bins = "rice"), alpha = 0.7, density = True, label = "Sample's density")
plt.plot(x, np.exp(-x), "r-", label = "Exp density")
plt.title("Rice rule")
plt.legend(loc = "best")

plt.show()