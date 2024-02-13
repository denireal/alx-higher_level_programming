-- Selects the `score` and `name` columns from the `second_table`
-- where the `score` is greater than or equal to 10
-- and orders the results by `score` in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
