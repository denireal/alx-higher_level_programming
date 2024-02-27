-- Selecting the title of TV shows and their corresponding genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id

-- Specifying the tables involved in the query and how they are joined
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id

-- Ordering the results alphabetically by the title of the TV show and then by the genre ID
ORDER BY tv_shows.title, tv_show_genres.genre_id;
