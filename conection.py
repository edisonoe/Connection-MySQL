import mysql.connector
connection = mysql.connector.connect(host="localhost", user ="root" passwd="")


cursor = conecction.cursor()
cursor.execute("show databases")

for base in cursor:
    print(base)

connection.close()
    