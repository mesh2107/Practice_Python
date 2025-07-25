#python program to connect
#to mysql database


import mysql.connector


#connecting from th server 
conn=mysql.connector.connect(user='root',
                             host='localhost',
                             database='first database')
print(conn)
#diconnecting from server
conn.close()