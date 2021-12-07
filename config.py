import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

#possivelmente por essa env var lá no config.py
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/upload')

#decidir sobre usar ou não essa variável de ambiente
#SECRET_KEY = 'um-nome-bem-seguro'