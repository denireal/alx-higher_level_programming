-- Selecting genre names from the tv_genres table
SELECT g.name

-- Specifying the tv_genres table and its alias
FROM tv_genres g

-- Filtering genre names that are not associated with the TV show 'Dexter'
WHERE g.name NOT IN (
      -- Subquery to select genre names associated with the TV show 'Dexter'
      SELECT g.name
      FROM tv_genres g
      INNER JOIN tv_show_genres m ON g.id = m.genre_id
      INNER JOIN tv_shows s ON m.show_id = s.id
      WHERE s.title = 'Dexter'
)

-- Ordering the result by genre name in ascending order
ORDER BY g.name ASC;
