-- Total Revenue
SELECT SUM(revenue)
FROM ecommerce_sales;

-- Revenue by Region
SELECT region,
       SUM(revenue) AS total_revenue
FROM ecommerce_sales
GROUP BY region
ORDER BY total_revenue DESC;

-- Top Categories
SELECT category,
       SUM(revenue) AS total_revenue
FROM ecommerce_sales
GROUP BY category
ORDER BY total_revenue DESC;

-- Payment Method Usage
SELECT payment_method,
       COUNT(*) AS orders
FROM ecommerce_sales
GROUP BY payment_method
ORDER BY orders DESC;