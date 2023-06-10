-- This script lists all the shows without
-- the genre Comedy in database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
	SELECT tv_shows.title
	FROM tv_shows
	LEFT JOIN tv_show_genres
	LEFT JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id
	ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_genres.name = 'Comedy')
ORDER BY tv_shows.title;
