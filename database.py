import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS datos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')

cur.executemany('INSERT INTO datos (nombre, edad) VALUES (?, ?)', [
    ('Ana', 25),
    ('Luis', 30),
    ('Carla', 22)
])

conn.commit()
conn.close()
