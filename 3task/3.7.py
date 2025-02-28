import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

A = np.array([1, 2])
B = np.array([2, 6])
C = np.array([8, 1])

N = 500

u = np.random.uniform(0, 1, N)
v = np.random.uniform(0, 1, N)

swap = u + v > 1
u[swap] = 1 - u[swap] # Прикольная штука
v[swap] = 1 - v[swap]

points = (1 - u - v)[:, np.newaxis] * A + u[:, np.newaxis] * B + v[:, np.newaxis] * C

fig, ax = plt.subplots(figsize=(16,9))

triangle = Polygon([A, B, C], closed=True, edgecolor='black', facecolor='lightblue', alpha=0.5)
ax.add_patch(triangle)

ax.scatter(points[:, 0], points[:, 1], color='red', s=5, label="Сгенерированные точки")

ax.set_xlim(min(A[0], B[0], C[0]) - 1, max(A[0], B[0], C[0]) + 1)
ax.set_ylim(min(A[1], B[1], C[1]) - 1, max(A[1], B[1], C[1]) + 1)
ax.set_aspect('equal')
ax.legend()
plt.title("Равномерное распределение точек в треугольнике")
plt.show()