from tokenize import String
import requests
import re
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

#find all
price_list = soup.findAll('h4', class_ = 'pull-right price')
for x in price_list:
    print(x.string)

title_list = soup.find_all('a', class_ = 'title')
for x in title_list:
    print(x.string)

reviews_list = soup.find_all('p',class_ = 'pull-right')[6:]
for x in reviews_list:
    print(x.string)

# find_all part 2
# Get more than one tag at a time

two_tag_list = soup.find_all(['h4','p'])
for x in two_tag_list:
    print(x)
for x in two_tag_list:
    print(x.string)
for x in two_tag_list:
    print(x.attrs)

# Filter based on boolean 

tag_with_id_list = soup.find_all(id = True)
for x in tag_with_id_list:
    print(x)

for x in tag_with_id_list:
    print(x.attrs['id'])

# Filtering based on string
tag_with_iphone_string_list = soup.find_all(string = 'Iphone')
for x in tag_with_iphone_string_list:
    print(x)
print(tag_with_iphone_string_list)
# Filtering based on re . compile  on string( most powerful )
string_re = soup.find_all(string=re.compile('Iph'))
print(string_re)
string_re1 = soup.find_all(string=re.compile('Nok'))
print(string_re1)

# Filtering based on re . compile on attributes ( most powerful )

class_name_list_with_pull = soup.find_all(class_ = re.compile('pull'))
print(class_name_list_with_pull)


class_name_list_with_pull_inside_ptag = soup.find_all('p', class_ = re.compile('pull') )
print(class_name_list_with_pull_inside_ptag)


class_name_list_with_pull_inside_ptag_with_limit = soup.find_all('p', class_ = re.compile('pull'), limit=3 )
print(class_name_list_with_pull_inside_ptag_with_limit)

# string on the list

Nokia_iphone_both_list = soup.find_all(string = [re.compile('Iph'), re.compile('Nok')])
print(Nokia_iphone_both_list)