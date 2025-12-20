from utils.DB_connection import getdbconnection

def executeselect(query):
    connection = getdbconnection()
    cursor = connection.cursor()
    
    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    
    connection.close()

    return data