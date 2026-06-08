import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.float_format', '{:,.0f}'.format)
pd.set_option('display.max_columns', None)

# Load data
df = pd.read_csv('socal2.csv')

# ── Basic Stats ──────────────────────────────
print("=== BASIC PRICE STATS ===")
print("Average price:", round(df['price'].mean(), 2))
print("Max price:", df['price'].max())
print("Min price:", df['price'].min())

# ── Top 10 Cities by Average Price ───────────
print("\n=== TOP 10 CITIES BY AVG PRICE ===")
print(df.groupby('citi')['price'].mean().sort_values(ascending=False).head(10))

# ── Top 10 Cities by Listings ─────────────────
print("\n=== TOP 10 CITIES BY LISTINGS ===")
print(df.groupby('citi').size().sort_values(ascending=False).head(10))

# ── Average Price by Bedroom Count ───────────
print("\n=== AVG PRICE BY BEDROOM COUNT ===")
print(df.groupby('bed')['price'].mean().sort_index())

# ── Price Tiers ───────────────────────────────
print("\n=== PRICE TIER DISTRIBUTION ===")
df['price_tier'] = 'Affordable'
df.loc[df['price'] > 500000, 'price_tier'] = 'Mid-range'
df.loc[df['price'] > 800000, 'price_tier'] = 'Luxury'
print(df['price_tier'].value_counts())

# ── Chart: Top 10 Cities by Avg Price ────────
top10_cities = df.groupby('citi')['price'].mean().sort_values(ascending=False).head(10)
top10_cities.plot(kind='bar')
plt.title('Top 10 Cities by Average Home Price')
plt.xlabel('City')
plt.ylabel('Average Price')
plt.tight_layout()
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.savefig('top10_cities_avg_price.png')
plt.show()

# ── Chart: Price Tier Distribution ────────────
tier_counts = df['price_tier'].value_counts()
tier_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Price Tier Distribution')
plt.ylabel('')
plt.savefig('price_tiers.png')
plt.show()

# —— Chart: Average Price by Bedroom Count ─────────
avg_bed_price = df.groupby('bed')['price'].mean().sort_index()
avg_bed_price.plot(kind='bar')
plt.title('Average Price by Bedroom Count')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Average Price')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.savefig('avg_price_by_bedrooms.png')
plt.show()