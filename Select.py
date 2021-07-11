from pprint import pprint
import sqlalchemy

dsn = 'postgresql://task4:task4@localhost:5432/task4'
engine = sqlalchemy.create_engine(dsn)
connection = engine.connect()

# 1.название и год выхода альбомов, вышедших в 2018 году

pprint(connection.execute(""" SELECT name, released FROM albums
WHERE released = 2018;""").fetchall())

# 2.название и продолжительность самого длительного трека

print(connection.execute(""" SELECT name, length FROM tracks
ORDER BY length DESC
LIMIT 1""").fetchall())

# 3.название треков, продолжительность которых не менее 3,5 минуты

print(connection.execute(""" SELECT name, length FROM tracks
WHERE length >= 210;""").fetchall())

# 4.названия сборников, вышедших в период с 2018 по 2020 год включительно

print(connection.execute(""" SELECT name FROM mixtapes
WHERE released BETWEEN 2017 AND 2020;""").fetchall())

# 5. исполнители, чье имя состоит из 1 слова;

print(connection.execute(""" SELECT name FROM artists
WHERE name NOT LIKE '%% %%';""").fetchall())

# 6. название треков, которые содержат слово "мой"/"my".
print(connection.execute(""" SELECT name FROM tracks
WHERE name LIKE '%%Мой%%' OR name LIKE '%%мой%%' OR name LIKE '%%My%%' OR name LIKE '%%my%%';""").fetchall())


