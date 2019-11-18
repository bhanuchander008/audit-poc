from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_marshmallow import Marshmallow
import os
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
app.config["SQLALCHEMY_ECHO"] = True


ma = Marshmallow(app)
db = SQLAlchemy(app)
db.init_app(app)





class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'



class ProductionConfig(Config):
    DEVELOPMENT = True
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://caratred:Welcome@123@localhost/auditpoc"



class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = False



class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Welcome@123@104.199.146.29/auditpoc"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True




class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
    )
