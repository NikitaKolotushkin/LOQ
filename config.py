import os
import random
import string

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    TESTING: bool = True
    SECRET_KEY: str = os.environ.get('SECRET_KEY') or "".join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(25))

    SQLALCHEMY_DATABASE_URI: str = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                                  'postgresql+psycopg2://postgres@db:5432/afo?client_encoding=utf8')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    TEMPLATES_AUTO_RELOAD = True
    UPLOAD_FOLDER: str = os.path.join(basedir, 'uploads')
    JSON_AS_ASCII: bool = True
    HOST: str = os.environ.get('APP_HOST', '0.0.0.0')
    PORT: int = int(os.environ.get('APP_PORT', 5000))
    RELOADER: bool = False
    DEBUG: bool = bool(os.environ.get('DEBUG', False))

    SECURITY_PASSWORD_SALT: str = 'MFxZkRG3Dv4wxLWK9Ujs5DV'


class DebugConfig(Config):
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                                  'postgresql+psycopg2://postgres@localhost:65534/eventselector')
    DEBUG: bool = True
    RELOADER: bool = True
