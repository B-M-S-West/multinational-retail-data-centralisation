/*
Query the database to find out which months have produced the most sales.
*/

SELECT ROUND(SUM(orders_table.product_quantity*dim_products.product_price)) AS total_sales, dim_date_times.month
FROM orders_table
JOIN dim_date_times ON  orders_table.date_uuid = dim_date_times.date_uuid
JOIN dim_products ON  orders_table.product_code = dim_products.product_code
GROUP BY dim_date_times.month
ORDER BY SUM(orders_table.product_quantity*dim_products.product_price) DESC;