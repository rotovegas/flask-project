from flask import Flask, render_template
app = Flask(__name__)

#def index():
#	return "hello"

@app.route('/')
def index():
	return render_template("index.html")
@app.route('/whereami')
def whereami():
	return "Koforidua"
if __name__ == '__main__':
	app.run(host="0.0.0.0")
