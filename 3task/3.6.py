import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import random

def rng(m = 2 ** 32, a = 1103515245, c = 12345, seed = 1):
    rng.current = seed
    while True:
        rng.current = (a * rng.current + c) % m
        yield rng.current / m

def f(x):
    return (np.exp(x) * (np.cos(x) ** 2))

integral = quad(f, -np.pi / 2, np.pi / 2)[0]

def f_density(x):
    return f(x) / integral

counter = 0
sample = []
random_gen = rng()
while counter < 1000: # Можно поставить 10000, тогда будет еще точнее
    current = -np.pi / 2 + next(random_gen) * np.pi  # Переносим [0,1] -> [-π/2, π/2]
    if random.uniform(0, 10 / np.pi) <= f_density(current):
        sample.append(current) 
        counter += 1
        
plt.figure(figsize = (16, 9))

point = np.linspace(-np.pi / 2, np.pi / 2, 1000)

plt.subplot(121)
plt.hist(sample, bins = np.histogram_bin_edges(sample, bins = "fd"), alpha = 0.7, density = True, label = "Sample's density")
plt.plot(point, f_density(point), "r-", label = "Exp density")
plt.title("Freedman-Diaconis rule")
plt.legend(loc = "best")


plt.subplot(122)
plt.hist(sample, bins = np.histogram_bin_edges(sample, bins = "rice"), alpha = 0.7, density = True, label = "Sample's density")
plt.plot(point, f_density(point), "r-", label = "Exp density")
plt.title("Rice rule")
plt.legend(loc = "best")

plt.show()