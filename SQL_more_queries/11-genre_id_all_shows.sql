-- Lists all the shows with their genre id, NULL when a show has no genre.
-- LEFT JOIN keeps every show, even without a link.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
