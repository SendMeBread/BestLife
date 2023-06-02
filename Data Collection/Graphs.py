import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
x1 = np.linspace(0, 85, 85)
y1 = -(1945/37584)*x1**2 + (1/.58)*x1 + 5
x2 = np.linspace(0, 85, 85)
y2 = -(2595/69629)*x2**2 + (1/.58)*x2 + 5
x3 = np.linspace(0, 85, 85)
y3 = -(3345/118784)*x3**2 + (1/.58)*x3 + 5
x4 = np.linspace(0, 85, 85)
y4 = -(1495/21141)*x4**2 + (1/.58)*x4 + 5
x5 = np.linspace(0, 85, 85)
y5 = -(479/11745)*x5**2 + (1/.58)*x5 + 5

plt.plot(x1, y1, "r", x2, y2, "g", x3, y3, "b", x4, y4, "y", x5, y5, "k")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()