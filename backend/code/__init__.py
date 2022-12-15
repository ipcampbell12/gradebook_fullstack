from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = 'gradebook.db'


def create_app(Config):
    app = Flask(__name__)

    # bring in all the configuration variables
    app.config.from_object(Config)

    db.init_app(app)

    from .models import Teacher, Student, Subject, Assessment, student_assessment

    with app.app_context():
        db.create_all()

    return app
