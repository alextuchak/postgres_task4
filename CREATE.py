# Создаем таблицы для базы данных
import sqlalchemy

dsn = 'postgresql://task4:task4@localhost:5432/task4'
engine = sqlalchemy.create_engine(dsn)
connection = engine.connect()
connection.execute("""CREATE TABLE IF NOT EXISTS Genre (Id SERIAL PRIMARY KEY,
Name VARCHAR(64) UNIQUE);

CREATE TABLE IF NOT EXISTS MixTapes (Id SERIAL PRIMARY KEY,
Name VARCHAR(64) UNIQUE,
Released INTEGER NOT NULL);

CREATE TABLE IF NOT EXISTS Albums (Id SERIAL PRIMARY KEY, 
Name VARCHAR(64) UNIQUE,
Released INTEGER NOT NULL,
AlbumGenre INTEGER REFERENCES Genre(id) NOT NULL);

CREATE TABLE IF NOT EXISTS Artists (Id SERIAL PRIMARY KEY, 
Name VARCHAR(64),
ArtistGenre INTEGER REFERENCES Genre(id) NOT NULL,
ArtistAlbum INTEGER REFERENCES Albums(id) NOT NULL);

CREATE TABLE IF NOT EXISTS Tracks (Id SERIAL,
Name VARCHAR(64),
Length INTEGER NOT NULL,
TrackArtist INTEGER REFERENCES Artists(id) NOT NULL,
TrackAlbum INTEGER REFERENCES Albums(id) NOT NULL,
TrackMixtapes INTEGER REFERENCES MixTapes(id) NULL);""")

