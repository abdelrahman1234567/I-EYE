#define ls 7
#define rs 3

#define lm1 22
#define lm2 23

#define rm1 26
#define rm2 27

void setup() {
   pinMode(ls,OUTPUT);
   pinMode(rs,OUTPUT);
   
   pinMode(lm1,OUTPUT);
   pinMode(lm2,OUTPUT);
   pinMode(rm1,OUTPUT);
   pinMode(rm2,OUTPUT);
}

void loop() {
  analogWrite(ls,150);
  analogWrite(rs,150);
  //Forward
  digitalWrite(lm1, LOW);
  digitalWrite(lm2, HIGH);

  digitalWrite(rm1, LOW);
  digitalWrite(rm2, HIGH);
  
  delay(2000);
  
  //Backward
  digitalWrite(lm1, HIGH);
  digitalWrite(lm2, LOW);

  digitalWrite(rm1, HIGH);
  digitalWrite(rm2, LOW);

  delay(2000);

  //Left
  digitalWrite(lm1, LOW);
  digitalWrite(lm2, HIGH);

  digitalWrite(rm1, HIGH);
  digitalWrite(rm2, LOW);

  delay(2000);

  //Right
  digitalWrite(lm1, HIGH);
  digitalWrite(lm2, LOW);

  digitalWrite(rm1, LOW);
  digitalWrite(rm2, HIGH);

  delay(2000);
}
