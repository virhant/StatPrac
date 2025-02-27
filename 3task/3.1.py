import numpy as np
from scipy import stats

def rng(m = 2 ** 32, a = 1103515245, c = 12345):
    rng.current = (a * rng.current + c) % m
    return rng.current / m

rng.current = 1

arr = np.array(list(rng() for _ in range(1000)))
ser_arr = arr.reshape(-1, 2)

k = 20
hist = np.histogram2d(ser_arr[:, 0], ser_arr[:, 1], bins = [np.linspace(0 , 1, k + 1), np.linspace(0 , 1, k + 1)])[0]
obs = hist.flatten()
exp = np.full_like(obs, obs.sum() / (k ** 2))

print(stats.chisquare(obs, exp))