from flask import Flask,request
from utils.executequery import executeQuery
from utils.executeselectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return"<html><body><h> this is a homepage <h><body><html> "

@server.post('/reading')
def createreading():
    id = request.form.get('id')
    temp = request.form.get('temp')
    humidity = request.form.get('humidity')

    query = f"insert into senors values({id}, {temp}, {humidity});"

    executeQuery(query=query)

    return "values are added successfully"

@server.get('/reading')
def retrive():
 query=" select * from senors;"
 data=executeSelectQuery(query=query)
 return f"senors:{data}"

@server.put('/reading')
def update():
    id=request.form.get('id')
    temp=request.form.get('temp')
    query=f"update senors set id ={id} where temp={temp} "

    executeQuery(query=query)
    return " sensor id is updated successfully"


@server.delete('/reading')
def delete():
    humidity=request.form.get('humidity')
    query=f"delete from senors where humidity={humidity}"
    executeQuery(query=query)
    return"1 row deleted sucessfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)