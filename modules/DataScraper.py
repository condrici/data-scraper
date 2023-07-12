import requests
from bs4 import BeautifulSoup
import re


class Price:
    format_comma_decimal_dot_thousands: str = "comma_decimal_dot_thousands"

    __regex_comma_decimal_dot_thousands: str = "^[0-9]{1,3}([.]{1}[0-9]{3})*([,]{1}[0-9]+){0,1}$"
    __whole_number: int
    __decimal_number: int | None
    __decimal_separator: str = ','

    def __init__(self, price: str, price_format: str):
        if price_format != self.format_comma_decimal_dot_thousands:
            raise Exception("Unknown or unsupported price format")

        if not re.search(self.__regex_comma_decimal_dot_thousands, price):
            raise ValueError("Price doesn't have expected format format_comma_decimal_dot_thousands")

        decimal_number = price.split(",")[-1]

        self.__whole_number = int(price.split(',')[0])
        self.__decimal_number = int(decimal_number) if decimal_number.isnumeric() else None

    # Type string is returned because decimal separator is a comma
    def get_price_whole_with_decimal(self) -> str:
        if isinstance(self.__decimal_number, int):
            return str(self.__whole_number) + self.__decimal_separator + str(self.__decimal_number)

        return str(self.__whole_number)

    def get_price_whole(self) -> int:
        return self.__whole_number


class PriceScraper:
    algorithm_emag_product_page = 'emag_product_page'

    def __init__(self, uri):
        self.uri = uri

    def scrape(self, scrape_algorithm) -> Price:
        if scrape_algorithm != self.algorithm_emag_product_page:
            raise ValueError('Unknown algorithm used')

        return self.__scrape_emag_product_page()

    def __scrape_emag_product_page(self) -> Price:
        raw_html = requests.get(self.uri)
        soup_data = BeautifulSoup(raw_html.content, "html.parser")
        price_string = \
            soup_data.select("p.product-new-price")[0].contents[0].text + \
            soup_data.select(".product-new-price sup")[0].text

        return Price(price_string, Price.format_comma_decimal_dot_thousands)
