import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
    ENV="development"
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'postgres://tgglsmnhnqmtcw:43cb713a679612c64051103450311acd6556e12d989697f8c6ff1ab033c082ce@ec2-54-247-94-127.eu-west-1.compute.amazonaws.com:5432/dk7sdk7pf9j6c'