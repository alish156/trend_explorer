import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_amazon_trending():
    url = "https://www.amazon.in/gp/bestsellers"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    products = soup.select(".zg-grid-general-faceout")
    
    data = []
    for p in products[:20]:
        title = p.select_one(".p13n-sc-truncated") or p.select_one("img")
        title = title.get("alt") if title else "No Title"

        price_tag = p.select_one(".p13n-sc-price")
        price = price_tag.text.strip() if price_tag else "N/A"

        data.append([title, price])

    return pd.DataFrame(data, columns=["Product Name", "Price"])
