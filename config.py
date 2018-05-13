import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24) # For session encode.
    ############### YOU SHOULD CONFIGURE ###############
    REDIS_URL = "redis://:root@redis:6379/0"
    DB_USER = 'nuaa'
    DB_PASSWORD = 'nuaa'
    DB_DATABASE = 'oversea'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@db:3306/{2}?charset=utf8'.format(
        DB_USER,
        DB_PASSWORD,
        DB_DATABASE
    )
    ROOT_URL = "/api"