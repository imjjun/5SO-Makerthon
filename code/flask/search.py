import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('SELECT * FROM maskdetection ORDER BY number')
for dataframe in cur.fetchone():
    print(dataframe)


con.close()