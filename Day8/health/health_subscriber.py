import paho.mqtt.client as mqtt
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="healthcare_iot"
)
cursor = db.cursor()

def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode()

    if topic == "health/alert":
        print("Doctor Alert:", payload)
        return 

    value = float(payload)

    if topic == "health/pulse":
        parameter = "Pulse"
        if value > 100:
            alert_msg = f"alert pulse is above threshold: {value}"
            client.publish("health/alert", alert_msg)

    elif topic == "health/spo2":
        parameter = "SpO2"
        if value > 95:
            alert_msg = f"alert SpO2 is above threshold: {value}"
            client.publish("health/alert", alert_msg)

    print(parameter, "=", value)

    query = "insert into patient_data (parameter, value) VALUES (%s, %s)"
    cursor.execute(query, (parameter, value))
    db.commit()

def on_alert(client, userdata, message):
    print("doctor alert:", message.payload.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect("localhost")
client.subscribe("health/pulse")
client.subscribe("health/spo2")
client.subscribe("health/alert")

client.loop_forever()