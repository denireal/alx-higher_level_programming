-- Selecting the titles of TV shows that belong to the genre 'Comedy'
SELECT tv_shows.title

-- Specifying the tables involved in the query and how they are joined
FROM tv_shows
INNER JOIN tv_show_genres m ON tv_shows.id = m.show_id
INNER JOIN tv_genres g ON m.genre_id = g.id

-- Filtering the results to include only rows where the genre name is 'Comedy'
WHERE g.name = 'Comedy'

-- Ordering the results alphabetically by the title of the TV show
ORDER BY tv_shows.title ASC;
