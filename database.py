import sqlite3 as db

con=db.connect("mydb.db")
#connetion
con.execute("drop table if exists mytable")
con.execute("create table mytable (id INTEGER primary key AUTOINCREMENT, name TEXT)")
print("Executed Table")
for i in range(5):
    name=input("Enter Your Name: ")
    con.execute("insert into mytable(name) values(?)",(name,))
con.commit()
rows=con.execute("select * from mytable")
for row in rows:
    print(row[0],"\t",row[1])