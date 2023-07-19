import unittest

import requests
from requests.models import Response

from modules.SearchAlgorithms import SearchAlgorithm


class TestPriceScraper(unittest.TestCase):

    # TODO: Replace hardcoded hostname with dynamic value

    HOSTNAME = 'http://localhost:8000/scraper'
    VALID_PARAM_ALGORITHM = SearchAlgorithm.ALGORITHM_EMAG_PRODUCT_PAGE
    VALID_PARAM_URL = 'https%3A%2F%2Fwww.emag.ro%2Fcovor-kring-meknes-1200-gsm-100-poliester-160x230-cm-maro-e2020-8b%2Fpd%2FD605NYMBM%2F%3Fref%3Dprofiled_categories_home_1_2%26provider%3Drec%26recid%3Drec_50_960f04ad2da835a164f95cd936f135f974327a0407a2c82a2245915f17cbca3d_1689072723%26scenario_ID%3D50'

    INVALID_PARAM_ALGORITHM = "invalid_algorithm"

    def test_scrape_success(self) -> None:
        valid_url = self.HOSTNAME \
                    + '/' + self.VALID_PARAM_URL \
                    + '/' + self.VALID_PARAM_ALGORITHM

        response = requests.get(valid_url)

        # Test HTTP response type and code

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, Response)

        # Test that response has price attributes set

        self.assertIsNotNone(
            response.json()['data']['attributes']['price'],
            str
        )

        self.assertIsNotNone(
            response.json()['data']['attributes']['whole_price'],
            str
        )

    def test_scrape_fail_incorrect_algorithm(self):
        url_with_invalid_algorithm = self.HOSTNAME + '/' \
                                     + self.VALID_PARAM_URL \
                                     + '/' + self.INVALID_PARAM_ALGORITHM

        response = requests.get(url_with_invalid_algorithm)

        self.assertEqual(response.status_code, 500)
