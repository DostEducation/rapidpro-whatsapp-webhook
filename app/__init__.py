from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.mixins import *

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object("config")

db.init_app(app)
