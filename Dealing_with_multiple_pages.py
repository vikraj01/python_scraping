import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.airbnb.co.in/s/Honolulu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&date_picker_type=calendar&checkin=2022-07-22&checkout=2022-07-30&source=structured_search_input_header&search_type=autocomplete_click'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# Part 2

# Getting the next page
# Looping through the page

# page_count = 1
# post_count = 0
Last_page = False

df = pd.DataFrame({'Links': [''], 'Title': [''], 'Price': [
                  ''], 'Description': [''], 'Rating': ['']})

while not Last_page:

    postings = soup.find_all('div', class_='c4mnd7m dir dir-ltr')

    for post in postings:
        link = post.find('a', class_='ln2bl2p dir dir-ltr').get('href')
        full_link = 'https://www.airbnb.co.in/' + link
        title = post.find('div', class_='t1jojoys dir dir-ltr').text
        description = post.find(
            'div', class_='n1v28t5c s1cjsi4j dir dir-ltr').text
        price = post.find_all('span', class_='a8jt5op dir dir-ltr')
        price_per_night = price[0].text
        total_price = price[1].text

        complete_price = price_per_night + ' ' + total_price

        ratings = post.find(
            'span', class_='t5eq1io r4a59j5 dir dir-ltr').get('aria-label')

        df = df.append({'Links': full_link, 'Title': title, 'Price': complete_price, 'Description': description, 'Rating': ratings})
        # post_count += 1

        # print(f'The count is {post_count}' +   '\nThe Link is : ' + full_link + '\nTitle is : ' + title + '\nDescription is ' + description
        # + '\nPrice per night is ' + price_per_night + '\nTotal price is ' + total_price
        # + '\nThe rating is ' + ratings + '\n\n')

    # print(f'The page count is {page_count}')

    if not soup.find('a', {'aria-label': 'Next'}):
        Last_page = True
    else:
        next_page = soup.find('a', {'aria-label': 'Next'}).get('href')
        next_page_full = 'https://www.airbnb.co.in/' + next_page
        url = next_page_full
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        # page_count += 1

# print(page_count, post_count)
