#!/usr/bin/python
import shelve 
from os import path 
from contextlib import closing 

import gpio_mpc_modul as mpc
import gpio_data_url_modul as radio
import gpio_main_modul as speaker
import gpio_vol_modul as volume
from flask import Flask, render_template, jsonify 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/gpio/play") 
def play():
    mpc.play()
    return render_template('index.html')

@app.route("/gpio/stop") 
def stop():
    mpc.stop()
    return render_template('index.html')

@app.route("/gpio/vol_up") 
def vol_up():
    volume.vol_Up()
    return render_template('index.html')

@app.route("/gpio/vol_down") 
def vol_down():
    volume.vol_Down()
    return render_template('index.html')

@app.route("/gpio/radio/1") 
def radio_1():
    radio.init_p("1")
    return render_template('index.html')

@app.route("/gpio/radio/2") 
def radio_2():
    radio.init_p("2")
    return render_template('index.html')

@app.route("/gpio/radio/3") 
def radio_3():
    radio.init_p("3")
    return render_template('index.html')

@app.route("/gpio/radio/4") 
def radio_4():
    radio.init_p("4")
    return render_template('index.html')

@app.route("/gpio/radio/5") 
def radio_5():
    radio.init_p("5")
    return render_template('index.html')

@app.route("/gpio/radio/6") 
def radio_6():
    radio.init_p("6")
    return render_template('index.html')

@app.route("/gpio/radio/7") 
def radio_7():
    radio.init_p("7")
    return render_template('index.html')

@app.route("/gpio/radio/8") 
def radio_8():
    radio.init_p("8")
    return render_template('index.html')

@app.route("/gpio/radio/9") 
def radio_9():
    radio.init_p("9")
    return render_template('index.html')

@app.route("/gpio/speaker/1") 
def speaker_1():
    speaker.init_p("1")
    return render_template('index.html')

@app.route("/gpio/speaker/2") 
def speaker_2():
    speaker.init_p("2")
    return render_template('index.html')

@app.route("/gpio/speaker/3") 
def speaker_3():
    speaker.init_p("3")
    return render_template('index.html')

@app.route("/gpio/speaker/4") 
def speaker_4():
    speaker.init_p("4")
    return render_template('index.html')

@app.route("/gpio/speaker/5") 
def speaker_5():
    speaker.init_p("5")
    return render_template('index.html')

@app.route("/gpio/speaker/6") 
def speaker_6():
    speaker.init_p("6")
    return render_template('index.html')

@app.route("/gpio/speaker/7") 
def speaker_7():
    speaker.init_p("7")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
