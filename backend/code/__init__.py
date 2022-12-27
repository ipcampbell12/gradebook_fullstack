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

    with app.app_context():

        from .routes.assessment import assessment_bp
        from .routes.student import student_bp
        from .routes.subject import subject_bp
        from .routes.teacher import teacher_bp
        from .routes.home import home_bp

        app.register_blueprint(assessment_bp, url_prefix='/assessment')
        app.register_blueprint(student_bp, url_prefix='/student')
        app.register_blueprint(subject_bp, url_prefix='/subject')
        app.register_blueprint(teacher_bp, url_prefix='/teacher')
        app.register_blueprint(home_bp, url_prefix='/home')

        db.create_all()
        return app
