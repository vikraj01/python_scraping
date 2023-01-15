from cgi import print_exception
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.demoblaze.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({'Link':[''],'Name':[''], 'Image-link':[''],'Price':[''],'Description':['']})

Posts = soup.find_all('div',class_ = 'col-lg-4 col-md-6 mb-4')

print(Posts)
for post in Posts:
    link = post.find('a',class_='hrefch').get('href')
    name = post.find('a',class_='hrefch').text
    image = post.find('img',class_='card-img-top img-fluid').get('src')
    price = post.find('h5').text
    description = post.find('p',id='article').text

    print(link,name,image,price,description)

    df2 = pd.DataFrame({'Link':[link],'Name':[name], 'Image-link':[image],'Price':[price],'Description':[description]})
    df = pd.concat([df,df2],ignore_index=True,axis=0)


# print(df)