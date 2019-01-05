#include <Servo.h>
// the servos are made in the order that the colours are scanned
Servo yellow;
Servo blue;
Servo red;
Servo green;
Servo orange;
Servo white;

char SerialData; // this will store the next move to be made
String str;
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
  if (Serial.available() > 0){
    SerialData = Serial.read();   
    str = SerialData + "";
    turn(str.charAt(0), str.charAt(1)); 
  }
}

void turn(String side, String dir){
  String sides = "ULFRBD";
  Servo servos[] = {yellow, blue, red, green, orange, white};
  int sideIndex = sides.indexOf(side);
  if (dir == "2"){ // this will be for a double turn
    servos[sideIndex].write(180); // this will probably have to be adjusted later
    delay(500); //this will probably have to be adjusted later
    servos[sideIndex].write(90); // this will stop the servo
  }else if(dir == "'"){ // this will be for the counter clockwise turn
    servos[sideIndex].write(0); // this will probably have to be adjusted later
    delay(250); //this will probably have to be adjusted later
    servos[sideIndex].write(90); // this will stop the servo
  }else{ // this will be for the clockwise turn
    servos[sideIndex].write(180); // this will probably have to be adjusted later
    delay(250); //this will probably have to be adjusted later
    servos[sideIndex].write(90); // this will stop the servo
  }
}
