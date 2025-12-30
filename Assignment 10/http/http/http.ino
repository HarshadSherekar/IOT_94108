#include<WiFi.h>
#include<HTTPClient.h>
#include<DHT.h>

const char *ssid = "SUNBEAM";
const char *password = "1234567890";

#define DHT_PIN 4
#define DHT_TYPE  DHT11

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  dht.begin();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi ");
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // put your main code here, to run repeatedly:
  float temp = dht.readTemperature();
  String body = "{\"temp\":" + String(temp) + ",\"loc\":\"hall\"}";

  //Serial.println(body);

  WiFiClient wifiClient;
  HTTPClient httpClient;
  httpClient.begin(wifiClient, "http://172.18.4.146:4000/temperature");
  httpClient.addHeader("Content-Type", "application/JSON");

  int status = httpClient.POST(body);

  Serial.printf("status = %d\n", status);
  httpClient.end();

  delay(5000);
}







