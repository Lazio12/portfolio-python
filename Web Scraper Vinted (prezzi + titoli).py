import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_vinted(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    items = []
    for item in soup.find_all("div", class_="feed-grid__item"):
        title_tag = item.find("a", class_="title")
        price_tag = item.find("span", class_="price")
        if title_tag and price_tag:
            title = title_tag.text.strip()
            price = price_tag.text.strip()
            items.append({"Titolo": title, "Prezzo": price})

    df = pd.DataFrame(items)
    df.to_excel("vinted_risultati.xlsx", index=False)
    print(f"Salvati {len(items)} annunci in vinted_risultati.xlsx")

if __name__ == "__main__":
    link = input("Inserisci URL Vinted: ")
    scrape_vinted(link)
