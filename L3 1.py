import sqlite3
import pandas as pd

conn = sqlite3.connect('mocies.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS Movie_Actor;

CREATE TABLE Movie(
Movie_Id INTEGER PRIMARY KEY,
Title    TEXT,
Genre    TEXT,
Year     INTEGER,
Rating   REAL,
Duration INTEGER
);
CREATE TABLE Actor (
Actor_Id   INTEGER PRIMARY KEY,
Actor_Name TEXT,
Birth_Year INTEGER,
COUNTRY    TEXT
);
CREATE TABLE Movie_Actor (
Movie_Id   INTEGER,
Actor_Id   INTEGER
);

INSERT INTO Movie VALUES
(1,'Chainsaw Man','Animation',1994,8.5,88)
(2,'Avatar','Si-Fi',2009,9.1,81)
(3,'Titanic','Drama',1967,8.9,102)
(4,'Star Wars','Si-Fi',2015,7.8,107)
(5,'The Avengers','Si-Fi',2012,9.2,143)
(6,'Jurassic Park','Action',1998,8.0,134)
(7,'Black Panther','Action',2018,7.5,98)
(8,'The Godfather','Crime',1972,9.2,103)
(9,'Goodfellas','Crime',1990,7.7,97)
(10,'Demon Slayer','Animation',2025,9.7,169)

INSERT INTO Actor VALUES
(1,'Miachel Colreone',1974,'USA'),
(2,'Vito Colreone',1970,'USA'),
(3,'Tanjiro Kamado',1830,'Japan'),
(4,'Muzan Kibutsuji',1720,'Japan'),
(5,'Tyranosauras Rex',2000,'USA'),
(6,'Leonardo Di Caprio',1940,'USA'),
(7,'Thanos',2015,'USA'),
(8,'Denji',2020,'Japan'),
(9,'Makima',1345,'Japan'),
(10,' Blue Avatar',2000,'USA');

INSERT INTO Movie_Actor VALUES
(1,2),(2,1),(5,1),(6,3),(6,8),(7,4),(8,7),(9,5),(11,2),(12,1);
""")
conn.commit()
print('Database Ready!')

genres = pd.read_sql("""SELECT DISTINCT (Genre)
FROM Movie;""",conn)
print(genres)

countries = pd.read_sql("""SELECT DISTNICT (Country)
FROM Actor;""",conn)
print(countries)

top_movies = pd.read_sql("""SELECT Title, Genre,Rating
FROM Movie
ORDER BY Rating DESC;""",conn)
print(top_movies)

oldest_first = pd.read_sql("""SELECT Title, Year
    FROM Movie
    ORDER BY Year;""", conn)
print(oldest_first)

youngest_actors = pd.read_sql("""SELECT Actor_Name, Birth_Year, Country
    FROM Actor
    ORDER BY Birth_Year DESC;""", conn)
print(youngest_actors)

action_count = pd.read_sql("""SELECT COUNT(Movie_Id)
    FROM Movie
    WHERE Genre == 'Action';""", conn)
print(action_count)

animation_mins = pd.read_sql("""SELECT SUM(Duration)
    FROM Movie
    WHERE Genre == 'Animation';""", conn)
print(animation_mins)

avg_rating = pd.read_sql("""SELECT AVG(Rating)
    FROM Movie;""", conn)
print(avg_rating)

avg_action_dur = pd.read_sql("""SELECT AVG(Duration)
    FROM Movie
    WHERE Genre == 'Action';""", conn)
print(avg_action_dur)

movies_per_genre = pd.read_sql("""SELECT Genre, COUNT(Movie_Id)
    FROM Movie
    GROUP BY Genre;""", conn)
print(movies_per_genre)

avg_per_genre = pd.read_sql("""SELECT Genre, AVG(Rating)
    FROM Movie
    GROUP BY Genre
    ORDER BY AVG(Rating) DESC;""", conn)
print(avg_per_genre)

conn.close()
