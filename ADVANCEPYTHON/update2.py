import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",password="",database="shopping2")

mycursor= mydb.cursor()

sql="UPDATE users SET p_name='tablet' where p_name = 'cloth' "

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")