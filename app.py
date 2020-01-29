from flask import Flask, render_template, request, redirect, url_for
from database import get_all_memes, create_meme, get_id, change_info
from werkzeug.utils import secure_filename
import os 

ON_COMPUTER = False

app = Flask(__name__)

FULL_PATH = "/home/meet/Desktop/y2-individual-Project-yl1920"

DEFAULT_IMAGE_URL = "/static/img/images.png"
UPLOAD_FOLDER = "/static/img"
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
	memes = get_all_memes()
	memes.reverse()
	print(memes)
	return render_template('index.html', memes = memes)


@app.route('/form' ,methods=["GET","POST"])
def forming():
	if request.method == 'POST':
		title = request.form["title"]
		description= request.form["description"]
		img_url= request.form["img_url"]
		create_meme(title, description,img_url)
		#identity = get_id(title)
		print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh')
		return redirect(url_for("hello_world"))
	else:
		print("HERE")
		return render_template('form.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	error= None
	if request.method == 'POST':
		if request.form['userName'] != 'ido' or request.form['password'] != 'ido123':
			error = 'Please try again.'
			return render_template("admin.html", error=error)
		else:
			return redirect("/edit")
	else:
		return render_template('admin.html', error=error)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
	if request.method == 'GET':
		memes = get_all_memes()
		return render_template("edit.html", memes = memes)		
	else:
		title = request.form["title"]
		description= request.form["description"]
		img_url= request.form["img_url"]
		change_info(title, description, img_url)
		return redirect("/")

# def change_info( title, description, img_url):
# 	declarative_base = session.query all().filter_by(meme_id=meme_id).first()
# 	declarative_base.title = title
# 	declarative_base.description = description
# 	declarative_base.img_url = img_url	
if __name__ == "__main__":
	app.run(host="0.0.0.0")
