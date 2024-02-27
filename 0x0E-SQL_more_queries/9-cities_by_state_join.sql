-- Retrieve the id and name of cities along with the name of their respective states,
-- ordered by city id.
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
