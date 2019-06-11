import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql+pg8000://Feeva:password@localhost:5432/bookreview'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
