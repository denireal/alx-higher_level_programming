-- Retrieve the id and name of cities in California, ordered by id.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
