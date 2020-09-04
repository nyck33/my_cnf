"""
conftest.py pytest_fixtures can be accessed by multiple test files
test function has fixture func name as param, then fixture func called and result
passed to test func
"""
import pytest
from cnf.main import setup_app
import pymongo

app = setup_app(dict(
    TESTING=True,
    LOGIN_DISABLED=False,
    MAIL_SUPPRESS_SEND=True,
    SERVER_NAME='localhost',
    WTF_CSRF_ENABLED=False,
))

app.app_context().push()


@pytest.fixture(scope='session')
def app():
    """Makes app parameter available to test funcs"""
    return app


@pytest.fixture(scope='session')
def db():
    return app.db


@pytest.fixture(scope='function')
def session(request):
    """Make a new connection"""
    # Connect to cnf
    client = pymongo.MongoClient("localhost", 27017)
    assert client
    testDB = client['testDB']
    assert client['testDB']

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()