import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
conn.execute("""CREATE TABLE author (
author_id     INTEGER PRIMARY KEY,
author_name   TEXT NOT NULL UNIQUE
)""")

conn.execute("""CREATE TABLE book (
book_id     INTEGER PRIMARY KEY,
book_title  TEXT NOT NULL,
author_id   INTEGER
)""")

conn.executemany("INSERT INTO author VALUES(?,?)",[
    (1, 'Robert Greene'),
    (2, 'Sun Tzu'),
    (3, 'Morgan Housel'),
    (4, 'Robert Kiyosaki'),
    (5, 'James Clear'),
    (6, 'Napoleon Hill'),    
])

conn.executemany("INSERT INTO books VALUES (?,?,?)",[
(1, '48 Laws of Power',       1),
(2, 'The Art of Seduction',   1),
(3, 'Laws of Human Nature',   2),
(4, 'The Art of War',         2),
(5, 'The Psycology of Money', 3),
(6, 'Atomic Habits',          3),
(7, 'Rich Dad Poor Dad',      4),
])
conn.commit()

authors = pd.read_sql("SELECT * FROM author", conn)
books = pd.read_sql("SELECT * FROM books", conn)
print("Author table:")
print(authors)
print()
print("Book table:")
print(books)
print()

inner = pd.read_sql(
    "SELECT author.author_name, book.book_title"
    "FROM author INNER JOIN book ON author.author_id = book.author_id",
    conn
)
print("INNER JOIN - authors matched with their books:")
print(inner)
print()

left = pd.read_sql(
    "SELECT author.author_name, book.book_title"
    "FROM author LEFT JOIN book ON author.author_id = book.author_id",
    conn
)
print("LEFT JOIN - all authors, NULL where no book found:")
print(left)
print()

cross = pd.read_sql(
    "SELECT author.author_name, book.book_title"
    "FROM author CROSS JOIN book WHERE author.author_id <= 2",
    conn
)
print("CROSS JOIN - first 2 authors paired with every book:")
print(cross)
print()

union = pd.read_sql(
    "SELECT author_name AS name, 'Author' AS type FROM author"
    "UNION"
    "SELECT book_title AS name, 'Book' AS type FROM book",
    conn
)
print("UNION - all author names and book titles combined:")
print(union)

conn.close()