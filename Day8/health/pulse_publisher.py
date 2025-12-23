import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost")

pulse = 89    
client.publish("health/pulse", pulse)

print("pulse sent:", pulse)
client.disconnect()