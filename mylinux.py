from flask import Flask, render_templates




app= Flask (__name__)





@app.route('/linux.html')
def linux():
	return render_templates('linux.html')




if __name__ =='__main__':
	app.run(host="0.0.0.0")
