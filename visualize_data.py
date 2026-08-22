import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("scraped_books_1000.csv")

rating_order = ["One", "Two", "Three", "Four", "Five"]
df["Rating"] = pd.Categorical(df["Rating"], categories=rating_order, ordered=True)

plt.figure(figsize=(10, 6))
plt.hist(df["Price"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.grid(axis="y", alpha=0.3)
plt.savefig("price_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(10, 6))
rating_counts = df["Rating"].value_counts().sort_index()
colors = ["#ff6b6b", "#ffa94d", "#ffd93d", "#6bcb77", "#4d96ff"]
plt.bar(rating_counts.index, rating_counts.values, color=colors, edgecolor="black")
plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.grid(axis="y", alpha=0.3)
plt.savefig("rating_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x="Rating", y="Price", data=df, palette="viridis")
plt.title("Price Distribution by Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")
plt.grid(axis="y", alpha=0.3)
plt.savefig("price_vs_rating_boxplot.png", dpi=300, bbox_inches="tight")
plt.show()

rating_to_num = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["Rating_Num"] = df["Rating"].map(rating_to_num)

plt.figure(figsize=(10, 6))
plt.scatter(df["Rating_Num"], df["Price"], color="purple", alpha=0.6, s=50)
plt.title("Price vs Rating (Scatter Plot)")
plt.xlabel("Rating (1=One, 5=Five)")
plt.ylabel("Price (£)")
plt.grid(alpha=0.3)
plt.xticks([1, 2, 3, 4, 5], ["One", "Two", "Three", "Four", "Five"])
plt.savefig("price_vs_rating_scatter.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(10, 6))
avg_price = df.groupby("Rating")["Price"].mean()
plt.bar(avg_price.index, avg_price.values, color="coral", edgecolor="black")
plt.title("Average Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.grid(axis="y", alpha=0.3)
for i, v in enumerate(avg_price.values):
    plt.text(i, v + 0.5, f"£{v:.2f}", ha="center", fontsize=10)
plt.savefig("avg_price_by_rating.png", dpi=300, bbox_inches="tight")
plt.show()

print("\n" + "=" * 50)
print("VISUALIZATION COMPLETE!")
print("=" * 50)
print("\n5 charts saved as PNG files:")
print("1. price_distribution.png")
print("2. rating_distribution.png")
print("3. price_vs_rating_boxplot.png")
print("4. price_vs_rating_scatter.png")
print("5. avg_price_by_rating.png")