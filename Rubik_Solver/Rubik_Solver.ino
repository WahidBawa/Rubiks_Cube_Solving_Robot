#include <Servo.h>
// the servos are made in the order that the colours are scanned
Servo yellow;
Servo blue;
Servo red;
Servo green;
Servo orange;
Servo white;

char SerialData; // this will store the next move to be made

void setup() {
  yellow.attach(A0);
  blue.attach(A1);
  red.attach(A2);
  green.attach(A3);
  orange.attach(A4);
  white.attach(A5);
  Serial.begin(9600);
}
void loop() {
  /* This will be for when we are actually transferring shit to arduino from python 
   * Serial.available(); this will be checking whether there is input left
   * Serial.read(); this will read the input, the above line will make sure that there is somthing left to read to prevent any errors. This will be stored as a char
   */
}
