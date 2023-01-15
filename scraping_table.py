# scraping a table is the most common 
# Used to get financial data and sports data , they
# are often in table in web pages , but they are not exportable
# export it into excel files

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')

# Now get all table header
headers = table.find_all('th')
for i in range(0,len(headers)):
    headers[i] = headers[i].text

# Create table's dataframe

df = pd.DataFrame(columns=headers)

# More Cleaner version of doing that 

for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    df.loc[len(df)] = row

df.to_csv('D:\Web_Developement_Base\Python_web_scraping/table_scraped.csv')
















# ********************** My Version Of Extraction ****************#

# * splat operator
# table_rows = []
# List_of_table_rows = [*table.thead.find_all('tr'), *table.tbody.find_all('tr')]
# Inside_row_data_list = []
# for i in range(1,len(List_of_table_rows)):
#     table_data = []
#     for x in List_of_table_rows[i].find_all('td'):
#         table_data.append(x.string)
#     Inside_row_data_list.append(table_data)

# for i in Inside_row_data_list:
#     df.loc[len(df)] = i










