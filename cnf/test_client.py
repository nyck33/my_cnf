'''
from JungeAlexander import parent dir module
'''
import unittest

# for importing module from parent dir
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from cnf.main import main, setup_app
#from flask import current_app as app

class FlaskClientTestCase(unittest.TestCase):

    def setUp(self):
        self.app = setup_app()
        # Import your views!
        with self.app.app_context():
            import cnf.views
        self.db = self.app.db
        #self.app.run()

        self.client = self.app.test_client(self)#, use_cookies=True)

    def test_home_page(self):
        response = self.client.get('/', content_type='html/text')
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
    unittest.main()



