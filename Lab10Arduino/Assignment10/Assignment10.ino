// EP305 Assignment 10 - outputs % of pot scale

//set global variables for max val and pin No.
int potPin = A0;
int potMax = 0;

void setup() {
  //set the baud rate
  Serial.begin(9600);
  
  //loop for 10 secs and obtain the max value of pot
  Serial.println("Turn the potentiometer through it's full range to obtain max value.");
  for(int i=10; i>=0; i--){
    int potValue = analogRead(potPin);
    if(potValue > potMax){
      potMax = potValue;
    }

    Serial.println("Waiting...");
    Serial.println(i);
    delay(1000);
  }
}

void loop() {
  //get the value of pot at current position
  float potValue = analogRead(potPin);
  //calculate it as a % usin max value obtained earlier
  float percent = (potValue / potMax) * 100; 
  Serial.println(percent);
  //wait 200ms between prints
  delay(200);

}
