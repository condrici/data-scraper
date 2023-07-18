from abc import abstractmethod

import requests
from bs4 import BeautifulSoup

from modules.PriceFormats import (
    PriceFormatFactory, FORMAT_COMMA_DECIMALS_DOT_THOUSANDS
)
from modules.Schema import PriceSchema


class SearchAlgorithm:

    ALGORITHM_EMAG_PRODUCT_PAGE = "emag_product_page"

    @abstractmethod
    def get_price(self, uri: str) -> PriceSchema | ValueError:
        pass


class HtmlScraperFactory:

    # The default should be used to get consistent results
    # For more information see the BeautifulSoup internals
    DEFAULT_PARSER = 'html.parser'

    def create(self, markup, features: str = DEFAULT_PARSER) -> BeautifulSoup:
        return BeautifulSoup(markup=markup, features=features)


class EmagProductPageSearchAlgorithm(SearchAlgorithm):

    def __init__(
        self,
        price_format_factory: PriceFormatFactory,
        html_scraper_factory: HtmlScraperFactory,
        http_requests: requests
    ) -> None:
        self.__price_format_factory = price_format_factory
        self.__html_scraper_factory = html_scraper_factory
        self.__http_requests = http_requests

    def get_price(self, uri: str) -> PriceSchema | ValueError:
        raw_html = self.__http_requests.get(uri)
        html_scraper = self.__html_scraper_factory.create(raw_html.content)

        # Retrieved price should match the expected format
        price_string = \
            html_scraper.select("p.product-new-price")[0].contents[0].text + \
            html_scraper.select(".product-new-price sup")[0].text

        return self.__price_format_factory.create(
            FORMAT_COMMA_DECIMALS_DOT_THOUSANDS
        ).get_price(price_string)


class SearchAlgorithmFactory:

    def create(self, algorithm: str) -> SearchAlgorithm:
        if algorithm == SearchAlgorithm.ALGORITHM_EMAG_PRODUCT_PAGE:
            return EmagProductPageSearchAlgorithm(
                http_requests=requests,
                html_scraper_factory=HtmlScraperFactory(),
                price_format_factory=PriceFormatFactory()
            )

        raise ValueError('Unknown algorithm used')
