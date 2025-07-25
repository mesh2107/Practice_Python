#creating database through query
import mysql.connector

database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   passwd='',
                                   db='amazon' )



#preparing cursor object
co= database.cursor()

#creating database
co.execute("CREATE TABLE customers(c_name varchar(250), p_name varchar(2500), p_price varchar(250), p_quantity varchar(250), p_category varchar(250), c_pay varchar(250), c_address varchar(250))")