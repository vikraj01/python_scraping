import random
import requests
from bs4 import BeautifulSoup


url_list = ['https://www.marketwatch.com/investing/stock/msft?mod=search_symbol',
'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol',
'https://www.marketwatch.com/investing/stock/tsla?mod=search_symbol']




def get_stock_details(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    opening_price = soup.find('bg-quote', class_='value').string
    closing_price = soup.find('td', class_='table__cell u-semi').string


    range_price = soup.find_all('div', class_='range__header')[2]
    week_range_52 = range_price.find_all('span', class_='primary')
    for i in (0, len(week_range_52)-1):
        week_range_52[i] = week_range_52[i].string

    
    analyst_rating = soup.find('li', class_='analyst__option active').string
    print(f"The opening price of the {soup.find('h1',class_ = 'company__name').string} is " + opening_price + "\nThe closing price is " + closing_price +
        "\nThe range is " + week_range_52[0] + " to " + week_range_52[1] + "\nAnalyst rating of the stock is " + analyst_rating)



for x in url_list:
    get_stock_details(x)
    print('\n\n')
        

