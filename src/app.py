from os import getenv
from dotenv import load_dotenv
from flask import Flask
from db import db


app = Flask(__name__)

load_dotenv()
app.config["SQLALCHEMY_DATABASE_URI"] = getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

import routes



