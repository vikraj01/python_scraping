from typing import Container
import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
#print(soup)

# find
# It is the main function that we use to search throughout the 
# html.  we can put tags, attribute Strings, basically everything
# it return what it's matches with the html 

print(soup.find('header'))
div_class = soup.find('div',{'class': 'container test-site' })
print(div_class)
print(soup.find('h4',{"class":"pull-right price"}))

# Class are used frequently
# So we use the following syntax

print(soup.find('h4', class_ = 'pull-right price'))