float value = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(1000000);
}
void loop() {
  // put your main code here, to run repeatedly:
  value = analogRead(A0);
  Serial.println(value * 5 / 1023);
  delayMicroseconds(600);
}
