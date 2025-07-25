import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="shopping")

mycursor= mydb.cursor()
sql= "INSERT INTO product (p_name, p_quantity, p_price, p_category) VALUES (%s ,%s,%s,%s)"
val= [
    ('cloth','2','200','cotton'),
    ('book','4','5000','paper'),
    ('apple','78','1000','food'),
    ('samsung','1','200000','mobile'),
    ('lenovo','3','7500000','laptop'),
    ('spoon','12','1000','things')
]

mycursor.executemany(sql,val)

mydb.commit()
print(mycursor.rowcount,"record was inserted.")