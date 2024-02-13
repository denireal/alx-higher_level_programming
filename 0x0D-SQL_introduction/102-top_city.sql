-- Selects the city and average temperature from the temperatures table
-- Filters the results to include only data for the months of July and August
-- Groups the results by city
-- Orders the results by average temperature in descending order
-- Limits the result to the top 3 cities
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8 GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
