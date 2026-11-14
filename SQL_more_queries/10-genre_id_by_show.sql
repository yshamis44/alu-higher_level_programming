-- Lists all the shows that have at least one genre linked, with the genre id.
-- INNER JOIN keeps only the shows that have a link.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
