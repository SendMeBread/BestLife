import matplotlib.pyplot as plt
import numpy as np
import mpld3


vals = np.array([0, 100])
labels = ['Lived', 'Died']
colors = ['#00d', '#c00']
plt.figure(facecolor="#000")
plt.axes().set_facecolor("#000")
plt.pie(vals, colors=colors)
legend = plt.legend(labels, title="Did They Live?")
frame = legend.get_frame()
frame.set_facecolor("#000")
frame.set_edgecolor("#f00")
frame.set_alpha(.75)
plt.setp(legend.get_title(), color="#f00")
for text in legend.get_texts():
    text.set_color("#0f0")
mpld3.save_html(plt.figure(), "why.html", template_type="simple")