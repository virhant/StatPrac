import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("populations.txt", skiprows = 1, unpack = True).astype(int)
year = data[0]
hare = data[1]
lynx = data[2]
carrot = data[3]

hare_ratio = hare / (hare + lynx)
lynx_ratio = lynx / (hare + lynx)

plt.bar(year, hare_ratio, color = "blue", label = "hare")
plt.bar(year, lynx_ratio, bottom = hare_ratio, color = "red", label = "lynx")

plt.legend(loc = "best")

plt.gca().yaxis.set_ticks(np.arange(0, 1.1, 0.1))

plt.show()