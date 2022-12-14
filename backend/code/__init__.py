from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = 'gradebook.db'


def create_app():
    app = Flask(__name__)

    # bring in all the configuration variables
    app.config.from_object('instance.config.DevConfig')

    db.init_app(app)

    from .models import Teacher, Student, Subject, Assessment, student_assessment


def create_datavase(app):
    if not path.exists('code/' + DB_NAME):
        db.create_all(app=app)
        print('database created!')
