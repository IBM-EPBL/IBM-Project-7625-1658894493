from flask import Flask,render_template, request,redirect;import os

app = Flask(__name__,template_folder="",static_folder="assets")
alert = '''<script>alert("{}");</script><meta http-equiv="refresh" content="0;url='/'"/>'''

@app.route('/',methods=['GET','POST'])
def index():
	global file
	if (request.method == "POST"):
		file = request.files['file']
		if (str(file) == "<FileStorage: '' ('application/octet-stream')>"):
			return alert.format("Please select a file.")
		elif (str(file.filename).lower().endswith(".pdf") == 0):
			return alert.format("Only PDF is allowed")
		file.save("assets/"+str(file.filename))
		return redirect("/upload")
	else:
		return render_template("index.html")

@app.route("/upload")
def upload():
	return render_template("view.html",url=file.filename)

@app.route("/delete")
def delete():
	os.remove(f"assets/{file.filename}")
	return render_template("index.html")

app.run(port=80)