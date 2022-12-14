
from os import environ, path
from dotenv import load_dotenv

# don't know what this does

# path to current file
basedir = path.abspath(path.dirname(__file__))

# connect to data stored in .env file
load_dotenv(path.join(basedir, '.env'))


# Base configuration
class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# HEY CHECK IT OUT! THAT'S SOME CLASS INHERITANCE!
class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
