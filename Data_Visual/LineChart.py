import pandas as pd 
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plot 

path = '/Users/VikramSingh/Pictures/Python-DataVisualization/DataVisualizationFile.xlsx' #File Location which we want to use for Data Visualization

data_Frame = pd.read_excel(path)  # Reading excel File
# print(data_Frame.head())       # Print first 5 records.
mpl.style.use(['ggplot'])
years = list(map(int,range(1980,2014)))
data_Frame.rename(columns={'OdName':'Country'},inplace=True)
data_Frame.set_index('Country', inplace=True)   #Setting country as index
print("Index is Set")
Haiti = data_Frame.loc['Haiti',years]
Haiti.index = Haiti.index.map(int)
# print(Haiti)
# Line Chart
Haiti.plot(kind='line')
plot.title('Immigrants from Haiti')
plot.ylabel('Number of immigrants')
plot.xlabel('Years')

plot.show()
