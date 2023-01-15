import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://trends.builtwith.com/websitelist/DataTables'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table')
headers = [header.text for header in table.find_all('th')][1:-1]
df = pd.DataFrame(columns=headers)

for table_row in table.find_all('tr')[1:-1]:
    row = []
    for table_data in table_row.find_all('td')[1:-1]:
        if(table_data.text):
            row.append(table_data.text)
        else:
            row.append('NULL')
    df.loc[len(df)] = row

df.to_csv("D:\Web_Developement_Base\Python_web_scraping\Practise_Beautiful_soup/table.csv")
