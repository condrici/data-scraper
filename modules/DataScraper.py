"""
Data Scraping functionality
It sends an HTTP request, retrieves the HTML data and uses an algorithm to extract the price from it
"""

import re

import requests
from bs4 import BeautifulSoup
from marshmallow_jsonapi import Schema, fields


class PriceSchema(Schema):
    id = fields.Str(dump_only=True)
    price = fields.Str()

    class Meta:
        type_ = "price"

    def create(self):
        return self


class Price:
    FORMAT_COMMA_DECIMAL_DOT_THOUSANDS: str = "comma_decimal_dot_thousands"

    __regex_comma_decimal_dot_thousands: str = "^[0-9]{1,3}([.]{1}[0-9]{3})*([,]{1}[0-9]+){0,1}$"
    __whole_number: int                 # Example: 100, 100.000
    __decimal_number: int | None        # Example: 20 (in 100,20), (in 100.000,30)
    __decimal_separator: str = ','      # The decimal separator is used to return data consistently

    def __init__(self, price: str, price_format: str):
        if price_format != self.FORMAT_COMMA_DECIMAL_DOT_THOUSANDS:
            raise ValueError("Unknown or unsupported price format")

        if not re.search(self.__regex_comma_decimal_dot_thousands, price):
            raise ValueError("Price doesn't have expected format format_comma_decimal_dot_thousands")

        decimal_number = price.split(",")[-1]

        self.__whole_number = int(price.split(',')[0])
        self.__decimal_number = int(decimal_number) if decimal_number.isnumeric() else None

    def get_price(self) -> PriceSchema:
        price_schema = PriceSchema()

        if isinstance(self.__decimal_number, int):
            price_schema.price = str(self.__whole_number) + self.__decimal_separator + str(self.__decimal_number)
        else:
            price_schema.price = self.__whole_number

        return price_schema


class PriceScraper:
    algorithm_emag_product_page = 'emag_product_page'

    def __init__(self, uri):
        self.uri = uri

    """Initiate scraping and determine which algorithm has to be used"""

    def scrape(self, scrape_algorithm) -> Price:
        if scrape_algorithm != self.algorithm_emag_product_page:
            raise ValueError('Unknown algorithm used')

        return self.__scrape_emag_product_page()

    """Send request to website and extract price from retrieved HTML data"""

    def __scrape_emag_product_page(self) -> Price:
        raw_html = requests.get(self.uri)
        soup_data = BeautifulSoup(raw_html.content, "html.parser")
        price_string = \
            soup_data.select("p.product-new-price")[0].contents[0].text + \
            soup_data.select(".product-new-price sup")[0].text

        return Price(price_string, Price.FORMAT_COMMA_DECIMAL_DOT_THOUSANDS)
