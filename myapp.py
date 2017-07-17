
from flask import Flask, render_template, send_from_directory
app = Flask(__name__)




@app.route('/img/<path:path>')
def send_js(path):
    return send_from_directory('img', path)

@app.route('/linux')
def linux():
        return render_template('linux.html')




@app.route('/')
def index():
	return render_template("index.html")


@app.route('/hello/<name>')
def foo(name):
    return render_template('index.html', to=name)



@app.route('/whereami')
def whereami():
	return "Koforidua"







if __name__ == '__main__':
	app.run(host="0.0.0.0")
