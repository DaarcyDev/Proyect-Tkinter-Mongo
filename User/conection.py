import mysql.connector

def conect():
    database=mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "tkinternotes",
        port = 3306
    )
    #print(database)
    cursor = database.cursor(buffered=True)
    return(database,cursor)

