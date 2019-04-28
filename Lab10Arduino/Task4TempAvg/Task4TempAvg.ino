// EP305 smaple sketch - temperature measurement with averaging

void setup() {
  Serial.begin(9600);
}

void loop() {
  // repeat the voltage measurement every millisecond
  // for 0.1 second (100 samples)
  const int NUM_SAMPLES = 100;
  // get the sum of all measurements
  // the "sum" variable will hold the sum of
  // all the measurements in one cycle
  int sum = 0.0;
  for(int i = 0; i < NUM_SAMPLES; i++){
    sum += analogRead(A1);
    delay(1); //one ms delay
  }
  float average = sum / float(NUM_SAMPLES); //avereage in internal ADC units
  float T = average * (5.0 / 1023.0) * 100.0; //convert to degC
  Serial.println(T); // output on the serial port

}
