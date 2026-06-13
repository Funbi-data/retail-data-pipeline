import pandas as pd

# Read dataset
df = pd.read_csv("data/ecommerce_dataset.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset dimensions
print("\nShape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns.tolist())