'''
from JungeAlexander import parent dir module
NOTE: leave incomplete test funcs commented out
Pymongo: file:///home/nobu/Desktop/comp4911/textbooks/Introduction%20to%20MongoDB%20and%20Python%20-%20DataCamp.html
/user/register and /user/sign-in -> redirects to '/'
'''
import unittest
from flask import (current_app as app, request, render_template,
                   abort, url_for, session, redirect)

# for importing module from parent dir
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
#from cnf import main
from cnf.main import main, setup_app
from flask import url_for, current_app as app

# learn mongoengine way later
import pymongo

class FlaskClientTestCase(unittest.TestCase):

    def setUp(self):
        #self.app = setup_app()
        self.app = app
        self.app_context = self.app.app_context()
        #push context
        self.app_context.push()
        # Import your views!
        with self.app_context:
            import cnf.views
        self.db_engine = self.app.db

        self.client = self.app.test_client(self)#, use_cookies=True)
        # set up pymongo
        self.pymongo_client = pymongo.MongoClient("localhost", 27017)
        assert self.pymongo_client
        self.db = self.pymongo_client['cnf']
        #assert self.db == self.db_engine
        # users collection
        self.users = self.db.users
    """
    # pymongo connect 
    def connect_cnf(self):
        # Connect to cnf
        client = pymongo.MongoClient("localhost", 27017)
        assert client
        db = client['cnf']
        '''
        # or from Python MongoBook
        try:
            c = pymongo.Connection(host="localhost", port=27017)
            print("Connected to MongoDB")
        except ConnectionError as e:
            sys.stderr.write("could not connect to MongoDB: %s" % e)
        '''
    """

    def test_home_page(self):
        #with self.app_context, self.app.test_request_context():
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Register' in response.get_data(as_text=True))

    def test_register(self):
        """
        1.  register new user and check that he she is in the users collection
        src: https://github.com/lingthio/Flask-User-starter-app/blob/master/tests/test_page_urls.py
        Check that food search page is accessible
        """
        with self.app_context, self.app.test_request_context():
            response = self.client.post(url_for('user.register'), follow_redirects=True,
                                        data=dict(username='example_user', password='Password1'))
            #assert response.status_code == 200
            self.assertEqual(response.status_code, 200)
            #check users table
            for user in self.users.find():
                if user.username == 'example_user':
                    assert user.username == 'example_user'
                    print('\nexample_user found\n')
                    assert user.password == 'Password1'

    def test_login(self):
        """
        'user.login'
        :return:
        """
        with self.app_context, self.app.test_request_context():
            response = self.client.post(url_for('user.login'), follow_redirects=True,
                                        data=dict(username='example_user', password='Password1'))
            #assert response.status_code == 200
            self.assertEqual(response.status_code, 200)
            #check users table
            for user in self.users.find():
                if user.username == 'example_user':
                    assert user.username == 'example_user'
                    print('\nexample_user found\n')
                    assert user.password == 'Password1'

    def test_food_search(self):
        # test that the food search page is now accessible
        #disable
        with self.app_context, self.app.test_request_context():
            response = self.client.get(url_for('main.food_search'), content_type='html/text',
                                       follow_redirects=True,
                                       data=dict(username='example_user', password='Password1'))
            self.assertEqual(response.status_code, 200)
            self.assertTrue('Canadian' in response.get_data(as_text=True))
    '''
    def test_del_user(self):
        """
        2.  then delete user and check that he she is gone
        :return:
        """
        pass

    def test_same_username(self):
        """
        3.  make two users with same name, check that this does not happen
        :return:
        """
        pass

    def test_register_input(self):
        """
        4.  test all password, username requirements (chars)
        :return:
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
    '''

if __name__ == '__main__':
    unittest.main()



