import requests
from bs4 import BeautifulSoup

class Amazon:
    def __init__(self, url, headers):
        self.price = 0
        self.url = url
        self.headers = headers
        self.soup = self.get_amazon_data()

    def get_amazon_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        amazon_data = response.text
        return BeautifulSoup(amazon_data, "html.parser")

    def get_amazon_price(self):
        price = self.soup.find(name="span", class_="a-offscreen")
        return float(price.get_text().split("$")[1])

    def get_product_title(self):
        title = self.soup.find(name="span", class_="a-size-large product-title-word-break")
        return title.get_text()
