#include <Servo.h> // imports the library for the servos
// the servos are made in the order that the colours are scanned
Servo yellow;
Servo blue;
Servo red;
Servo green;
Servo orange;
Servo white;

char SerialData; // this will store the next move to be made
String str; // this will be used later to convert the char to string
void setup() {
  // this is just attaching the servos to their respective pins
  yellow.attach(A0);
  blue.attach(A1);
  red.attach(A2);
  green.attach(A3);
  orange.attach(A4);
  white.attach(A5);
//  yellow.write(180);
  Serial.begin(9600);
}
void loop() {
  /* This will be for when we are actually transferring shit to arduino from python 
   * Serial.available(); this will be checking whether there is input left
   * Serial.read(); this will read the input, the above line will make sure that there is somthing left to read to prevent any errors. This will be stored as a char
   */
  if (Serial.available() > 0){ // this will check if their is any more input left to take from the serial port which is written to with the python code
    SerialData = Serial.read(); // this will actually read the input from the serial port assuming that their is actual input to be read
    str = SerialData + ""; // this just converts the char type variable to a string type variable
//    turn(str.charAt(0), str.charAt(1)); // this will take in the side that needs to be turned and also the direction of the turn
    Serial.println(str); //this is for testing purposes to see the actual input from the python side of things
  }
}

void turn(String side, String dir){
  String sides = "ULFRBD"; // this will be used to determine the index of the servos depending on which side needs to be turned
  Servo servos[] = {yellow, blue, red, green, orange, white}; // this is just a simple list that stores the servos that are to be turned
  int sideIndex = sides.indexOf(side); // this will get the index of the side that needs to be turned, this is basically the index we will use to determine which servo will be used
  if (dir == "2"){ // this will be for a double turn
    servos[sideIndex].write(180); // this will probably have to be adjusted later
    delay(1000); //this will probably have to be adjusted later
    servos[sideIndex].write(90); // this will stop the servo
  }else if(dir == "'"){ // this will be for the counter clockwise turn
    servos[sideIndex].write(0); // this will probably have to be adjusted later
    delay(1000); //this will probably have to be adjusted later
    servos[sideIndex].write(90); // this will stop the servo
  }else{ // this will be for the clockwise turn
    servos[sideIndex].write(180); // this will probably have to be adjusted later
    delay(1000); //this will probably have to be adjusted later
    servos[sideIndex].write(90); // this will stop the servo
  }
}
