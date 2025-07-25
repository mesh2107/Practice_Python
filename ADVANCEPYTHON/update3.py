import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",password="",database="shopping2")

mycursor= mydb.cursor()

sql="UPDATE users SET p_name= 'pencil' , p_price=  '100' , p_quantity='200', p_category='study' where p_name= 'spoon' "

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")