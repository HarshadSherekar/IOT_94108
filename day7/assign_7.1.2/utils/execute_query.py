from utils.DB_connection import getdbconnection

def execute_Query(query):
    connection = getdbconnection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
