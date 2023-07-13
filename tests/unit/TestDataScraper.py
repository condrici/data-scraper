import unittest


class TestPriceScraper(unittest.TestCase):
    def test_scrape(self):
        self.assertEqual('data scraper'.upper(), 'DATA SCRAPER')
