import matplotlib.pyplot as plt
import numpy as np
import mpld3


vals = np.array([0, 100])
labels = ['Lived', 'Died']
colors = ['#00d', '#c00']
plt.pie(vals, colors=colors)
plt.legend(labels, title="Did they live?")
mpld3.show()
mpld3.save_html(plt.figure(), 'why_not.html')