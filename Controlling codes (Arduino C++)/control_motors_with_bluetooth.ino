#define ls 7
#define rs 3

#define lm1 22
#define lm2 23

#define rm1 26
#define rm2 27
int last = 0;
void setup(){
  pinMode(ls,OUTPUT);
  pinMode(rs,OUTPUT);
  
  pinMode(lm1,OUTPUT);
  pinMode(lm2,OUTPUT);
  pinMode(rm1,OUTPUT);
  pinMode(rm2,OUTPUT);
  Serial.begin(9600);  
  pinMode(13,OUTPUT);
}

void loop(){
  if(Serial.available()){
    int x = Serial.read();
    //Serial.println(x);
    if(x == 's')last = 0;
    else if(x == 'l') last=1;
    else if(x == 'r') last=2;
    else if(x == 'f') last=3;
    else if(x == 'b') last=4;
  }
  if(last == 0){
    //Serial.println("STOP");
    Stop();
  }
  else if(last == 1){
    //Serial.println("LEFT");
    Left(150,150);
  }
  else if(last == 2){
    //Serial.println("RIGHT");
    Right(150,150);
  }
  else if(last == 3){
    //Serial.println("FORWARD");
    Forward(150,150);
  }
  else{
    //Serial.println("BACKWARD");
    Backward(150,150);
  }
}
