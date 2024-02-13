-- Selects the state and maximum temperature from the temperatures table
-- Groups the results by state
-- Orders the results by state name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
