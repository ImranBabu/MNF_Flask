from app import app
from flask import render_template,flash,redirect,url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index1')
def index():
    user = {"username" : "Imran"}
    a = ["Imran","Muzamil","Surya"]
    return render_template("index.html",title = "Imran's Flask ",user = user,ex_list = a)

@app.route('/login',methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login Requested for User {} , remember me = {}".format(form.uname.data,form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html",title = "Sign In",form = form)
