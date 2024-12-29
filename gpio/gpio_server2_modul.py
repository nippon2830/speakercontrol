#!/usr/bin/python
import shelve 
from os import path 
from cPickle import HIGHEST_PROTOCOL 
from contextlib import closing 
import gpio_main_modul as gpio 
import gpio_mpc_modul as mpc
from flask import Flask, render_template, url_for 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/gpio/play") 
def play():
    mpc.play()

@app.route("/gpio/stop") 
def stop():
    mpc.stop()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
