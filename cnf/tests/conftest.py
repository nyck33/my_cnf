"""
conftest.py pytest_fixtures can be accessed by multiple test files
test function has fixture func name as param, then fixture func called and result
passed to test func

added localhost.localdomain to /etc/hosts
"""
import pytest
from cnf.main import setup_app
import pymongo

config_name = 'testing'
the_app = setup_app(config_name, dict(
                    TESTING=True,
                    LOGIN_DISABLED=False,
                    MAIL_SUPPRESS_SEND=True,
                    SERVER_NAME='localhost.localdomain',
                    WTF_CSRF_ENABLED=False,
                ))

# the_app = setup_app()

the_app.app_context().push()


@pytest.fixture(scope='session')
def app():
    """Makes app parameter available to test funcs"""
    return the_app


@pytest.fixture(scope='session', autouse=True)
def db():
    """Create a test copy of cnf for session"""
    client = pymongo.MongoClient("localhost", 27017)
    if not client['cnf_test']:
        client.admin.command('copydb', fromdb='cnf',
                             todb='cnf_test')
    db = client['cnf_test']
    #delete example_user from user collection
    user_coll = db.users
    myquery = {"username": "example_user"}
    user_coll.delete_one(myquery)
    return db


@pytest.fixture(scope='function')
def data():
    pass


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


