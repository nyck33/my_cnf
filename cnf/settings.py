import os
import datetime
from urllib.parse import urljoin

APP_NAME = "cnf"
APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + "system error"

#Flask Settings
CSRF_ENABLES = True

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# looks like a trick to get it to select default True == True
DEBUG = (os.getenv('CNF_DEBUG', 'True') == 'True')
TESTING = (os.getenv('CNF_TESTING', 'True') == 'True')
FLASK_DEBUG = DEBUG
FLASK_BIND = os.getenv('CNF_BIND', 'localhost')
FLASK_PORT = int(os.getenv('CNF_PORT', 8888))
ROOT_URL = 'http://' + FLASK_BIND + ':' + str(FLASK_PORT) + '/'

TEMPLATE_FOLDER = os.path.join(ROOT_PATH, 'cnf', 'templates')
STATIC_FOLDER = os.path.join(ROOT_PATH, 'cnf', 'static')

MONGODB_HOST = os.getenv('CNF_MONGO_HOST', 'localhost')
MONGODB_PORT = int(os.getenv('CNF_MONGO_PORT', 27017))
MONGODB_DB = os.getenv('CNF_MONGO_DB', 'cnf') # name of db

#encryption, cryptographically signs client-side cookies so they cannot be tampered with
#if tampered, session becomes invalid, insecure not to be used production
SECRET_KEY = 'this key is not secure so be careful until it is'

# Flask-User Settings
# from https://flask-user.readthedocs.io/en/latest/configuring_settings.html
USER_APP_NAME = "cnf"
USER_ENABLE_EMAIL = False  # register with email
USER_ENABLE_CONFIRM_EMAIL = False # force users to confirm email
USER_ENABLE_USERNAME = True  # enable username authentication
USER_REQUIRE_RETYPE_PASSWORD = False  # simplify register form
USER_EMAIL_SENDER_NAME = 'nobu'
#USER_EMAIL_SENDER_EMAIL = 'nobu.kim66@gmail.com' # set up Flask Mail for this
USER_ENABLE_CHANGE_USERNAME = True
USER_ENABLE_CHANGE_PASSWORD = True
USER_ENABLE_FORGOT_PASSWORD = True
#USER_ENABLE_REGISTER = True
USER_ENABLE_REGISTRATION = True
USER_ENABLE_REMEMBER_ME = True
USER_AFTER_LOGIN_ENDPOINT = 'main.member_page'
USER_AFTER_LOGOUT_ENDPOINT = 'main.home_page'


# Flask-Mail settings
# For smtp.gmail.com to work, you MUST set "Allow less secure apps" to ON in Google Accounts.
# Change it in https://myaccount.google.com/security#connectedapps (near the bottom).
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = 'nobu.kim66@gmail.com'
MAIL_PASSWORD = 'Ilovetennis99!'
#ADMINS = ['"Admin One" <admin@gmail.com>,]

# Sendgrid settings
#SENDGRID_API_KEY='place-your-sendgrid-api-key-here'
