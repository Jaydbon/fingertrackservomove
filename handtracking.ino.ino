#include <Servo.h>
Servo fstJoint;
int angle = 10;
int angleCalc;
int led = 13;
int yes = 2;
int led2 = 12;

void setup() {
  Serial.begin(9600);
  fstJoint.attach(7);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
}


void loop() {
  if (Serial.available() > 0) {}
    digitalWrite(12, HIGH);
    angle = Serial.parseInt();
    digitalWrite(12, LOW);

    digitalWrite(13, HIGH);
    angleCalc = map(angle, 0, 150, 1, 180);
    fstJoint.write(angleCalc);
    digitalWrite(13, LOW);
}
