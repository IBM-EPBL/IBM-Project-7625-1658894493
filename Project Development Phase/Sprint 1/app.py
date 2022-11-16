from flask import Flask,render_template,request

app = Flask(__name__,template_folder='template')

@app.route('/', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('signup.html')
    
@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
	app.run(port=5000,debug=True)