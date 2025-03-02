from itertools import permutations
import numpy as np
from scipy import stats
import math

def rng(m = 2 ** 32, a = 1103515245, c = 12345):
    rng.current = (a * rng.current + c) % m
    return rng.current / m

rng.current = 1

def order_stat(d):
    sample = np.array(list(rng() for _ in range(500 * d)))
    perm_list = list(permutations(list(range(0, d))))
    obs = [0 for _ in range(math.factorial(d))]
    
    split_sample = np.split(sample, 500)
    
    for i in range(500):
        current_index = perm_list.index(tuple(np.argsort(split_sample[i])))
        obs[current_index] += 1
        
    exp = np.full(math.factorial(d), 500 / math.factorial(d))    
    print(stats.chisquare(obs, exp))
    
order_stat(6)