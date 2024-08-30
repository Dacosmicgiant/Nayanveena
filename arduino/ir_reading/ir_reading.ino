// old code
// int ObstaclePin = A2;     // Analog pin where the sensor is connected
// int onIR = 7;             // Digital pin to control the IR sensor power
// int ReadObstacle = 0;     // Variable to store the analog reading
// unsigned long startTime = 0;

// void setup() {
//   pinMode(onIR, OUTPUT);        // Set the IR power pin as an output
//   digitalWrite(onIR, LOW);      // Start with the IR sensor off
//   Serial.begin(9600);           // Initialize serial communication at 9600 bps
//   startTime = millis();         // Record the start time
// }

// void loop() {
//   // Check if 2 seconds have passed
//   if (millis() - startTime <= 2000) {  
//     digitalWrite(onIR, HIGH);   // Turn on the IR sensor
//     ReadObstacle = analogRead(ObstaclePin);  // Read the analog value from the sensor
//     Serial.println(ReadObstacle);            // Print the analog sensor value
//     delay(200);                              // Short delay to avoid flooding the Serial Monitor
//   } else {
//     digitalWrite(onIR, LOW);    // Turn off the IR sensor after 2 seconds
//     while (true);               // Stop the loop after 2 seconds
//   }
// }

int ObstaclePin = A2;     // Analog pin where the sensor is connected
int onIR = 7;             // Digital pin to control the IR sensor power
int ReadObstacle = 0;     // Variable to store the analog reading
unsigned long startTime = 0;

void setup() {
  pinMode(onIR, OUTPUT);        // Set the IR power pin as an output
  digitalWrite(onIR, LOW);      // Start with the IR sensor off
  Serial.begin(9600);           // Initialize serial communication at 9600 bps
  startTime = millis();         // Record the start time

  // Print CSV headers
  Serial.println("Time (ms),Sensor Value");
}

void loop() {
  // Check if 2 seconds have passed
  if (millis() - startTime <= 2000) {  
    digitalWrite(onIR, HIGH);   // Turn on the IR sensor
    ReadObstacle = analogRead(ObstaclePin);  // Read the analog value from the sensor
    
    // Print time since start and sensor value in CSV format
    Serial.print(millis() - startTime);
    Serial.print(",");
    Serial.println(ReadObstacle); 
     
    delay(5);  // Short delay to avoid flooding the Serial Monitor
  } else {
    digitalWrite(onIR, LOW);    // Turn off the IR sensor after 2 seconds
    while (true);               // Stop the loop after 2 seconds
  }
}
