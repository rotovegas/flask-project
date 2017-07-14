from flask import Flask
app = Flask(__name__)

#def index():
#	return "hello"

@app.route('/')
def index():
	return "hello"
@app.route('/whereami')
def whereami():
	return "Koforidua"
if __name__ == '__main__':
	app.run(host="0.0.0.0")
