'''
from JungeAlexander import parent dir module
https://flask.palletsprojects.com/en/1.1.x/appcontext/#creating-an-application-context
Application Context:
The application context keeps track of the application-level data during a request,
CLI command, or other activity.  Access current_app and g proxies instead of
passing around application to each function.
current_app points to the application handling the current activity.
Flask automatically pushes application context when handling request,
View funcs, error handlers and other funcs that run during request will have
access to current_app.

'''
import unittest

# for importing module from parent dir
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from flask import current_app as app
from cnf.main_test import app

class FlaskClientTestCase(unittest.TestCase):

    def setUp(self):

        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

        #self.app_context = self.app.app_context()
        #self.app_context.push()
        # self.tester or self.client
        self.tester = self.app.test_client(self) # , use_cookies=True)

    def test_home_page(self):
        #tester = app.test_client(self)
        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Register' in response.get_data(as_text=True))

    def test_users(self):
        """
        1.  make a fake user and check that he she is in the users collection
        2.  then delete user and check that he she is gone
        3.  make two users with same name, check that this does not happen
        4.  test all password, username requirements (chars)
        """
        pass

    def test_search(self):
        """
        1.  test a random food and make sure it's the correct one
        2.  test nonsense input
        """
        pass

    def test_show(self):
        """
        1. test that food_id from search and info displayed match
        :return:
        """
        pass


if __name__ == '__main__':
    with app.app_context():
        import cnf.views
    unittest.main()



