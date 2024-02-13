-- Selects the `score` and `name` columns from the `second_table`
-- where the `name` column is not empty
-- and orders the result set by the `score` column in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
