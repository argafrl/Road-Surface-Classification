#include <Arduino.h>

#define pwm1 5
#define pwm2 6
#define pwm3 9
#define pwm4 10

// Kerikil 20
// Paving 30
// Aspal 40
// Lantai 50

void setup() {
  pinMode(pwm1, OUTPUT);
  pinMode(pwm2, OUTPUT);
  pinMode(pwm3, OUTPUT);
  pinMode(pwm4, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(1);
}
int i;
int isStop = 0;
int kiri = 0;
int kanan = 0;
int incrementDecrement = 5;
int handleLeftWheel = 0;
int handleRightWheel = 0;

void adjustSpeed(int leftWheel, int rightWheel) {
  kiri = leftWheel;
  kanan = 0.84 * rightWheel;
};

void setSpeed(int inputSpeed){
    if (kiri < inputSpeed)
        {
            if (kiri >= inputSpeed-incrementDecrement)
            {
                adjustSpeed(inputSpeed, inputSpeed);
            }
            else
            {
                handleLeftWheel+=incrementDecrement;
                handleRightWheel+=incrementDecrement;
                adjustSpeed(handleLeftWheel, handleRightWheel);
            }
            analogWrite(pwm1, 0);
            analogWrite(pwm2, kiri);
            analogWrite(pwm3, 0);
            analogWrite(pwm4, kanan);
            delay(50); 
        }
    if (kiri > inputSpeed)
    {
        if (kiri <= inputSpeed+incrementDecrement)
        {
            adjustSpeed(inputSpeed, inputSpeed);
        }
        else
        {
            handleLeftWheel-=incrementDecrement;
            handleRightWheel-=incrementDecrement;
            adjustSpeed(handleLeftWheel, handleRightWheel);
        }
        analogWrite(pwm1, 0);
        analogWrite(pwm2, kiri);
        analogWrite(pwm3, 0);
        analogWrite(pwm4, kanan);
        delay(50); 
    }
};

void loop() {
  if (Serial.available() > 0)
  {
    int data;
    i = Serial.readString().toInt();
    if (i == 5){
      isStop = 1;
    } else {
      if (i == 0 && isStop == 0){
        // Aspal
        setSpeed(40);
      } else if (i == 1 && isStop == 0){
        // Kerikil
        setSpeed(20);
      } else if (i == 2 && isStop == 0){
        // Lantai
        setSpeed(50);
      } else if (i == 4 && isStop == 0){
        // Paving
        setSpeed(30);
      }       
    }

    if (isStop == 1){
      setSpeed(0);
    };
    
    delay(100);

    Serial.println(String(kiri) + " - " + String(kanan));
  }
}