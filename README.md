# Retail Data Pipeline

## Project Overview

This project demonstrates an end-to-end ETL pipeline using Python, Pandas, PostgreSQL, SQL, Git, and GitHub.

## Architecture

CSV Dataset
↓
Python Extract
↓
Python Transform
↓
PostgreSQL Load
↓
SQL Analytics

## ETL Process

### Extract
Read ecommerce sales data from CSV.

### Transform
- Checked missing values
- Removed duplicates
- Converted data types

### Load
Loaded cleaned data into PostgreSQL.

## Analytics Queries

### Revenue by Region

```sql
SELECT region,
       SUM(revenue) AS total_revenue
FROM ecommerce_sales
GROUP BY region
ORDER BY total_revenue DESC;
```

### Revenue by Category

```sql
SELECT category,
       SUM(revenue) AS total_revenue
FROM ecommerce_sales
GROUP BY category
ORDER BY total_revenue DESC;
```

### Orders by Payment Method

```sql
SELECT payment_method,
       COUNT(*) AS orders
FROM ecommerce_sales
GROUP BY payment_method
ORDER BY orders DESC;
```

## Technologies

- Python
- Pandas
- PostgreSQL
- SQL
- Git
- GitHub