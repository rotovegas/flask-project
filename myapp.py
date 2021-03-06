import os
import paho.mqtt.client as mqtt
from flask import Flask, render_template, send_from_directory

client = mqtt.Client()
client.connect("moorhouseassociates.com", 1883, 60)

app = Flask(__name__)



@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/')
def btn():
	print("button clicked")
	client.publish("test/all", "hello guyz.......@Gomah")
	return ""

@app.route('/img/<path:path>')
def send_js(path):
    return send_from_directory('img', path)



@app.route('/linux')
def linux():
        return render_template('linux.html')




@app.route('/python')
def python():
        return render_template('python.html')


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/hello/<name>')
def foo(name):
    return render_template('index.html', to=name)



@app.route('/whereami')
def whereami():
	return "Koforidua"

