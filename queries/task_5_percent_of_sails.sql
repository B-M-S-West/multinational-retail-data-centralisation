/*
The sales team wants to know which of the different store types is generated the most revenue so they know where to focus.
Find out the total and percentage of sales coming from each of the different store types.
*/

SELECT dim_store_details.store_type, 
ROUND(CAST(SUM(orders_table.product_quantity*dim_products.product_price) AS numeric),2) AS total_sales,
ROUND(CAST(SUM(100.0*orders_table.product_quantity*dim_products.product_price)/(SUM(SUM(orders_table.product_quantity*dim_products.product_price)) OVER ()) AS numeric),2) AS percentage_total
FROM orders_table
JOIN dim_date_times ON  orders_table.date_uuid = dim_date_times.date_uuid
JOIN dim_products ON  orders_table.product_code = dim_products.product_code
JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY dim_store_details.store_type
ORDER BY percentage_total DESC;