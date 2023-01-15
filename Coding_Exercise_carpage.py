from numpy import true_divide
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')


df = pd.DataFrame({'Link': [''], 'Name': [''], 'Price': [''], 'Color': ['']})


for i in range(15):

    posting = soup.find_all('div', class_='media soft push-none rule')

    for post in posting:
        try:
            link = 'https://www.carpages.ca/' + post.find('h4', class_='hN').find('a').get('href')
            name = post.find('h4', class_='hN').find('a').text
            price = post.find('strong', class_='delta').text.strip()
            color = post.find_all('div', class_='grey l-column l-column--small-6 l-column--medium-4')[1].find('span').text.strip()
            
            df2 = pd.DataFrame({'Link': [link], 'Name': [name], 'Price': [price], 'Color': [color]})
            df = pd.concat([df, df2], ignore_index = True, axis = 0)
        except:
            pass

    if soup.find('a', {'title':'Next Page'}):
        next_page = 'https://www.carpages.ca/' + soup.find('a', {'title':'Next Page'}).get('href')
        page = requests.get(next_page)
        soup = BeautifulSoup(page.text, 'lxml')
    else:
        break

df.to_csv(
    'D:\Web_Developement_Base\Python_web_scraping/used_car.csv')




# Scrape through multiple pages
# get the link of each posting
# get the name of each car
# get the price of the car
# get the color of each car
# put all the data into a table
# do this for the first 10 to 15 pages

