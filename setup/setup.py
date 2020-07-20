from flask import Flask
from flask_pymongo import PyMongo
import setup

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/data-monitoring'
setup.db = PyMongo(app)
