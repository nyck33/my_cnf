import unittest

from cnf.main import main, setup_app
from flask import url_for

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = setup_app()
        self.app_context = self.app.app_context()
        with self.app_context:
            import cnf.views
        self.app_context.push()
        #self.db = self.app.db
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get(url_for('cnf.login'))
        self.assertTrue('Register' in response.get_data(as_text=True))




