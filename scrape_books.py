# Web Scraping Script for Books to Scrape
# Libraries import karein
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target website ka URL
url = "http://books.toscrape.com/"

# Website se data fetch karein
response = requests.get(url)

# Check karein ke response successful hai ya nahi
print("Status Code:", response.status_code)  # 200 = Success

# HTML content ko parse karein
soup = BeautifulSoup(response.content, "html.parser")

# Saari books find karein (article class="product_pod")
all_books = soup.find_all("article", class_="product_pod")

# Data store karne ke liye empty list
books_data = []

# Har book se data nikaalein
for book in all_books:
    # Book ka title (h3 > a tag ke andar "title" attribute)
    title = book.h3.a["title"]
    
    # Book ki price (p class="price_color")
    price = book.find("p", class_="price_color").text
    
    # Book ki rating (p class="star-rating" ki second class)
    rating_tag = book.find("p", class_="star-rating")
    rating = rating_tag["class"][1]  # "One", "Two", "Three", etc.
    
    # Sab data ko list mein add karein
    books_data.append({
        "Title": title,
        "Price": price,
        "Rating": rating
    })

# DataFrame banayein (table form mein)
df = pd.DataFrame(books_data)

# CSV file mein save karein
df.to_csv("scraped_books.csv", index=False)

# Result check karein
print(f"\n✅ Total {len(df)} books scraped successfully!")
print("\n📊 Pehle 5 rows:")
print(df.head())