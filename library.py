import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library" 
)
mycursor=mydb.cursor()
'''mycursor.execute("create database library")
print("database created successfully.")'''
'''mycursor.execute("create table library (id int(2) primary key Auto_Increment, book_name varchar (155), genre varchar(155), author varchar(10), price varchar(120))")
print("Table created successfully.")'''
mycursor= mydb.cursor()
'''sql ="insert into library ( id, book_name, genre, author, price) values(%s,%s,%s,%s,%s)"
val=('',"Data Structure","Computer science","Thomas H.Cormen","499")
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")'''
'''mycursor.execute("select * from library")
result=mycursor.fetchall()
for x in result:
    print(x)'''
'''sql= ("select *from library where book_name ='Data Structure'")
mycursor.execute(sql)
result=mycursor.fetchall()
for x in result:
    print(x)'''
 #update#
'''sql=("update library set book_name=%s where book_name=%s")
val =("Computer Architecture","Data Structure")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")'''
#delete#
'''sql=("delete from library where price ='499'")
mycursor.execute(sql)
mydb.commit()
print("data deleted successfully")'''