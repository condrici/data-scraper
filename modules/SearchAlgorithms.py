from abc import abstractmethod

import requests
from bs4 import BeautifulSoup

from modules.PriceFormats import CommaDecimalsDotThousandsPriceFormat
from modules.Schema import PriceSchema


class SearchAlgorithm:

    @abstractmethod
    def get_price(self, uri: str) -> PriceSchema | ValueError:
        pass


class EmagProductPageSearchAlgorithm(SearchAlgorithm):

    def get_price(self, uri: str) -> PriceSchema | ValueError:
        raw_html = requests.get(uri)
        soup_data = BeautifulSoup(raw_html.content, "html.parser")

        # Retrieved price should match the expected format
        price_string = \
            soup_data.select("p.product-new-price")[0].contents[0].text + \
            soup_data.select(".product-new-price sup")[0].text

        return CommaDecimalsDotThousandsPriceFormat().get_price(price_string)

