import os
basedir = os.path.abspath(os.path.dirname(__file__))
env_dist = os.environ
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@db:3306/{2}?charset=utf8'.format(
        env_dist['DB_USER'],
        env_dist['DB_PASSWORD'],
        env_dist['DB_DATABASE']
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24) # For session encode.
    REDIS_URL = "redis://:root@redis:6379/0"