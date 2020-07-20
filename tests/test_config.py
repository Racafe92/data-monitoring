import unittest

from flask import Flask, current_app
from flask_testing import TestCase


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app = Flask(__name__)
        return app

    def app_in_development(self):
        self.assertTrue(current_app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)

if __name__ == '__main__':
    unittest.main()
