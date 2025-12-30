#include <WiFi.h>
#include <ArduinoMqttClient.h>
#include <DHT.h>

// WiFi credentials
const char *ssid = "SUNBEAM";
const char *password = "1234567890";

// MQTT Broker
const char *broker = "172.18.1.151";
int port = 1883;

// MQTT topics
const char *tempTopic = "room/temperature";
const char *humTopic  = "room/humidity";

// DHT settings
#define DHTPIN 4        // GPIO 4
#define DHTTYPE DHT11   // Change to DHT22 if needed

DHT dht(DHTPIN, DHTTYPE);

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

unsigned long lastPublish = 0;

void setup() {
  Serial.begin(115200);

  // Start DHT sensor
  dht.begin();

  // Connect WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");

  // Connect MQTT
  Serial.print("Connecting to MQTT broker");
  while (!mqttClient.connect(broker, port)) {
    Serial.print(".");
    delay(2000);
  }
  Serial.println("\nMQTT connected");
}

void loop() {
  mqttClient.poll();

  // Publish every 5 seconds
  if (millis() - lastPublish >= 5000) {
    lastPublish = millis();

    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature(); // Celsius

    // Check if readings failed
    if (isnan(humidity) || isnan(temperature)) {
      Serial.println("Failed to read from DHT sensor!");
      return;
    }

    // Publish temperature
    mqttClient.beginMessage(tempTopic);
    mqttClient.print(temperature);
    mqttClient.endMessage();

    // Publish humidity
    mqttClient.beginMessage(humTopic);
    mqttClient.print(humidity);
    mqttClient.endMessage();

    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.print(" °C | Humidity: ");
    Serial.print(humidity);
    Serial.println(" %");
  }
}
