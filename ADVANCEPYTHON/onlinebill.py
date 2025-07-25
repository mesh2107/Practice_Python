import mysql.connector


database= mysql.connector.connect(host='localhost',
                                   user='root',
                                   passwd='',
                                   db='movies' )
co= database.cursor()

co.execute("CREATE TABLE ONLINEBILL(id  int(50) primary key,name varchar(250),address varchar(250),phone varchar(250),pincode varchar(250),quantity varchar(250))")
