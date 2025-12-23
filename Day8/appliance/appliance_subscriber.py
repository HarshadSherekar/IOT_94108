import paho.mqtt.client as mqtt
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="home_automation"
)
cursor = db.cursor()

def on_message(client, userdata, message):
    appliance = message.topic.split("/")[1]
    status = message.payload.decode()

    print(f"{appliance} is {status}")

    query = "insert into appliance_status (appliance_name, status) values (%s, %s)"
    cursor.execute(query, (appliance, status))
    db.commit()

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subscriber.on_message = on_message

subscriber.connect("localhost")
subscriber.subscribe("home/#")

subscriber.loop_forever()