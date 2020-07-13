import pandas as pd 
import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 

path = '/Users/VikramSingh/Pictures/Python-DataVisualization/DataVisualizationFile.xlsx'

data_frame = pd.read_excel(path)
data_frame.rename(columns={'OdName':'Country'},inplace=True)
data_frame.set_index('Country',inplace=True)
years = list(map(int, range(1980,2014)))

data_frame['Total'] = data_frame.sum(axis=1)
data_frame.sort_values(['Total'],ascending=False,axis=0,inplace=True)

top5 = data_frame.head()
top5 = top5[years].transpose()
print(top5)

top5.plot(kind='area')
plt.title('Immigrants trend of top 5 countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Year')

plt.show()