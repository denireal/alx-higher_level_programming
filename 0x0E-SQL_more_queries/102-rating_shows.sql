-- Selecting the title of TV shows and the sum of their ratings
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating

-- Specifying the tables involved in the query and how they are joined
FROM tv_shows
INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id

-- Grouping the results by show_id to calculate the sum of ratings for each TV show
GROUP BY tv_show_ratings.show_id

-- Ordering the results by the total rating in descending order
ORDER BY rating DESC;
