#include "DHT.h"

#define DHTPIN 7
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

const int numAnalogPins = 6; 
const int numDigitalPins = 14;


void setup() {
  Serial.begin(9600);
  dht.begin();
  delay(1000);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');

    // Analaog commands
    if (command.startsWith("A")) {
      int pin_number = command.substring(1).toInt();

      if (pin_number >= 0 && pin_number < numAnalogPins) {
        int value = analogRead(pin_number);
        Serial.print("A");
        Serial.print(pin_number);
        Serial.print(":");
        Serial.println(value);
      }
    }

    // Digital pins
    if (command.startsWith("D")) {
      int pin_number = command.substring(1).toInt();

      if (pin_number >= 0 && numDigitalPins) {
        // dht 22 on pin 7
        if (pin_number == 7){
          float humidity = dht.readHumidity();
          float temperature = dht.readTemperature();
          Serial.print("D");
          Serial.print(pin_number);
          Serial.print(":");
          Serial.print(humidity);
          Serial.print("-");
          Serial.println(temperature);
        }
      }
    }
  }


}
