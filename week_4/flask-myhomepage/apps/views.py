from flask import render_template, Flask
from apps import app

#app = Flask(__name__)

@app.route('/')
@app.route('/preview')
def index():
#    return "Hello, World!"
	return render_template("preview.html")

@app.route("/main.html")
def second():
	return render_template("main.html")

#if __name__ =="__main__":
#	app.run()