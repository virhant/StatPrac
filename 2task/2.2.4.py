import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("populations.txt", skiprows = 1, unpack = True).astype(int)
year = data[0]
hare = data[1]
lynx = data[2]
carrot = data[3]

expected_values = np.round(np.mean([hare, lynx, carrot], axis = 1), decimals = 2)
standar_deviations = np.round(np.std([hare, lynx, carrot], axis = 1), decimals = 2)

list(map(lambda x, y, z: print(f"{x}: ", f"{y}, " ,z), ["ev and std of hare is", "ev and std of lynx is", "ev and std of carrot is"], expected_values, standar_deviations))

plt.figure(1, figsize = (16, 9))

plt.subplot(131)
plt.hist(hare, bins = np.histogram_bin_edges(hare, bins = "fd"), color = "blue", density = True)
plt.axvline(expected_values[0], color = 'black')
# plt.axvline(standar_deviations[0] + expected_values[0], color = 'black')
# plt.axvline(- standar_deviations[0] + expected_values[0], color = 'black')
plt.title("Hare", weight = "bold")

plt.subplot(132)
plt.hist(lynx, bins = np.histogram_bin_edges(lynx, bins = "fd"), color = "red", density = True)
plt.axvline(expected_values[1], color = 'black')
# plt.axvline(standar_deviations[1] + expected_values[1], color = 'black')
# plt.axvline(- standar_deviations[1] + expected_values[1], color = 'black')
plt.title("Lynx", weight = "bold")

plt.subplot(133)
plt.hist(carrot, bins = np.histogram_bin_edges(carrot, bins = "fd"), color = "orange", density = True)
plt.axvline(expected_values[2], color = 'black')
# plt.axvline(standar_deviations[2] + expected_values[2], color = 'black')
# plt.axvline(- standar_deviations[2] + expected_values[2], color = 'black')
plt.title("Carrot", weight = "bold")

plt.show()