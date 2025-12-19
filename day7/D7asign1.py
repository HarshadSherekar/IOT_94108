from flask import Flask,request
from utils.executequery import executeQuery
from utils.executeselectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return"<html><body><h> this is a homepage <h><body><html> "

@server.post('/reading/<int:id><float:temp><float:humidity>')
def createreading():
    id = request.form.get('id')
    temp = request.form.get('temp')
    humidity = request.form.get('humidity')

    query = f"insert into senors values({id}, {temp}, {humidity});"

    executeQuery(query=query)

    return "values are added successfully"



if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)