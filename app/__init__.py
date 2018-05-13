from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

from config import Config


app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)

app.debug = True

redis_store = FlaskRedis(app)
db = SQLAlchemy(app)

from app.resources.application import Applications, Application
from app.resources.applicant import Applicants, Applicant

from app.resources.user import Users
from app.resources.token import Tokens
from app.resources.search import ApplicationSearch

from app.resources.tag import Tags
from app.resources.country import Countries
from app.resources.recommendation import Recommendations
from app.resources.research import Researches
from app.resources.project import Projects

api.add_resource(Applications, Config.ROOT_URL + '/applications')
api.add_resource(Application, Config.ROOT_URL + '/applications/<application_id>')

api.add_resource(Applicants, Config.ROOT_URL + '/applicants')
api.add_resource(Applicant, Config.ROOT_URL + '/applicants/<applicant_id>')

api.add_resource(Tokens, Config.ROOT_URL + '/tokens')

api.add_resource(Users, Config.ROOT_URL + '/users')

api.add_resource(ApplicationSearch, Config.ROOT_URL + '/search/applications')

api.add_resource(Tags, Config.ROOT_URL + '/tags')

api.add_resource(Countries, Config.ROOT_URL + '/countries')

api.add_resource(Recommendations, Config.ROOT_URL + '/recommendations')

api.add_resource(Researches, Config.ROOT_URL + '/researches')

api.add_resource(Projects, Config.ROOT_URL + '/projects')

# https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc