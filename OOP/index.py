import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='my_base'
)
mycursor = mydb.cursor()
