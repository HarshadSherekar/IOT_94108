import paho.mqtt.client as mqtt

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
publisher.connect("localhost")

publisher.publish("home/light", "ON")
publisher.disconnect()