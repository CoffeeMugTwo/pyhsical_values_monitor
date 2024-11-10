//Libraries
#include <DHT.h>

//Constants
#define DHTPIN 2     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal

float hum;  //Stores humidity value
float temp;

void setup() {
 Serial.begin(9600);
 dht.begin();
 delay(1000);
}

void loop() {

 if (Serial.available() > 0) {
  char serIn = Serial.read();
  if (serIn == '0') {
    int sensorValue = analogRead(A0);
    Serial.println(sensorValue);
  }
  else if (serIn == '1') {
    int sensorValue = analogRead(A1);
    Serial.println(sensorValue);
  }
  else if (serIn == '2') {
    int sensorValue = analogRead(A2);
    Serial.println(sensorValue);
  }
  else if (serIn == '3') {
    int sensorValue = analogRead(A3);
    Serial.println(sensorValue);
  }
  else if (serIn == '4') {
    int sensorValue = analogRead(A4);
    Serial.println(sensorValue);
  }
  else if (serIn == '5') {
    int sensorValue = analogRead(A5);
    Serial.println(sensorValue);
  }
  else if (serIn == '6') {
    int sensorValue = analogRead(A6);
    Serial.println(sensorValue);
  }
  else if (serIn == '7') {
    int sensorValue = analogRead(A7);
    Serial.println(sensorValue);
  }
  else if (serIn == '8') {
    int sensorValue = analogRead(A8);
    Serial.println(sensorValue);
  }
  else if (serIn == '9') {
    int sensorValue = analogRead(A9);
    Serial.println(sensorValue);
  }
  else if (serIn == 'A') {
    int sensorValue = analogRead(A10);
    Serial.println(sensorValue);
  }
  else if (serIn == 'B') {
    int sensorValue = analogRead(A11);
    Serial.println(sensorValue);
  }
  else if (serIn == 'C') {
    int sensorValue = analogRead(A12);
    Serial.println(sensorValue);
  }
  else if (serIn == 'D') {
    int sensorValue = analogRead(A13);
    Serial.println(sensorValue);
  }
  else if (serIn == 'E') {
    int sensorValue = analogRead(A14);
    Serial.println(sensorValue);
  }
  else if (serIn == 'F') {
    int sensorValue = analogRead(A15);
    Serial.println(sensorValue);
  }
  else if (serIn == 'G') {
    temp = dht.readTemperature();
    Serial.println(temp);
  }
  else if (serIn == 'H') {
    hum = dht.readHumidity();
    Serial.println(hum);
  } 
 }    

 
}
