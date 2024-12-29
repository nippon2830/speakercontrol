#!/usr/bin/python
#import required Python libraries
import time, re, string, sys, array;
import subprocess


param_url = sys.argv[1];
program = "mpc"
param_stop = " stop"
param_play = " play"
param_clear = " clear"

def getUrl_parameter(param_url):
 filepath = ('/home/pi/gpio/radio_urls.per')
 with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       if cnt == int(setting):
        sl = line.strip()
        print("Line {}: {}".format(cnt, sl))
        return sl
       else:
        line = fp.readline()
        cnt += 1



def init():
 subprocess.Popen([program]+param_play.split())

init();
