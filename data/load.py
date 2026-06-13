import pandas as pd
from sqlalchemy import create_engine

# Read dataset
df = pd.read_csv("data/ecommerce_dataset.csv")

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Connect to PostgreSQL
engine = create_engine(
    "postgresql://postgres:Gloria@localhost:5432/Salesdb"
)

# Rename columns to match PostgreSQL table
df.columns = [
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "category",
    "quantity",
    "price",
    "discount",
    "payment_method",
    "revenue"
]

# Load data into PostgreSQL
df.to_sql(
    "ecommerce_sales",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully!")