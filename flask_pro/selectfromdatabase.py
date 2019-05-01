from config import databaseconfig as dc

conn = dc.conn
cursor = conn.cursor()
cursor.execute("select * from setclass_info")

d = cursor.fetchall()
for i in d:
    print(i)