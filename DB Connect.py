import sqlite3 as db
conn=db.connect("Test.db")
con=conn.cursor()
con.execute("create table if not exists Stud (id int primary key, name text not null, dept text not null)")
print("Table Created ...")
conn.commit()
#Record insert
print("Inserting Records.....")
con.execute("insert into Stud values(1,'Tauseef','I.T')")
con.execute("insert into Stud values(2,'Sufyan','M.E')")
con.execute("insert into Stud values(3,'Mohsin','C.O')")
size=int(input("Enter Number of Record to Be Insert : "))
for i in range(size):
    print("Record : ",(i+1))
    idd=int(input("Enter ID : "))
    name=input("Enter Name : ")
    dpt=input("Enter Department : ")
    con.execute("insert into Stud values(?,?,?)",(idd,name,dpt))
print(con.lastrowid,"Records Inserted ...")
conn.commit()
#Display
print("Displaying Records ...")
cursor=con.execute("select * from Stud")
print("\t ID \t Name \t\t Department")
for rows in cursor:
    print("\t",rows[0],"\t",rows[1],"\t\t",rows[2])
conn.commit()
#Update Table
ser=input("Enter Id to be Update : ")
dep=input("Enter Department : ")
fnd=con.execute("update Stud set dept=? where id = ?",(dep,ser))
conn.commit()
print("After Update Displaying Records ...")
cursor=con.execute("select * from Stud")
print("\t ID \t Name \t\t Department")
for rows in cursor:
    print("\t",rows[0],"\t",rows[1],"\t\t",rows[2])
conn.commit()
#multiline function
res=con.execute("select min(id) from Stud")
print("Minimum id : ",res.fetchone()[0])
conn.commit()
