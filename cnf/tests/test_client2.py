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

from flask import current_app as app, url_for, request, session, redirect
from cnf.main_test import app

import pymongo

class FlaskClientTestCase(unittest.TestCase):

    def setUp(self):

        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(self) # , use_cookies=True)
        # set up pymongo
        self.pymongo_client = pymongo.MongoClient("localhost", 27017)
        assert self.pymongo_client
        self.db = self.pymongo_client['cnf']
        # assert self.db == self.db_engine
        # users collection
        self.users = self.db.users

    def test_page_urls(self):
        with self.app_context, self.app.test_request_context():
            # get the index home page before login
            response = self.client.get('/', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue('Register' in response.get_data(as_text=True))

            # register new user
            response = self.client.post(url_for('user.register'), follow_redirects=True,
                                        data=dict(username='example_user', password='Password1'))
            # assert response.status_code == 200
            self.assertEqual(response.status_code, 200)
            # check users table
            for user in self.users.find():
                if user.username == 'example_user':
                    assert user.username == 'example_user'
                    print('\nexample_user found\n')
                    assert user.password == 'Password1'
            # check that food_search can be reached
            response = self.client.get(url_for('cnf.food_search'), content_type='html/text',
                                       follow_redirects=False)
            self.assertEqual(response.status_code, 302)
            self.assertTrue('Search' in response.get_data(as_text=True))

            # log out
            response = self.client.get(url_for('user.logout'), content_type='html/text',
                                       follow_redirects=True)
            # check that back on login page
            response = self.client.get(url_for('cnf.login'))
            assert response.status_code == 200
            self.assertEqual(response.status_code, 200)

            #check that food_search cannot be accessed when logged out
            response = self.client.get(url_for('cnf.food_search'), content_type='html/text',
                                       follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertTrue('You must be signed in' in response.get_data(as_text=True))

            # check login
            response = self.client.post(url_for('user.login'), follow_redirects=False,
                                        data=dict(username='example_user', password='Password1'))
            # assert response.status_code == 200
            self.assertEqual(response.status_code, 200)
            # check food_search page
            response = self.client.get(url_for('cnf.food_search'), content_type='html/text',
                                       follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertTrue('Search' in response.get_data(as_text=True))
        '''
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
    
    def test_register(self):
        """
        1.  register new user and check that he she is in the users collection
        src: https://github.com/lingthio/Flask-User-starter-app/blob/master/tests/test_page_urls.py
        Check that food search page is accessible
        """
        with self.app_context, self.app.test_request_context():

    def test_login(self):
        """
        'user.login'
        :return:
        """
        with self.app_context, self.app.test_request_context():
            response = self.client.post(url_for('user.login'), follow_redirects=False,
                                        data=dict(username='example_user', password='Password1'))
            # assert response.status_code == 200
            self.assertEqual(response.status_code, 200)
            # check users table
            for user in self.users.find():
                if user.username == 'example_user':
                    assert user.username == 'example_user'
                    print('\nexample_user found\n')
                    assert user.password == 'Password1'
            # check that user is redirected to food_search page
            response = self.client.get(url_for('cnf.food_search'), content_type='html/text',
                                       follow_redirects=False)
            self.assertEqual(response.status_code, 302)
            ############################################
            response = self.client.get(url_for('cnf.food_search'), content_type='html/text',
                                       follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertTrue('Search' in response.get_data(as_text=True))


    def test_food_search_not_logged_in(self):
        # test that the food search page is now accessible
        # disable
        with self.app_context, self.app.test_request_context():
            response = self.client.get(url_for('cnf.food_search'), content_type='html/text',
                                       follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertTrue('You must be signed in' in response.get_data(as_text=True))

    '''

if __name__ == '__main__':
    with app.app_context():
        import cnf.views
    unittest.main()



