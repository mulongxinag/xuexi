import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# cursor.execute("CREATE TABLE student(id INTEGER PRIMARY KEY,name VARCHAR (20),sex VARCHAR (10)，age INTEGER ,phone VARCHAR (20))")
cursor.execute('CREATE TABLE student(id INTEGER PRIMARY KEY,name VARCHAR (10),sex VARCHAR (10),age INTEGER ,phone VARCHAR (20))')
cursor.execute("INSERT INTO student(id,name,sex,age,phone)VALUES(1,'test','nan',12,'12345')")
data = cursor.execute("SELECT * FROM student").fetchall()
print(data)
conn.commit()
conn.close()