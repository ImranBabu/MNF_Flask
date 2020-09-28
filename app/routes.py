from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {"username" : "Imran"}
    a = ["Imran","Muzamil","Surya"]
    return render_template("index.html",title = "Imran's Flask ",user = user,ex_list = a)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html",title = "Sign In",form = form)
