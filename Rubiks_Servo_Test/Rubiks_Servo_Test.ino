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
int numMoves = 4; // This is the number of moves the algorithm will take to solve the cube

int led = 13;
int counter = 0;
String str = "";

int n;
boolean lengthFetched = false;

boolean startSolve = false;

void setup() {
  pinMode(led, OUTPUT);
  
  // this is just attaching the servos to their respective pins
  yellow.attach(7);
  blue.attach(4);
  red.attach(5);
  green.attach(3);
  orange.attach(6);
  white.attach(2);
  
  // This to stop the servos
  yellow.write(90);
  blue.write(90);
  red.write(90);
  green.write(90);
  orange.write(90);
  white.write(90);
  
  Serial.begin(9600);
}
void loop() {
  /* This will be for when we are actually transferring stuff to arduino from python 
   * Serial.available(); this will be checking whether there is input left
   * Serial.read(); this will read the input, the above line will make sure that there is somthing left to read to prevent any errors. This will be stored as a char
   */
  Servo servos[] = {yellow, blue, red, green, orange, white}; // this is just a simple list that stores the servos that are to be turned
  while (!Serial.available()) {} // wait for data to arrive
  while (Serial.available() && !lengthFetched){
    char SerialData = Serial.read();
    str += SerialData;
    counter++;
    if (counter % 1  == 0){
      n = str.toInt();
      Serial.println(n);
      lengthFetched = true;
      str = "";
      counter = 0;
    }
  }

  // while (Serial.available() && !startSolve){
  //   char SerialData = Serial.read();
  //   if (SerialData == "1"){
  //     startSolve = true;
  //     Serial.println(SerialData);
  //   }
  // }
  startSolve = true;
  // for (int i = 1; i < n; i++) Serial.println(i);
  while (Serial.available() && counter < n * 2 && startSolve){ // this will check if their is any more input left to take from the serial port which is written to with the python code
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
        servos[sideIndex].write(100); // this will probably have to be adjusted later
        Serial.println("turning twice");
        if (side == 'L') delay(1125); //this will probably have to be adjusted later
        if (side == 'R') delay(710);
        if (side == 'F') delay(800);
        if (side == 'B') delay(800);
        if (side == 'U') delay(710);
        if (side == 'D') delay(710);
        servos[sideIndex].write(90); // this will stop the servo
        delay(100);  
      }else if(dir == '\''){ // this will be for the counter clockwise turn
        servos[sideIndex].write(0); // this will probably have to be adjusted later
        Serial.println("inverse");
        if (side == 'L') delay(400); //this will probably have to be adjusted later
        if (side == 'R') delay(400);
        if (side == 'F') delay(400);
        if (side == 'B') delay(480);
        if (side == 'U') delay(400);
        if (side == 'D') delay(400);
        servos[sideIndex].write(90); // this will stop the servo
        delay(100);
      }else{ // this will be for the clockwise turn
        Serial.println("clockwise");
        servos[sideIndex].write(180); // this will probably have to be adjusted later
        if (side == 'L') delay(440); //this will probably have to be adjusted later
        if (side == 'R') delay(400);
        if (side == 'F') delay(400);
        if (side == 'B') delay(450);
        if (side == 'U') delay(500);
        if (side == 'D') delay(400);
        servos[sideIndex].write(90); // this will stop the servo
        delay(1000);
      }
        str = "";
      }
  }
  
}
