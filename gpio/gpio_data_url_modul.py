#!/usr/bin/python
#import required Python libraries
import subprocess,sys
import gpio_mpc_modul as mpc
import gpio_vol_modul as vol

param_url = "1";

if len(sys.argv) > 1:
    param_url = sys.argv[1];

def getUrl_parameter():
 filepath = ('/home/pi/gpio/radio_urls.lst')
 with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       if cnt == int(getUrl()):
        sl = line.strip()
        #print("Line {}: {}".format(cnt, sl))
        return sl
       else:
        line = fp.readline()
        cnt += 1

#write pin to file
def setUrl(url_selected):
 fobj_out = open("/home/pi/gpio/gpio_url.per","w")
 fobj_out.write(url_selected)
 fobj_out.close()

#read and return pin from file
def getUrl():
 fobj = open("/home/pi/gpio/gpio_url.per")
 for line in fobj:
   return line.rstrip()
 fobj.close()

def next():
 url_now = int(getUrl())
 if url_now < 9: 
  url_new = url_now + 1
 else:
  url_new = 1 
 init_p(str(url_new))

def prev():
 url_now = int(getUrl())
 if url_now > 2: 
  url_new = url_now - 1
 else:
  url_new = 9
 init_p(str(url_new))

def init_p(new_url):
 setUrl(new_url)
 init()

def init():
 vol.init_p("80")
 mpc.stop()
 mpc.clear()
 mpc.change(getUrl_parameter())
 mpc.play()

init_p(param_url);
