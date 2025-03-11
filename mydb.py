import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root123'
)

cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE mojaBaza")

print("All done")