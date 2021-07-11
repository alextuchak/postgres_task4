# Заполняем таблицы
import sqlalchemy

dsn = 'postgresql://task4:task4@localhost:5432/task4'
engine = sqlalchemy.create_engine(dsn)
connection = engine.connect()
# Заполняем таблицу с жанрами
connection.execute(""" INSERT INTO genre(name)
VALUES ('Pop');

INSERT INTO genre(name)
VALUES ('Rock');

INSERT INTO genre(name)
VALUES ('Alternative');

INSERT INTO genre(name)
VALUES ('Electronic');

INSERT INTO genre(name)
VALUES ('Rap')
""")
# # Заполняем таблицу со сборниками
connection.execute(""" INSERT INTO mixtapes (name, released)
Values ('Pop music', 2021);

INSERT INTO mixtapes (name, released)
Values ('Rock music', 2018);

INSERT INTO mixtapes (name, released)
Values ('Alternative music', 2020);

INSERT INTO mixtapes (name, released)
Values ('Electronic music', 2019);

INSERT INTO mixtapes (name, released)
Values ('Rap music', 2021);

""")

# # Заполняем таблицу с альбомами
connection.execute(""" INSERT INTO albums (name, released, albumgenre)
 Values ('Неси меня к берегу', 2021, 1);

 INSERT INTO albums (name, released, albumgenre)
 Values ('Hope Above Adversity', 2021, 1);

 INSERT INTO albums (name, released, albumgenre)
 Values ('ЛЕГЕНДА', 2018, 2);

 INSERT INTO albums (name, released, albumgenre)
 Values ('Origins', 2018, 2);

 INSERT INTO albums (name, released, albumgenre)
 Values ('BADLANDS', 2020, 3);

 INSERT INTO albums (name, released, albumgenre)
 Values ('Tickets To My Downfall', 2020, 3);

 INSERT INTO albums (name, released, albumgenre)
 Values ('Renovatio', 2019, 4);

 INSERT INTO albums (name, released, albumgenre)
 Values ('amo', 2019, 4);

 INSERT INTO albums (name, released, albumgenre)
 Values ('New Era', 2021, 5);

 INSERT INTO albums (name, released, albumgenre)
 Values ('КОНДИТЕРСКАЯ', 2021, 5);
 """)

# Заполняем таблицу с Артистами
connection.execute(""" INSERT INTO artists (name, artistgenre, artistalbum)
 Values ('UNTONE CHERNOV',1,1);
 
 INSERT INTO artists (name, artistgenre, artistalbum)
 Values ('Dylan Cartlidge',1,2);
 
 INSERT INTO artists (name, artistgenre, artistalbum)
 Values ('КИНО',2,3);
 
 INSERT INTO artists (name, artistgenre, artistalbum)
 Values ('Imagine Dragons',2,4);
 
 INSERT INTO artists (name, artistgenre, artistalbum)
 Values ('Halsey',3,5);
 
 INSERT INTO artists (name, artistgenre, artistalbum)
 Values ('Machine Gun Kelly',3,6);
 
 INSERT INTO artists (name, artistgenre, artistalbum)
 Values ('Intelligency',4,7);
 
 INSERT INTO artists (name, artistgenre, artistalbum)
 Values ('Bring Me The Horizon',4,8);
 
 INSERT INTO artists (name, artistgenre, artistalbum)
 Values ('VibeTGK',5,9);
 
 INSERT INTO artists (name, artistgenre, artistalbum)
 Values ('LILCAK3',5,10);
 """)
# Заполняем таблицу с Песнями
connection.execute(""" INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Неси меня к берегу',216,1,1,1); 

INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Парами',219,1,1,1);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Yellow Brick Road',224,2,2,1);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Brown Bread',240,2,2,1);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Звезда по имени Солнце',203,3,3,2);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Группа крови',239,3,3,2);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Natural',189,4,4,2);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Bad Liar',260,4,4,2);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Castle',274,5,5,3);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('New Americana',199,5,5,3);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('bloody valentine',205,6,6,3);
  
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('my ex best friend',138,6,6,3);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Места не было для любви',261,7,7,4);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Into the Summer',279,7,7,4);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('i apologise if you feel something',139,8,8,4);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('in the dark',271,8,8,4);

 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('My Style',179,9,9,5);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Milkyway',163,9,9,5);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Мой Малой',121,10,10,5);
 
 INSERT INTO tracks (name, length, trackartist, trackalbum, trackmixtapes)
 Values ('Никакой Паники',103,10,10,5);
""")