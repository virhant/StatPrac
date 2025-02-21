import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("populations.txt", skiprows = 1, unpack = True).astype(int)
year = data[0]
hare = data[1]
lynx = data[2]
carrot = data[3]

plt.scatter(hare, lynx, c = year, cmap = "seismic", marker = "o")

plt.xlabel("Hare", weight = "bold")
plt.ylabel("Lynx", weight = "bold")

plt.show()