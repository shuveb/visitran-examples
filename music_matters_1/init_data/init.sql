CREATE SCHEMA IF NOT EXISTS dev_music_matters_1;
CREATE SCHEMA IF NOT EXISTS raw_music_matters_1;
SET search_path TO raw_music_matters_1;

CREATE TABLE IF NOT EXISTS artists (
	id varchar(32),
	name varchar(256),
	popularity integer,
	followers integer,
	genres varchar(128)
);

CREATE TABLE IF NOT EXISTS albums (
	id varchar(32),
	name varchar(256),
	release_date date,
	release_date_precision varchar(8),
	tracks_count integer
);

CREATE TABLE IF NOT EXISTS tracks (
	id varchar(32),
	name varchar(256),
	duration_ms integer,
	explicit boolean,
	popularity integer,
	type varchar(128),
	artist_id varchar(32),
	album_id varchar(32),
	album_track_number integer,
	isrc_code varchar(32)
);

CREATE TABLE IF NOT EXISTS top_50_tracks (
	id varchar(32)
);

CREATE TABLE IF NOT EXISTS recently_played (
	track_id varchar(32),
	played_at timestamp,
	context varchar(32)
);

truncate table artists ;
truncate table albums ;
truncate table tracks ;
truncate table top_50_tracks ;
truncate table recently_played; 

copy artists from '/tmp/music_matters/artists.csv' csv header;
copy albums from '/tmp/music_matters/albums.csv' csv header;
copy tracks from '/tmp/music_matters/tracks.csv' csv header;
copy top_50_tracks from '/tmp/music_matters/top_50_tracks.csv' csv header;
copy recently_played from '/tmp/music_matters/recently_played.csv' csv header;

-- Top tracks played
select rp.track_id, t."name", a."name", count(rp.track_id) as play_count 
from
	recently_played rp
join tracks t 
	on rp.track_id = t.id
join artists a 
	on t.artist_id = a.id 
group by 
	track_id, t."name", a."name" 
order by 
	play_count desc ;

-- Top artists
select t.artist_id, a."name", count(t.artist_id) as artist_play_count
from recently_played rp
join tracks t  
	on rp.track_id = t.id
join artists a 
	on t.artist_id = a.id 
group by t.artist_id, a."name"
order by artist_play_count desc ;
