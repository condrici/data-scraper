import unittest
from unittest.mock import patch, MagicMock

from modules.SearchAlgorithms import (
    SearchAlgorithm, SearchAlgorithmFactory,
    EmagProductPageSearchAlgorithm, HtmlScraperFactory
)
from modules.PriceFormats import PriceFormatFactory


class TestSearchAlgorithmFactory(unittest.TestCase):

    def test_create(self) -> None:
        with self.assertRaises(ValueError) as context:
            SearchAlgorithmFactory().create('nonexistent_algorithm')

        # Test with nonexistent algorithm

        self.assertEqual('Unknown algorithm used', str(context.exception))

        # Test with existing algorithm

        self.assertIsInstance(
            SearchAlgorithmFactory().create(
                SearchAlgorithm.ALGORITHM_EMAG_PRODUCT_PAGE
            ), SearchAlgorithm
        )


class TestEmagProductPageSearchAlgorithm(unittest.TestCase):

    @patch('requests.models.Request')
    def test_get_price(self, request_object) -> None:

        # Test with a valid HTML CODE

        mocked_html_code = self.__get_valid_html_code()
        algorithm = self.__get_algorithm_mocked(request_object, mocked_html_code)

        self.assertEqual(
            '100,50',
            algorithm.get_price('http://www.google.com').price
        )

        self.assertEqual(
            '100',  # TODO: Look into why tests fails if 100 is a string
            algorithm.get_price('http://').whole_price
        )

        # Test with invalid HTML CODE

        with self.assertRaises(IndexError) as context:
            mocked_html_code = self.__get_invalid_html_code()
            algorithm = self.__get_algorithm_mocked(request_object, mocked_html_code)
            algorithm.get_price('http://')

        self.assertEqual('list index out of range', str(context.exception))

        # TODO: Look into further scenarios like remote CAPTCHA

    def __get_algorithm_mocked(self, request_object, html_code: str):

        # While the algorithm is mocked, BeautifulSoup performs an actual test
        # where the scraper actually extracts the price from the HTML

        request_object.content = html_code

        http_requests = MagicMock()
        http_requests.get.return_value = request_object

        algorithm = EmagProductPageSearchAlgorithm(
            PriceFormatFactory(), HtmlScraperFactory(), http_requests
        )

        return algorithm

    def __get_valid_html_code(self):
        return \
            '<p class="product-new-price">' \
            '100' \
            '<sup><small class="mf-decimal">,</small>50</sup> ' \
            '<span>Lei</span></p>'

    def __get_invalid_html_code(self):
        return ''