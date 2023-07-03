from modules.DataScraper import PriceScraper

price_scraper = PriceScraper("https://...")
price = price_scraper.scrape(PriceScraper.algorithm_emag_product_page).get_price_full()
print(price)
