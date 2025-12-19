from utils.dbconnection import getDBConnection
def executeSelectQuery(query):
    
    connection = getDBConnection()

    cursor = connection.cursor()

    cursor.execute(query)

    connection.commit()

    cursor.close()

    connection.close()

    return data
