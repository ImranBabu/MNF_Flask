from app import app
from flask import render_template,flash,redirect,url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {"username" : "Imran"}
    a = ["Imran","Muzamil","Surya"]
    return render_template("index.html",title = "Imran's Flask ",user = user,ex_list = a)

@app.route('/login',methods = ["GET","POST"])
def login_fun():
    form = LoginForm()
    if form.validate_on_submit():
        print("Username ---- : ",form.uname.data," Password : ------", form.password.data)
        flash("Login Requested for User {} , remember me = {}".format(form.uname.data,form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html",title = "Sign In",form = form)
