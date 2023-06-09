import matplotlib.pyplot as plt
import numpy as np

vals = np.array([0, 100])
labels = ['Lived', 'Died']
colors = ['#00d', '#c00']

def plot():
    fig, ax = plt.subplots()
    ax.pie(vals, colors=colors)
    ax.legend(labels title="Did They Live?")
    display(fig, target="graph-area", append=False)

plot()