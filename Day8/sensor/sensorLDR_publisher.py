import paho.mqtt.client as mqtt

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
publisher.connect("localhost")

publisher.publish("sensor/ldr", 3050.5)
publisher.disconnect()