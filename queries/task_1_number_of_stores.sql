/*
The Operations team would like to know which countries we currently operate 
in and which country now has the most stores.
*/


SELECT country_code AS country, COUNT(*) as total_no_stores
FROM dim_store_details 
GROUP BY country_code
ORDER BY COUNT(*) DESC;