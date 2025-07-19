from scraper.amazon_scraper import get_amazon_price
from sheets.sheets_updater import update_sheet
import csv

def read_products(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def main():
    products = read_products("data/products.csv")
    results = []

    for product in products:
        url = product['url']
        if "amazon" in url:
            results.append(get_amazon_price(url))

    update_sheet(results)

if __name__ == "__main__":
    main()
