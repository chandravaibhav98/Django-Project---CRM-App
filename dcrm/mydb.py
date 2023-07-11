# Install mysql
# pip install mysql,mysql-connector,mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='10081998',
)

# prepare a cursor object
cursorObject = database.cursor()

# Create a database
def deleteDatabase():
    DeleteDatabaseQuery = "DROP DATABASE django;"
    print('Database created! : django')
    cursorObject.execute(DeleteDatabaseQuery)
    

def createDatabase():
    createDatabaseQuery = "CREATE DATABASE django;"
    print('Database created! : django')
    cursorObject.execute(createDatabaseQuery)
    
deleteDatabase()
createDatabase()


