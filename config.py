import os


POSTGRES_HOST = os.environ.get('POSTGRES_HOST', '')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '')
POSTGRES_USER = os.environ.get('POSTGRES_USER', '')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '')
POSTGRES_DB = os.environ.get('POSTGRES_DB', '')
POSTGRES_URL = POSTGRES_HOST + ':' + str(POSTGRES_PORT)

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=POSTGRES_USER, pw=POSTGRES_PASSWORD, url=POSTGRES_URL, db=POSTGRES_DB)


class Config(object):
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TwitterConfig(object):
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY', '')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', '')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', '')
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET', '')
