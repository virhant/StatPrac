import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("populations.txt", skiprows = 1, unpack = True).astype(int)
year = data[0]
hare = data[1]
lynx = data[2]
carrot = data[3]

top_every_year = []

def top(x, y, arr):
    if x > y:
        arr.append("H")
        return
    arr.append("L")
    return
    
list(map(lambda x, y: top(x, y, top_every_year), hare, lynx))
print(top_every_year)

plt.pie([top_every_year.count("H"), top_every_year.count("L")], labels = ["Hare", "Lynx"], autopct = "%1.1f%%", colors = [(0, 0, 1, 0.5), (1, 0, 0, 0.5)])

plt.show()