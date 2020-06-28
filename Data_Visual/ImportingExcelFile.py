import pandas as pd 
import numpy as np
from openpyxl import Workbook

df_can = pd.read_excel('https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)        #Fetching file from server

# df_can.to_excel('DataVisualizationFile.xlsx')
# df_can.to_csv('DataVisualization.csv')
                       