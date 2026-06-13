import pandas as pd

# Read dataset
df = pd.read_csv("data/ecommerce_dataset.csv")

print("=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATES ===")
print(df.duplicated().sum())

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("\n=== UPDATED DATA TYPES ===")
print(df.dtypes)