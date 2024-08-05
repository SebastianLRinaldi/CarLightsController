//We always have to include the library
#include "LedControl.h"

/*
 Now we need a LedControl to work with.
 ***** These pin numbers will probably not work with your hardware *****
 pin 12 is connected to the DataIn 
 pin 11 is connected to the CLK 
 pin 10 is connected to LOAD 
 We have only a single MAX72XX.
 */

int DIN = 11;
int CS = 7;
int CLK = 13;

LedControl lc=LedControl(DIN,CLK,CS,1);

/* we always wait a bit between updates of the display */
unsigned long delaytime=1000;

void setup() {
  /*
   The MAX72XX is in power-saving mode on startup,
   we have to do a wakeup call
   */
  lc.shutdown(0,false);
  /* Set the brightness to a medium values */
  lc.setIntensity(0,15);
  /* and clear the display */
  lc.clearDisplay(0);

  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  Serial.println("Starting Car");
}

// Should be a return string for if the light is on or off
void Bothlights(int col, bool active)
{
  lc.setLed(0,0,col,active);
  lc.setLed(0,1,col,active);
}

void lightTest(int col)
{
  Bothlights(col, true);
  delay(delaytime);
  Bothlights(col, false);
}



// Should print with the return what type of lights activated or deactived
void exhaustLights()
{
  int col = 1;
  lightTest(col);
}

void RightRearLights()
{
  int col = 2;
  lightTest(col);
}

void LeftRearLights()
{
  int col = 3;
  lightTest(col);
}

void RightFrontLights()
{
  int col = 5;
  lightTest(col);
}

void LeftFrontLights()
{
  int col = 4;
  lightTest(col);
}

void FogLights()
{
  int col = 6;
  lightTest(col);
}

void DayTimeLights()
{
  int col = 7;
  lightTest(col);
}





void carLights() {
  for(int row=0;row<2;row++) {
    for(int col=1;col<8;col++) {
      lc.setLed(0,row,col,true);
      Serial.print("ROW: ");
      Serial.print(row);
      Serial.print(" COL: ");
      Serial.println(col);
      delay(delaytime);
      lc.setLed(0,row,col,false);
    }
  }
}

void allCarLightPairsTest()
{
  exhaustLights();
  RightRearLights();
  LeftRearLights();
  RightFrontLights();
  LeftFrontLights();
  FogLights();
  DayTimeLights();
}

void loop() { 
  allCarLightPairsTest();
}
