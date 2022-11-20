from flask import Flask,render_template,redirect,request,session
from flask_session import Session
from flask_mail import Mail,Message
import ibm_db
import secrets

app = Flask(__name__,template_folder='template')

secret_key = secrets.token_hex(16)
app.secret_key = secret_key
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

mail = Mail(app)

#Configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '7376192IT185@smartinternz.com'
app.config['MAIL_PASSWORD'] = 'PNTIBMJc'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


#IBM DB2 Database Connecting and Retreiving
hostname = "55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
uid = "tcw14000"
pwd = "tIIfDfPaQSrD84SC"
driver = "{IBM DB2 ODBC DRIVER}"
db = "bludb"
port = "31929"
protocol = "TCPIP"
cert = "DigiCertGlobalRootCA.crt"

dsn = (
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "UID={3};"
    "SECURITY=SSL;"
    "SSLServerCertificate={4};"
    "PWD={5};"
).format(db, hostname, port, uid, cert, pwd)

print(dsn)
conn = ibm_db.connect(dsn, "", "")


#Routing Pages using the Pyhton Flask
@app.route('/', methods=['GET','POST'])
def login():
    msg = ""
    uid = ""
    if request.method=='GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        sql = "SELECT * FROM USERS WHERE EMAIL=? AND PASSWORD=?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        if account:
            uid = (account["USERNAME"])
            return render_template('index.html',uid = uid)
        else:
            msg = "Entered Username or Password is wrong!!!"
            return render_template('login.html',msg = msg)


@app.route('/signup', methods=['GET','POST'])
def signup():
    msg = ''
    if request.method=='GET':
        return render_template('signup.html')
    if request.method=='POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if(username!="" and email!="" and password!=""):
            print(username,email,password)
            sql = "INSERT INTO USERS VALUES(?,?,?)"
            stmt = ibm_db.prepare(conn,sql)
            ibm_db.bind_param(stmt,1,username)
            ibm_db.bind_param(stmt,2,email)
            ibm_db.bind_param(stmt,3,password)
            ibm_db.execute(stmt)
            return render_template('index.html',uid = username)
        else:
            msg ='Please fill out the necessary details'
            return render_template('signup.html',msg=msg)

@app.route("/logout")
def logout():
    session.clear()       
    return redirect("/")

if __name__ == '__main__':
	app.run(port=5000,debug=True)