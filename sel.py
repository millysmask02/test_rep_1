import sqlite3

con = sqlite3.connect('school.sqlite')
cur = con.cursor()

que_select_cols = '''SELECT name, mark FROM class'''
que_select_all = '''SELECT * FROM class WHERE mark > 4'''
q = ''' SELECT * FROM class'''

cur.execute(q)
res = cur.fetchall()
print(res)

con.commit()
con.close()