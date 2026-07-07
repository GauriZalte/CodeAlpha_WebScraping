import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

# 5 pages = 100 books (20 books per page)
for page in range(1, 6):

    url = base_url.format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.find("p", class_="star-rating")["class"][1]

        data.append([title, price, rating])

df = pd.DataFrame(data, columns=["Title", "Price", "Rating"])

df.to_csv("books.csv", index=False)

print("Success!")
print(f"Total Books Scraped: {len(df)}")