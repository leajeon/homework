"""
settings.py

Configuration for Flask app

"""
import os
from datetime import timedelta


class Config(object):
    # Set secret key to use session
    SECRET_KEY = "likelion-flaskr-secret-key"
    debug = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "maturity0324@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///blog?instance=loyal-semiotics-662:newprojectdb'
    migration_directory = 'migrations'

