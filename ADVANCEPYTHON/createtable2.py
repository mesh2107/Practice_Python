#creating database through query
import mysql.connector

database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   passwd='',
                                   db='shopping2' )



#preparing cursor object
co= database.cursor()

#creating database
co.execute("CREATE TABLE PRODUCT2(id  int(50) primary key,p_name varchar(250),p_quantity varchar(250),p_price varchar(250),p_category varchar(250))")