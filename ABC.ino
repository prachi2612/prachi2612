
#include "DHT.h"

#define dht_1 2
#define DHTTYPE DHT11
DHT dht(dht_1, DHTTYPE);

const int echoPin = 2; // Echo Pin of Ultrasonic Sensor
const int pingPin = 3; // Trigger Pin of Ultrasonic Sensor
float vol = 0.0, l_minute;
unsigned char flowsensor = 2; // Sensor Input
unsigned long currentTime;
unsigned long cloopTime;
unsigned long flow_frequency;
void flow () // Interrupt function to increment flow
{
  flow_frequency++;
}
int led = 13;
int resval = 0;  // holds the value
int respin = A3; // sensor pin used

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  dht.begin();
  pinMode(pingPin, OUTPUT); // initialising pin 3 as output
  pinMode(echoPin, INPUT); // initialising pin 2 as input
  pinMode(flowsensor, INPUT);
  digitalWrite(flowsensor, HIGH); // Optional Internal Pull-Up
  attachInterrupt(digitalPinToInterrupt(flowsensor), flow, RISING); // Setup Interrup
  pinMode (2 , INPUT);
}

void loop() {
  int a=0;
  long duration, inches, cm;
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(pingPin, LOW);
  duration = pulseIn(echoPin, HIGH); // using pulsin function to determine total time
  inches = microsecondsToInches(duration); // calling method
  cm = microsecondsToCentimeters(duration); // calling method
    currentTime = millis();
    if (currentTime >= (cloopTime + 1000))
  {
    cloopTime = currentTime; // Updates cloopTime
    if (flow_frequency != 0)
    {
      l_minute = (flow_frequency / 7.5); // (Pulse frequency x 60 min) / 7.5Q = flowrate in L/hour
      flow_frequency = 0; // Reset Counter
      a=l_minute;
    }
    else {
      a=0;
    }

  }
  resval = analogRead(respin); //Read data from analog pin and store it to resval variable
  digitalWrite(led, HIGH);
  digitalWrite(led, LOW);
  float hum = dht.readHumidity();
  float temp = dht.readTemperature();
  Serial.print("h= ");
  Serial.print(hum);
  Serial.print(",");
  Serial.print("t= ");
  Serial.print(temp);
  Serial.print(",");
  int rain = digitalRead(2);
  Serial.print("r= ");
  Serial.print(rain);
  Serial.print(",");
  Serial.print(cm);
  Serial.print("cm");
  Serial.print(",");
  Serial.print(a, DEC); // Print litres/hour
  Serial.println("");


  delay(200);
}

long microsecondsToInches(long microseconds) // method to covert microsec to inches
{
  return microseconds / 74 / 2;
}
long microsecondsToCentimeters(long microseconds) // method to covert microsec to centimeters
{
  return microseconds / 29 / 2;
}
