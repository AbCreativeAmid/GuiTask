import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG 		            = False
    TESTING      	        = False
    CSRF_ENABLED            = True
    SECRET_KEY 	            = os.environ.get('SECRET_KEY') or 'if-you-can-then-guess'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    MAX_CONTENT_LENGTH = 4*1024*1024    

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
