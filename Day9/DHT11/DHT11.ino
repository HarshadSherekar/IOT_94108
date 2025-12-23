#include "DHT.h"

#define DHTPIN 4        // GPIO pin where DHT11 data pin is connected
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  delay(1000);
  Serial.println("DHT11 Sensor Reading Started");
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature(); // Celsius

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %  |  Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  delay(2000);
}