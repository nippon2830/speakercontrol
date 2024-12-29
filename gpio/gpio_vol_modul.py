#!/usr/bin/python
#import required Python libraries
import time, re, string, sys, array;
import subprocess


volume_param = sys.argv[1];
volume_set = "40"
program = "amixer"
line = "-q -M sset PCM " + volume_param +"%"


def init():
 subprocess.Popen([program]+line.split())
 print(volume_param);

init();
