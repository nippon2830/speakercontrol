#!/usr/bin/python
import shelve 
from os import path 
from cPickle import HIGHEST_PROTOCOL 
from contextlib import closing 
from flask import Flask, url_for 
import gpio_main_modul as gpio 

SHELVE_DB = 'shelve.db' 
app = Flask(__name__) 
app.config.from_object(__name__) 
db = shelve.open(path.join(app.root_path, app.config['SHELVE_DB']),protocol=HIGHEST_PROTOCOL, writeback=True) 

@app.route("/gpio/change/<pinParam>") 
def setGpio(pinParam):
  db.setdefault('messages', [])
  db['messages'] = (pinParam)
  gpio.initIP(pinParam);
  return pinParam; 

@app.route("/gpio/nochange/<pinParam>") 
def setNoGpio(pinParam):
  gpio.initIP(pinParam);
  return pinParam; 

@app.route('/gpio/status') 
def getStatus():
 return app.response_class(''.join(db['messages']), mimetype='text/plain') 

@app.route('/gpio/off') 
def gpioOff():
 gpio.closeAll();
 db.setdefault('messages', [])
 db['messages'] = ("0000000000000000")
 return "GPIO OFF!" 

@app.route('/gpio/on') 
def gpioOn():
 gpio.openAll();
 db.setdefault('messages', [])
 db['messages'] = ("1111111111111111")
 return "GPIO ON!" 

@app.route("/") 
def hello():
 return "GPIO Test!" 

def init():
 gpio.initIP(db['messages']); 

with closing(db): 

if __name__ == "__main__":
 init();
 app.run(host='0.0.0.0', port=82, debug=True)
