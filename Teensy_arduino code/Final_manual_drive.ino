float Kp =1.8;
float Kd = 1.2;
float Ki = 0;
float k = 0.5;
int P, I , D;
int initial, error;
float PIDval;
int FL,FR,BL,BR;
long val ;
long val2 = 0;
int previous;
int my_val;
int steer1;
int pinAIN1 = 14;
int pinAIN2 = 15; //Direction
int pinPWMA = 22; //Speed
int pinPWMB = 23;
int pinBIN1 = 16;
int pinBIN2 = 17;

int pinAIN1_2 = 29;
int pinAIN2_2 = 28; //Direction
int pinPWMA_2 = 20; //Speed
int pinPWMB_2 = 21;
int pinBIN1_2 = 27;
int pinBIN2_2 = 26;

void setup() {
   Serial.begin(9600); // begin transmission
   //Serial.setTimeout(200);
  pinMode(pinPWMA, OUTPUT);
  pinMode(pinPWMB, OUTPUT);
  
  pinMode(pinAIN1, OUTPUT);
  pinMode(pinAIN2, OUTPUT);
  
  pinMode(pinBIN1, OUTPUT);
  pinMode(pinBIN2, OUTPUT);

  pinMode(pinPWMA_2, OUTPUT);
  pinMode(pinPWMB_2, OUTPUT);
    
  pinMode(pinAIN1_2, OUTPUT);
  pinMode(pinAIN2_2, OUTPUT);
  
  pinMode(pinBIN1_2, OUTPUT);
  pinMode(pinBIN2_2, OUTPUT);  
}


void motor_stop()
{
digitalWrite(pinAIN1,HIGH);
digitalWrite(pinAIN2,LOW);

digitalWrite(pinBIN1,HIGH);
digitalWrite(pinBIN2,LOW);

digitalWrite(pinPWMA,LOW);
digitalWrite(pinPWMB,LOW);



digitalWrite(pinAIN1_2,LOW);
digitalWrite(pinAIN2_2,HIGH);

digitalWrite(pinBIN1_2,LOW);
digitalWrite(pinBIN2_2,HIGH);

digitalWrite(pinPWMA_2,LOW);
digitalWrite(pinPWMB_2,LOW);

//delay(200);

}

void motor_move(int(FL),int(FR),int(BL),int(BR))
{
digitalWrite(pinAIN1,HIGH);
digitalWrite(pinAIN2,LOW);

digitalWrite(pinBIN1,HIGH);
digitalWrite(pinBIN2,LOW);

analogWrite(pinPWMA,BR);
analogWrite(pinPWMB,FR);



digitalWrite(pinAIN1_2,LOW);
digitalWrite(pinAIN2_2,HIGH);

digitalWrite(pinBIN1_2,LOW);
digitalWrite(pinBIN2_2,HIGH);

analogWrite(pinPWMA_2,FL);
analogWrite(pinPWMB_2,BL);

Serial.println("out");
Serial.println(FL);
Serial.println(FR);
Serial.println(BL);
Serial.println(BR);

//delay(2000);

}
void loop() 
{
   
    
  //while (Serial.available() == 0) 
      
    val = Serial.parseFloat();
    int button_val = int(val/1000000);
    int acc = int((val-(button_val*1000000))/1000);
    int steer = int((val-(button_val*1000000)-(acc*1000)));
   // Serial.println(button_val);
    //Serial.println(acc);
    //Serial.println(steer);

    steer1 = steer-50;
    
 my_val = (steer1*abs(steer1))/50;
 //Serial.println(my_val);

 //  Serial.println(PIDval); 
 //   if (steer == 0)
  // {
   // steer = val2;
  // }
   //Serial.println(val);
   //val2 = Serial.parseInt();
   //Serial.println(val2);
   //PIDval= PIDloop(steer);
   //Serial.println(PIDval);

if (acc > 20){
    FR = acc - my_val; 
  FL = acc + my_val;
  BR = acc - my_val;
  BL = acc + my_val;
  }
 
else
 {


  FL = 0;
  FR = 0;
  BR = 0;
  BL =0;
  Serial.println("Loop");
  }
  Serial.println(BR);
  motor_move(FL,FR,BL,BR);
  
  
}
