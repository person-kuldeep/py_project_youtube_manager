import sqlite3

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS movie(
            title TEXT,
            year INTEGER,
            score REAL
    )
''')

# res = cur.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())

# res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
# print(res.fetchone() is None)

cur.execute("""
    INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5)            

""")

con.commit()

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Moonty Python's Life of Brian", 1979, 8.0),
]

cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()

# res = cur.execute("SELECT title FROM movie")
# print(res.fetchall())

for row in cur.execute("SELECT title, year FROM movie ORDER BY year"):
    print(row)

con.close()


new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')

new_con.close()
