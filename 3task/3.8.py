import numpy as np
import matplotlib.pyplot as plt

N = 500

theta = np.random.uniform(0, 2 * np.pi, N)  
r = np.sqrt(np.random.uniform(0, 1, N))   

x = r * np.cos(theta)
y = r * np.sin(theta)

fig, ax = plt.subplots(figsize = (16, 9))

circle = plt.Circle((0, 0), 1, color = 'blue', fill = False, linewidth = 2)
ax.add_patch(circle)

ax.scatter(x, y, color='red', s = 5, label = "Сгенерированные точки")

ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.legend(loc = "best")
plt.title("Равномерное распределение точек внутри круга")
plt.show()
