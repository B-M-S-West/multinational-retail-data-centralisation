/*
The sales team is looking to expand their territory in Germany. 
Determine which type of store is generating the most sales in Germany.
*/

SELECT ROUND(CAST(SUM(orders_table.product_quantity*dim_products.product_price) AS numeric),2) as total_sales, 
dim_store_details.store_type, 
dim_store_details.country_code
FROM orders_table
JOIN dim_date_times ON  orders_table.date_uuid = dim_date_times.date_uuid
JOIN dim_products ON  orders_table.product_code = dim_products.product_code
JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE dim_store_details.country_code = 'DE'
GROUP BY dim_store_details.store_type,dim_store_details.country_code
ORDER BY SUM(orders_table.product_quantity*dim_products.product_price)  ASC;