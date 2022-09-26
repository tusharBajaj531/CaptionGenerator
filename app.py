<<<<<<< HEAD
from flask import Flask,render_template, redirect,request
import Caption_it

app = Flask(__name__)

@app.route("/")
def start():
	return render_template("index.html")

@app.route("/",methods = ["POST"])
def pred():
	if request.method == "POST":
		f = request.files["userfile"]
		path = f"./static/{f.filename}"
		f.save(path)
		caption = Caption_it.caption_this_image(path)
		result_dic = {
		"image":path,
		"caption":caption
		}


	return render_template("index.html",your_result=result_dic)

if __name__ == "__main__":
=======
from flask import Flask,render_template, redirect,request
import Caption_it

app = Flask(__name__)

@app.route("/")
def start():
	return render_template("index.html")

@app.route("/",methods = ["POST"])
def pred():
	if request.method == "POST":
		f = request.files["userfile"]
		path = f"./static/{f.filename}"
		f.save(path)
		caption = Caption_it.caption_this_image(path)
		result_dic = {
		"image":path,
		"caption":caption
		}


	return render_template("index.html",your_result=result_dic)

if __name__ == "__main__":
>>>>>>> 83c0892079aa331cefae6f2bd69f2933434ad3e3
	app.run(debug=False,host="0.0.0.0")	