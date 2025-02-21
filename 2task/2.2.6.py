import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("populations.txt", skiprows = 1, unpack = True).astype(int)
year = data[0]
hare = data[1]
lynx = data[2]
carrot = data[3]

print("The correlation between the populations of hares and lynxes is ", np.round(np.corrcoef(hare, lynx)[0, 1], decimals = 3))

plt.figure(figsize = (16, 9))

plt.plot(year[1:], hare[1:] - hare[0:-1], "b-", label = "Hare change")
plt.plot(year[1:], lynx[1:] - lynx[0:-1], "r-", label = "Lynx change")

plt.legend(loc = "best", fontsize = 14)

plt.minorticks_on()
plt.gca().xaxis.set_ticks(np.arange(1900, 1921, 4))

plt.grid(True)

plt.show()