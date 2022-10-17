from flask import Flask, request, render_template

app = Flask(__name__,template_folder="",static_folder="assets")
alert = '''<script>alert("{}");</script><meta http-equiv="refresh" content="0;url='/'"/>'''
@app.route('/', methods = ['GET', 'POST'])

def index():
    global name,qualification,age,email,file
    if(request.method == 'POST'):
        name = request.form['name']
        qualification = request.form['qualification']
        age = request.form['age']
        email = request.form['email']
        if (name =="" or qualification == "" or age =="" or email == ""):
            return alert.format("Please fill all the inputs.")
        return render_template("view.html",name=name,qualification=qualification,age=age,email=email)
    else:
        return render_template("index.html")

app.run(port=80)