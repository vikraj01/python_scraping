import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# find_all 3
# product_name = soup.findAll(class_ = re.compile('title'))
product_name = soup.find_all('a', class_='title')

# price = soup.find_all('h4', class_ = 'pull-right price')
prices = soup.find_all('h4', class_=re.compile('pull'))

reviews = soup.find_all('p', class_=re.compile('pull'))

descriptions = soup.find_all('p', class_='description')


product_name_list = []
for i in product_name:
    name = i.text
    product_name_list.append(name)

price_list = []
for i in prices:
    price = i.text
    price_list.append(price)


review_list = []
for i in reviews:
    review = i.text
    review_list.append(review)

description_list = []
for i in descriptions:
    description = i.text
    description_list.append(description)

table = pd.DataFrame({'Product Name': product_name_list,
                     'Description': description_list, 'Price': price_list, 'Review': review_list})

print(table)

# Extracting data from nested HTML tags
# Reducing html to more simpler chunks and then extract the data 

boxes = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')[2]
print(boxes.find('a').text)
print(boxes.find('p', class_ = 'description').string)


box2 = soup.find_all('ul', class_ = 'nav', id = 'side-menu')[0]
print(box2.find_all('li')[1].text)

