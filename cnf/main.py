import warnings
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_script import Server, Manager
from flask_bootstrap import Bootstrap

import cnf.settings
import cnf.scripts


# pymongo has issues...
warnings.filterwarnings("ignore", category=DeprecationWarning, module='mongoengine')


def setup_app():
    app = Flask(
        __name__,
        template_folder=cnf.settings.TEMPLATE_FOLDER,
    )
    app.config.from_object(cnf.settings)
    with app.app_context():
        app.db = MongoEngine(app)
<<<<<<< HEAD
        #app.bootstrap = Bootstrap(app)
=======
        app.bootstrap = Bootstrap(app)
>>>>>>> edd871ec905f2483e8cf4a63ad773fe1efd1881d
        app.manager = Manager(app)
        app.manager.add_command(
            'runserver',
            Server(
                host=app.config['FLASK_BIND'],
                port=app.config['FLASK_PORT']
            )
        )
        app.manager.add_command('import', cnf.scripts.Import())

    return app


def main():  # pragma: no cover
    app = setup_app()

    # Import your views!
    with app.app_context():
        import cnf.views
    #app.run()
    app.manager.run()
<<<<<<< HEAD

'''
if __name__== "__main__":  # pragma: no cover
    app = setup_app()

=======

'''
if __name__== "__main__":  # pragma: no cover
    app = setup_app()

>>>>>>> edd871ec905f2483e8cf4a63ad773fe1efd1881d
    # Import your views!
    with app.app_context():
        import cnf.views
    #app.run()
    app.manager.run()
<<<<<<< HEAD
=======


python cnf/main.py runserver
>>>>>>> edd871ec905f2483e8cf4a63ad773fe1efd1881d
'''