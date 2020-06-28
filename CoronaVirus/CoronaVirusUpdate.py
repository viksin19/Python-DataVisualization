import requests
from bs4 import BeautifulSoup
import numpy as np
from tabulate import tabulate
import os
import matplotlib.pyplot as plt


def extract_content(row): return [x.text.replace('\n', '') for x in row]


_url = 'https://www.mohfw.gov.in/'
SHORT_HEADERS = ['S.No.', 'Name of State / UT',
                 'Active Cases*', 'Cured/Discharged/Migrated*', 'Deaths**','Total Confirmed cases*']
response = requests.get(_url).content

soup = BeautifulSoup(response, 'html.parser')

header = extract_content(soup.tr.find_all('th'))

statistic = []
total_rows = soup.find_all('tr')

for row in total_rows:
    stats = extract_content(row.find_all('td'))
    if stats:
        if len(stats) == 6:
            stats = ['', *stats]
            statistic.append(stats)
        # elif len(stats) == 0:
        #     statistic.append(stats)


# statistic[-1][0] = len(statistic)
# statistic[-1][1] = "Total cases"print(len(statistic))
corona_table = tabulate(statistic, headers=SHORT_HEADERS)
# print(corona_table)
#Fetching all The States

States = []
for row in statistic:
    States.append(row[2])

y_pos = np.arange(len(States))

Total_Cases = []
for row in statistic[:len(statistic)-1]:
    Total_Cases.append(int(row[3]))
Total_Cases.append(sum(Total_Cases))
plt.barh(y_pos,Total_Cases,align='center', alpha=0.5)
plt.yticks(y_pos,States)
plt.xlim(1,Total_Cases[-1]+100)
plt.xlabel('Total number of cases')
plt.title('Corona Virus Cases in India')
plt.savefig('Corona.png')
