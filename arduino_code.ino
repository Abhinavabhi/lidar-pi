#include <Servo.h>
Servo myservo;
void setup() {
   myservo.attach(8);
   digitalWrite(6,LOW);
   digitalWrite(7,HIGH);
   //analogWrite(5,255);
}

void loop() {
  analogWrite(5,115);
    {
if(digitalRead(0)==HIGH && digitalRead(1)==LOW)
{
 myservo.write(120);
}
if(digitalRead(1)==HIGH && digitalRead(0)==LOW)
{
myservo.write(60);
}
if(digitalRead(1)==LOW && digitalRead(0)==LOW)

{
  myservo.write(90);
} 
}

}



