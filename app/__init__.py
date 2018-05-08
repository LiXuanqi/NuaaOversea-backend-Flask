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
from app.resources.token import Tokens, Token
from app.resources.search import ApplicationSearch

from app.resources.tag import Tags
from app.resources.country import Countries
from app.resources.recommendation import Recommendations
from app.resources.research import Researches
from app.resources.project import Projects

api.add_resource(Applications, '/applications')
api.add_resource(Application, '/applications/<application_id>')

api.add_resource(Applicants, '/applicants')
api.add_resource(Applicant, '/applicants/<applicant_id>')

api.add_resource(Tokens, '/tokens')
api.add_resource(Token, '/tokens/<access_token>')

api.add_resource(Users, '/users')

api.add_resource(ApplicationSearch, '/search/applications')

api.add_resource(Tags, '/tags')

api.add_resource(Countries, '/countries')

api.add_resource(Recommendations, '/recommendations')

api.add_resource(Researches, '/researches')

api.add_resource(Projects, '/projects')

# https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc