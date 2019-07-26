int leftWhisker = 5;
int rightWhisker = 7;

void setup() {
  Serial.begin(9600);

  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);
  
}

void loop() {
  int leftWhiskerValue = digitalRead(leftWhisker);
  int rightWhiskerValue = digitalRead(rightWhisker);

//  Serial.print("Left: ");
//  Serial.print(leftWhiskerValue);
//  Serial.print("Right: ");
//  Serial.print(rightWhiskerValue);
//  Serial.println("");

  if(leftWhiskerValue == 0 && rightWhiskerValue == 0){
    Serial.println("Left and right are pressed!!!!!");
  }else if(leftWhiskerValue == 0){
    Serial.print("Left is pressed.");
  }else if(rightWhiskerValue == 0){
    Serial.println("Right is pressed.");
  }else{
    Serial.println("No Whiskers are pressed. :(");
  }

  delay(200);
  

}
