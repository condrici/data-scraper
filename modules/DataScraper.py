"""Data Scraping functionality
It sends an HTTP request, retrieves the HTML data
and uses an algorithm to extract the price from it
"""

from modules.SearchAlgorithms import EmagProductPageSearchAlgorithm
from modules.Schema import PriceSchema


class PriceScraper:
    ALGORITHM_EMAG_PRODUCT_PAGE = "emag_product_page"

    def __init__(self, uri):
        self.uri = uri

    """Initiate scraping and determine which algorithm has to be used"""

    def scrape(self, scrape_algorithm: str) -> PriceSchema:
        if scrape_algorithm != self.ALGORITHM_EMAG_PRODUCT_PAGE:
            raise ValueError('Unknown algorithm used')

        return EmagProductPageSearchAlgorithm().get_price(self.uri)
