from flask import Flask, request
from utils.execute_query import execute_Query
from utils.execute_select_query import executeselect

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page!</h1></body></html>"

@server.post('/moisture')
def newRecord():
    # .get() returns None if the key is missing, preventing crashes
    id = request.form.get('id')
    moisture_level = request.form.get('moisture_level')
    dta = request.form.get('dta')

    if not all([id, moisture_level, dta]):
        return "Missing data", 400

    query = f"insert into soil_moisture values({id}, {moisture_level}, '{dta}');"
    execute_Query(query=query)
    return "record is added successfully"

@server.get('/moisture')
def retrieve():
    id = request.args.get('id')
   
    if id is None:
        return "Please provide a id parameter in the URL (e.g., /sensor?id=1)", 400

    query = f"select * from soil_moisture where id = {id};"

    data = executeselect(query=query)
    return f"Record : {data}"

@server.put('/moisture')
def updateRecord():
    moisture_level = request.form.get('moisture_level')
    id = request.form.get('id')

    if not all([moisture_level, id]):
        return "Missing id or moisture_level", 400

    query = f"update soil_moisture set moisture_level = {moisture_level} where id = {id};"
    execute_Query(query=query)
    return "moisture_level is updated!"

@server.delete('/moisture')
def delete():
    id = request.form.get('id')

    if id is None:
        return "Missing id", 400

    query = f"delete from soil_moisture where id = {id};"
    execute_Query(query=query)
    return "Record Deleted!"
    
if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
