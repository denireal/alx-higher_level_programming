-- Selects the city and average temperature from the temperatures table
-- Groups the results by city
-- Orders the results by average temperature in descending order
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
