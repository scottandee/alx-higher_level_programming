-- This script counts the numbers of 
-- shows that are linked to each genres
SELECT tv_genres.name AS 'genre',
COUNT(tv_show_genres.genre_id) AS 'number of shows'
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name, tv_show_genres.genre_id
ORDER BY 'number of shows' DESC
