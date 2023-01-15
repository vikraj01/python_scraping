import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2019/REG'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find(
    'table', class_="d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}")

# Get headers
headers = [th.text for th in table.find_all('th')]

# Create DataFrame
df = pd.DataFrame(columns=headers)

# Get rows data
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    df.loc[len(df)] = row

df.to_csv(
    'D:\Web_Developement_Base\Python_web_scraping/Nfl_standings_2019_scrapped.csv')
