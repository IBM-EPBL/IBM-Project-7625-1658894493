from flask import Flask, render_template, request

app = Flask(__name__,template_folder="",static_folder="assets")
alert = '''<script>alert("{}");</script><meta http-equiv="refresh" content="0;url='/'"/>'''
@app.route('/',methods=['GET','POST']) 

def index():
	if (request.method == "POST"):
		name =  request.form['name']
		email =  request.form['email']
		phone =  request.form['phone']
		if (name=="" or email=="" or phone ==""):
			return alert.format("Please fill all the inputs.")
		return render_template("view.html",name=name,email=email,phone=phone)
	else:
		return render_template("index.html")

app.run(port=80)