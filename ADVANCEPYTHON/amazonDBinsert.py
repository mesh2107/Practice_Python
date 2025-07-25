import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="amazon")

mycursor= mydb.cursor()
sql= "INSERT INTO customers (c_name, p_name, p_price, p_quantity, p_category, c_pay, c_address) VALUES (%s ,%s,%s,%s, %s,%s,%s)"
val= [
    ('aaa','cloth','2','200','cotton','4524152','AAAA'),
    ('bbb','book','4','5000','paper','84585','BBBB'),
    ('ccc','apple','78','1000','food','95282','CCCC'),
    ('ddd','samsung','1','200000','mobile','41452','DDDD'),
    ('eee','lenovo','3','7500000','laptop','8526','EEEEE'),
    ('fff','spoon','12','1000','things','9862485','FFFFF')
]

mycursor.executemany(sql,val)

mydb.commit()
print(mycursor.rowcount,"record was inserted.")