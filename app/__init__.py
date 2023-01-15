#import flask module
from flask import Flask
#create instance of app
app = Flask(__name__)
#import routes from routes.py
from . import routes