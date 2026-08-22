import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

all_books_data = []

for page_num in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"
    response = requests.get(url)
    
    if response.status_code != 200:
        break
    
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    if not books:
        break
    
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating_tag = book.find("p", class_="star-rating")
        rating = rating_tag["class"][1]
        
        all_books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })
    
    time.sleep(0.5)
    print(f"Page {page_num} done! Total: {len(all_books_data)}")

df = pd.DataFrame(all_books_data)
df["Price"] = df["Price"].str.replace("£", "").astype(float)
df.to_csv("scraped_books_1000.csv", index=False)

print(f"\nTotal {len(df)} books scraped successfully!")
print(df.head())