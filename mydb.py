import mysql.connector
dataBase = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    passwd = "Adetomi13!"

)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE adet")

print("All Done!")