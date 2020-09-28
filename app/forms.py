from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

<<<<<<< HEAD
class loginform(flaskform):
    username =stringfield("username",validators[DataRequired])
    password =passwordfield("password",validators[DataRequired])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

                
                          
=======
class LoginForm(FlaskForm):
    uname = StringField("Username",validators = [DataRequired()])
    password = PasswordField("Password",validators = [DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
>>>>>>> 9e6fd87deb66b1cec55c0e840f4e0985e44559a3
