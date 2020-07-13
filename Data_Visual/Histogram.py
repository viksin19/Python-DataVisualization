import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


path = '/Users/VikramSingh/Pictures/Python-DataVisualization/DataVisualizationFile.xlsx' #File Location which we want to use for Data Visualization

# Preparing data frame for Histogram
data_frame = pd.read_excel(path)
data_frame.rename(columns={'OdName':'Country'}, inplace=True)
data_frame.set_index('Country',inplace=True)
data_frame['Total'] = data_frame.sum(axis=1)

count , edges = np.histogram(data_frame[2013])

data_frame[2013].plot(kind='hist',xticks=edges)
plt.title('Histogram of Immigrants in 2013')
plt.ylabel('No. of Countries')
plt.xlabel('No. of immigrants')

plt.show()