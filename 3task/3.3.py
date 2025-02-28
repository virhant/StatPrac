import numpy as np
from scipy import stats

def rng_bad(m = 2 ** 31, a = 65539, c = 0):
    rng_bad.current = (a * rng_bad.current + c) % m
    return rng_bad.current / m

rng_bad.current = 1

arr = np.array(list(rng_bad() for _ in range(1000)))
ser_arr = arr.reshape(-1, 2)

k = 20
hist = np.histogram2d(ser_arr[:, 0], ser_arr[:, 1], bins = [np.linspace(0 , 1, k + 1), np.linspace(0 , 1, k + 1)])[0]
obs = hist.flatten()
exp = np.full_like(obs, obs.sum() / (k ** 2))

print(stats.chisquare(obs, exp))