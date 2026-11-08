import sqlite3
import pandas as pd
conn = sqlite3.connect(':memory:')
conn.execute(
    "CREATE TABLE experiment ("
    "experiment_id INTEGER PRIMARY
    KEY,"
    "experiment_name TEXT NOT NULL, "
    "subject TEXT NOT NULL, "
    "duration_mans INTEGER NOT NULL)"
)

conn.execute(
    "CREATE TABLE material ("
    "material_id INTEGER PRIMARY KEY,
"
    "experiment_id INTEGER NOT NULL,
"
    "item TEXT NOT NULL,"
    "quantity_g INTEGER NOT NULL)"
)

conn.executemany("INSERT INTO
experiment")