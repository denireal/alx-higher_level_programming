-- Selecting the genre name from the tv_genres table and the count of shows associated with each genre
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows

-- Specifying the tables involved in the query and how they are joined
FROM tv_genres

-- Inner joining the tv_genres table with the tv_show_genres table on genre_id
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id

-- Grouping the results by genre_id to count the number of shows associated with each genre
GROUP BY tv_show_genres.genre_id

-- Ordering the results by the number of shows associated with each genre in descending order
ORDER BY number_of_shows DESC;
