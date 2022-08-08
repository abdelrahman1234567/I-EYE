void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  //Serial.println(Serial.read());
  Serial.println(Serial.read());
  /*if(Serial.read()=='1'){
    digitalWrite(LED_BUILTIN,HIGH);
    //Serial.println("LED is ON");
  }
  if(Serial.read()=='0'){
    digitalWrite(LED_BUILTIN,LOW);
   // Serial.println("LED is OFF");
  }*/
}
