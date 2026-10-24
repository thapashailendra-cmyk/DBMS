import sqlite3
import pandas as pd

conn = sqlite3.connect('cricket.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Player_Match;

CREATE TABLE Team(
Team_Id INTEGER PRIMARY KEY,
Team_Name TEXT
);

CREATE TABLE Match(
Match_Id       INTEGER PRIMARY KEY,
Season_Id      INTEGER,
Match_Winner   INTEGER,
Win_Margin      INTEGER
);

CREATE TABLE Player_Match(
Match_Id    INTEGER,
Player_Id   Integer
);

INSERT INTO Team VALUES
(1,'Real Madrod'),(2,)
INSERT INTO Match VALUES
(1,7,5,35),(2,7,5,22),(3,8,5,45),(4,8,5,8),
(5,8,1,67),(6,8,6,19),(7,9,5,33),(8,9,1,28),
(9,9,5,12),(10,9,6,55),(11,9,3,38),(12,9,7,4);

INSERT INTO Player_Match VALUES
(1,101),(1,102),(2,103),(3,101),(4,104),(5,102);
""")
conn.commit()
print('Database Ready!')

tables = pd.read_sql("""SELECT *
FROM sqlite_master
WHERE type = 'table';""",conn)
print(tables)

matches = pd.read_sql("""SELECT *
FROM Match;""",conn)
print(matches)
print('Rows and columns:',matches.shape)
conn.close()