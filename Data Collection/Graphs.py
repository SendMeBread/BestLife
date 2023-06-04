import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
from mpl_toolkits import mplot3d
qx1 = np.linspace(0, 85, 85)
qy1 = -(1945/37584)*qx1**2 + (1/.58)*qx1 + 5
qx2 = np.linspace(0, 85, 85)
qy2 = -(2595/69629)*qx2**2 + (1/.58)*qx2 + 5
qx3 = np.linspace(0, 85, 85)
qy3 = -(3345/118784)*qx3**2 + (1/.58)*qx3 + 5
qx4 = np.linspace(0, 85, 85)
qy4 = -(1495/21141)*qx4**2 + (1/.58)*qx4 + 5
qx5 = np.linspace(0, 85, 85)
qy5 = -(479/11745)*qx5**2 + (1/.58)*qx5 + 5

lx1 = np.linspace(0,85,85)
ly1 = 2*lx1



xtick_list = []
ytick_list = []
for i in range(11):
    xtick_list.append(i * 10)
    ytick_list.append(i * 5.5)
fig, axs = plt.subplots(2)
axs[0].plot(qx1, qy1, "r", qx2, qy2, "g", qx3, qy3, "b", qx4, qy4, "y", qx5, qy5, "k")
axs[1].plot(lx1, ly1)
for ax in axs.flat:
    if ax == axs[0]:
        ytick_list.remove(5.5)
        ytick_list.append(5)
    if ax == axs[1:]:
        ytick_list.remove(5)
        ytick_list.append(5.5)
    ax.set_ylim(bottom=0, top=55)
    ax.set_xlim(left=0, right=100)
    ax.set_xticks(xtick_list)
    ax.set_yticks(ytick_list)
plt.show()