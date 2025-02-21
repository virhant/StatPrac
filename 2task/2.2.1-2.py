import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("populations.txt", skiprows = 1, unpack = True).astype(int)
year = data[0]
hare = data[1]
lynx = data[2]
carrot = data[3]

max_p = np.max(data[1:], axis = 1)
max_index = np.argmax(data[1:], axis = 1)
max_y = data[0][max_index]

plt.figure(figsize = (16, 9))

plt.plot(year, hare, "b-", label = "hare population")
plt.plot(year, lynx, "r-", label = "lynx population")
plt.plot(year, carrot, "orange", label = "carrot yield")

plt.plot(max_y, max_p, "o", color = "black")
list(map(lambda px, py: plt.text(px, py + 1000, f"{px} year, {py} population", ha = "left", size = 9, weight = "heavy"), max_y, max_p))

plt.legend(loc = "best", fontsize = 14)
plt.xlabel("year", fontweight = "bold", fontsize = 14)
plt.ylabel("population", fontweight = "bold", fontsize = 14)

plt.minorticks_on()
plt.gca().xaxis.set_ticks(np.arange(1900, 1921, 4))
plt.grid(True)