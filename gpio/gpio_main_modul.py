#!/usr/bin/python 
#import required Python libraries
import RPi.GPIO as GPIO 
import gpio_set_modul as gsm 
import gpio_data_modul as gdm
import time, re, string, sys, array;

# Use BCM GPIO references instead of physical pin numbers

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 

print("Test GPIO");

#pinListTest = [4,23];
pinList = [18,14,15,4,3,2,17,27,23,24,10,22]; 
pinNr = [0,1,2,3,4,5,6,7,8,9,10,11]
pinPort = [0,1,0,1,0,1,0,1,0,1,0,1];
#----------------------#
#|8|7|24|23|11|10|9|22|#
#----------------------#
#|3|2|14|4|15|18|27|17|#
#----------------------# 

#highpins = []; lowpins = []; pinPort = [];

speaker_set = sys.argv[1];
#stateP = sys.argv[2];

def getPinPort():
 pinState = gdm.getPins_parameter(speaker_set)
 count = 0
 for i in str(pinState):
  pinPort[count] = i
  count = count + 1

def setPinPort():
 gdm.setPins(''.join(map(str,pinPort)))
 print ''.join(map(str,pinPort))

def initIP(pinParam):
 if(len(pinParam) > 0):
  pinPort = pinParam;
 else:
  pinPort = [];
 init(pinPort); 

def initOP():
# if(len(sys.argv) > 0):
#  pinPort = sys.argv[1]; else: pinPort = [];
 init(pinPort); 

def closeAll():
 lowPins = pinList;
 highPins = [];
 setAllPins(highPins, lowPins); 

def openAll():
 lowPins = [];
 highPins = pinList;
 setAllPins(highPins, lowPins);

def setPin(pin, state):
 init()
 set = "false"
# print("pin1: ", pin)
 pinN = int(pin)-1
# print("pin2: ", pinN) 
 count = 0
 pnr = 0
 for i in pinNr:
  if(int(i) == int(pinN)):
#   print(pinN, " + ", i)
   set = "true"
   pinS = pinList[i]
   pnr = count
  count = count + 1
# print("count3: " , pnr)
 if(set == "true"):
  if(state == "on"):
   pinPort[pnr] = 1
   gsm.setPin(pinS, "1")
  if(state == "off"):
   pinPort[pnr] = 0 
   gsm.setPin(pinS,"0")
  setPinPort()
 else:
  print("Wrong Pin or State")


# loop through pins and sort by high or low
def initpins(pinCode):
 pin = 0;
 lowPins = [];
 highPins = [];
 for i in pinCode:
  if(int(i) == 0):
   #print("low" , i);
   lowPins.append(pinList[pin])
  else:
   #print("high",i);
   highPins.append(pinList[pin])
  pin = pin + 1;
 setAllPins(highPins, lowPins)

# loop through sortet pins and set high or low
def setAllPins(highPins,lowPins):
 pin = 0
 for i in lowPins:
  #print("low" ,i);
  gsm.setPin(i, "0");
 for j in highPins:
  #print("high" ,j);
  gsm.setPin(j, "1");

# Set all Pins like code
def init():
 getPinPort()
 if (len(pinPort)) != 12:
  print("Wrong pinnumbers")
 else:
  print("pinnumbers ok")
  try:
   initpins(pinPort);
  except KeyboardInterrupt:
   print("Quit");
 
init();
#setPin(int(pinP),stateP)
#setPinPort();
