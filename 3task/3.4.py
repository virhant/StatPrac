import numpy as np
import matplotlib.pyplot as plt

def rng(m = 2 ** 32, a = 1103515245, c = 12345):
    rng.current = (a * rng.current + c) % m
    return rng.current / m

rng.current = 1

#weights = np.random.dirichlet(np.ones(10)) # В примере указаные неправильные веса, так как их сумма не равна единице
future_weights = list(rng() for _ in range(10))
weights = np.array(future_weights) / sum(future_weights)
digits = np.arange(10)

sort_index = np.argsort(weights)

#np.random.seed(1) # Чтобы график не менялся при каждом запуске
sample = np.random.choice(digits[sort_index], size = 1000, p = weights[sort_index])

plt.hist(sample, bins = np.arange(-0.5, 10.5, 1), alpha = 0.7)

plt.ylabel("Frequency")
plt.xlabel("Digits")
plt.show()

print(weights)
print(digits[sort_index])
print(sum(weights))