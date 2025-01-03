#!/usr/bin/python
#import required Python libraries
import sys, subprocess;
import gpio_mpc_modul as mpc
import gpio_vol_modul as vol
import gpio_data_modul as gdm


#write pin to file
def setInfo(info_set):
 fobj_out = open("/home/pi/gpio/gpio_info.per","w")
 fobj_out.write(info_set)
 fobj_out.close()

#read and return pin from file
def getInfo():
 fobj = open("/home/pi/gpio/gpio_info.per")
 for line in fobj:
   return line.rstrip()
 fobj.close()

def init():
 print(mpc.info("name"))
 print(mpc.info("title"))
 print(vol.getVolume() + "%")
 print(gdm.getPins())

init();
