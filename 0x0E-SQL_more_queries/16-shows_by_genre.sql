-- Selecting the title of TV shows and the name of their corresponding genres
SELECT tv_shows.title, tv_genres.name

-- Specifying the tables involved and how they are joined
FROM tv_shows

-- Left joining the tv_shows table with the tv_show_genres table based on the show_id
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id

-- Left joining the tv_show_genres table with the tv_genres table based on the genre_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id

-- Ordering the results alphabetically by the title of the TV show and the genre name
ORDER BY tv_shows.title, tv_genres.name;
