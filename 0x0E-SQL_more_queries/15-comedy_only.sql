-- This script list all comedy shows
-- on the database
SELECT tv_shows.title
FROM tv_shows
RIGHT JOIN tv_genres
RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title
