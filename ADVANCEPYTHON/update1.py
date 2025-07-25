import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",password="",database="shopping2")

mycursor= mydb.cursor()

sql="UPDATE users SET p_name= 'pencil' where p_name = 'apple' "

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")