import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory01"
)
mycursor=mydb.cursor()
'''mycursor.execute("create database inventory01")
print("database created successfully.")'''
'''mycursor.execute("create table inventory (id int(2) primary key Auto_Increment, items varchar (155), goods varchar(155), merchandise varchar(10), materials varchar(120))")
print("Table created successfully.")'''
mycursor= mydb.cursor()
sql ="insert into inventory ( id, items, goods, merchandise, materials) values(%s,%s,%s,%s,%s)"
val=('',"wood","wheat","clothing","wool")
'''mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")'''
'''mycursor.execute("select * from inventory")
result=mycursor.fetchall()
for x in result:
    print(x)'''
'''sql= ("select *from inventory where items ='wood'")
mycursor.execute(sql)
result=mycursor.fetchall()
for x in result:
    print(x)'''
    #update#
'''sql=("update inventory set items=%s where items=%s")
val =("cotton","wood")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")'''
#delete#
sql=("delete from inventory where materials ='wood'")
mycursor.execute(sql)
mydb.commit()
print("data deleted successfully")