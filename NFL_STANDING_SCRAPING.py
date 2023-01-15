import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2019/REG'
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

table = soup.find('table')
headers = [th.text for th in table.find_all('th')]
df = pd.DataFrame(columns=headers)


for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [k.text for k in row_data]
    df.loc[len(df)] = row

df.to_csv('D:\Web_Developement_Base\Python_web_scraping\Practise_Beautiful_soup/Nfl_standings_2019_scrapped.csv')


