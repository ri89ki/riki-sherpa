import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="recepie"
)
mycursor=mydb.cursor()
mycursor.execute("create database recepie")
print("database created successfully.")
'''mycursor.execute("create table recepie (food_name int(2) primary key Auto_Increment, ingridents varchar (155), quantity varchar(155), process varchar(10), servings varchar(120))")
print("Table created successfully.")'''
mycursor= mydb.cursor()
sql ="insert into recepie (food_name, ingridents, quantity, process, servings) values(%s,%s,%s,%s,%s)"
val=("soup","beet and carrot","two","cutting and boiling","two")
'''mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")'''
'''mycursor.execute("select * from recepie")
result=mycursor.fetchall()
for x in result:
    print(x)'''
'''sql= ("select *from recepie where ingridents ='beet and carrot'")
mycursor.execute(sql)
result=mycursor.fetchall()
for x in result:
    print(x)'''
    #update#
'''sql=("update recepie set ingridents=%s where ingridents=%s")
val =("ingridents","potato")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")'''
#delete#
'''sql=("delete from recepie where servings ='four'")
mycursor.execute(sql)
mydb.commit()
print("data deleted successfully")'''