from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

def setup_db(app, database_path = database_path):
    if database_path.startswith("postgres://"):
        database_path = database_path.replace("postgres://", "postgres://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.app = app
    db.init_app(app)
    db.create_all()

'''
@TODO:
Create models
'''
