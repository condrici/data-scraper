import requests
from bs4 import BeautifulSoup


class Price:
    def __init__(self, price_integer: str, price_decimal_point_with_number: str):
        self.price_integer = price_integer
        self.price_decimal_point_with_number = price_decimal_point_with_number

    def get_price_full(self) -> str:
        return self.price_integer + self.price_decimal_point_with_number

    def get_price_integer(self):
        return self.price_integer

    def get_price_decimal_point_with_number(self):
        return self.price_decimal_point_with_number


class PriceScraper:
    def __init__(self, uri):
        self.uri = uri

    def get_price(self) -> Price:
        raw_html = requests.get(self.uri)
        soup_data = BeautifulSoup(raw_html.content, "html.parser")
        price_integer = soup_data.select("p.product-new-price")[0].contents[0].text
        price_decimal_point_with_number = soup_data.select(".product-new-price sup")[0].text
        return Price(price_integer, price_decimal_point_with_number)
