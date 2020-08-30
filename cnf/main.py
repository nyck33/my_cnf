'''
app.config.from_object(cnf.settings):  https://flask.palletsprojects.com/en/1.1.x/config/
https://flask-user.readthedocs.io/en/latest/mongodb_app.html
'''

import warnings
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_script import Server, Manager
from flask_bootstrap import Bootstrap
from flask_user import login_required, UserManager, UserMixin
import datetime

import cnf.settings
import cnf.scripts
import cnf.login_form

# pymongo has issues...
warnings.filterwarnings("ignore", category=DeprecationWarning, module='mongoengine')

#app=None

def setup_app():
    app = Flask(
        __name__,
        #static_url_path='',
        #static_folder='static',
        static_folder=cnf.settings.STATIC_FOLDER,
        template_folder=cnf.settings.TEMPLATE_FOLDER,
    )
    app.config.from_object(cnf.settings)
    # configure encryption key
    # app.config['USER_EMAIL_SENDER_EMAIL'] = ''
    with app.app_context():
        app.db = MongoEngine(app)
        app.bootstrap = Bootstrap(app)
        app.manager = Manager(app)
        app.manager.add_command(
            'runserver',
            Server(
                host=app.config['FLASK_BIND'],
                port=app.config['FLASK_PORT']
            )
        )
        app.manager.add_command('import', cnf.scripts.Import())

        # Define User document
        # NB: Make sure to add flask_user UserMixin
        class User(app.db.Document, UserMixin):
            #email_confirmed_at = app.db.StringField('confirmed at', datetime.datetime.now())
            active = app.db.BooleanField(default=True)
            # User info
            first_name = app.db.StringField(default='')
            last_name = app.db.StringField(default='')
            email = app.db.StringField(default='')
            # User authentication info
            username = app.db.StringField(default='')
            password = app.db.StringField()
            # Relationships
            roles = app.db.ListField(app.db.StringField(), default=[])

    user_manager = UserManager(app, app.db, User)

    return app


def main(test=False):  # pragma: no cover
    app = setup_app()

    # Import your views!
    with app.app_context():
        import cnf.views
    app.manager.run()
    # if test == True, return app
    #if test:
     #   return app

'''
if __name__ == "__main__":  # pragma: no cover
    app = setup_app()

    # Import your views!
    with app.app_context():
        import cnf.views
    #app.run()
    app.manager.run()

'''

#python cnf/main.py runserver


