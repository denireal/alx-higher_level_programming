-- Selecting titles of TV shows from the tv_shows table
SELECT s.title

-- Specifying the tv_shows table and its alias
FROM tv_shows s

-- Filtering out titles of TV shows associated with the genre 'Comedy'
WHERE s.title NOT IN (
      -- Subquery to select titles of TV shows associated with the genre 'Comedy'
      SELECT s.title
      FROM tv_shows s
      INNER JOIN tv_show_genres m ON s.id = m.show_id
      INNER JOIN tv_genres g ON m.genre_id = g.id
      WHERE g.name = 'Comedy'
)

-- Ordering the result by title of the TV show in ascending order
ORDER BY s.title ASC;
