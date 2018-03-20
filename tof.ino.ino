#include <Wire.h>
#include "Adafruit_VL6180X.h"
#include <Servo.h>
Adafruit_VL6180X vl = Adafruit_VL6180X();
Servo myservo;
float pos = 0;
const float Pi = 3.14159; 
void setup() {
   myservo.attach(9); 
  Serial.begin(115200);
  while (!Serial) {
    delay(1);
  }
  
 if (! vl.begin()) {   
    while (1);
  } 
}

void loop() { 

  for (pos = 0; pos <= 180; pos += 1) {  
      myservo.write(pos);
             uint8_t range = vl.readRange();
              Serial.println(String(range)+"p"+String(pos));
              delay(10);
  }
  /*for (pos = 180; pos >= 0; pos -= .5) { 
      myservo.write(pos);      
       uint8_t range = vl.readRange();
   {           
   Serial.println(String(range)+"p"+String(pos*Pi/180)+"p"+String(pos));
   delay(10);
 }
  }*/
  myservo.write(0);
  delay(2000);
}
