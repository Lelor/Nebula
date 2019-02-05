from os import environ

from server.database.model import db_uri


class BaseConfig:

    SECRET_KEY = b'q\xaa|\xca|\xb3a{?\xd5\x87\xf7\xf7\xa45\xca'

    # sessions
    SESSION_COOKIE_NAME = 'test-session'

    # JSON formatting
    JSONIFY_PRETTYPRINT_REGULAR = True

    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(BaseConfig):
    XPTO = 'ABC123'
    ENV = 'teste'
    DEBUG = True


class ProdConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False


config_objects = {
    'development': DevConfig(),
    'production': ProdConfig()
}


def get_config():
    return config_objects[environ.get('FLASK_ENV', 'production')]
