import mysql.connector

database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   passwd='', )



#preparing cursor object
co= database.cursor()

#creating database
co.execute("CREATE DATABASE amazon")