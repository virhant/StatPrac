import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("populations.txt", skiprows = 1, unpack = True).astype(int)
year = data[0]
hare = data[1]
lynx = data[2]
carrot = data[3]

X_t = np.vstack((np.ones(20), lynx[0:20], carrot[0:20]))
beta = np.linalg.inv(X_t @ X_t.T) @ X_t @ hare[0:20]

estimate_hare_1920 = (np.vstack((1, lynx[20], carrot[20]))).T @ beta
error_est = abs((estimate_hare_1920 - hare[20]) / hare[20])
print(f"Estimate is {estimate_hare_1920}, real value is {hare[20]}. Error is {error_est}")