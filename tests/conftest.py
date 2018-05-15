import pytest

# TODO: use relative path.
import sys
sys.path.append('/Users/lixuanqi/GitHub/NuaaOversea-backend-Flask')

from pytest_mysql import factories

from app import create_app

mysql_my_proc = factories.mysql_proc(
    host='localhost',
    port=7777
)
mysql_my = factories.mysql('mysql_my_proc')

@pytest.fixture
def app():

    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:@127.0.0.1:7777/test?charset=utf8'
    })

    # with app.app_context():
    #     # init_db()
    #
    yield app
    #
    # os.close(db_fd)
    # os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        # return self._client.post(
        #     '/oversea/api/users'
        # )
        pass

    def logout(self):
        pass

@pytest.fixture
def auth(client):
    return AuthActions(client)