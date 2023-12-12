/*
The company stakeholders want assurances that the company has been doing well recently.
Find which months in which years have had the most sales historically.
*/

SELECT ROUND(CAST(SUM(orders_table.product_quantity*dim_products.product_price) AS numeric),2) AS total_sales, dim_date_times.year, dim_date_times.month
FROM orders_table
JOIN dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
JOIN dim_products ON orders_table.product_code = dim_products.product_code
JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY dim_date_times.month,dim_date_times.year
ORDER BY SUM(orders_table.product_quantity*dim_products.product_price)  DESC;