import pandas as pd

df = pd.read_csv("scraped_books_1000.csv")

print("=" * 50)
print("DATA OVERVIEW")
print("=" * 50)
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print(f"\nColumn names: {df.columns.tolist()}")
print(f"\nData types:\n{df.dtypes}")

print("\n" + "=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("SUMMARY STATISTICS")
print("=" * 50)
print(f"Average Price: £{df['Price'].mean():.2f}")
print(f"Minimum Price: £{df['Price'].min():.2f}")
print(f"Maximum Price: £{df['Price'].max():.2f}")
print(f"Median Price: £{df['Price'].median():.2f}")

print("\n" + "=" * 50)
print("RATING DISTRIBUTION")
print("=" * 50)
print(df["Rating"].value_counts())

print("\n" + "=" * 50)
print("MOST EXPENSIVE BOOK")
print("=" * 50)
most_expensive = df.loc[df["Price"].idxmax()]
print(f"Title: {most_expensive['Title']}")
print(f"Price: £{most_expensive['Price']:.2f}")
print(f"Rating: {most_expensive['Rating']}")

print("\n" + "=" * 50)
print("CHEAPEST BOOK")
print("=" * 50)
cheapest = df.loc[df["Price"].idxmin()]
print(f"Title: {cheapest['Title']}")
print(f"Price: £{cheapest['Price']:.2f}")
print(f"Rating: {cheapest['Rating']}")

print("\n" + "=" * 50)
print("HIGHEST RATED BOOKS (5-STAR)")
print("=" * 50)
highest_rated = df[df["Rating"] == "Five"]
print(f"Total 5-star books: {len(highest_rated)}")
print(highest_rated[["Title", "Price", "Rating"]].head())

print("\n" + "=" * 50)
print("AVERAGE PRICE BY RATING")
print("=" * 50)
print(df.groupby("Rating")["Price"].mean().sort_values(ascending=False))

print("\n" + "=" * 50)
print("MISSING VALUES CHECK")
print("=" * 50)
print(df.isnull().sum())