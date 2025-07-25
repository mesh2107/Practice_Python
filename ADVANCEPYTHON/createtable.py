#creating database through query
import mysql.connector

database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   passwd='',
                                   db='movies' )



#preparing cursor object
co= database.cursor()

#creating database
co.execute("CREATE TABLE USERS(id  int(50)primary key,name varchar(250),password varchar(250))")