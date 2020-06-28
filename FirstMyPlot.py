from matplotlib.backends.backend_agg import FigureCanvasAgg as FigCan
from matplotlib.figure import Figure

import numpy as np

fig = Figure()
canvas = FigCan(fig)

x = np.random.randn(1000)
ax = fig.add_subplot(111)

ax.hist(x, 100)
ax.set_title(r'Normal distribution with $\mu = 0, \sigma = 1$')
fig.savefig('FirstHistogram.png')

