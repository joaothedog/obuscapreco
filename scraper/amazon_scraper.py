from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_amazon_price(product_url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(product_url)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    title = soup.select_one("#productTitle")
    price = soup.select_one(".a-offscreen")

    driver.quit()

    return {
        "site": "Amazon",
        "title": title.text.strip() if title else "N/A",
        "price": price.text.strip() if price else "N/A",
        "url": product_url
    }
