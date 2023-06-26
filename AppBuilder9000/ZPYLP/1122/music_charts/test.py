import requests
from bs4 import BeautifulSoup as bs
import time

from django.shortcuts import render


def hot_one_hundred(request):
    URL = 'https://www.billboard.com/charts/hot-100'
    response = requests.get(URL)
    soup = bs(response.content, 'html.parser')
    song_data = soup.findAll('li', attrs={"class": 'chart-list__element display--flex'})

    for store in song_data:
        number = store.button.span.span.text
        title = store.button.find('span', class_='chart-element__information')
        title2 = title.find('span', class_='chart-element__information__song text--truncate color--primary').text
        artist = title.find('span', class_='chart-element__information__artist text--truncate color--secondary').text

        return print(title2)
