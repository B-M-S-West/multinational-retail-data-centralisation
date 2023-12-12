/*
Sales would like the get an accurate metric for how quickly the company is making sales.
Determine the average time taken between each sale grouped by year.
*/

-- This updates the time stamp to have the correct date
UPDATE dim_date_times
SET timestamp = (TO_DATE(year || '-' || month || '-' || day, 'YYYY-MM-DD')::date + (timestamp::time))

-- This gets the average time taken between each sale
WITH sales_time AS (
  SELECT 
    dim_date_times.year,
    dim_date_times.timestamp,
    LEAD(dim_date_times.timestamp) OVER (PARTITION BY dim_date_times.year ORDER BY dim_date_times.timestamp) AS next_sale_time
  FROM orders_table
  JOIN dim_date_times ON  orders_table.date_uuid = dim_date_times.date_uuid
)
SELECT 
  year,
  TO_CHAR(
    INTERVAL '1 second' * AVG(EXTRACT(EPOCH FROM (next_sale_time - timestamp))),
    'HH24 "hours" MI "minutes" SS "seconds" MS "milliseconds"'
  ) AS actual_time_taken
FROM sales_time
WHERE next_sale_time IS NOT NULL
GROUP BY year
ORDER BY actual_time_taken DESC;
