//EP305 Assignment 2 - streaming POT measuremrnt

//set pin to Potentiometer
const int POTpin = A2;
const int NUM_SAMPLES = 20;

int data[NUM_SAMPLES]; //buffer for samples
long stamp = 0; //buffer for time-stamps
int sum = 0; //used for averaging
float avg = 0;

void setup() {
  Serial.begin(19200);
}

void loop() {
  for(auto i=0; i<NUM_SAMPLES; i++){
    stamp = micros(); //get time stamp
    stamp /= 1000; //convert to miliseconds
    data[i] = analogRead(POTpin); //getsample
    // using a baud rate of 19200 the delay between 
    //measurements can not be less than 10ms
    delay(5); 
  }
  //get average of 20 samples
  for(auto i=0; i<NUM_SAMPLES; i++){
    sum += data[i];
  }
  avg = sum/NUM_SAMPLES;
  Serial.println("START"); //output new block marker
  Serial.print(stamp); //output time-stamp
  Serial.print(" "); //followed by
  Serial.print(avg); //the sample
  Serial.println(); //one per line
  sum = 0;
}
