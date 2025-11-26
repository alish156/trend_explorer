import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_flipkart_trending():
    url = "https://www.flipkart.com/search?q=trending+products"
    headers = {"User-Agent": "Mozilla/5.0"}

    # 🔥 Prevent Streamlit Cloud blank page
    try:
        r = requests.get(url, headers=headers, timeout=5)
    except:
        return pd.DataFrame(
            [["Error fetching Flipkart data", "N/A"]],
            columns=["Product Name", "Price"]
        )

    soup = BeautifulSoup(r.text, "lxml")

    products = soup.select("._1AtVbE")

    data = []
    for p in products[:20]:
        title = p.select_one("._4rR01T")
        price = p.select_one("._30jeq3")

        if title and price:
            data.append([title.text.strip(), price.text.strip()])

    # If no products found → avoid blank table
    if not data:
        return pd.DataFrame(
            [["No trending products found", "N/A"]],
            columns=["Product Name", "Price"]
        )

    return pd.DataFrame(data, columns=["Product Name", "Price"])
