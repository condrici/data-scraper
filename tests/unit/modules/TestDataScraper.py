import unittest
from unittest.mock import patch

from modules.DataScraper import PriceScraper
from modules.SearchAlgorithms import SearchAlgorithmFactory


class TestPriceScraper(unittest.TestCase):

    def test_scrape(self) -> None:

        # Test with nonexistent algorithm
        # The url parameter is not validated currently TODO: Validate URL

        with self.assertRaises(ValueError) as context:
            self.__get_price_scraper().scrape(
                'https://some-url.com', 'nonexistent_algorithm'
            )

        self.assertEqual('Unknown algorithm used', str(context.exception))

        # Test with original object and mocked dependencies

        price_scraper = self.__get_price_scraper_with_mocked_dependencies()
        self.assertEqual(price_scraper.scrape('test', 'test'), True)

    """ Original scrape functionality """
    """ Useful for testing internal exceptions due to invalid arguments """

    def __get_price_scraper(self):
        search_algorithm_factory = SearchAlgorithmFactory()
        return PriceScraper(search_algorithm_factory)

    """ Mocked price scraper """
    """ Useful for mocking the actual HTTP request via get_price """

    @patch('modules.SearchAlgorithms.SearchAlgorithmFactory')
    @patch('modules.SearchAlgorithms.SearchAlgorithm')
    def __get_price_scraper_with_mocked_dependencies(
            self,
            mock_search_algorithm_factory,
            mock_search_algorithm
    ):
        mock_search_algorithm.get_price.return_value = True
        mock_search_algorithm_factory.create.return_value = \
            mock_search_algorithm

        return PriceScraper(mock_search_algorithm_factory)
