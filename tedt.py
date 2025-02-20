import matplotlib.pyplot as plt
import numpy as np

f1 = lambda x: 2 * np.sin(x) - np.cos(2 * x)
f2 = lambda x: 2 * np.cos(x) + 2 * np.sin(2 * x)

px = -2.4
py = f1(px)

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
x[0] = -2 * np.pi
x[-1] = 2 * np.pi
y1 = f1(x)
y2 = f2(x)

plt.figure(figsize=(10, 5))

plt.plot(x, y1, "b-", label = "f(x) = 2sin(x) - cos(2x)")
plt.plot(x, y2, "r--", label = "f'(x) = 2cos(x) + 2sin(2x)")
plt.plot(px, py, "ko", zorder = 3)

plt.plot([px - 1.2, px + 1.2], [f2(px) * (-1.2) + py, f2(px) * 1.2 + py], "g-", label = f"Tangent at x = {px}")
plt.plot([px, px, 0], [0, py, py], color = "purple", linestyle = "--", alpha = 0.5)
plt.annotate(f"f({px}) = {py:.1f}", xy = (px, py), xytext = (px + 0.8, py - 2), color = "black", arrowprops = {"arrowstyle" : "->", "connectionstyle" : "arc3, rad = 0.2"})

plt.legend(loc = "best")
plt.axhline(0, color = 'black', linewidth = 1)
plt.axvline(0, color = 'black', linewidth = 1)
plt.xlim(-2 * np.pi, 2 * np.pi)
plt.grid(True)

plt.show()