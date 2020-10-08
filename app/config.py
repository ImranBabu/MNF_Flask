import os

class Config(object):
    SECRET_KEY = "Module_not_Found"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath("app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
