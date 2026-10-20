import pymysql

con = pymysql.connect(
    host="localhost",
    user="root",
    password="sahil1532"
)

if con:
    print("Connection successful")

con.close()