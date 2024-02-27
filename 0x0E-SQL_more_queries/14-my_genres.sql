-- Selecting the names of TV genres associated with the TV show 'Dexter'
SELECT tv_genres.name

-- Specifying the tables involved in the query and how they are joined
FROM tv_genres
INNER JOIN tv_show_genres m ON tv_genres.id = m.genre_id
INNER JOIN tv_shows s ON m.show_id = s.id

-- Filtering the results to include only rows where the title of the TV show is 'Dexter'
WHERE s.title = 'Dexter'

-- Ordering the results alphabetically by the name of the TV genre
ORDER BY tv_genres.name ASC;
