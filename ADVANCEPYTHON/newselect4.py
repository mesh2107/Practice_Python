import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",password="",database="shopping2")

mycursor= mydb.cursor()

sql="select * from users order by p_category desc"     #alphabetical order

mycursor.execute(sql)

myresult= mycursor.fetchall()
x=0
for x in myresult:
    print(x)