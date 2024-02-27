-- Selecting the title of TV shows and their corresponding genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id

-- Specifying the tables involved in the query and how they are joined
FROM tv_shows

-- Left joining the tv_shows table with the tv_show_genres table on show_id
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id

-- Filtering the results to include only rows where the show_id in tv_show_genres is NULL
-- This effectively selects TV shows that have no corresponding genre IDs
WHERE tv_show_genres.show_id IS NULL

-- Ordering the results alphabetically by the title of the TV show and then by the genre ID
ORDER BY tv_shows.title, tv_show_genres.genre_id;
