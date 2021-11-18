-- impoerting DB dump o your MySQL server:
SELECT
tv_shows.title,
tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id;
