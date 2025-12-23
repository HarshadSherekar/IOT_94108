#define LDR_PIN 34
void setup() {
  Serial.begin(115200);
  pinMode(LDR_PIN,INPUT);
  Serial.println("ADC setup is done");
}

void loop() {
  int value=analogRead(LDR_PIN);
  Serial.printf("light intensity %d",value);
  delay(2000);

}
