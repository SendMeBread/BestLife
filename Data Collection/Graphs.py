import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
t_s = 2.5
t_a = (((972 - t_s)/712) + ((122 - t_s)/103))/2
x = np.arange(-80, 1, 80)
print("Values of x:", x)
y = x * t_a
plt.plot(x, y)
plt.title("BIBO 3D Print Time Deviation")
plt.xlabel("x")
plt.ylabel("y")
plt.show()