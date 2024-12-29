#!/usr/bin/python
#import required Python libraries
import subprocess,sys
import gpio_mpc_modul as mpc


param_url = sys.argv[1];

def getUrl_parameter(url_setting):
 filepath = ('/home/pi/gpio/radio_urls.per')
 with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       if cnt == int(url_setting):
        sl = line.strip()
        print("Line {}: {}".format(cnt, sl))
        return sl
       else:
        line = fp.readline()
        cnt += 1

def init():
 mpc.stop()
 mpc.clear()
 mpc.change(getUrl_parameter(param_url))
 mpc.play()

init();
