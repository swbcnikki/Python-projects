from django.test import TestCase

# Create your tests here.
import requests
from bs4 import BeautifulSoup
# get result from webpage
result = requests.get("https://www.mintstategold.com/canadian-gold-1oz-2021-maple-leaf-bu-18997.html")

#
src = result.content
soup = BeautifulSoup(src, 'html.parser')

# print(soup.prettify())
item = soup.find('div', class_="price-box instock price-final_price")
get_item = str(item.span.findChild("meta"))
get_item = get_item.split('"')[1]
get_item = '$' + get_item

print(get_item)
