#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x3F, 20, 4);

#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance.

boolean unlocked = false; //allows device to be used (if this is false, then "started" cannot be true) 
boolean started = false; //switch this to true when button is pressed
unsigned long start_time; //starting milliseconds
unsigned long new_time; //current milliseconds (will take difference to determine stopwatch time)

int mill = 0;
int seconds = 0;
int minutes = 0;

const int goButtonPin = 6; //digital pin for buttons
const int stopButtonPin =  7;
int goButtonState = 0;  //stores read value for button status
int stopButtonState = 0; 

void setup() {
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
  lcd.print("00:00:00");
  SPI.begin(); // Initiate SPI bus
  mfrc522.PCD_Init(); // Initiate MFRC522
  pinMode(goButtonPin, INPUT);
  pinMode(stopButtonPin, INPUT);
}

void Scan_For_Card(){
  if ( ! mfrc522.PICC_IsNewCardPresent()) { // Look for new cards
    return; 
  } 
  if ( ! mfrc522.PICC_ReadCardSerial()) { // Select one of the cards
    return;
  } 
  String content= "";
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
    content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
    content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  content.toUpperCase();
  if (content.substring(1) == "84 7A 2C D0") { //change here the UID of the card/cards that you want to give access
    unlocked = true; //start button can now start device
  }
  else {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Time: 00:00:000");
    lcd.setCursor(1, 1);
    lcd.print("Access Denied!"); //nothing happens
    delay(2000);
    lcd.clear();
  }
}

void Check_Buttons(){
  goButtonState = digitalRead(goButtonPin);
  stopButtonState = digitalRead(stopButtonPin);
  if (goButtonState == HIGH && unlocked == true) {
    if (!started){
      lcd.clear();
      start_time = millis(); //only start timer when button is first pressed (not every time)
    }
    started = true;
  }
  if (stopButtonState == HIGH) {
    started = false;
  }
}

void Timing(){
    new_time = millis();
    mill = new_time - start_time;
    seconds = (mill / 1000) % 60;
    minutes = mill / 60000;
}

void LCD_Display(){
  lcd.setCursor(0, 0);
  lcd.print("Time: ");
  if (minutes < 10) {
    lcd.print("0");
    lcd.print(minutes);
    lcd.print(":");
  }
  else {
    lcd.print(minutes);
    lcd.print(":");
  }
  if (seconds < 10) {
    lcd.print("0");
    lcd.print(seconds);
    lcd.print(":");
  }
  else {
    lcd.print(seconds);
    lcd.print(":");
  }
  if (mill < 10) {
    lcd.print("00");
    lcd.print(mill % 1000);
  }
  else {
    lcd.print(mill % 1000);
  }
  lcd.setCursor(0, 1);
  
  if (unlocked && !started && mill > 0){
    lcd.print("Status: STOPPED");
  }
  else if (unlocked && !started) {
    lcd.print("Status: UNLOCKED");
  }
  else if (started){
    lcd.print("Status: SOLVING");
  }
  else{
    lcd.print("Status: LOCKED");
  }
}

void loop() {
  Check_Buttons();
  if (unlocked && started){ //only time when device is unlocked and button is pressed
    Timing();
  }
  else{
    Scan_For_Card(); //no need to scan for card if device is going
  }
  LCD_Display();
}
