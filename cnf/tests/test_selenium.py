'''
from p.207 gringberg flask book 1e
'''

from selenium import webdriver
import unittest
from cnf.main import setup_app
import cnf.settings as settings

class SeleniumTestCase(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        #start Firefox
        try:
            cls.client = webdriver.Firefox()
        except:
            pass
        # skip these tests if browser cannot be started
        if cls.client:
            #create app,
            cls.app = setup_app()
            cls.app_context = cls.app.app_context()
            cls.app_context.push()

            #suppress logging to keep unittest output clean
            import logging
            logger = logging.getLogger('werkzeug')
            logger.setLevel("ERRROR")

            #db already present

            #not adding an admin user

@classmethod
def tearDownClass(cls):
    if cls.client:
        # stop flask server and browser
        cls.client.get('http://localhost:8888/shutdown')
        cls.client.close()
        # remove application context
        cls.app_context.pop()


def setUp(self):
    if not self.client:
        self.skipTest('Web browser not available')


def tearDown(self):
    pass