import requests
from bs4 import BeautifulSoup
import lxml

# function for permorming a Beautiful Soup web Scrape
def popnews():
    url = "https://hotstuff4geeks.com/funko-pop-news/"
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/95.0.4638.54 Safari/537.36",
        "Accept-Language": "en",
    }

    r = requests.get(url, headers=headers)
    # variable for using the BeautifulSoup and lxml python library.
    soup = BeautifulSoup(r.text, "lxml")
    pop_news = soup.find_all('article')
    for news in pop_news:
        # scraping the <h2> tag and classes: elementor-post__title, elementor-pose-date, href links from each article
        # that is shown above in the pop_news variable.
        names_pop = news.find('h2', class_='elementor-post__title').text
        date_pop = news.find(class_='elementor-post-date').text
        info_pop = news.a['href']
        print(names_pop.strip() if names_pop is not None else '')
        print(date_pop.strip())
        print(info_pop)
        print(' ')

popnews()