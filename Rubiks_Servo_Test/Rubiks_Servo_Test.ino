#include <Servo.h> // imports the library for the servos
// the servos are made in the order that the colours are scanned
Servo yellow;
Servo blue;
Servo red;
Servo green;
Servo orange;
Servo white;

char SerialData; // this will store the next move to be made


String sides = "ULFRBD"; // this will be used to determine the index of the servos depending on which side needs to be turned
int sideIndex; // this will get the index of the side that needs to be turned, this is basically the index we will use to determine which servo will be used

int led = 13;
int counter = 0;
String str = "";
void setup() {
  // this is just attaching the servos to their respective pins
  pinMode(led, OUTPUT);
  yellow.attach(A0);
  blue.attach(A1);
  red.attach(A2);
  green.attach(A3);
  orange.attach(A4);
  white.attach(A5);
  yellow.write(90);
  blue.write(90);
  red.write(90);
  green.write(90);
  orange.write(90);
  white.write(90);
  Serial.begin(9600);
}
void loop() {
  /* This will be for when we are actually transferring shit to arduino from python 
   * Serial.available(); this will be checking whether there is input left
   * Serial.read(); this will read the input, the above line will make sure that there is somthing left to read to prevent any errors. This will be stored as a char
   */
  Servo servos[] = {yellow, blue, red, green, orange, white}; // this is just a simple list that stores the servos that are to be turned
  while (!Serial.available()) {} // wait for data to arrive
  while (Serial.available() && counter < 6 * 2){ // this will check if their is any more input left to take from the serial port which is written to with the python code
    char SerialData = Serial.read(); // this will actually read the input from the serial port assuming that their is actual input to be read
    str += SerialData; // this just converts the char type variable to a string type variable 
    counter++;
    if (counter % 2 == 0){
//      Serial.println(str);
      char side = str.charAt(0);
      char dir = str.charAt(1);
      Serial.println(str.charAt(0));
      sideIndex = sides.indexOf(side);
      if (dir == '2'){ // this will be for a double turn
        servos[sideIndex].write(180); // this will probably have to be adjusted later
        Serial.println("turning twice");
        delay(1000); //this will probably have to be adjusted later
        servos[sideIndex].write(90); // this will stop the servo
      }else if(dir == '\''){ // this will be for the counter clockwise turn
        servos[sideIndex].write(0); // this will probably have to be adjusted later
        Serial.println("inverse");
        delay(350); //this will probably have to be adjusted later
        servos[sideIndex].write(90); // this will stop the servo
        delay(100);
      }else{ // this will be for the clockwise turn
        Serial.println("clockwise");
        servos[sideIndex].write(180); // this will probably have to be adjusted later
        delay(350); //this will probably have to be adjusted later
        servos[sideIndex].write(90); // this will stop the servo
        delay(100);
      }
        str = "";
      }
  }
  
}
