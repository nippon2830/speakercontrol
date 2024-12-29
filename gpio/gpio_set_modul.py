#!/usr/bin/python import required Python libraries
import RPi.GPIO as GPIO 
import time, re, string, sys;

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

#print("Test GPIO");

# init list with pin parameter

#pinP = sys.argv[1]; 
#stateP = sys.argv[2]; 

def setPin(pin,state):
 if(state == "1"):
  GPIO.setup(pin,GPIO.OUT)
  #print("Pin:", pin, ":", state, " HIGH");
 else:
  GPIO.setup(pin, GPIO.IN)
  #print("Pin:", pin, ":", state, " LOW"); 

def main(pin,state):
 #GPIO.setup(pin, GPIO.OUT); 
 #func = GPIO.gpio_function(pin); 
 #print("Pin:",func); time.sleep(0.5);
 if(state == "s"):
  getStatus(pin);
 else:
  setPin(pin,state); 

def getStatus(pin):
 try:
  with open("/sys/class/gpio/gpio2/direction") as pin:
    status = pin.read(1)
 except:
  print "Remember to export the pin first!"
  status = "Unknown"
 print status
  
#main(int(pinP),stateP);
