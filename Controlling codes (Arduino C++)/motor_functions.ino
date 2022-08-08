void Backward(int leftSpeed,int rightSpeed){
  analogWrite(ls,leftSpeed);
  analogWrite(rs,rightSpeed);
  
  digitalWrite(lm1, LOW);
  digitalWrite(lm2, HIGH);

  digitalWrite(rm1, LOW);
  digitalWrite(rm2, HIGH);
}

void Forward(int leftSpeed,int rightSpeed){
  analogWrite(ls,leftSpeed);
  analogWrite(rs,rightSpeed);
  
  digitalWrite(lm1, HIGH);
  digitalWrite(lm2, LOW);

  digitalWrite(rm1, HIGH);
  digitalWrite(rm2, LOW);
}

void Right(int leftSpeed,int rightSpeed){
  analogWrite(ls,leftSpeed);
  analogWrite(rs,rightSpeed);
  
  digitalWrite(lm1, HIGH);
  digitalWrite(lm2, LOW);

  digitalWrite(rm1, LOW);
  digitalWrite(rm2, HIGH);
}

void Left(int leftSpeed,int rightSpeed){
  analogWrite(ls,leftSpeed);
  analogWrite(rs,rightSpeed);
  
  digitalWrite(lm1, LOW);
  digitalWrite(lm2, HIGH);

  digitalWrite(rm1, HIGH);
  digitalWrite(rm2, LOW);
}

void Stop(){
  analogWrite(ls,0);
  analogWrite(rs,0);
}
