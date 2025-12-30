#include <WiFi.h>
#include <ArduinoMqttClient.h>

const char *ssid = "SUNBEAM";
const char *password = "1234567890";

const char *broker = "172.18.1.151";
int port = 1883;

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

const int ledPin = 2;

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");

  Serial.print("Connecting to MQTT broker");
  while (!mqttClient.connect(broker, port)) {
    Serial.print(".");
    delay(2000);
  }
  Serial.println("\nMQTT connected");

  mqttClient.subscribe("room/light");
  Serial.println("Subscribed to topic: room/light");
}

void loop() {
  mqttClient.poll();

  int messageSize = mqttClient.parseMessage();
  if (messageSize) {
    char message[messageSize + 1];

    for (int i = 0; i < messageSize; i++) {
      message[i] = mqttClient.read();
    }
    message[messageSize] = '\0';

    Serial.print("Received: ");
    Serial.println(message);

    if (strcmp(message, "ON") == 0) {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED ON");
    } 
    else if (strcmp(message, "OFF") == 0) {
      digitalWrite(ledPin, LOW);
      Serial.println("LED OFF");
    }
  }
}