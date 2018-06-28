import click
from flask import Flask, request
from flask.cli import with_appcontext
from flask_restful import Api
from config import Config

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

from app.models import db, Country, Research, Recommendation, Project, Tag

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # init db
    db.init_app(app)

    # Handle request.
    @app.before_request
    def before_request():
        print(request.headers)

    # init RESTful api

    api = Api(app, prefix=Config.ROOT_URL)

    api.add_resource(Applications, '/applications')
    api.add_resource(Application, '/applications/<application_id>')

    api.add_resource(Applicants, '/applicants')
    api.add_resource(Applicant, '/applicants/<applicant_id>')

    api.add_resource(Tokens, '/tokens')

    api.add_resource(Users, '/users')

    api.add_resource(ApplicationSearch, '/search/applications')

    api.add_resource(Tags, '/tags')

    api.add_resource(Countries, '/countries')

    api.add_resource(Recommendations, '/recommendations')

    api.add_resource(Researches, '/researches')

    api.add_resource(Projects, '/projects')

    api.init_app(app)

    # add commands to cli.
    app.cli.add_command(init_db_command)

    return app

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# TODO: import from sql.
def init_db():
    db.drop_all()
    db.create_all()

    # Init tag
    db.session.add(Tag(id=1, name="渣三维"))
    db.session.add(Tag(id=2, name="转专业"))
    db.session.add(Tag(id=3, name="高GT"))
    db.session.add(Tag(id=4, name="高GPA"))

    # Init project
    db.session.add(Project(id=1, name="无相关实习经历，有个人项目", value=2))
    db.session.add(Project(id=2, name="国内小公司实习", value=2))
    db.session.add(Project(id=3, name="国内大公司实习", value=3))
    db.session.add(Project(id=4, name="BAT实习", value=4))
    db.session.add(Project(id=5, name="外企实习", value=5))

    # Init Recommendation
    db.session.add(Recommendation(id=1, name="无推荐信", value=1))
    db.session.add(Recommendation(id=2, name="国内普通推", value=2))
    db.session.add(Recommendation(id=3, name="海外普通推", value=3))
    db.session.add(Recommendation(id=4, name="国内牛推", value=4))
    db.session.add(Recommendation(id=5, name="海外牛推", value=5))

    # Init Research
    db.session.add(Research(id=1, name="无科研经历", value=1))
    db.session.add(Research(id=2, name="初步的科研经历", value=2))
    db.session.add(Research(id=3, name="大学实验室做过较深入的研究", value=3))
    db.session.add(Research(id=4, name="1~3个月的海外研究经历", value=4))
    db.session.add(Research(id=5, name="大于3个月的海外研究经历", value=5))

    # Init Country
    db.session.add(Country(id=1, name="美国"))
    db.session.add(Country(id=2, name="英国"))
    db.session.add(Country(id=3, name="加拿大"))
    db.session.add(Country(id=4, name="澳大利亚"))
    db.session.add(Country(id=5, name="德国"))
    db.session.add(Country(id=6, name="法国"))
    db.session.add(Country(id=7, name="香港"))
    db.session.add(Country(id=8, name="日本"))
    db.session.add(Country(id=9, name="新加坡"))

    db.session.commit()



# https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc