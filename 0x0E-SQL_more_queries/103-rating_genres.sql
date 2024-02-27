-- Selecting the name of TV genres and the sum of ratings for all TV shows within each genre
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating

-- Specifying the tables involved in the query and how they are joined
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id

-- Grouping the results by genre_id to calculate the sum of ratings for all TV shows within each genre
GROUP BY tv_show_genres.genre_id

-- Ordering the results by the total rating in descending order
ORDER BY rating DESC;
