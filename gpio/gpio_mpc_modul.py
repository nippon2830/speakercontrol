#!/usr/bin/python
#import required Python libraries
import subprocess

program = "mpc"
param_stop = " stop"
param_play = " play"
param_clear = " clear"
param_add = " add "
param_info = " -f %"
param_current = '% current'

def clear():
 subprocess.Popen([program]+param_clear.split())

def change(param_url):
 param_full = param_add + param_url
 subprocess.Popen([program]+param_full.split())

def stop():
 subprocess.Popen([program]+param_stop.split())

def play():
 subprocess.Popen([program]+param_play.split())

def info(param_val):
 param_all = param_info + param_val + param_current
 info = subprocess.check_output([program]+param_all.split())
 return info
