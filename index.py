from modules.DataScraper import PriceScraper

price_scraper = PriceScraper("https://...")
price = price_scraper.get_price().get_price_full()
print(price)
