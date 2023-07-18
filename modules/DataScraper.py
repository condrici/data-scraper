"""Data Scraping functionality
It sends an HTTP request, retrieves the HTML data
and uses an algorithm to extract the price from it
"""

from modules.Schema import PriceSchema
from modules.SearchAlgorithms import SearchAlgorithmFactory


class PriceScraper:
    __search_algorithm_factory: SearchAlgorithmFactory

    def __init__(self, search_algorithm_factory: SearchAlgorithmFactory) -> None:
        self.__search_algorithm_factory = search_algorithm_factory

    """Initiate scraping and determine which algorithm has to be used"""

    def scrape(self, scrape_url: str, scrape_algorithm: str) -> PriceSchema:
        return self.__search_algorithm_factory.create(
            scrape_algorithm
        ).get_price(scrape_url)
