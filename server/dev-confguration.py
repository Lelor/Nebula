from os.path import join, abspath, dirname

ENV = 'development'
DEBUG = True

SECRET_KEY = b'q\xaa|\xca|\xb3a{?\xd5\x87\xf7\xf7\xa45\xca'

# sessions
SESSION_COOKIE_NAME = 'test-session'

# JSON formatting
JSONIFY_PRETTYPRINT_REGULAR = True

SQLALCHEMY_DATABASE_URI = f'sqlite:///{join(abspath(dirname(__file__)), "storage.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = True