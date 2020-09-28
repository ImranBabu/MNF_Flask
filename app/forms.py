from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class loginform(flaskform):
    username =stringfield("username",validators[DataRequired])
    password =passwordfield("password",validators[DataRequired])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

                
                          
