import matplotlib.pyplot as plt
import numpy as np

vals = np.array([0, 100])
labels = ['Lived', 'Died']
colors = ['#00d', '#c00']
plt.pie(vals, colors=colors)
plt.legend(labels, title="Did they live?")
plt