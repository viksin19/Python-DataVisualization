import numpy as np
import matplotlib.pyplot as pyplot

x = np.random.randn(1000)   #It will generate 1-D array with 1000 floating points numbers
pyplot.hist(x,200)   # Histogram with 200 rectangles attached to each other.
pyplot.title(r'Normal Distribution $\mu = 0, \sigma=1$')    #Setting the title of histogram.
pyplot.show()    # Ploting and displaying Histogram


# It will generate 2-D array of 3X4 with random floating pointing number.
#print(np.random.randn(3,4)) 