import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
zline = np.linspace(0, 1, 2)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot(xline, yline, zline, 'gray')
