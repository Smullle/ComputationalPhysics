// EP305 smaple sketch - fast LDR measuremnt

const int NUM_SAMPLES = 400;
const int ldrPin = A0;

int data[NUM_SAMPLES];

void setup() {
  Serial.begin(115200);
}

void loop() {
  // measure as fast as possible
  for(auto i = 0; i < NUM_SAMPLES; i++){
    data[i] = analogRead(ldrPin);
    delay(1);
  }
  for(auto i = 0; i < NUM_SAMPLES; i++){
    Serial.println(data[i]); 
  }
}
