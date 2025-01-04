#!/usr/bin/python
#import required Python libraries
import sys, subprocess,json;
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

def getInfoJson():
  return json.loads(getInfo())
  

def init():
 i_radio = mpc.info("name").rstrip('\n')
 i_title = mpc.info("title").rstrip('\n')
 i_volume = vol.getVolume() + "%"
 i_pins = gdm.getPins()
 json_string = '{"radio": "' + i_radio + '", "title": "' + i_title + '", "volume": "' + i_volume + '", "pins": "' + i_pins + '"}'
 setInfo(json_string)
 print(getInfo())

init();
