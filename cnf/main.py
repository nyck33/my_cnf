
'''
app.config.from_object(cnf.settings):  https://flask.palletsprojects.com/en/1.1.x/config/
https://flask-user.readthedocs.io/en/latest/mongodb_app.html
'''
import warnings
from flask import Flask, Blueprint
from flask_mongoengine import MongoEngine
from flask_script import Server, Manager
from flask_bootstrap import Bootstrap
from flask_user import login_required, UserManager, UserMixin
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

from datetime import datetime

import cnf.settings
import cnf.scripts
import cnf.login_form

# pymongo has issues...
warnings.filterwarnings("ignore", category=DeprecationWarning, module='mongoengine')

#instantiate Flask extensions
csrf_protect = CSRFProtect()
mail = Mail()


def setup_app(extra_config_settings={}):
    app = Flask(
        __name__, # special variable that gets string val of __main__ when executing script
        #static_url_path='',
        #static_folder='static',
        static_folder=cnf.settings.STATIC_FOLDER,
        template_folder=cnf.settings.TEMPLATE_FOLDER,
    )

    app.config.from_object(cnf.settings)
    # load extra settings from extra config settings param
    app.config.update(extra_config_settings)

    with app.app_context():
        app.db = MongoEngine(app)
        mail.init(app)
        csrf_protect.init_app(app)
        #register blueprints
        from cnf.views import register_blueprints
        register_blueprints(app)

        # Define bootstrap is hidden_field for flask bootstrap's
        # bootstrap wtf.html
        from wtforms.fields import HiddenField

        def is_hidden_field_filter(field):
            return isinstance(field, HiddenField)

        app.jinja_env.globals['bootstrap_is_hidden_field'] = is_hidden_field_filter
        #init_email_error_handler(app)
        from cnf.models import User
        from cnf.views.main_views import user_profile_page

        #setup Flask-User to handle user account related issues
        user_manager = UserManager(app, app.db, User)

        @app.context_processor
        def context_processor():
            return dict(user_manager=user_manager)

        app.bootstrap = Bootstrap(app)
        app.manager = Manager(app)
        app.manager.add_command(
            'runserver',
            Server(
                host=app.config['FLASK_BIND'],
                port=app.config['FLASK_PORT']
            )
        )
        # import csv files
        app.manager.add_command('import', cnf.scripts.Import())

    return app


def main(test=False):  # pragma: no cover
    app = setup_app()

    # Import your views!
    with app.app_context():
        import cnf.views
    app.manager.run() 


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
