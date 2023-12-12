/*
The operations team would like to know the overall staff numbers in each location around the world.
Perform a query to determine the staff numbers in each of the countries the company sells in.
*/
SELECT SUM(dim_store_details.staff_numbers) AS total_staff_numbers, dim_store_details.country_code
FROM dim_store_details
GROUP BY dim_store_details.country_code
ORDER BY SUM(dim_store_details.staff_numbers)  DESC;