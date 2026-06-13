# Retail Data Pipeline

## Project Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using Python and PostgreSQL.

## Technologies

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- SQL
- Git

## Pipeline Architecture

CSV Dataset
↓
Extract
↓
Transform
↓
Load
↓
PostgreSQL
↓
Analytics Queries

## ETL Steps

### Extract
- Loaded ecommerce dataset using Pandas

### Transform
- Checked missing values
- Checked duplicates
- Converted dates to datetime format

### Load
- Loaded 1000 records into PostgreSQL


## Key Business Insights

### Revenue by Region
- North generated the highest revenue (3.38M)
- West generated the lowest revenue (2.56M)

### Revenue by Category
- Fashion was the highest-performing category
- Electronics was the second-highest category

### Payment Methods
- COD was the most popular payment method
- Net Banking was the least used payment method