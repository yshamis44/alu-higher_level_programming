-- Lists all the shows with all their genres, NULL when a show has no genre.
-- LEFT JOIN twice, so the shows without a genre are kept.
SELECT tv_shows.title, tv_genres.name FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id ORDER BY tv_shows.title ASC, tv_genres.name ASC;
