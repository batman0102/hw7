import sqlite3
db=sqlite3.connect('homework.db')
c=db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS homework(
name TEXT,
age INTEGER,
hobby TEXT,
lastname TEXT,
year_of_birth INTEGER,
points INTEGER
) ''')

c.execute('''DELETE FROM homework WHERE rowid % 2 = 0''')

c.execute(''' UPDATE homework SET name="genius" WHERE points>10 ''')

c.execute('''SELECT rowid, * FROM homework WHERE length(lastname)>10''')


for i in c.fetchall():
    print(i)

db.commit()
db.close()