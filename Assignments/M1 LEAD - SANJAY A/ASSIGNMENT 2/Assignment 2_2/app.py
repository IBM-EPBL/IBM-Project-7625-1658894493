from flask import Flask,render_template, request,make_response,session,redirect
import random; from string import ascii_lowercase

app = Flask(__name__,template_folder="",static_folder="assets")
app.secret_key = '53cr37'
alert = '''<script>alert("{}");</script><meta http-equiv="refresh" content="0;url='/'"/>'''

@app.route('/',methods=['GET','POST']) 
def index():
	global name
	if (request.method == "POST"):
		name = request.form['name']
		session['name'] = name
		if (name==""):
			return alert.format("Please fill name.")
		resp = make_response(redirect("/viewcookie"))
		resp.set_cookie('COOKIE',''.join(random.choice(ascii_lowercase) for _ in range(18)))
		return resp
	else:
		return render_template("index.html")

@app.route("/viewcookie")
def getcookie():
	cookie = request.cookies.get('COOKIE')
	return render_template('view.html',name=name,cookie=cookie)

@app.route("/logout")
def logout():
	session.pop('name',None)
	return redirect("/")
app.run(port=80)
