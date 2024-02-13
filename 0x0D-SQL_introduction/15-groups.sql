-- Retrieves the distinct values of the `score` column from the `second_table`
-- along with the count of occurrences for each distinct score value,
-- and orders the result set by the count of occurrences in descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
