#!/usr/bin/python
#import required Python libraries
import sys, subprocess;

volume_param = "80";

if len(sys.argv) > 1:
    volume_param = sys.argv[1];

program = "amixer"
program_param = "-q -M sset PCM "
program_post = "%"

#write pin to file
def setVolume(vol_set):
 fobj_out = open("/home/pi/gpio/gpio_volume.per","w")
 fobj_out.write(vol_set)
 fobj_out.close()

#read and return pin from file
def getVolume():
 fobj = open("/home/pi/gpio/gpio_volume.per")
 for line in fobj:
   return line.rstrip()
 fobj.close()

def vol_Up():
 vol_now = int(getVolume())
 if vol_now < 91: 
  vol_new = vol_now + 10
  init_p(str(vol_new))

def vol_Down():
 vol_now = int(getVolume())
 if vol_now > 10: 
  vol_new = vol_now - 10
  init_p(str(vol_new))

def init_p(vol_set):
 setVolume(vol_set)
 init()

def init():
 line = program_param + getVolume() + program_post
 subprocess.Popen([program]+line.split())
 #print(line)

#init_p(volume_param);
