import os
basedir = os.path.abspath(os.path.dirname(__file__))
env = os.environ
class Config(object):
    ############### YOU SHOULD CONFIGURE ###############

    DB_USER = "root"
    DB_PASSWORD = "root"
    DB_DATABASE = "nuaaoversea"
    DB_URL = '127.0.0.1:3306'
    ROOT_URL = ""

    #####################################################
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8'.format(
        DB_USER,
        DB_PASSWORD,
        DB_URL,
        DB_DATABASE
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TOKEN_SECRET_KEY = os.urandom(24) # For session encode.
