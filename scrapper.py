#########       BASICS OF HTML      ##########

import requests
from bs4 import BeautifulSoup


url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
#print(soup)


#tags
#print(soup.header)


#navigable Strings
# is just a string corresponding to a text within a tag

tag = soup.header.p
tag_stringified = tag.string
print(tag_stringified)

# Attributes
tag = soup.header.a
print(tag.attrs)
print(tag['data-toggle'])

# Added a new attributes
tag['new_attribute'] = 'This is the new attributes'
print(tag.attrs)

# Comment
# Comment is just a special type of navigable string just displayed with special formatting
 


'''
There's three way to make soup :
soup = BeautifulSoup(page.text, 'html.parser')
soup = BeautifulSoup(page.text, 'lxml')
soup = BeautifulSoup(page.text, features='xml')
'''

