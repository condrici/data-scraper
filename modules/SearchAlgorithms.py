from abc import abstractmethod

import requests
from bs4 import BeautifulSoup

from modules.PriceFormats import PriceFormatFactory, \
    FORMAT_COMMA_DECIMALS_DOT_THOUSANDS
from modules.Schema import PriceSchema

ALGORITHM_EMAG_PRODUCT_PAGE = "emag_product_page"


class SearchAlgorithm:

    @abstractmethod
    def get_price(self, uri: str) -> PriceSchema | ValueError:
        pass


class EmagProductPageSearchAlgorithm(SearchAlgorithm):
    __price_format_factory: PriceFormatFactory

    def __init__(self, price_format_factory: PriceFormatFactory):
        self.__price_format_factory = price_format_factory

    def get_price(self, uri: str) -> PriceSchema | ValueError:
        raw_html = requests.get(uri)
        soup_data = BeautifulSoup(raw_html.content, "html.parser")

        # Retrieved price should match the expected format
        price_string = \
            soup_data.select("p.product-new-price")[0].contents[0].text + \
            soup_data.select(".product-new-price sup")[0].text

        return self.__price_format_factory.create(
            FORMAT_COMMA_DECIMALS_DOT_THOUSANDS
        ).get_price(price_string)


class SearchAlgorithmFactory:

    def create(self, algorithm: str) -> SearchAlgorithm:
        if algorithm == ALGORITHM_EMAG_PRODUCT_PAGE:
            return EmagProductPageSearchAlgorithm(PriceFormatFactory())

        raise ValueError('Unknown algorithm used')
