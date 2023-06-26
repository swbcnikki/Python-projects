from bs4 import BeautifulSoup
from urllib.request import urlopen


def web_scrape():
    Chessbase_url = "https://shop.chessbase.com/en/openings/spanish_open"
    page = urlopen(Chessbase_url)
    html = page.read().decode("utf-8")

    soup = BeautifulSoup(html, 'html.parser')
    # selects the div tag which has the paragraph im targeting
    tag = soup.find(class_="col-xs-12 col-sm-8 body")

    print(str(tag.p.string))
    # returns the paragraph of the div tag that i targeted
    return str(tag.p.string)


if __name__ == "__main__":
    web_scrape()
