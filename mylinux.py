from flask import Flask, render_linux




app= Flask (__name__)





@app.route('/linux.html')
def mylinux():
	return render_linux('linux.html')




if __name__ =='__main__':
	app.run(host="0.0.0.0")
