from os import getenv
from dotenv import load_dotenv
from flask import Flask
from db import db

def create_app():
    flask_app = Flask(__name__)

    load_dotenv()
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = \
        getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(flask_app)
    return flask_app

app = create_app()

import routes # pylint: disable=unused-import, wrong-import-position, cyclic-import
